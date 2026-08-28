// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for German (`de`).
class AppLocalizationsDe extends AppLocalizations {
  AppLocalizationsDe([String locale = 'de']) : super(locale);

  @override
  String get appName => 'Was Essen Wir?';

  @override
  String get appTagline =>
      'Entscheide mit einem Dreh am Glücksrad, was du heute isst!';

  @override
  String get navWheel => 'Glücksrad';

  @override
  String get navCuisines => 'Küchen';

  @override
  String get navFavorites => 'Favoriten';

  @override
  String get navHistory => 'Verlauf';

  @override
  String get navSettings => 'Einstellungen';

  @override
  String get wheelSpin => 'RAD DREHEN';

  @override
  String get wheelSpinning => 'Entscheidung läuft...';

  @override
  String get wheelResultTitle => 'Heutiger Vorschlag!';

  @override
  String get wheelResultSubtitle =>
      'Wir haben dieses köstliche Gericht für dich ausgewählt:';

  @override
  String get wheelSeeRecipe => 'Rezept & Details ansehen';

  @override
  String get wheelSpinAgain => 'Nochmal drehen';

  @override
  String get wheelFilterCuisine => 'Nach Küche filtern';

  @override
  String get wheelAllCuisines => 'Alle Küchen';

  @override
  String get cuisineTitle => 'Weltküchen';

  @override
  String get cuisineSubtitle => 'Entdecke köstliche Rezepte aus aller Welt';

  @override
  String cuisineFoodsCount(int count) {
    return '$count Gerichte';
  }

  @override
  String get cuisinePremiumBadge => 'PREMIUM';

  @override
  String get cuisineUnlock => 'Küche freischalten';

  @override
  String get detailIngredients => 'Zutaten';

  @override
  String get detailSteps => 'Zubereitungsschritte';

  @override
  String get detailPrepTime => 'Vorbereitung';

  @override
  String get detailCookTime => 'Kochzeit';

  @override
  String get detailCalories => 'Kalorien';

  @override
  String get detailServings => 'Portionen';

  @override
  String get detailDifficulty => 'Schwierigkeit';

  @override
  String detailMinutes(int min) {
    return '$min Min.';
  }

  @override
  String detailCalorieUnit(int cal) {
    return '$cal kcal';
  }

  @override
  String detailServingsCount(int count) {
    return '$count Personen';
  }

  @override
  String get difficultyEasy => 'Einfach';

  @override
  String get difficultyMedium => 'Mittel';

  @override
  String get difficultyHard => 'Schwer';

  @override
  String get favoritesTitle => 'Meine Favoriten';

  @override
  String get favoritesEmptyTitle => 'Noch keine Favoriten';

  @override
  String get favoritesEmptyDesc =>
      'Tippe auf das Herzsymbol bei jedem Rezept, um es hier schnell griffbereit zu haben.';

  @override
  String get favoritesRemoved => 'Aus Favoriten entfernt';

  @override
  String get favoritesAdded => 'Zu Favoriten hinzugefügt';

  @override
  String get historyTitle => 'Entscheidungsverlauf';

  @override
  String get historyEmptyTitle => 'Noch kein Verlauf';

  @override
  String get historyEmptyDesc =>
      'Deine Drehungen am Rad werden hier protokolliert.';

  @override
  String get historyClear => 'Verlauf löschen';

  @override
  String get historyClearConfirm =>
      'Möchtest du wirklich deinen gesamten Verlauf löschen?';

  @override
  String get historyCleared => 'Verlauf gelöscht';

  @override
  String get settingsTitle => 'Einstellungen';

  @override
  String get settingsLanguage => 'Sprache';

  @override
  String get settingsTheme => 'Design';

  @override
  String get settingsThemeDark => 'Dunkelmodus';

  @override
  String get settingsSound => 'Soundeffekte';

  @override
  String get settingsHaptic => 'Haptisches Feedback';

  @override
  String get settingsPremium => 'Premium-Mitgliedschaft';

  @override
  String get settingsRestore => 'Käufe wiederherstellen';

  @override
  String get settingsAbout => 'Über die App';

  @override
  String settingsVersion(String version) {
    return 'Version $version';
  }

  @override
  String get premiumTitle => 'Vollzugriff freischalten';

  @override
  String get premiumSubtitle =>
      'Hol dir alle 10 Weltküchen, unbegrenzte Drehungen und ein werbefreies Erlebnis!';

  @override
  String get premiumFeature1 => 'Alle 6 Premium-Weltküchen freischalten';

  @override
  String get premiumFeature2 => 'Zugriff auf über 160 detaillierte Rezepte';

  @override
  String get premiumFeature3 => 'Eigene Filter- und Ausschlussregeln';

  @override
  String get premiumFeature4 => 'Vollständig werbefreies Erlebnis';

  @override
  String get premiumBuyButton => 'Jetzt Premium sichern';

  @override
  String get premiumRestore => 'Kauf wiederherstellen';

  @override
  String get premiumSuccess => 'Willkommen bei Premium!';

  @override
  String get commonCancel => 'Abbrechen';

  @override
  String get commonConfirm => 'Bestätigen';

  @override
  String get commonSave => 'Speichern';

  @override
  String get commonClose => 'Schließen';

  @override
  String get commonShare => 'Rezept Teilen';

  @override
  String commonShareText(Object dishName) {
    return 'Schau mal, was ich in der Was Essen App gefunden habe: $dishName!';
  }

  @override
  String get onboardingTitle1 => 'Keine Ahnung, was du essen sollst?';

  @override
  String get onboardingSubtitle1 =>
      'Mach Schluss mit der täglichen Unentschlossenheit beim Essen!';

  @override
  String get onboardingTitle2 => 'Dreh das Glücksrad!';

  @override
  String get onboardingSubtitle2 =>
      'Überlass die Entscheidung dem Zufall mit realistischen Klängen.';

  @override
  String get onboardingTitle3 => 'Entdecke Weltküchen';

  @override
  String get onboardingSubtitle3 =>
      'Über 160 detaillierte Rezepte aus 10 Weltküchen.';

  @override
  String get onboardingSkip => 'Überspringen';

  @override
  String get onboardingNext => 'Weiter';

  @override
  String get onboardingStart => 'Jetzt Starten!';
}
