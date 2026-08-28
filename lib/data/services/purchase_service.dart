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

  // ─── Product IDs (Official Store Bundle Identifier Format) ───────
  static const String productMonthly = 'com.neyesek.app.premium.monthly';
  static const String productYearly = 'com.neyesek.app.premium.yearly';

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

  Future<void> init() async {
    final prefs = await SharedPreferences.getInstance();
    _isPremium = prefs.getBool(_keyIsPremium) ?? false;
    notifyListeners();

    try {
      _isAvailable = await _iap.isAvailable();
      debugPrint('IAP init: store available = $_isAvailable');

      if (_isAvailable) {
        // IMPORTANT: Listen to purchase stream FIRST, before anything else.
        // This ensures we catch and complete any pending transactions that
        // are stuck in the queue (which cause the black screen).
        final Stream<List<PurchaseDetails>> purchaseUpdated = _iap.purchaseStream;
        _subscription = purchaseUpdated.listen(
          _onPurchaseUpdate,
          onDone: () => _subscription?.cancel(),
          onError: (error) {
            debugPrint('IAP stream error: $error');
            _errorMessage = error.toString();
            notifyListeners();
          },
        );

        // Start loading products in background without blocking app startup
        unawaited(loadProducts());
      }
    } catch (e) {
      debugPrint('IAP Initialization notice: $e');
    }
  }

  Future<void> loadProducts() async {
    if (!_isAvailable) {
      _isAvailable = await _iap.isAvailable();
      if (!_isAvailable) return;
    }
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      final ProductDetailsResponse response = await _iap.queryProductDetails(allProductIds);
      if (response.notFoundIDs.isNotEmpty) {
        debugPrint('IAP Warning - Not Found IDs: ${response.notFoundIDs}');
      }
      _products = response.productDetails;
      debugPrint('IAP loadProducts: loaded ${_products.length} products: ${_products.map((p) => p.id).toList()}');
    } catch (e) {
      _errorMessage = 'Ürünler yüklenirken hata oluştu: $e';
      debugPrint('IAP loadProducts error: $e');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<bool> buyProduct(ProductDetails product) async {
    debugPrint('IAP buyProduct: initiating purchase for ${product.id} (${product.title})');
    final PurchaseParam purchaseParam = PurchaseParam(productDetails: product);
    try {
      final result = await _iap.buyNonConsumable(purchaseParam: purchaseParam);
      debugPrint('IAP buyProduct: buyNonConsumable returned $result');
      return result;
    } catch (e) {
      debugPrint('IAP buyProduct error: $e');
      rethrow;
    }
  }

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

      // Check if product is already cached
      debugPrint('IAP buyPlan: looking for $productId in ${_products.length} cached products');
      ProductDetails? targetProduct;

      for (final p in _products) {
        if (p.id == productId) {
          targetProduct = p;
          break;
        }
      }

      // If not in cache, query directly from store
      if (targetProduct == null) {
        debugPrint('IAP buyPlan: not in cache, querying store...');
        final response = await _iap.queryProductDetails({productId, ...allProductIds});
        debugPrint('IAP buyPlan: store returned ${response.productDetails.length} products, notFoundIDs: ${response.notFoundIDs}');

        if (response.productDetails.isNotEmpty) {
          _products = response.productDetails;
          for (final p in _products) {
            if (p.id == productId) {
              targetProduct = p;
              break;
            }
          }
        }
      }

      if (targetProduct == null) {
        throw Exception(
          'Ürün bulunamadı ($productId). Apple Store ile bağlantı kurulamadı '
          'veya ürün henüz yüklenemedi. Lütfen internet bağlantınızı kontrol '
          'edip tekrar deneyin.',
        );
      }

      debugPrint('IAP buyPlan: found product, initiating purchase...');
      return await buyProduct(targetProduct);
    } catch (e) {
      _errorMessage = e.toString();
      debugPrint('IAP buyPlan error: $e');
      rethrow;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> restorePurchases() async {
    _isLoading = true;
    notifyListeners();
    try {
      await _iap.restorePurchases();
    } catch (e) {
      _errorMessage = 'Geri yükleme hatası: $e';
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> _onPurchaseUpdate(List<PurchaseDetails> purchaseDetailsList) async {
    for (final purchaseDetails in purchaseDetailsList) {
      debugPrint(
        'IAP Purchase Update: status=${purchaseDetails.status}, '
        'productID=${purchaseDetails.productID}, '
        'pendingComplete=${purchaseDetails.pendingCompletePurchase}',
      );

      if (purchaseDetails.status == PurchaseStatus.pending) {
        _isLoading = true;
        notifyListeners();
      } else {
        if (purchaseDetails.status == PurchaseStatus.error) {
          _errorMessage = purchaseDetails.error?.message ?? 'Satın alma hatası';
          debugPrint('IAP Error: $_errorMessage (code: ${purchaseDetails.error?.code})');
          _isLoading = false;
        } else if (purchaseDetails.status == PurchaseStatus.canceled) {
          // User dismissed the Apple payment sheet — clear loading state
          debugPrint('IAP Purchase canceled by user');
          _errorMessage = null;
          _isLoading = false;
        } else if (purchaseDetails.status == PurchaseStatus.purchased ||
            purchaseDetails.status == PurchaseStatus.restored) {
          debugPrint('IAP Purchase success/restored for ${purchaseDetails.productID}');
          final valid = await _verifyPurchase(purchaseDetails);
          if (valid) {
            await _setPremium(true);
          }
          _isLoading = false;
        }

        // CRITICAL: Always complete pending purchases to clear the queue.
        // Unfinished transactions block future purchases and cause black screens.
        if (purchaseDetails.pendingCompletePurchase) {
          debugPrint('IAP Completing purchase for ${purchaseDetails.productID}');
          await _iap.completePurchase(purchaseDetails);
        }
        notifyListeners();
      }
    }
  }

  Future<bool> _verifyPurchase(PurchaseDetails purchaseDetails) async {
    return true;
  }

  Future<void> _setPremium(bool premium) async {
    _isPremium = premium;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_keyIsPremium, premium);
    notifyListeners();
  }

  Future<void> toggleDebugPremium() async {
    await _setPremium(!_isPremium);
  }

  Future<void> setDebugPremium(bool premium) async {
    await _setPremium(premium);
  }

  @override
  void dispose() {
    _subscription?.cancel();
    super.dispose();
  }
}
