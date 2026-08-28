import 'package:shared_preferences/shared_preferences.dart';
import '../models/food_item.dart';
import 'food_service.dart';

class FavoritesService {
  static final FavoritesService instance = FavoritesService._internal();
  FavoritesService._internal();

  static const String _keyFavorites = 'favorite_food_ids';
  Set<String>? _favoriteIds;

  Future<Set<String>> getFavoriteIds() async {
    if (_favoriteIds != null) {
      return _favoriteIds!;
    }
    final prefs = await SharedPreferences.getInstance();
    final list = prefs.getStringList(_keyFavorites) ?? [];
    _favoriteIds = list.toSet();
    return _favoriteIds!;
  }

  Future<bool> isFavorite(String foodId) async {
    final favorites = await getFavoriteIds();
    return favorites.contains(foodId);
  }

  Future<bool> toggleFavorite(String foodId) async {
    final favorites = await getFavoriteIds();
    final isFav = favorites.contains(foodId);

    if (isFav) {
      favorites.remove(foodId);
    } else {
      favorites.add(foodId);
    }

    final prefs = await SharedPreferences.getInstance();
    await prefs.setStringList(_keyFavorites, favorites.toList());
    return !isFav;
  }

  Future<List<FoodItem>> getFavoriteFoods() async {
    final favIds = await getFavoriteIds();
    if (favIds.isEmpty) return [];

    final allFoods = await FoodService.instance.getAllFoods();
    return allFoods.where((food) => favIds.contains(food.id)).toList();
  }
}
