import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/food_item.dart';
import 'food_service.dart';

class SpinHistoryItem {
  final String foodId;
  final DateTime timestamp;

  SpinHistoryItem({
    required this.foodId,
    required this.timestamp,
  });

  Map<String, dynamic> toJson() => {
    'foodId': foodId,
    'timestamp': timestamp.toIso8601String(),
  };

  factory SpinHistoryItem.fromJson(Map<String, dynamic> json) => SpinHistoryItem(
    foodId: json['foodId'] as String,
    timestamp: DateTime.parse(json['timestamp'] as String),
  );
}

class HistoryService {
  static final HistoryService instance = HistoryService._internal();
  HistoryService._internal();

  static const String _keyHistory = 'spin_history_list';
  static const int _maxHistoryCount = 50;

  Future<List<SpinHistoryItem>> getHistoryItems() async {
    final prefs = await SharedPreferences.getInstance();
    final jsonList = prefs.getStringList(_keyHistory) ?? [];

    return jsonList
        .map((item) {
          try {
            return SpinHistoryItem.fromJson(json.decode(item) as Map<String, dynamic>);
          } catch (_) {
            return null;
          }
        })
        .whereType<SpinHistoryItem>()
        .toList()
      ..sort((a, b) => b.timestamp.compareTo(a.timestamp));
  }

  Future<void> addHistory(String foodId) async {
    final prefs = await SharedPreferences.getInstance();
    final currentList = await getHistoryItems();

    final newItem = SpinHistoryItem(foodId: foodId, timestamp: DateTime.now());
    currentList.insert(0, newItem);

    if (currentList.length > _maxHistoryCount) {
      currentList.removeRange(_maxHistoryCount, currentList.length);
    }

    final jsonList = currentList.map((i) => json.encode(i.toJson())).toList();
    await prefs.setStringList(_keyHistory, jsonList);
  }

  Future<void> clearHistory() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_keyHistory);
  }

  Future<List<(FoodItem, DateTime)>> getHistoryWithFoods() async {
    final historyItems = await getHistoryItems();
    if (historyItems.isEmpty) return [];

    final allFoods = await FoodService.instance.getAllFoods();
    final Map<String, FoodItem> foodMap = {for (var f in allFoods) f.id: f};

    final List<(FoodItem, DateTime)> results = [];
    for (final item in historyItems) {
      final food = foodMap[item.foodId];
      if (food != null) {
        results.add((food, item.timestamp));
      }
    }
    return results;
  }
}
