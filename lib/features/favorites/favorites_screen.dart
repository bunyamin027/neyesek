import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_animate/flutter_animate.dart';

import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/food_image.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../core/widgets/gradient_background.dart';
import '../../data/models/food_item.dart';
import '../../data/services/favorites_service.dart';
import '../../l10n/app_localizations.dart';
import '../recipe_detail/recipe_detail_screen.dart';

class FavoritesScreen extends StatefulWidget {
  const FavoritesScreen({super.key});

  @override
  State<FavoritesScreen> createState() => _FavoritesScreenState();
}

class _FavoritesScreenState extends State<FavoritesScreen> {
  List<FoodItem> _favoriteFoods = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadFavorites();
  }

  Future<void> _loadFavorites() async {
    final foods = await FavoritesService.instance.getFavoriteFoods();
    if (!mounted) return;
    setState(() {
      _favoriteFoods = foods;
      _isLoading = false;
    });
  }

  Future<void> _removeFavorite(FoodItem food) async {
    HapticFeedback.lightImpact();
    await FavoritesService.instance.toggleFavorite(food.id);
    _loadFavorites();
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final langCode = Localizations.localeOf(context).languageCode;

    return Scaffold(
      body: GradientBackground(
        child: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // ─── Üst Başlık ───
              Padding(
                padding: const EdgeInsets.fromLTRB(20, 16, 20, 12),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      l10n?.favoritesTitle ?? 'Favorilerim',
                      style: AppTextStyles.displaySmall.copyWith(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    if (_favoriteFoods.isNotEmpty)
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                        decoration: BoxDecoration(
                          color: AppColors.primary.withValues(alpha: 0.2),
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: AppColors.primary, width: 1),
                        ),
                        child: Text(
                          '${_favoriteFoods.length}',
                          style: AppTextStyles.labelLarge.copyWith(
                            color: AppColors.primary,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                  ],
                ),
              ).animate().fadeIn(duration: 400.ms),

              // ─── Liste ───
              Expanded(
                child: _isLoading
                    ? const Center(child: CircularProgressIndicator(color: AppColors.primary))
                    : _favoriteFoods.isEmpty
                        ? _buildEmptyState(l10n)
                        : ListView.builder(
                            padding: const EdgeInsets.fromLTRB(20, 8, 20, 30),
                            physics: const BouncingScrollPhysics(),
                            itemCount: _favoriteFoods.length,
                            itemBuilder: (context, index) {
                              final food = _favoriteFoods[index];
                              return _buildFavoriteItem(food, langCode, l10n, index);
                            },
                          ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildEmptyState(AppLocalizations? l10n) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 40),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: 90,
              height: 90,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: AppColors.frostedGlassDark,
              ),
              child: const Icon(
                Icons.favorite_border_rounded,
                color: AppColors.textMuted,
                size: 42,
              ),
            ),
            const SizedBox(height: 20),
            Text(
              l10n?.favoritesEmptyTitle ?? 'Henüz Favori Yok',
              style: AppTextStyles.headlineSmall.copyWith(color: Colors.white),
            ),
            const SizedBox(height: 8),
            Text(
              l10n?.favoritesEmptyDesc ?? 'Hızlıca erişmek istediğiniz tariflerin kalp simgesine dokunarak buraya kaydedin.',
              style: AppTextStyles.bodySmall.copyWith(color: AppColors.textMuted, height: 1.4),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    ).animate().fadeIn(duration: 500.ms);
  }

  Widget _buildFavoriteItem(FoodItem food, String langCode, AppLocalizations? l10n, int index) {
    return Dismissible(
      key: Key(food.id),
      direction: DismissDirection.endToStart,
      onDismissed: (_) => _removeFavorite(food),
      background: Container(
        alignment: Alignment.centerRight,
        padding: const EdgeInsets.only(right: 20),
        margin: const EdgeInsets.only(bottom: 12),
        decoration: BoxDecoration(
          color: Colors.redAccent.withValues(alpha: 0.8),
          borderRadius: BorderRadius.circular(18),
        ),
        child: const Icon(Icons.delete_outline_rounded, color: Colors.white, size: 28),
      ),
      child: GestureDetector(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => RecipeDetailScreen(food: food),
            ),
          ).then((_) => _loadFavorites());
        },
        child: FrostedGlassContainer(
          margin: const EdgeInsets.only(bottom: 12),
          padding: const EdgeInsets.all(14),
          borderRadius: 18,
          child: Row(
            children: [
              FoodImage(
                food: food,
                width: 54,
                height: 54,
                borderRadius: BorderRadius.circular(16),
                emojiSize: 26,
              ),
              const SizedBox(width: 14),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      food.getName(langCode),
                      style: AppTextStyles.titleMedium.copyWith(
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      '${food.cuisineId.toUpperCase()} • ${food.calories} kcal • ${food.prepTime + food.cookTime} ${l10n?.detailMinutes(food.prepTime + food.cookTime) ?? 'dk'}',
                      style: AppTextStyles.labelSmall.copyWith(color: AppColors.textMuted),
                    ),
                  ],
                ),
              ),
              IconButton(
                icon: const Icon(Icons.favorite_rounded, color: AppColors.accent, size: 24),
                onPressed: () => _removeFavorite(food),
              ),
            ],
          ),
        ),
      ),
    ).animate().fadeIn(delay: (40 * index).ms).slideX(begin: 0.1, end: 0);
  }
}
