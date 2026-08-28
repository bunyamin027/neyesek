import 'package:flutter/material.dart';
import 'package:flutter_fortune_wheel/flutter_fortune_wheel.dart';

import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_text_styles.dart';
import '../../../data/models/food_item.dart';

/// Yemek Çarkı Widget'ı
/// flutter_fortune_wheel üzerine custom tasarım.
class FoodWheel extends StatelessWidget {
  final List<FoodItem> foods;
  final Stream<int> selectedStream;
  final VoidCallback onAnimationEnd;

  const FoodWheel({
    super.key,
    required this.foods,
    required this.selectedStream,
    required this.onAnimationEnd,
  });

  @override
  Widget build(BuildContext context) {
    return FortuneWheel(
      selected: selectedStream,
      onAnimationEnd: onAnimationEnd,
      physics: CircularPanPhysics(
        duration: const Duration(seconds: 1),
        curve: Curves.decelerate,
      ),
      animateFirst: false,
      duration: const Duration(seconds: 4),
      indicators: [
        FortuneIndicator(
          alignment: Alignment.topCenter,
          child: _buildIndicator(),
        ),
      ],
      items: List.generate(foods.length, (index) {
        final food = foods[index];
        final langCode = Localizations.localeOf(context).languageCode;
        return FortuneItem(
          style: FortuneItemStyle(
            color: food.color,
            borderColor: food.color.withValues(alpha: 0.8),
            borderWidth: 2,
            textAlign: TextAlign.center,
            textStyle: AppTextStyles.wheelItem,
          ),
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 4),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Text(food.emoji, style: const TextStyle(fontSize: 18)),
                const SizedBox(width: 4),
                Flexible(
                  child: Text(
                    food.getName(langCode),
                    style: AppTextStyles.wheelItem,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
              ],
            ),
          ),
        );
      }),
    );
  }

  /// Çark göstergesi (indicator / ok)
  Widget _buildIndicator() {
    return Container(
      width: 36,
      height: 36,
      decoration: BoxDecoration(
        color: AppColors.background,
        shape: BoxShape.circle,
        border: Border.all(color: AppColors.primary, width: 3),
        boxShadow: [
          BoxShadow(
            color: AppColors.primary.withValues(alpha: 0.5),
            blurRadius: 12,
            spreadRadius: 2,
          ),
        ],
      ),
      child: const Icon(
        Icons.arrow_downward_rounded,
        color: AppColors.primary,
        size: 18,
      ),
    );
  }
}
