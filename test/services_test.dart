import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:ne_yesek/data/models/wheel_filter.dart';
import 'package:ne_yesek/data/services/locale_service.dart';
import 'package:ne_yesek/data/services/purchase_service.dart';
import 'package:ne_yesek/data/services/favorites_service.dart';
import 'package:ne_yesek/data/services/history_service.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  setUp(() {
    SharedPreferences.setMockInitialValues({});
  });

  group('LocaleService Tests', () {
    test('LocaleService default and change locale', () async {
      final service = LocaleService.instance;
      await service.init();
      expect(service.currentLocale.languageCode, 'tr');

      await service.setLocale('en');
      expect(service.currentLocale.languageCode, 'en');
      expect(service.getLanguageName('en'), 'English');
      expect(service.getLanguageFlag('en'), '🇬🇧');

      await service.setLocale('es');
      expect(service.currentLocale.languageCode, 'es');

      await service.setLocale('de');
      expect(service.currentLocale.languageCode, 'de');
    });
  });

  group('PurchaseService Tests', () {
    test('Product IDs conform to bundle identifier format', () {
      expect(PurchaseService.productMonthly, 'com.neyesek.app.premium.monthly');
      expect(PurchaseService.productYearly, 'com.neyesek.app.premium.yearly');
      expect(PurchaseService.allProductIds.length, 2);
    });

    test('Debug Premium Toggle and Set', () async {
      final service = PurchaseService.instance;
      await service.init();
      expect(service.isPremium, false);

      await service.toggleDebugPremium();
      expect(service.isPremium, true);

      await service.setDebugPremium(false);
      expect(service.isPremium, false);

      await service.setDebugPremium(true);
      expect(service.isPremium, true);
    });
  });

  group('FavoritesService Tests', () {
    test('Toggle favorite and check', () async {
      final favService = FavoritesService.instance;
      expect(await favService.isFavorite('tr_kebap'), false);

      final added = await favService.toggleFavorite('tr_kebap');
      expect(added, true);
      expect(await favService.isFavorite('tr_kebap'), true);

      final removed = await favService.toggleFavorite('tr_kebap');
      expect(removed, false);
      expect(await favService.isFavorite('tr_kebap'), false);
    });
  });

  group('HistoryService Tests', () {
    test('Add history and clear', () async {
      final historyService = HistoryService.instance;
      await historyService.clearHistory();
      expect((await historyService.getHistoryItems()).isEmpty, true);

      await historyService.addHistory('tr_kebap');
      await historyService.addHistory('it_pizza');

      final items = await historyService.getHistoryItems();
      expect(items.length, 2);
      expect(items.first.foodId, 'it_pizza');

      await historyService.clearHistory();
      expect((await historyService.getHistoryItems()).isEmpty, true);
    });
  });

  group('WheelFilter Tests', () {
    test('WheelFilter copyWith and activeFilterCount', () {
      const filter = WheelFilter();
      expect(filter.hasActiveFilters, false);
      expect(filter.activeFilterCount, 0);

      final updated = filter.copyWith(
        selectedTag: 'vegetarian',
        maxTimeMinutes: 30,
        maxCalories: 500,
        difficulty: 'easy',
      );

      expect(updated.hasActiveFilters, true);
      expect(updated.activeFilterCount, 4);
      expect(updated.selectedTag, 'vegetarian');
      expect(updated.maxTimeMinutes, 30);
      expect(updated.maxCalories, 500);
      expect(updated.difficulty, 'easy');

      final cleared = updated.copyWith(clearTag: true, clearTime: true);
      expect(cleared.selectedTag, null);
      expect(cleared.maxTimeMinutes, null);
      expect(cleared.activeFilterCount, 2);
    });
  });
}
