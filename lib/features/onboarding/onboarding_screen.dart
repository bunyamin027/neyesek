import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:smooth_page_indicator/smooth_page_indicator.dart';

import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/animated_button.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../core/widgets/gradient_background.dart';
import '../../data/services/locale_service.dart';
import '../../l10n/app_localizations.dart';
import '../navigation/main_nav_screen.dart';

/// 3 Adımlı Çok Dilli Onboarding Ekranı
class OnboardingScreen extends StatefulWidget {
  const OnboardingScreen({super.key});

  @override
  State<OnboardingScreen> createState() => _OnboardingScreenState();
}

class _OnboardingScreenState extends State<OnboardingScreen> {
  final PageController _pageController = PageController();
  int _currentPage = 0;

  bool get _isLastPage => _currentPage == 2;

  Future<void> _completeOnboarding() async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool('onboarding_completed', true);
    if (!mounted) return;
    Navigator.of(context).pushReplacement(
      PageRouteBuilder(
        pageBuilder: (context, animation, secondaryAnimation) =>
            const MainNavScreen(),
        transitionsBuilder: (context, animation, secondaryAnimation, child) {
          return FadeTransition(
            opacity: animation,
            child: child,
          );
        },
        transitionDuration: const Duration(milliseconds: 600),
      ),
    );
  }

  void _nextPage() {
    HapticFeedback.selectionClick();
    if (_isLastPage) {
      _completeOnboarding();
    } else {
      _pageController.nextPage(
        duration: const Duration(milliseconds: 400),
        curve: Curves.easeInOutCubic,
      );
    }
  }

  void _showLanguageSelector() {
    final l10n = AppLocalizations.of(context);
    final service = LocaleService.instance;

    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (context) => Container(
        padding: const EdgeInsets.fromLTRB(20, 20, 20, 30),
        decoration: BoxDecoration(
          color: AppColors.surface,
          borderRadius: const BorderRadius.vertical(top: Radius.circular(28)),
          border: Border.all(color: AppColors.glassBorder, width: 1.5),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Center(
              child: Container(
                width: 40,
                height: 4,
                decoration: BoxDecoration(
                  color: AppColors.textMuted.withValues(alpha: 0.3),
                  borderRadius: BorderRadius.circular(2),
                ),
              ),
            ),
            const SizedBox(height: 16),
            Text(
              l10n?.settingsLanguage ?? 'Dil Seçimi / Language',
              style: AppTextStyles.titleLarge.copyWith(color: Colors.white, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),
            ...LocaleService.supportedLocales.map((locale) {
              final code = locale.languageCode;
              final isSelected = service.currentLanguageCode == code;
              return GestureDetector(
                onTap: () {
                  HapticFeedback.selectionClick();
                  service.setLocale(code);
                  Navigator.pop(context);
                },
                child: FrostedGlassContainer(
                  margin: const EdgeInsets.only(bottom: 10),
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                  borderRadius: 16,
                  child: Row(
                    children: [
                      Text(service.getLanguageFlag(code), style: const TextStyle(fontSize: 24)),
                      const SizedBox(width: 14),
                      Expanded(
                        child: Text(
                          service.getLanguageName(code),
                          style: AppTextStyles.bodyMedium.copyWith(
                            color: Colors.white,
                            fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                          ),
                        ),
                      ),
                      if (isSelected)
                        const Icon(Icons.check_circle_rounded, color: AppColors.primary, size: 22),
                    ],
                  ),
                ),
              );
            }),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final localeService = LocaleService.instance;

    final pages = [
      _OnboardingPageData(
        emoji: '🍕',
        title: l10n?.onboardingTitle1 ?? 'Ne Yiyeceğine Karar Veremiyor musun?',
        subtitle: l10n?.onboardingSubtitle1 ?? 'Her gün "Bugün ne yesek?" derdine eğlenceli çarkımızla son verin!',
        bgEmojis: ['🍔', '🍜', '🥙', '🌮', '🍣', '🍝'],
      ),
      _OnboardingPageData(
        emoji: '🎰',
        title: l10n?.onboardingTitle2 ?? 'Çarkı Çevir!',
        subtitle: l10n?.onboardingSubtitle2 ?? 'Kararı şansa bırak, günün lezzetini çark belirlesin.',
        bgEmojis: ['🎯', '🎲', '✨', '🎪', '🎡', '🎠'],
      ),
      _OnboardingPageData(
        emoji: '🌍',
        title: l10n?.onboardingTitle3 ?? 'Dünya Mutfaklarını Keşfet',
        subtitle: l10n?.onboardingSubtitle3 ?? '10 farklı mutfaktan 160+ detaylı tarif parmaklarının ucunda.',
        bgEmojis: ['🇹🇷', '🇮🇹', '🇯🇵', '🇲🇽', '🇹🇭', '🇮🇳'],
      ),
    ];

    return Scaffold(
      body: GradientBackground(
        child: SafeArea(
          child: Column(
            children: [
              // Üst Bar: Dil Seçici & Skip Butonu
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    // Dil Seçici Çipi
                    GestureDetector(
                      onTap: _showLanguageSelector,
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                        decoration: BoxDecoration(
                          color: AppColors.frostedGlassDark,
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: AppColors.glassBorder),
                        ),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Text(localeService.getLanguageFlag(localeService.currentLanguageCode)),
                            const SizedBox(width: 6),
                            Text(
                              localeService.currentLanguageCode.toUpperCase(),
                              style: AppTextStyles.labelSmall.copyWith(color: Colors.white, fontWeight: FontWeight.bold),
                            ),
                          ],
                        ),
                      ),
                    ),

                    // Skip Butonu
                    TextButton(
                      onPressed: _completeOnboarding,
                      child: Text(
                        l10n?.onboardingSkip ?? 'Atla',
                        style: AppTextStyles.bodyMedium.copyWith(
                          color: AppColors.textMuted,
                        ),
                      ),
                    ),
                  ],
                ),
              ).animate().fadeIn(delay: 300.ms, duration: 400.ms),

              // Sayfa içeriği
              Expanded(
                child: PageView.builder(
                  controller: _pageController,
                  itemCount: pages.length,
                  onPageChanged: (index) {
                    setState(() => _currentPage = index);
                    HapticFeedback.selectionClick();
                  },
                  itemBuilder: (context, index) {
                    return _OnboardingPage(data: pages[index]);
                  },
                ),
              ),

              // Alt kısım: Indicator + Buton
              Padding(
                padding: const EdgeInsets.fromLTRB(32, 0, 32, 40),
                child: Column(
                  children: [
                    // Sayfa göstergesi
                    SmoothPageIndicator(
                      controller: _pageController,
                      count: pages.length,
                      effect: ExpandingDotsEffect(
                        dotHeight: 8,
                        dotWidth: 8,
                        expansionFactor: 4,
                        dotColor: AppColors.textMuted.withValues(alpha: 0.3),
                        activeDotColor: AppColors.primary,
                      ),
                    ),
                    const SizedBox(height: 32),

                    // İleri / Başla butonu
                    AnimatedSwitcher(
                      duration: const Duration(milliseconds: 300),
                      child: AnimatedButton(
                        key: ValueKey(_isLastPage),
                        text: _isLastPage
                            ? (l10n?.onboardingStart ?? 'Hemen Başla')
                            : (l10n?.onboardingNext ?? 'İleri'),
                        onPressed: _nextPage,
                        width: double.infinity,
                        icon: _isLastPage ? Icons.rocket_launch_rounded : null,
                      ),
                    ),
                  ],
                ),
              )
                  .animate()
                  .fadeIn(delay: 600.ms, duration: 500.ms)
                  .slideY(begin: 0.3, end: 0),
            ],
          ),
        ),
      ),
    );
  }
}

