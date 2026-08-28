import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_animate/flutter_animate.dart';

import 'package:share_plus/share_plus.dart';
import '../../core/constants/app_strings.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/animated_button.dart';
import '../../core/widgets/food_image.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../data/models/food_item.dart';
import '../../l10n/app_localizations.dart';
import '../recipe_detail/recipe_detail_screen.dart';

/// Sonuç Ekranı — Bottom Sheet olarak gösterilir.
/// Çark durduğunda seçilen yemeği premium bir tasarımla sunar.
class ResultScreen extends StatelessWidget {
  final FoodItem food;
  final VoidCallback onSpinAgain;

  const ResultScreen({
    super.key,
    required this.food,
    required this.onSpinAgain,
  });

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final langCode = Localizations.localeOf(context).languageCode;
    return Container(
      constraints: BoxConstraints(
        maxHeight: MediaQuery.of(context).size.height * 0.65,
      ),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: const BorderRadius.vertical(top: Radius.circular(32)),
        boxShadow: [
          BoxShadow(
            color: food.color.withValues(alpha: 0.3),
            blurRadius: 40,
            offset: const Offset(0, -10),
          ),
        ],
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Drag handle
          Container(
            margin: const EdgeInsets.only(top: 12),
            width: 40,
            height: 4,
            decoration: BoxDecoration(
              color: AppColors.textMuted.withValues(alpha: 0.3),
              borderRadius: BorderRadius.circular(2),
            ),
          ),

          Padding(
            padding: const EdgeInsets.fromLTRB(24, 24, 24, 32),
            child: Column(
              children: [
                // Üst etiket
                Text(
                  l10n?.wheelResultTitle ?? AppStrings.resultTitle,
                  style: AppTextStyles.bodyMedium.copyWith(
                    color: AppColors.primary,
                    fontWeight: FontWeight.w600,
                  ),
                )
                    .animate()
                    .fadeIn(duration: 400.ms)
                    .slideY(begin: -0.2, end: 0),

                const SizedBox(height: 20),

                // Büyük Fotoğraf / Emoji + glow
                Container(
                  width: 120,
                  height: 120,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(28),
                    boxShadow: [
                      BoxShadow(
                        color: food.color.withValues(alpha: 0.35),
                        blurRadius: 40,
                        spreadRadius: 5,
                      ),
                    ],
                  ),
                  child: FoodImage(
                    food: food,
                    width: 120,
                    height: 120,
                    borderRadius: BorderRadius.circular(28),
                    emojiSize: 56,
                  ),
                )
                    .animate()
                    .scale(
                      begin: const Offset(0.3, 0.3),
                      end: const Offset(1.0, 1.0),
                      duration: 600.ms,
                      curve: Curves.elasticOut,
                    )
                    .fadeIn(duration: 300.ms),

                const SizedBox(height: 20),

                // Yemek adı
                Text(
                  food.getName(langCode),
                  textAlign: TextAlign.center,
                  style: AppTextStyles.displaySmall.copyWith(
                    color: AppColors.textPrimary,
                  ),
                )
                    .animate()
                    .fadeIn(delay: 200.ms, duration: 400.ms)
                    .slideY(begin: 0.2, end: 0),

                const SizedBox(height: 12),

                // Mutfak etiketi
                FrostedGlassContainer(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 16,
                    vertical: 8,
                  ),
                  borderRadius: 12,
                  blurAmount: 10,
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(
                        Icons.restaurant_rounded,
                        color: food.color,
                        size: 16,
                      ),
                      const SizedBox(width: 8),
                      Text(
                        food.cuisineId.toUpperCase(),
                        style: AppTextStyles.bodySmall.copyWith(
                          color: AppColors.textSecondary,
                          fontWeight: FontWeight.w600,
                          letterSpacing: 1,
                        ),
                      ),
                    ],
                  ),
                )
                    .animate()
                    .fadeIn(delay: 300.ms, duration: 400.ms)
                    .scale(
                      begin: const Offset(0.9, 0.9),
                      end: const Offset(1.0, 1.0),
                    ),

                const SizedBox(height: 16),

                // Açıklama
                if (food.getDescription(langCode).isNotEmpty)
                  Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: AppColors.frostedGlassDark,
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Text(
                      food.getDescription(langCode),
                      style: AppTextStyles.bodyMedium.copyWith(
                        color: AppColors.textSecondary,
                        height: 1.5,
                      ),
                      textAlign: TextAlign.center,
                    ),
                  )
                      .animate()
                      .fadeIn(delay: 400.ms, duration: 400.ms),

                const SizedBox(height: 24),

                // Butonlar
                Column(
                  children: [
                    // Tarifi Gör Butonu
                    AnimatedButton(
                      text: l10n?.wheelSeeRecipe ?? 'Tarifi ve Detayları Gör',
                      onPressed: () {
                        HapticFeedback.lightImpact();
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => RecipeDetailScreen(food: food),
                          ),
                        );
                      },
                      width: double.infinity,
                      height: 52,
                      icon: Icons.menu_book_rounded,
                    ),
                    const SizedBox(height: 10),
                    // Tekrar Çevir ve Paylaş butonları
                    Row(
                      children: [
                        Expanded(
                          child: TextButton.icon(
                            onPressed: () {
                              HapticFeedback.mediumImpact();
                              onSpinAgain();
                            },
                            icon: const Icon(Icons.refresh_rounded, color: AppColors.textSecondary),
                            label: Text(
                              l10n?.wheelSpinAgain ?? 'Tekrar Çevir',
                              style: AppTextStyles.labelLarge.copyWith(color: AppColors.textSecondary),
                            ),
                          ),
                        ),
                        IconButton(
                          icon: const Icon(Icons.share_rounded, color: AppColors.textSecondary),
                          onPressed: () {
                            HapticFeedback.lightImpact();
                            final name = food.getName(langCode);
                            final shareText = l10n?.commonShareText(name) ?? 'Bugün Ne Yesek uygulamasında harika bir yemek seçtik: $name!';
                            Share.share('$shareText\n\n🍽️ $name (${food.cuisineId.toUpperCase()})\n🔥 ${food.calories} kcal');
                          },
                        ),
                      ],
                    ),
                  ],
                )
                    .animate()
                    .fadeIn(delay: 500.ms, duration: 400.ms)
                    .slideY(begin: 0.3, end: 0),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
