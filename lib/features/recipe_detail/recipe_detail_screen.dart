import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_animate/flutter_animate.dart';

import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/food_image.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../core/widgets/gradient_background.dart';
import 'package:share_plus/share_plus.dart';
import '../../data/models/food_item.dart';
import '../../data/services/favorites_service.dart';
import '../../l10n/app_localizations.dart';

class RecipeDetailScreen extends StatefulWidget {
  final FoodItem food;

  const RecipeDetailScreen({super.key, required this.food});

  @override
  State<RecipeDetailScreen> createState() => _RecipeDetailScreenState();
}

class _RecipeDetailScreenState extends State<RecipeDetailScreen> {
  bool _isFavorite = false;
  final Set<int> _checkedIngredients = {};

  @override
  void initState() {
    super.initState();
    _checkFavorite();
  }

  Future<void> _checkFavorite() async {
    final fav = await FavoritesService.instance.isFavorite(widget.food.id);
    if (!mounted) return;
    setState(() => _isFavorite = fav);
  }

  Future<void> _toggleFavorite() async {
    HapticFeedback.lightImpact();
    final newFav = await FavoritesService.instance.toggleFavorite(widget.food.id);
    if (!mounted) return;
    setState(() => _isFavorite = newFav);

    final l10n = AppLocalizations.of(context);
    final msg = newFav
        ? (l10n?.favoritesAdded ?? 'Favorilere eklendi')
        : (l10n?.favoritesRemoved ?? 'Favorilerden çıkarıldı');

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(msg),
        duration: const Duration(seconds: 2),
        backgroundColor: AppColors.surfaceLight,
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final langCode = Localizations.localeOf(context).languageCode;
    final food = widget.food;

    final name = food.getName(langCode);
    final description = food.getDescription(langCode);
    final ingredients = food.getIngredients(langCode);
    final steps = food.getSteps(langCode);

    return Scaffold(
      body: GradientBackground(
        child: CustomScrollView(
          physics: const BouncingScrollPhysics(),
          slivers: [
            // ─── Sliver App Bar with Nefis Yemek Tarifleri Style Full-Bleed Cover Photo ───
            SliverAppBar(
              expandedHeight: 300,
              pinned: true,
              backgroundColor: AppColors.background,
              elevation: 0,
              leading: Padding(
                padding: const EdgeInsets.all(8.0),
                child: Container(
                  decoration: BoxDecoration(
                    color: Colors.black.withValues(alpha: 0.45),
                    shape: BoxShape.circle,
                    border: Border.all(color: Colors.white.withValues(alpha: 0.2)),
                  ),
                  child: IconButton(
                    icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white, size: 18),
                    onPressed: () => Navigator.pop(context),
                  ),
                ),
              ),
              actions: [
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 8.0),
                  child: Container(
                    decoration: BoxDecoration(
                      color: Colors.black.withValues(alpha: 0.45),
                      shape: BoxShape.circle,
                      border: Border.all(color: Colors.white.withValues(alpha: 0.2)),
                    ),
                    child: IconButton(
                      icon: const Icon(Icons.share_rounded, color: Colors.white, size: 20),
                      onPressed: () {
                        HapticFeedback.lightImpact();
                        final shareText = l10n?.commonShareText(name) ?? 'Bugün Ne Yesek uygulamasında harika bir tarif buldum: $name!';
                        Share.share('$shareText\n\n🍽️ $name (${food.cuisineId.toUpperCase()})\n⏱️ ${food.prepTime + food.cookTime} dk | 🔥 ${food.calories} kcal');
                      },
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 8.0),
                  child: Container(
                    decoration: BoxDecoration(
                      color: Colors.black.withValues(alpha: 0.45),
                      shape: BoxShape.circle,
                      border: Border.all(color: Colors.white.withValues(alpha: 0.2)),
                    ),
                    child: IconButton(
                      icon: Icon(
                        _isFavorite ? Icons.favorite_rounded : Icons.favorite_border_rounded,
                        color: _isFavorite ? AppColors.accent : Colors.white,
                        size: 22,
                      ),
                      onPressed: _toggleFavorite,
                    ),
                  ),
                ),
                const SizedBox(width: 16),
              ],
              flexibleSpace: FlexibleSpaceBar(
                background: Stack(
                  fit: StackFit.expand,
                  children: [
                    // Full-Bleed Real Food Photo or Styled Illustration
                    if (food.imagePath.trim().isNotEmpty) ...[
                      FoodImage(
                        food: food,
                        fit: BoxFit.cover,
                        borderRadius: BorderRadius.zero,
                      ),
                      // Top & Bottom gradient shadows for contrast
                      Container(
                        decoration: BoxDecoration(
                          gradient: LinearGradient(
                            begin: Alignment.topCenter,
                            end: Alignment.bottomCenter,
                            colors: [
                              Colors.black.withValues(alpha: 0.65),
                              Colors.transparent,
                              Colors.black.withValues(alpha: 0.4),
                              AppColors.background,
                            ],
                            stops: const [0.0, 0.35, 0.75, 1.0],
                          ),
                        ),
                      ),
                    ] else ...[
                      Container(
                        decoration: BoxDecoration(
                          gradient: RadialGradient(
                            colors: [
                              food.color.withValues(alpha: 0.4),
                              food.color.withValues(alpha: 0.1),
                              AppColors.background,
                            ],
                            radius: 0.9,
                          ),
                        ),
                      ),
                      Center(
                        child: Container(
                          width: 110,
                          height: 110,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: food.color.withValues(alpha: 0.25),
                            border: Border.all(color: food.color.withValues(alpha: 0.8), width: 2.5),
                            boxShadow: [
                              BoxShadow(
                                color: food.color.withValues(alpha: 0.4),
                                blurRadius: 30,
                                spreadRadius: 4,
                              ),
                            ],
                          ),
                          child: Center(
                            child: Text(food.emoji, style: const TextStyle(fontSize: 54)),
                          ),
                        ).animate().scale(duration: 500.ms, curve: Curves.easeOutBack),
                      ),
                    ],

                    // Bottom Floating Cuisine Badge
                    Positioned(
                      bottom: 16,
                      left: 20,
                      child: FrostedGlassContainer(
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 7),
                        borderRadius: 20,
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Text(food.emoji, style: const TextStyle(fontSize: 16)),
                            const SizedBox(width: 6),
                            Text(
                              food.cuisineId.toUpperCase(),
                              style: AppTextStyles.bodySmall.copyWith(
                                color: AppColors.textPrimary,
                                fontWeight: FontWeight.w700,
                                letterSpacing: 1.5,
                              ),
                            ),
                          ],
                        ),
                      ).animate().fadeIn(duration: 400.ms).slideY(begin: 0.3, end: 0),
                    ),
                  ],
                ),
              ),
            ),

            // ─── Main Content ───
            SliverToBoxAdapter(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(20, 16, 20, 40),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Başlık
                    Text(
                      name,
                      style: AppTextStyles.displaySmall.copyWith(
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ).animate().fadeIn(duration: 300.ms),

                    const SizedBox(height: 8),

                    // Açıklama
                    if (description.isNotEmpty)
                      Text(
                        description,
                        style: AppTextStyles.bodyMedium.copyWith(
                          color: AppColors.textSecondary,
                          height: 1.5,
                        ),
                      ).animate().fadeIn(delay: 100.ms),

                    const SizedBox(height: 20),

                    // ─── Meta Bilgi Kartları (Kalori, Süre, Porsiyon, Zorluk) ───
                    Row(
                      children: [
                        Expanded(
                          child: _buildMetaCard(
                            icon: Icons.timer_outlined,
                            title: l10n?.detailPrepTime ?? 'Hazırlık',
                            value: l10n?.detailMinutes(food.prepTime) ?? '${food.prepTime} dk',
                            color: AppColors.primary,
                          ),
                        ),
                        const SizedBox(width: 8),
                        Expanded(
                          child: _buildMetaCard(
                            icon: Icons.soup_kitchen_outlined,
                            title: l10n?.detailCookTime ?? 'Pişirme',
                            value: l10n?.detailMinutes(food.cookTime) ?? '${food.cookTime} dk',
                            color: AppColors.accent,
                          ),
                        ),
                        const SizedBox(width: 8),
                        Expanded(
                          child: _buildMetaCard(
                            icon: Icons.local_fire_department_outlined,
                            title: l10n?.detailCalories ?? 'Kalori',
                            value: '${food.calories} kcal',
                            color: Colors.orangeAccent,
                          ),
                        ),
                        const SizedBox(width: 8),
                        Expanded(
                          child: _buildMetaCard(
                            icon: Icons.people_outline_rounded,
                            title: l10n?.detailServings ?? 'Porsiyon',
                            value: l10n?.detailServingsCount(food.servings) ?? '${food.servings} kişi',
                            color: Colors.greenAccent,
                          ),
                        ),
                      ],
                    ).animate().fadeIn(delay: 200.ms).slideY(begin: 0.1, end: 0),

                    const SizedBox(height: 28),

                    // ─── Malzemeler ───
                    Text(
                      l10n?.detailIngredients ?? 'Malzemeler',
                      style: AppTextStyles.headlineSmall.copyWith(
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                    const SizedBox(height: 12),

                    ...List.generate(ingredients.length, (index) {
                      final item = ingredients[index];
                      final isChecked = _checkedIngredients.contains(index);

                      return GestureDetector(
                        onTap: () {
                          HapticFeedback.selectionClick();
                          setState(() {
                            if (isChecked) {
                              _checkedIngredients.remove(index);
                            } else {
                              _checkedIngredients.add(index);
                            }
                          });
                        },
                        child: FrostedGlassContainer(
                          margin: const EdgeInsets.only(bottom: 8),
                          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                          borderRadius: 14,
                          child: Row(
                            children: [
                              Icon(
                                isChecked ? Icons.check_circle_rounded : Icons.circle_outlined,
                                color: isChecked ? AppColors.primary : AppColors.textMuted,
                                size: 22,
                              ),
                              const SizedBox(width: 14),
                              Expanded(
                                child: Text(
                                  item,
                                  style: AppTextStyles.bodyMedium.copyWith(
                                    color: isChecked ? AppColors.textMuted : AppColors.textPrimary,
                                    decoration: isChecked ? TextDecoration.lineThrough : null,
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      );
                    }).animate().fadeIn(delay: 300.ms),

                    const SizedBox(height: 28),

                    // ─── Hazırlanış Adımları ───
                    Text(
                      l10n?.detailSteps ?? 'Hazırlanış Adımları',
                      style: AppTextStyles.headlineSmall.copyWith(
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                    const SizedBox(height: 12),

                    ...List.generate(steps.length, (index) {
                      final step = steps[index];
                      return FrostedGlassContainer(
                        margin: const EdgeInsets.only(bottom: 12),
                        padding: const EdgeInsets.all(16),
                        borderRadius: 16,
                        child: Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Container(
                              width: 28,
                              height: 28,
                              decoration: BoxDecoration(
                                color: AppColors.primary.withValues(alpha: 0.2),
                                shape: BoxShape.circle,
                                border: Border.all(color: AppColors.primary, width: 1.5),
                              ),
                              child: Center(
                                child: Text(
                                  '${index + 1}',
                                  style: AppTextStyles.bodySmall.copyWith(
                                    color: AppColors.primary,
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ),
                            ),
                            const SizedBox(width: 14),
                            Expanded(
                              child: Text(
                                step,
                                style: AppTextStyles.bodyMedium.copyWith(
                                  color: AppColors.textPrimary,
                                  height: 1.5,
                                ),
                              ),
                            ),
                          ],
                        ),
                      );
                    }).animate().fadeIn(delay: 400.ms),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildMetaCard({
    required IconData icon,
    required String title,
    required String value,
    required Color color,
  }) {
    return FrostedGlassContainer(
      padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 6),
      borderRadius: 14,
      child: Column(
        children: [
          Icon(icon, color: color, size: 20),
          const SizedBox(height: 6),
          Text(
            title,
            style: AppTextStyles.labelSmall.copyWith(
              color: AppColors.textMuted,
              fontSize: 10,
            ),
            textAlign: TextAlign.center,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
          ),
          const SizedBox(height: 2),
          Text(
            value,
            style: AppTextStyles.bodySmall.copyWith(
              fontWeight: FontWeight.bold,
              color: Colors.white,
              fontSize: 11,
            ),
            textAlign: TextAlign.center,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
          ),
        ],
      ),
    );
  }
}
