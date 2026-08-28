import 'package:flutter/material.dart';

/// Mutfak (Cuisine) veri modeli
class Cuisine {
  final String id;
  final String emoji;
  final String flagEmoji;
  final Color primaryColor;
  final Color secondaryColor;
  final String imagePath;
  final bool isPremium;
  final int foodCount;
  final int sortOrder;

  // Çoklu dil içerik
  final Map<String, String> name;
  final Map<String, String> description;

  const Cuisine({
    required this.id,
    required this.emoji,
    required this.flagEmoji,
    required this.primaryColor,
    required this.secondaryColor,
    this.imagePath = '',
    this.isPremium = false,
    this.foodCount = 0,
    this.sortOrder = 0,
    required this.name,
    this.description = const {},
  });

  /// Bayrak emojisi getter
  String get flag => flagEmoji;

  /// Dile göre isim döndürür
  String getName(String langCode) {
    return name[langCode] ?? name['en'] ?? name.values.first;
  }

  /// Dile göre açıklama döndürür
  String getDescription(String langCode) {
    if (description.isEmpty) return '';
    return description[langCode] ?? description['en'] ?? description.values.first;
  }

  /// JSON'dan Cuisine oluşturur
  factory Cuisine.fromJson(Map<String, dynamic> json) {
    return Cuisine(
      id: json['id'] as String,
      emoji: json['emoji'] as String,
      flagEmoji: json['flag'] as String,
      primaryColor: Color(int.parse(json['primaryColor'] as String, radix: 16)),
      secondaryColor: Color(int.parse(json['secondaryColor'] as String, radix: 16)),
      imagePath: json['image'] as String? ?? '',
      isPremium: json['isPremium'] as bool? ?? false,
      foodCount: json['foodCount'] as int? ?? 0,
      sortOrder: json['sortOrder'] as int? ?? 0,
      name: _parseMap(json['name']),
      description: _parseMap(json['description']),
    );
  }

  static Map<String, String> _parseMap(dynamic data) {
    if (data == null) return {};
    if (data is Map) {
      return data.map((k, v) => MapEntry(k.toString(), v.toString()));
    }
    return {};
  }
}
