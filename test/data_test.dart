import 'dart:convert';
import 'dart:io';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('All cuisine JSON files must exist and be valid JSON', () {
    final cuisinesFile = File('assets/data/cuisines.json');
    expect(cuisinesFile.existsSync(), true);

    final cuisinesData = json.decode(cuisinesFile.readAsStringSync());
    final cuisinesList = cuisinesData['cuisines'] as List<dynamic>;
    expect(cuisinesList.length, 10);

    for (final c in cuisinesList) {
      final cuisineId = c['id'] as String;
      final foodFile = File('assets/data/foods/$cuisineId.json');
      expect(foodFile.existsSync(), true, reason: 'Food file missing for $cuisineId');

      final foodData = json.decode(foodFile.readAsStringSync());
      final foodsList = foodData['foods'] as List<dynamic>;
      expect(foodsList.isNotEmpty, true, reason: 'Food list empty for $cuisineId');

      for (final f in foodsList) {
        expect(f['id'], isNotNull);
        expect(f['name']['tr'], isNotNull);
        expect(f['name']['en'], isNotNull);
        expect(f['ingredients'], isNotEmpty);
        expect(f['steps'], isNotEmpty);
      }
    }
  });
}
