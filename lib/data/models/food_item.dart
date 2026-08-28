import 'package:flutter/material.dart';

/// Yemek öğesi veri modeli — Tam tarif desteği
class FoodItem {
  final String id;
  final String cuisineId;
  final String emoji;
  final String imagePath;
  final Color color;
  final int prepTimeMinutes;
  final int cookTimeMinutes;
  final String difficulty; // "easy", "medium", "hard"
  final int calories;
  final int servings;
  final bool isPremium;
  final List<String> tags;

  // Çoklu dil içerik — Map<langCode, value>
  final Map<String, String> name;
  final Map<String, String> description;
  final List<Map<String, String>> ingredients;
  final List<Map<String, String>> steps;

  const FoodItem({
    required this.id,
    required this.cuisineId,
    required this.emoji,
    this.imagePath = '',
    required this.color,
    this.prepTimeMinutes = 0,
    this.cookTimeMinutes = 0,
    this.difficulty = 'medium',
    this.calories = 0,
    this.servings = 2,
    this.isPremium = false,
    this.tags = const [],
    required this.name,
    this.description = const {},
    this.ingredients = const [],
    this.steps = const [],
  });

  /// Dile göre isim döndürür, fallback: en → ilk dil
  String getName(String langCode) {
    return name[langCode] ?? name['en'] ?? name.values.first;
  }

  /// Dile göre açıklama döndürür
  String getDescription(String langCode) {
    if (description.isEmpty) return '';
    return description[langCode] ?? description['en'] ?? description.values.first;
  }

  /// Dile göre malzeme listesi döndürür
  List<String> getIngredients(String langCode) {
    return ingredients
        .map((i) => i[langCode] ?? i['en'] ?? i.values.first)
        .toList();
  }

  /// Dile göre adım listesi döndürür
  List<String> getSteps(String langCode) {
    return steps
        .map((s) => s[langCode] ?? s['en'] ?? s.values.first)
        .toList();
  }

  /// Hazırlık ve pişirme süresi getter'ları
  int get prepTime => prepTimeMinutes;
  int get cookTime => cookTimeMinutes;

  /// Toplam süre (hazırlık + pişirme)
  int get totalTimeMinutes => prepTimeMinutes + cookTimeMinutes;

  /// Zorluk seviyesini emoji olarak döndürür
  String get difficultyEmoji {
    switch (difficulty) {
      case 'easy':
        return '🟢';
      case 'medium':
        return '🟡';
      case 'hard':
        return '🔴';
      default:
        return '🟡';
    }
  }

  /// Zorluk seviyesini dile göre metin olarak döndürür
  String getDifficultyText(String langCode) {
    final texts = {
      'easy': {'en': 'Easy', 'tr': 'Kolay', 'es': 'Fácil', 'de': 'Einfach'},
      'medium': {
        'en': 'Medium',
        'tr': 'Orta',
        'es': 'Media',
        'de': 'Mittel',
      },
      'hard': {
        'en': 'Hard',
        'tr': 'Zor',
        'es': 'Difícil',
        'de': 'Schwer',
      },
    };
    return texts[difficulty]?[langCode] ??
        texts[difficulty]?['en'] ??
        difficulty;
  }

  /// JSON'dan FoodItem oluşturur
  factory FoodItem.fromJson(Map<String, dynamic> json, {bool isPremium = false}) {
    return FoodItem(
      id: json['id'] as String,
      cuisineId: json['cuisineId'] as String,
      emoji: json['emoji'] as String,
      imagePath: json['image'] as String? ?? '',
      color: Color(int.parse(json['color'] as String, radix: 16)),
      prepTimeMinutes: json['prepTime'] as int? ?? 0,
      cookTimeMinutes: json['cookTime'] as int? ?? 0,
      difficulty: json['difficulty'] as String? ?? 'medium',
      calories: json['calories'] as int? ?? 0,
      servings: json['servings'] as int? ?? 2,
      isPremium: json['isPremium'] as bool? ?? isPremium,
      tags: (json['tags'] as List<dynamic>?)
              ?.map((t) => t as String)
              .toList() ??
          [],
      name: _parseLocalizedMap(json['name']),
      description: _parseLocalizedMap(json['description']),
      ingredients: _parseLocalizedList(json['ingredients']),
      steps: _parseLocalizedList(json['steps']),
    );
  }

  /// Lokalize map parse helper
  static Map<String, String> _parseLocalizedMap(dynamic data) {
    if (data == null) return {};
    if (data is Map) {
      return data.map((k, v) => MapEntry(k.toString(), v.toString()));
    }
    return {};
  }

  /// Lokalize list parse helper — `List<Map>` ve `Map<lang, List>` formatlarını destekler
  static List<Map<String, String>> _parseLocalizedList(dynamic data) {
    if (data == null) return [];
    if (data is List) {
      return data.map((item) {
        if (item is Map) {
          return item.map((k, v) => MapEntry(k.toString(), v.toString()));
        }
        return <String, String>{};
      }).toList();
    }
    if (data is Map) {
      final languages = data.keys.map((k) => k.toString()).toList();
      if (languages.isEmpty) return [];

      int maxLen = 0;
      for (final lang in languages) {
        final list = data[lang];
        if (list is List && list.length > maxLen) {
          maxLen = list.length;
        }
      }

      final List<Map<String, String>> result = [];
      for (int i = 0; i < maxLen; i++) {
        final Map<String, String> itemMap = {};
        for (final lang in languages) {
          final list = data[lang];
          if (list is List && i < list.length) {
            itemMap[lang] = list[i].toString();
          }
        }
        result.add(itemMap);
      }
      return result;
    }
    return [];
  }
}
