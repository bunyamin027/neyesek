import 'dart:async';
import 'package:flutter/foundation.dart';
import 'package:in_app_purchase/in_app_purchase.dart';
import 'package:shared_preferences/shared_preferences.dart';

class PurchaseService extends ChangeNotifier {
  static final PurchaseService instance = PurchaseService._internal();
  PurchaseService._internal();

  final InAppPurchase _iap = InAppPurchase.instance;
  StreamSubscription<List<PurchaseDetails>>? _subscription;

  static const String _keyIsPremium = 'user_is_premium_active';

  // ─── Product IDs — Must match App Store Connect exactly ─────────
  static const String productMonthly = 'com.kahramanapp.neyesek.premium.monthly';
  static const String productYearly = 'com.kahramanapp.neyesek.premium.yearly';

  static const Set<String> allProductIds = {
    productMonthly,
    productYearly,
  };

  bool _isAvailable = false;
  bool get isAvailable => _isAvailable;

  bool _isPremium = false;
  bool get isPremium => _isPremium;

  List<ProductDetails> _products = [];
  List<ProductDetails> get products => _products;

  bool _isLoading = false;
  bool get isLoading => _isLoading;

  String? _errorMessage;
  String? get errorMessage => _errorMessage;

  bool _purchaseConfirmedThisSession = false;

  /// Initialize IAP — call once at app startup.
  Future<void> init() async {
    // Do NOT restore premium from SharedPreferences blindly.
    // Only trust purchases verified via the purchaseStream.
    // This prevents the old debug toggle value from persisting.
    _isPremium = false;
    _purchaseConfirmedThisSession = false;

    // Clear any stale debug/test premium state
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_keyIsPremium, false);
    notifyListeners();