/// Onboarding sayfa verisi
class _OnboardingPageData {
  final String emoji;
  final String title;
  final String subtitle;
  final List<String> bgEmojis;

  const _OnboardingPageData({
    required this.emoji,
    required this.title,
    required this.subtitle,
    required this.bgEmojis,
  });
}

/// Tek bir onboarding sayfası
class _OnboardingPage extends StatelessWidget {
  final _OnboardingPageData data;

  const _OnboardingPage({required this.data});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 32),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // Arka plan emojileri
          SizedBox(
            height: 200,
            child: Stack(
              alignment: Alignment.center,
              children: [
                // Yüzen arka plan emojileri
                for (int i = 0; i < data.bgEmojis.length; i++)
                  Positioned(
                    left: (i % 3) * 100.0 + 20,
                    top: (i ~/ 3) * 80.0 + 20,
                    child: Text(
                      data.bgEmojis[i],
                      style: TextStyle(
                        fontSize: 28,
                        color: Colors.white.withValues(alpha: 0.1),
                      ),
                    )
                        .animate(
                          onPlay: (controller) => controller.repeat(
                            reverse: true,
                          ),
                        )
                        .moveY(
                          begin: -8,
                          end: 8,
                          duration: Duration(milliseconds: 2000 + i * 300),
                          curve: Curves.easeInOut,
                        ),
                  ),
                // Ana emoji
                Text(data.emoji, style: const TextStyle(fontSize: 80))
                    .animate()
                    .scale(
                      begin: const Offset(0.5, 0.5),
                      end: const Offset(1.0, 1.0),
                      duration: 600.ms,
                      curve: Curves.elasticOut,
                    )
                    .fadeIn(duration: 400.ms),
              ],
            ),
          ),

          const SizedBox(height: 32),

          // Başlık
          Text(
            data.title,
            style: AppTextStyles.displayMedium,
            textAlign: TextAlign.center,
          )
              .animate()
              .fadeIn(delay: 200.ms, duration: 500.ms)
              .slideY(begin: 0.2, end: 0),

          const SizedBox(height: 16),

          // Alt başlık
          Text(
            data.subtitle,
            style: AppTextStyles.bodyLarge.copyWith(
              color: AppColors.textSecondary,
            ),
            textAlign: TextAlign.center,
          )
              .animate()
              .fadeIn(delay: 400.ms, duration: 500.ms)
              .slideY(begin: 0.2, end: 0),
        ],
      ),
    );
  }
}
