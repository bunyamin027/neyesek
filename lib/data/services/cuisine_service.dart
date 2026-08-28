import 'dart:convert';
import 'package:flutter/services.dart';
import '../models/cuisine.dart';

class CuisineService {
  static final CuisineService instance = CuisineService._internal();
  CuisineService._internal();

  List<Cuisine>? _cachedCuisines;

  Future<List<Cuisine>> getAllCuisines() async {
    if (_cachedCuisines != null && _cachedCuisines!.isNotEmpty) {
      return _cachedCuisines!;
    }

    try {
      final jsonString = await rootBundle.loadString('assets/data/cuisines.json');
      final Map<String, dynamic> data = json.decode(jsonString);
      final List<dynamic> list = data['cuisines'] as List<dynamic>;

      _cachedCuisines = list.map((json) => Cuisine.fromJson(json as Map<String, dynamic>)).toList()
        ..sort((a, b) => a.sortOrder.compareTo(b.sortOrder));

      return _cachedCuisines!;
    } catch (e) {
      return [];
    }
  }

  Future<Cuisine?> getCuisineById(String id) async {
    final cuisines = await getAllCuisines();
    try {
      return cuisines.firstWhere((c) => c.id == id);
    } catch (_) {
      return null;
    }
  }

  Future<List<Cuisine>> getFreeCuisines() async {
    final cuisines = await getAllCuisines();
    return cuisines.where((c) => !c.isPremium).toList();
  }

  Future<List<Cuisine>> getPremiumCuisines() async {
    final cuisines = await getAllCuisines();
    return cuisines.where((c) => c.isPremium).toList();
  }

  void clearCache() {
    _cachedCuisines = null;
  }
}
