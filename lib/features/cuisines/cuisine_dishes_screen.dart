import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';

import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/food_image.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../core/widgets/gradient_background.dart';
import '../../data/models/cuisine.dart';
import '../../data/models/food_item.dart';
import '../../data/services/food_service.dart';
import '../../l10n/app_localizations.dart';
import '../recipe_detail/recipe_detail_screen.dart';

class CuisineDishesScreen extends StatefulWidget {
  final Cuisine cuisine;

  const CuisineDishesScreen({super.key, required this.cuisine});

  @override
  State<CuisineDishesScreen> createState() => _CuisineDishesScreenState();
}

class _CuisineDishesScreenState extends State<CuisineDishesScreen> {
  List<FoodItem> _foods = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadFoods();
  }

  Future<void> _loadFoods() async {
    final foods = await FoodService.instance.getFoodsByCuisine(widget.cuisine.id);
    if (!mounted) return;
    setState(() {
      _foods = foods;
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final langCode = Localizations.localeOf(context).languageCode;
    final cuisine = widget.cuisine;

    return Scaffold(
      body: GradientBackground(
        child: SafeArea(
          child: Column(
            children: [
              // ─── Header Bar ───
              Padding(
                padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
                child: Row(
                  children: [
                    IconButton(
                      icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white),
                      onPressed: () => Navigator.pop(context),
                    ),
                    const SizedBox(width: 8),
                    Text(cuisine.emoji, style: const TextStyle(fontSize: 28)),
                    const SizedBox(width: 10),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            cuisine.getName(langCode),
                            style: AppTextStyles.headlineMedium.copyWith(color: Colors.white),
                          ),
                          Text(
                            l10n?.cuisineFoodsCount(_foods.length) ?? '${_foods.length} yemek',
                            style: AppTextStyles.bodySmall.copyWith(color: AppColors.textSecondary),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),

              // ─── Foods List ───
              Expanded(
                child: _isLoading
                    ? const Center(child: CircularProgressIndicator(color: AppColors.primary))
                    : _foods.isEmpty
                        ? Center(
                            child: Text(
                              'Bu mutfakta henüz yemek bulunmuyor.',
                              style: AppTextStyles.bodyMedium,
                            ),
                          )
                        : ListView.builder(
                            padding: const EdgeInsets.fromLTRB(20, 8, 20, 30),
                            physics: const BouncingScrollPhysics(),
                            itemCount: _foods.length,
                            itemBuilder: (context, index) {
                              final food = _foods[index];
                              return _buildFoodCard(food, langCode, l10n, index);
                            },
                          ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildFoodCard(FoodItem food, String langCode, AppLocalizations? l10n, int index) {
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => RecipeDetailScreen(food: food),
          ),
        );
      },
      child: FrostedGlassContainer(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.all(14),
        borderRadius: 18,
        child: Row(
          children: [
            // Image / Emoji container
            FoodImage(
              food: food,
              width: 58,
              height: 58,
              borderRadius: BorderRadius.circular(16),
              emojiSize: 26,
            ),
            const SizedBox(width: 14),

            // Name & Info
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
                  Row(
                    children: [
                      Icon(Icons.timer_outlined, size: 14, color: AppColors.textMuted),
                      const SizedBox(width: 4),
                      Text(
                        '${food.prepTime + food.cookTime} ${l10n?.detailMinutes(food.prepTime + food.cookTime) ?? 'dk'}',
                        style: AppTextStyles.labelSmall.copyWith(color: AppColors.textMuted),
                      ),
                      const SizedBox(width: 12),
                      Icon(Icons.local_fire_department_outlined, size: 14, color: AppColors.primary),
                      const SizedBox(width: 4),
                      Text(
                        '${food.calories} kcal',
                        style: AppTextStyles.labelSmall.copyWith(color: AppColors.textMuted),
                      ),
                      const SizedBox(width: 12),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                        decoration: BoxDecoration(
                          color: _getDifficultyColor(food.difficulty).withValues(alpha: 0.2),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Text(
                          _getDifficultyLabel(food.difficulty, l10n),
                          style: AppTextStyles.labelSmall.copyWith(
                            color: _getDifficultyColor(food.difficulty),
                            fontSize: 10,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),

            const Icon(Icons.arrow_forward_ios_rounded, color: AppColors.textMuted, size: 16),
          ],
        ),
      ),
    ).animate().fadeIn(delay: (50 * index).ms).slideX(begin: 0.1, end: 0);
  }

  Color _getDifficultyColor(String difficulty) {
    switch (difficulty.toLowerCase()) {
      case 'easy':
        return Colors.greenAccent;
      case 'medium':
        return Colors.amberAccent;
      case 'hard':
        return Colors.redAccent;
      default:
        return Colors.blueAccent;
    }
  }

  String _getDifficultyLabel(String difficulty, AppLocalizations? l10n) {
    switch (difficulty.toLowerCase()) {
      case 'easy':
        return l10n?.difficultyEasy ?? 'Kolay';
      case 'medium':
        return l10n?.difficultyMedium ?? 'Orta';
      case 'hard':
        return l10n?.difficultyHard ?? 'Zor';
      default:
        return difficulty;
    }
  }
}
