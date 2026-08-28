import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class LocaleService extends ChangeNotifier {
  static final LocaleService instance = LocaleService._internal();
  LocaleService._internal();

  static const String _keyLocale = 'selected_locale_code';
  static const List<Locale> supportedLocales = [
    Locale('tr'),
    Locale('en'),
    Locale('es'),
    Locale('de'),
  ];

  Locale _currentLocale = const Locale('tr');
  Locale get currentLocale => _currentLocale;
  String get currentLanguageCode => _currentLocale.languageCode;

  Future<void> init() async {
    final prefs = await SharedPreferences.getInstance();
    final savedCode = prefs.getString(_keyLocale);
    if (savedCode != null && supportedLocales.any((l) => l.languageCode == savedCode)) {
      _currentLocale = Locale(savedCode);
    } else {
      // Default to device locale if supported, else 'tr'
      _currentLocale = const Locale('tr');
    }
    notifyListeners();
  }

  Future<void> setLocale(String languageCode) async {
    if (!supportedLocales.any((l) => l.languageCode == languageCode)) return;
    _currentLocale = Locale(languageCode);
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_keyLocale, languageCode);
    notifyListeners();
  }

  String getLanguageName(String code) {
    switch (code) {
      case 'tr':
        return 'Türkçe';
      case 'en':
        return 'English';
      case 'es':
        return 'Español';
      case 'de':
        return 'Deutsch';
      default:
        return code;
    }
  }

  String getLanguageFlag(String code) {
    switch (code) {
      case 'tr':
        return '🇹🇷';
      case 'en':
        return '🇬🇧';
      case 'es':
        return '🇪🇸';
      case 'de':
        return '🇩🇪';
      default:
        return '🌐';
    }
  }
}
