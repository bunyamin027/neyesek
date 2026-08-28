import 'dart:convert';
import 'dart:math';
import 'package:flutter/services.dart';
import '../models/food_item.dart';
import '../models/wheel_filter.dart';
import 'cuisine_service.dart';

class FoodService {
  static final FoodService instance = FoodService._internal();
  FoodService._internal();

  final Map<String, List<FoodItem>> _cachedFoodsByCuisine = {};
  List<FoodItem>? _cachedAllFoods;

  Future<List<FoodItem>> getFoodsByCuisine(String cuisineId) async {
    if (_cachedFoodsByCuisine.containsKey(cuisineId)) {
      return _cachedFoodsByCuisine[cuisineId]!;
    }

    try {
      final path = 'assets/data/foods/$cuisineId.json';
      final jsonString = await rootBundle.loadString(path);
      final Map<String, dynamic> data = json.decode(jsonString);
      final List<dynamic> list = data['foods'] as List<dynamic>;

      final foods = list.map((item) => FoodItem.fromJson(item as Map<String, dynamic>)).toList();
      _cachedFoodsByCuisine[cuisineId] = foods;
      return foods;
    } catch (e) {
      return [];
    }
  }

  Future<List<FoodItem>> getAllFoods() async {
    if (_cachedAllFoods != null && _cachedAllFoods!.isNotEmpty) {
      return _cachedAllFoods!;
    }

    final cuisines = await CuisineService.instance.getAllCuisines();
    final List<FoodItem> all = [];

    for (final cuisine in cuisines) {
      final foods = await getFoodsByCuisine(cuisine.id);
      all.addAll(foods);
    }

    _cachedAllFoods = all;
    return all;
  }

  Future<FoodItem?> getFoodById(String foodId) async {
    final allFoods = await getAllFoods();
    try {
      return allFoods.firstWhere((f) => f.id == foodId);
    } catch (_) {
      return null;
    }
  }

  Future<List<FoodItem>> getFoodsForWheel({
    String? selectedCuisineId,
    WheelFilter? filter,
    bool isPremiumUser = false,
  }) async {
    final targetCuisineId = filter?.cuisineId ?? selectedCuisineId;
    List<FoodItem> list;

    if (targetCuisineId != null && targetCuisineId.isNotEmpty && targetCuisineId != 'all') {
      list = await getFoodsByCuisine(targetCuisineId);
    } else {
      list = await getAllFoods();
    }

    if (!isPremiumUser) {
      list = list.where((f) => !f.isPremium).toList();
    }

    if (filter != null) {
      if (filter.selectedTag != null && filter.selectedTag!.isNotEmpty) {
        list = list.where((f) => f.tags.contains(filter.selectedTag)).toList();
      }

      if (filter.maxTimeMinutes != null) {
        list = list.where((f) => f.totalTimeMinutes <= filter.maxTimeMinutes!).toList();
      }

      if (filter.maxCalories != null) {
        list = list.where((f) => f.calories <= filter.maxCalories!).toList();
      }

      if (filter.difficulty != null && filter.difficulty!.isNotEmpty) {
        list = list.where((f) => f.difficulty.toLowerCase() == filter.difficulty!.toLowerCase()).toList();
      }

      if (filter.excludedFoodIds.isNotEmpty) {
        list = list.where((f) => !filter.excludedFoodIds.contains(f.id)).toList();
      }
    }

    return list;
  }

  Future<FoodItem?> getRandomFood({
    String? selectedCuisineId,
    bool isPremiumUser = false,
  }) async {
    final availableFoods = await getFoodsForWheel(
      selectedCuisineId: selectedCuisineId,
      isPremiumUser: isPremiumUser,
    );

    if (availableFoods.isEmpty) return null;
    final random = Random();
    return availableFoods[random.nextInt(availableFoods.length)];
  }

  void clearCache() {
    _cachedFoodsByCuisine.clear();
    _cachedAllFoods = null;
  }
}
