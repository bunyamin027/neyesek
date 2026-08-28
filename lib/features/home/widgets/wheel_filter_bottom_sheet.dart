import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../core/theme/app_colors.dart';
import '../../../core/theme/app_text_styles.dart';
import '../../../core/widgets/animated_button.dart';
import '../../../data/models/wheel_filter.dart';
import '../../../l10n/app_localizations.dart';

class WheelFilterBottomSheet extends StatefulWidget {
  final WheelFilter currentFilter;
  final ValueChanged<WheelFilter> onApply;

  const WheelFilterBottomSheet({
    super.key,
    required this.currentFilter,
    required this.onApply,
  });

  @override
  State<WheelFilterBottomSheet> createState() => _WheelFilterBottomSheetState();
}

class _WheelFilterBottomSheetState extends State<WheelFilterBottomSheet> {
  late WheelFilter _filter;

  @override
  void initState() {
    super.initState();
    _filter = widget.currentFilter;
  }

  void _clearAll() {
    HapticFeedback.lightImpact();
    setState(() {
      _filter = WheelFilter(cuisineId: _filter.cuisineId);
    });
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);

    final tags = [
      (tag: 'vegetarian', label: 'Vejetaryen', emoji: '🥗'),
      (tag: 'meat', label: 'Et / Tavuk', emoji: '🥩'),
      (tag: 'seafood', label: 'Deniz Ürünü', emoji: '🦐'),
      (tag: 'soup', label: 'Çorba', emoji: '🥣'),
      (tag: 'street_food', label: 'Sokak Lezzeti', emoji: '🌮'),
      (tag: 'dessert', label: 'Tatlı', emoji: '🍰'),
    ];

    final times = [
      (val: 15, label: '15 dk altı'),
      (val: 30, label: '30 dk altı'),
      (val: 60, label: '60 dk altı'),
    ];

    final calories = [
      (val: 300, label: '< 300 kcal'),
      (val: 500, label: '< 500 kcal'),
      (val: 800, label: '< 800 kcal'),
    ];

    final difficulties = [
      (val: 'easy', label: 'Kolay', color: Colors.greenAccent),
      (val: 'medium', label: 'Orta', color: Colors.amberAccent),
      (val: 'hard', label: 'Zor', color: Colors.redAccent),
    ];

    return Container(
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 30),
      decoration: BoxDecoration(
        color: AppColors.surface,
        borderRadius: const BorderRadius.vertical(top: Radius.circular(32)),
        border: Border.all(color: AppColors.glassBorder, width: 1.5),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Drag Handle
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
          const SizedBox(height: 14),

          // Header
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'Çark Filtreleri',
                style: AppTextStyles.titleLarge.copyWith(color: Colors.white, fontWeight: FontWeight.bold),
              ),
              if (_filter.hasActiveFilters)
                TextButton(
                  onPressed: _clearAll,
                  child: const Text('Temizle', style: TextStyle(color: AppColors.primary)),
                ),
            ],
          ),
          const SizedBox(height: 16),

          // ─── Yemek Türü ───
          Text('Yemek Türü / Kategori', style: AppTextStyles.bodySmall.copyWith(color: AppColors.textSecondary, fontWeight: FontWeight.w600)),
          const SizedBox(height: 8),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: tags.map((t) {
              final isSelected = _filter.selectedTag == t.tag;
              return _buildChoiceChip(
                label: '${t.emoji} ${t.label}',
                isSelected: isSelected,
                onTap: () {
                  setState(() {
                    _filter = _filter.copyWith(
                      selectedTag: isSelected ? null : t.tag,
                      clearTag: isSelected,
                    );
                  });
                },
              );
            }).toList(),
          ),

          const SizedBox(height: 18),

          // ─── Maksimum Süre ───
          Text('Maksimum Süre', style: AppTextStyles.bodySmall.copyWith(color: AppColors.textSecondary, fontWeight: FontWeight.w600)),
          const SizedBox(height: 8),
          Row(
            children: times.map((tm) {
              final isSelected = _filter.maxTimeMinutes == tm.val;
              return Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: _buildChoiceChip(
                    label: tm.label,
                    isSelected: isSelected,
                    onTap: () {
                      setState(() {
                        _filter = _filter.copyWith(
                          maxTimeMinutes: isSelected ? null : tm.val,
                          clearTime: isSelected,
                        );
                      });
                    },
                  ),
                ),
              );
            }).toList(),
          ),

          const SizedBox(height: 18),

          // ─── Kalori ───
          Text('Kalori Limiti', style: AppTextStyles.bodySmall.copyWith(color: AppColors.textSecondary, fontWeight: FontWeight.w600)),
          const SizedBox(height: 8),
          Row(
            children: calories.map((cal) {
              final isSelected = _filter.maxCalories == cal.val;
              return Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: _buildChoiceChip(
                    label: cal.label,
                    isSelected: isSelected,
                    onTap: () {
                      setState(() {
                        _filter = _filter.copyWith(
                          maxCalories: isSelected ? null : cal.val,
                          clearCalories: isSelected,
                        );
                      });
                    },
                  ),
                ),
              );
            }).toList(),
          ),

          const SizedBox(height: 18),

          // ─── Zorluk Derecesi ───
          Text(l10n?.detailDifficulty ?? 'Zorluk Derecesi', style: AppTextStyles.bodySmall.copyWith(color: AppColors.textSecondary, fontWeight: FontWeight.w600)),
          const SizedBox(height: 8),
          Row(
            children: difficulties.map((df) {
              final isSelected = _filter.difficulty == df.val;
              return Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: _buildChoiceChip(
                    label: df.label,
                    isSelected: isSelected,
                    onTap: () {
                      setState(() {
                        _filter = _filter.copyWith(
                          difficulty: isSelected ? null : df.val,
                          clearDifficulty: isSelected,
                        );
                      });
                    },
                  ),
                ),
              );
            }).toList(),
          ),

          const SizedBox(height: 24),

          // ─── Uygula Butonu ───
          AnimatedButton(
            text: 'Filtreleri Uygula (${_filter.activeFilterCount})',
            onPressed: () {
              HapticFeedback.mediumImpact();
              widget.onApply(_filter);
              Navigator.pop(context);
            },
            width: double.infinity,
            height: 52,
            icon: Icons.tune_rounded,
          ),
        ],
      ),
    );
  }

  Widget _buildChoiceChip({
    required String label,
    required bool isSelected,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: () {
        HapticFeedback.selectionClick();
        onTap();
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
        decoration: BoxDecoration(
          color: isSelected ? AppColors.primary : AppColors.frostedGlassDark,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isSelected ? AppColors.primaryLight : AppColors.glassBorder,
            width: 1.5,
          ),
        ),
        child: Center(
          child: Text(
            label,
            style: AppTextStyles.bodySmall.copyWith(
              color: isSelected ? Colors.white : AppColors.textSecondary,
              fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
              fontSize: 12,
            ),
          ),
        ),
      ),
    );
  }
}
