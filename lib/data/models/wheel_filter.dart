class WheelFilter {
  final String cuisineId; // 'all' or specific cuisine id
  final String? selectedTag; // 'vegetarian', 'meat', 'seafood', 'dessert', 'soup', 'breakfast', 'street_food'
  final int? maxTimeMinutes; // 15, 30, 60
  final int? maxCalories; // 300, 500, 700
  final String? difficulty; // 'easy', 'medium', 'hard'
  final Set<String> excludedFoodIds;

  const WheelFilter({
    this.cuisineId = 'all',
    this.selectedTag,
    this.maxTimeMinutes,
    this.maxCalories,
    this.difficulty,
    this.excludedFoodIds = const {},
  });

  WheelFilter copyWith({
    String? cuisineId,
    String? selectedTag,
    bool clearTag = false,
    int? maxTimeMinutes,
    bool clearTime = false,
    int? maxCalories,
    bool clearCalories = false,
    String? difficulty,
    bool clearDifficulty = false,
    Set<String>? excludedFoodIds,
  }) {
    return WheelFilter(
      cuisineId: cuisineId ?? this.cuisineId,
      selectedTag: clearTag ? null : (selectedTag ?? this.selectedTag),
      maxTimeMinutes: clearTime ? null : (maxTimeMinutes ?? this.maxTimeMinutes),
      maxCalories: clearCalories ? null : (maxCalories ?? this.maxCalories),
      difficulty: clearDifficulty ? null : (difficulty ?? this.difficulty),
      excludedFoodIds: excludedFoodIds ?? this.excludedFoodIds,
    );
  }

  bool get hasActiveFilters =>
      (selectedTag != null && selectedTag!.isNotEmpty) ||
      maxTimeMinutes != null ||
      maxCalories != null ||
      (difficulty != null && difficulty!.isNotEmpty) ||
      excludedFoodIds.isNotEmpty;

  int get activeFilterCount {
    int count = 0;
    if (selectedTag != null && selectedTag!.isNotEmpty) count++;
    if (maxTimeMinutes != null) count++;
    if (maxCalories != null) count++;
    if (difficulty != null && difficulty!.isNotEmpty) count++;
    if (excludedFoodIds.isNotEmpty) count++;
    return count;
  }
}