    try {
      _isAvailable = await _iap.isAvailable();
      debugPrint('IAP init: store available = $_isAvailable');

      if (_isAvailable) {
        // Listen to purchase stream FIRST to catch pending transactions.
        if (_subscription == null) {
          final Stream<List<PurchaseDetails>> purchaseUpdated = _iap.purchaseStream;
          _subscription = purchaseUpdated.listen(
            _onPurchaseUpdate,
            onDone: () {
              _subscription?.cancel();
              _subscription = null;
            },
            onError: (error) {
              debugPrint('IAP stream error: $error');
              _errorMessage = error.toString();
              notifyListeners();
            },
          );
        }

        // Load products in background
        unawaited(loadProducts());

        // Restore purchases on launch to check for active subscriptions.
        // This will trigger _onPurchaseUpdate with restored purchases,
        // which will set _isPremium = true only if there's a real subscription.
        unawaited(_restoreOnLaunch());
      }
    } catch (e) {
      debugPrint('IAP Initialization notice: $e');
    }
  }

  /// Silently restore purchases on launch to validate subscription status.
  Future<void> _restoreOnLaunch() async {
    try {
      await _iap.restorePurchases();
      debugPrint('IAP: Launch restore completed. isPremium=$_isPremium');
    } catch (e) {
      debugPrint('IAP: Launch restore failed (non-critical): $e');
    }
  }

  /// Fetch product details from App Store / Google Play.
  Future<void> loadProducts() async {
    if (!_isAvailable) {
      _isAvailable = await _iap.isAvailable();
      if (!_isAvailable) return;
    }
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      final ProductDetailsResponse response =
          await _iap.queryProductDetails(allProductIds);
      if (response.notFoundIDs.isNotEmpty) {
        debugPrint('IAP Warning - Not Found IDs: ${response.notFoundIDs}');
      }
      _products = response.productDetails;
      debugPrint(
        'IAP loadProducts: loaded ${_products.length} products: '
        '${_products.map((p) => '${p.id}=${p.price}').toList()}',
      );
    } catch (e) {
      _errorMessage = 'Ürünler yüklenirken hata oluştu: $e';
      debugPrint('IAP loadProducts error: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Get a specific product by ID. Returns null if not loaded.
  ProductDetails? getProduct(String productId) {
    for (final p in _products) {
      if (p.id == productId) return p;
    }
    return null;
  }

  /// Initiate a subscription purchase.
  Future<bool> buyPlan(String productId) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      if (!_isAvailable) {
        _isAvailable = await _iap.isAvailable();
        debugPrint('IAP buyPlan: store available = $_isAvailable');
      }

      if (!_isAvailable) {
        throw Exception('Uygulama içi satın alma bu cihazda kullanılamıyor.');
      }

      // Find product (cached or fresh query)
      ProductDetails? targetProduct = getProduct(productId);

      if (targetProduct == null) {
        debugPrint('IAP buyPlan: not in cache, querying store...');
        final response =
            await _iap.queryProductDetails({productId, ...allProductIds});
        debugPrint(
          'IAP buyPlan: store returned ${response.productDetails.length} '
          'products, notFoundIDs: ${response.notFoundIDs}',
        );
        if (response.productDetails.isNotEmpty) {
          _products = response.productDetails;
          targetProduct = getProduct(productId);
        }
      }

      if (targetProduct == null) {
        throw Exception(
          'Ürün bulunamadı ($productId). Lütfen App Store Connect\'te '
          'bu ürün ID\'lerinin oluşturulduğundan emin olun ve internet '
          'bağlantınızı kontrol edin.',
        );
      }

      debugPrint('IAP buyPlan: initiating purchase for ${targetProduct.id}');
      final PurchaseParam purchaseParam =
          PurchaseParam(productDetails: targetProduct);
      final result = await _iap.buyNonConsumable(purchaseParam: purchaseParam);
      debugPrint('IAP buyPlan: buyNonConsumable returned $result');
      return result;
    } catch (e) {
      _errorMessage = e.toString();
      debugPrint('IAP buyPlan error: $e');
      rethrow;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Restore previously purchased subscriptions (Apple Guideline 3.1.2).
  Future<void> restorePurchases() async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();
    try {
      await _iap.restorePurchases();
    } catch (e) {
      _errorMessage = 'Geri yükleme hatası: $e';
      debugPrint('IAP restorePurchases error: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  /// Handle purchase updates from the App Store / Google Play.
  Future<void> _onPurchaseUpdate(
      List<PurchaseDetails> purchaseDetailsList) async {
    for (final purchaseDetails in purchaseDetailsList) {
      debugPrint(
        'IAP Update: status=${purchaseDetails.status}, '
        'productID=${purchaseDetails.productID}, '
        'pendingComplete=${purchaseDetails.pendingCompletePurchase}',
      );

      if (purchaseDetails.status == PurchaseStatus.pending) {
        _isLoading = true;
        notifyListeners();
      } else {
        if (purchaseDetails.status == PurchaseStatus.error) {
          _errorMessage =
              purchaseDetails.error?.message ?? 'Satın alma hatası';
          debugPrint(
            'IAP Error: $_errorMessage (code: ${purchaseDetails.error?.code})',
          );
          _isLoading = false;
        } else if (purchaseDetails.status == PurchaseStatus.canceled) {
          debugPrint('IAP Purchase canceled by user');
          _errorMessage = null;
          _isLoading = false;
        } else if (purchaseDetails.status == PurchaseStatus.purchased ||
            purchaseDetails.status == PurchaseStatus.restored) {
          debugPrint(
            'IAP Purchase success/restored for ${purchaseDetails.productID}',
          );
          // Only activate premium for our known product IDs
          if (allProductIds.contains(purchaseDetails.productID)) {
            _purchaseConfirmedThisSession = true;
            await _setPremium(true);
          }
          _isLoading = false;
        }

        // CRITICAL: Always complete pending purchases to clear the queue.
        if (purchaseDetails.pendingCompletePurchase) {
          debugPrint('IAP Completing purchase for ${purchaseDetails.productID}');
          await _iap.completePurchase(purchaseDetails);
        }
        notifyListeners();
      }
    }
  }

  Future<void> _setPremium(bool premium) async {
    _isPremium = premium;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_keyIsPremium, premium);
    debugPrint('IAP _setPremium: $premium');
    notifyListeners();
  }

  @override
  void dispose() {
    _subscription?.cancel();
    super.dispose();
  }
}
