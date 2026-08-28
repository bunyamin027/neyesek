import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/animated_button.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../data/services/purchase_service.dart';
import '../../l10n/app_localizations.dart';

class PremiumScreen extends StatefulWidget {
  const PremiumScreen({super.key});

  @override
  State<PremiumScreen> createState() => _PremiumScreenState();
}

class _PremiumScreenState extends State<PremiumScreen> {
  // 0: Monthly, 1: Yearly (Default selected - Best Value)
  int _selectedPlanIndex = 1;
  bool _isProcessing = false;

  static const String privacyPolicyUrl = 'https://www.kahramanapp.com/privacy';
  static const String eulaUrl = 'https://www.apple.com/legal/internet-services/itunes/dev/stdeula/';

  final List<({
    String id,
    String title,
    String price,
    String billedText,
    String subtitle,
    String? badge,
    bool isPopular,
  })> _plans = [
    (
      id: PurchaseService.productMonthly,
      title: 'Aylık Plan',
      price: '₺49.99',
      billedText: '/ ay',
      subtitle: 'Esnek üyelik, dilediğin an iptal et',
      badge: null,
      isPopular: false,
    ),
    (
      id: PurchaseService.productYearly,
      title: 'Yıllık Plan',
      price: '₺24.99',
      billedText: '/ ay (Yıllık ₺299.99)',
      subtitle: '12 ay sınırsız erişim • En avantajlı paket',
      badge: '%50 TASARRUF',
      isPopular: true,
    ),
  ];

  @override
  void initState() {
    super.initState();
    PurchaseService.instance.addListener(_onPurchaseStateChanged);
  }

  @override
  void dispose() {
    PurchaseService.instance.removeListener(_onPurchaseStateChanged);
    super.dispose();
  }

