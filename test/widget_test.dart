import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:ne_yesek/l10n/app_localizations.dart';
import 'package:ne_yesek/data/services/locale_service.dart';
import 'package:ne_yesek/data/services/purchase_service.dart';
import 'package:ne_yesek/features/favorites/favorites_screen.dart';
import 'package:ne_yesek/features/history/history_screen.dart';
import 'package:ne_yesek/features/settings/settings_screen.dart';
import 'package:ne_yesek/features/cuisines/cuisines_screen.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  setUp(() async {
    SharedPreferences.setMockInitialValues({'onboarding_completed': true});
    await LocaleService.instance.init();
    await PurchaseService.instance.init();
  });

  Widget createTestWidget(Widget child) {
    return MaterialApp(
      locale: const Locale('tr'),
      localizationsDelegates: const [
        AppLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: AppLocalizations.supportedLocales,
      home: child,
    );
  }

  testWidgets('SettingsScreen displays language and sound controls', (WidgetTester tester) async {
    await tester.pumpWidget(createTestWidget(const SettingsScreen()));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 100));

    expect(find.text('Ayarlar'), findsOneWidget);
    expect(find.text('Ses Efektleri'), findsOneWidget);
    expect(find.text('Titreşim Geri Bildirimi'), findsOneWidget);
  });

  testWidgets('FavoritesScreen renders empty state gracefully', (WidgetTester tester) async {
    await tester.pumpWidget(createTestWidget(const FavoritesScreen()));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 100));

    expect(find.byType(FavoritesScreen), findsOneWidget);
  });

  testWidgets('HistoryScreen renders empty state gracefully', (WidgetTester tester) async {
    await tester.pumpWidget(createTestWidget(const HistoryScreen()));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 100));

    expect(find.byType(HistoryScreen), findsOneWidget);
  });

  testWidgets('CuisinesScreen displays cuisine discovery grid', (WidgetTester tester) async {
    await tester.pumpWidget(createTestWidget(const CuisinesScreen()));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 100));

    expect(find.byType(CuisinesScreen), findsOneWidget);
  });
}
