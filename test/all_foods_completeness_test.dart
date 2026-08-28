import 'dart:convert';
import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:ne_yesek/data/models/food_item.dart';

void main() {
  test('Verify ALL foods across all cuisines have ingredients and steps in all 4 languages', () {
    final dir = Directory('assets/data/foods');
    final files = dir.listSync().whereType<File>().where((f) => f.path.endsWith('.json'));

    int totalFoods = 0;
    final List<String> issues = [];

    for (final file in files) {
      final content = file.readAsStringSync();
      final Map<String, dynamic> json = jsonDecode(content);
      final list = json['foods'] as List<dynamic>;

      for (final raw in list) {
        totalFoods++;
        final food = FoodItem.fromJson(raw as Map<String, dynamic>);
        
        for (final lang in ['tr', 'en', 'es', 'de']) {
          final name = food.getName(lang);
          final ings = food.getIngredients(lang);
          final steps = food.getSteps(lang);

          if (name.isEmpty) {
            issues.add('${food.id} missing name in $lang');
          }
          if (ings.isEmpty) {
            issues.add('${food.id} ($name) missing ingredients in $lang');
          }
          if (steps.isEmpty) {
            issues.add('${food.id} ($name) missing steps in $lang');
          }
        }
      }
    }

    expect(totalFoods, greaterThan(200));
    expect(issues.isEmpty, true, reason: 'Some dishes have empty ingredients or steps: $issues');
  });
}