  void _onPurchaseStateChanged() {
    if (!mounted) return;
    if (PurchaseService.instance.isPremium) {
      final l10n = AppLocalizations.of(context);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(l10n?.premiumSuccess ?? 'Tebrikler! Premium üyelik aktif edildi! 🎉'),
          backgroundColor: AppColors.primary,
          behavior: SnackBarBehavior.floating,
        ),
      );
      Navigator.pop(context);
    }
  }

  Future<void> _handlePurchase(String productId) async {
    if (_isProcessing) return;
    HapticFeedback.heavyImpact();

    final service = PurchaseService.instance;

    try {
      // Don't show full-screen overlay — Apple's StoreKit payment sheet
      // must be visible on top. The PurchaseService listener handles
      // loading state via purchaseStream updates.
      setState(() => _isProcessing = true);
      await service.buyPlan(productId);
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(e.toString().replaceAll('Exception: ', '')),
          backgroundColor: AppColors.error,
          behavior: SnackBarBehavior.floating,
        ),
      );
    } finally {
      if (mounted) {
        setState(() => _isProcessing = false);
      }
    }
  }

  Future<void> _handleRestore() async {
    if (_isProcessing) return;
    setState(() => _isProcessing = true);
    HapticFeedback.lightImpact();

    final l10n = AppLocalizations.of(context);
    await PurchaseService.instance.restorePurchases();

    if (!mounted) return;
    setState(() => _isProcessing = false);

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          PurchaseService.instance.isPremium
              ? (l10n?.premiumSuccess ?? 'Premium üyeliğiniz başarıyla geri yüklendi! 🎉')
              : (l10n?.settingsRestore ?? 'Satın alımlar kontrol edildi.'),
        ),
        backgroundColor: AppColors.surfaceLight,
        behavior: SnackBarBehavior.floating,
      ),
    );

    if (PurchaseService.instance.isPremium) {
      Navigator.pop(context);
    }
  }

  Future<void> _openUrl(String urlString) async {
    HapticFeedback.selectionClick();
    final uri = Uri.parse(urlString);
    try {
      if (await canLaunchUrl(uri)) {
        await launchUrl(uri, mode: LaunchMode.externalApplication);
      }
    } catch (e) {
      debugPrint('Could not launch url: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final selectedPlan = _plans[_selectedPlanIndex];

    return Scaffold(
      backgroundColor: const Color(0xFF0E0E18),
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.close_rounded, color: Colors.white, size: 28),
          onPressed: () => Navigator.pop(context),
        ),
        actions: [
          Padding(
            padding: const EdgeInsets.only(right: 8),
            child: TextButton.icon(
              onPressed: _isProcessing ? null : _handleRestore,
              icon: _isProcessing
                  ? const SizedBox(
                      width: 14,
                      height: 14,
                      child: CircularProgressIndicator(strokeWidth: 2, color: AppColors.gold),
                    )
                  : const Icon(Icons.restore_rounded, size: 16, color: AppColors.gold),
              label: Text(
                l10n?.premiumRestore ?? 'Geri Yükle',
                style: AppTextStyles.bodySmall.copyWith(
                  color: AppColors.gold,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
        ],
      ),
      body: Stack(
        children: [
          ListView(
            physics: const BouncingScrollPhysics(),
            padding: const EdgeInsets.fromLTRB(20, 4, 20, 30),
            children: [
              // Golden Gourmet Crown
              Center(
                child: Container(
                  width: 80,
                  height: 80,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    gradient: LinearGradient(
                      colors: [
                        AppColors.gold.withValues(alpha: 0.35),
                        AppColors.goldLight.withValues(alpha: 0.15),
                      ],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    border: Border.all(color: AppColors.gold, width: 2),
                    boxShadow: [
                      BoxShadow(
                        color: AppColors.gold.withValues(alpha: 0.35),
                        blurRadius: 28,
                        spreadRadius: 2,
                      ),
                    ],
                  ),
                  child: const Center(
                    child: Icon(
                      Icons.workspace_premium_rounded,
                      color: AppColors.gold,
                      size: 46,
                    ),
                  ),
                ),
              ).animate().scale(duration: 400.ms, curve: Curves.easeOutBack),

              const SizedBox(height: 14),

              Text(
                'Ne Yesek? Premium',
                style: AppTextStyles.headlineMedium.copyWith(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  letterSpacing: -0.5,
                ),
                textAlign: TextAlign.center,
              ).animate().fadeIn(delay: 100.ms),

              const SizedBox(height: 6),

              Text(
                '10 Dünya Mutfağı, 212+ Otantik Tarif ve Reklamsız Gurme Deneyimi',
                style: AppTextStyles.bodySmall.copyWith(
                  color: AppColors.textSecondary,
                  height: 1.4,
                ),
                textAlign: TextAlign.center,
              ).animate().fadeIn(delay: 150.ms),

              const SizedBox(height: 20),

              // ─── Features Checklist ───
              FrostedGlassContainer(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                borderRadius: 18,
                backgroundColor: const Color(0x18FFFFFF),
                child: Column(
                  children: [
                    _buildFeatureRow(
                      Icons.public_rounded,
                      'Tüm 10 Dünya Mutfağına Tam Erişim',
                      'Japon, Kore, Meksika, Fransız, Hint ve Çin mutfaklarının kilidini açın.',
                    ),
                    const SizedBox(height: 10),
                    _buildFeatureRow(
                      Icons.menu_book_rounded,
                      '212+ Detaylı Otantik Yemek Tarifi',
                      'Malzeme listeleri, kalori, süreler ve adım adım pişirme rehberleri.',
                    ),
                    const SizedBox(height: 10),
                    _buildFeatureRow(
                      Icons.tune_rounded,
                      'Akıllı Çark Filtreleri',
                      'Vejetaryen, hızlı pişen, düşük kalorili veya zorluk filtrelerini dilediğince uygula.',
                    ),
                    const SizedBox(height: 10),
                    _buildFeatureRow(
                      Icons.block_rounded,
                      'Sıfır Reklam, Kesintisiz Akış',
                      'Hiçbir kesinti olmadan hızlı ve keyifli bir gurme deneyimi.',
                    ),
                  ],
                ),
              ).animate().fadeIn(delay: 200.ms).slideY(begin: 0.08, end: 0),

              const SizedBox(height: 20),

              // ─── Subscription Plan Cards (Monthly & Yearly) ───
              ...List.generate(_plans.length, (index) {
                final plan = _plans[index];
                final isSelected = _selectedPlanIndex == index;

                return GestureDetector(
                  onTap: () {
                    if (_selectedPlanIndex == index) {
                      // Already selected — trigger purchase (DayZero pattern)
                      _handlePurchase(plan.id);
                    } else {
                      // First tap — just select the plan
                      setState(() => _selectedPlanIndex = index);
                    }
                  },
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 200),
                    margin: const EdgeInsets.only(bottom: 12),
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: isSelected
                          ? AppColors.gold.withValues(alpha: 0.16)
                          : const Color(0x18FFFFFF),
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(
                        color: isSelected ? AppColors.gold : AppColors.glassBorder,
                        width: isSelected ? 2 : 1,
                      ),
                      boxShadow: isSelected
                          ? [
                              BoxShadow(
                                color: AppColors.gold.withValues(alpha: 0.25),
                                blurRadius: 16,
                                offset: const Offset(0, 4),
                              ),
                            ]
                          : null,
                    ),
                    child: Row(
                      children: [
                        // Radio Selection Circle
                        Container(
                          width: 24,
                          height: 24,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: isSelected ? AppColors.gold : Colors.transparent,
                            border: Border.all(
                              color: isSelected ? AppColors.gold : AppColors.textMuted,
                              width: 2,
                            ),
                          ),
                          child: isSelected
                              ? const Icon(Icons.check, size: 16, color: Colors.black)
                              : null,
                        ),
                        const SizedBox(width: 14),

                        // Plan Info
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Row(
                                children: [
                                  Text(
                                    plan.title,
                                    style: AppTextStyles.titleMedium.copyWith(
                                      fontWeight: FontWeight.bold,
                                      color: Colors.white,
                                    ),
                                  ),
                                  if (plan.badge != null) ...[
                                    const SizedBox(width: 8),
                                    Container(
                                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                                      decoration: BoxDecoration(
                                        gradient: const LinearGradient(
                                          colors: [AppColors.gold, AppColors.goldLight],
                                        ),
                                        borderRadius: BorderRadius.circular(8),
                                        boxShadow: [
                                          BoxShadow(
                                            color: AppColors.gold.withValues(alpha: 0.3),
                                            blurRadius: 8,
                                          ),
                                        ],
                                      ),
                                      child: Text(
                                        plan.badge!,
                                        style: const TextStyle(
                                          color: Colors.black,
                                          fontWeight: FontWeight.w800,
                                          fontSize: 10,
                                        ),
                                      ),
                                    ),
                                  ],
                                ],
                              ),
                              const SizedBox(height: 3),
                              Text(
                                plan.subtitle,
                                style: AppTextStyles.bodySmall.copyWith(
                                  color: AppColors.textMuted,
                                  fontSize: 12,
                                ),
                              ),
                            ],
                          ),
                        ),

                        // Price Column
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.end,
                          children: [
                            Text(
                              plan.price,
                              style: AppTextStyles.titleMedium.copyWith(
                                color: isSelected ? AppColors.gold : Colors.white,
                                fontWeight: FontWeight.w800,
                                fontSize: 18,
                              ),
                            ),
                            Text(
                              plan.billedText,
                              style: AppTextStyles.labelSmall.copyWith(
                                color: AppColors.textMuted,
                                fontSize: 10,
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                );
              }).animate().fadeIn(delay: 250.ms),

              const SizedBox(height: 12),

              // ─── Purchase Action Button ───
              AnimatedButton(
                text: _selectedPlanIndex == 1
                    ? 'Yıllık Premium\'a Geç'
                    : 'Aylık Premium\'a Geç',
                onPressed: () => _handlePurchase(selectedPlan.id),
                width: double.infinity,
                height: 56,
                icon: Icons.star_rounded,
              ).animate().fadeIn(delay: 350.ms).slideY(begin: 0.12, end: 0),

              const SizedBox(height: 16),

              // ─── Auto-Renew Disclosure (App Store Required) ───
              Text(
                'Abonelik, cari dönemin bitiminden en az 24 saat önce iptal edilmediği sürece otomatik olarak yenilenir. Ödemeler onaylandığında iTunes / Google Play Hesabınızdan tahsil edilir. Aboneliğinizi istediğiniz zaman Hesap Ayarlarınızdan yönetebilir veya iptal edebilirsiniz.',
                style: AppTextStyles.labelSmall.copyWith(
                  color: AppColors.textMuted.withValues(alpha: 0.65),
                  fontSize: 10,
                  height: 1.45,
                ),
                textAlign: TextAlign.center,
              ),

              const SizedBox(height: 16),

              // ─── Legal Footer: EULA, Privacy & Restore Links ───
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  _buildLegalLink(
                    'Kullanım Koşulları (EULA)',
                    () => _openUrl(eulaUrl),
                  ),
                  _buildLegalDivider(),
                  _buildLegalLink(
                    'Gizlilik Politikası',
                    () => _openUrl(privacyPolicyUrl),
                  ),
                  _buildLegalDivider(),
                  _buildLegalLink(
                    'Geri Yükle',
                    _handleRestore,
                  ),
                ],
              ),
            ],
          ),


        ],
      ),
    );
  }

  Widget _buildFeatureRow(IconData icon, String title, String subtitle) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          margin: const EdgeInsets.only(top: 2),
          padding: const EdgeInsets.all(6),
          decoration: BoxDecoration(
            color: AppColors.gold.withValues(alpha: 0.15),
            shape: BoxShape.circle,
          ),
          child: Icon(icon, color: AppColors.gold, size: 16),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                title,
                style: AppTextStyles.bodyMedium.copyWith(
                  color: Colors.white,
                  fontWeight: FontWeight.w600,
                  fontSize: 13,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                subtitle,
                style: AppTextStyles.bodySmall.copyWith(
                  color: AppColors.textMuted,
                  fontSize: 11,
                  height: 1.3,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildLegalLink(String text, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 4),
        child: Text(
          text,
          style: AppTextStyles.labelSmall.copyWith(
            color: AppColors.textSecondary,
            fontSize: 10,
            decoration: TextDecoration.underline,
            decorationColor: AppColors.textMuted,
          ),
        ),
      ),
    );
  }

  Widget _buildLegalDivider() {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 4),
      child: Text(
        '•',
        style: TextStyle(
          color: AppColors.textMuted.withValues(alpha: 0.5),
          fontSize: 10,
        ),
      ),
    );
  }
}
