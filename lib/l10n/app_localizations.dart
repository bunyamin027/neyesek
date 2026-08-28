import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:intl/intl.dart' as intl;

import 'app_localizations_de.dart';
import 'app_localizations_en.dart';
import 'app_localizations_es.dart';
import 'app_localizations_tr.dart';

// ignore_for_file: type=lint

/// Callers can lookup localized strings with an instance of AppLocalizations
/// returned by `AppLocalizations.of(context)`.
///
/// Applications need to include `AppLocalizations.delegate()` in their app's
/// `localizationDelegates` list, and the locales they support in the app's
/// `supportedLocales` list. For example:
///
/// ```dart
/// import 'l10n/app_localizations.dart';
///
/// return MaterialApp(
///   localizationsDelegates: AppLocalizations.localizationsDelegates,
///   supportedLocales: AppLocalizations.supportedLocales,
///   home: MyApplicationHome(),
/// );
/// ```
///
/// ## Update pubspec.yaml
///
/// Please make sure to update your pubspec.yaml to include the following
/// packages:
///
/// ```yaml
/// dependencies:
///   # Internationalization support.
///   flutter_localizations:
///     sdk: flutter
///   intl: any # Use the pinned version from flutter_localizations
///
///   # Rest of dependencies
/// ```
///
/// ## iOS Applications
///
/// iOS applications define key application metadata, including supported
/// locales, in an Info.plist file that is built into the application bundle.
/// To configure the locales supported by your app, you’ll need to edit this
/// file.
///
/// First, open your project’s ios/Runner.xcworkspace Xcode workspace file.
/// Then, in the Project Navigator, open the Info.plist file under the Runner
/// project’s Runner folder.
///
/// Next, select the Information Property List item, select Add Item from the
/// Editor menu, then select Localizations from the pop-up menu.
///
/// Select and expand the newly-created Localizations item then, for each
/// locale your application supports, add a new item and select the locale
/// you wish to add from the pop-up menu in the Value field. This list should
/// be consistent with the languages listed in the AppLocalizations.supportedLocales
/// property.
abstract class AppLocalizations {
  AppLocalizations(String locale)
    : localeName = intl.Intl.canonicalizedLocale(locale.toString());

  final String localeName;

  static AppLocalizations? of(BuildContext context) {
    return Localizations.of<AppLocalizations>(context, AppLocalizations);
  }

  static const LocalizationsDelegate<AppLocalizations> delegate =
      _AppLocalizationsDelegate();

  /// A list of this localizations delegate along with the default localizations
  /// delegates.
  ///
  /// Returns a list of localizations delegates containing this delegate along with
  /// GlobalMaterialLocalizations.delegate, GlobalCupertinoLocalizations.delegate,
  /// and GlobalWidgetsLocalizations.delegate.
  ///
  /// Additional delegates can be added by appending to this list in
  /// MaterialApp. This list does not have to be used at all if a custom list
  /// of delegates is preferred or required.
  static const List<LocalizationsDelegate<dynamic>> localizationsDelegates =
      <LocalizationsDelegate<dynamic>>[
        delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ];

  /// A list of this localizations delegate's supported locales.
  static const List<Locale> supportedLocales = <Locale>[
    Locale('de'),
    Locale('en'),
    Locale('es'),
    Locale('tr'),
  ];

  /// No description provided for @appName.
  ///
  /// In en, this message translates to:
  /// **'What to Eat?'**
  String get appName;

  /// No description provided for @appTagline.
  ///
  /// In en, this message translates to:
  /// **'Decide what to eat with a spin of the wheel!'**
  String get appTagline;

  /// No description provided for @navWheel.
  ///
  /// In en, this message translates to:
  /// **'Wheel'**
  String get navWheel;

  /// No description provided for @navCuisines.
  ///
  /// In en, this message translates to:
  /// **'Cuisines'**
  String get navCuisines;

  /// No description provided for @navFavorites.
  ///
  /// In en, this message translates to:
  /// **'Favorites'**
  String get navFavorites;

  /// No description provided for @navHistory.
  ///
  /// In en, this message translates to:
  /// **'History'**
  String get navHistory;

  /// No description provided for @navSettings.
  ///
  /// In en, this message translates to:
  /// **'Settings'**
  String get navSettings;

  /// No description provided for @wheelSpin.
  ///
  /// In en, this message translates to:
  /// **'SPIN THE WHEEL'**
  String get wheelSpin;

  /// No description provided for @wheelSpinning.
  ///
  /// In en, this message translates to:
  /// **'Deciding for you...'**
  String get wheelSpinning;

  /// No description provided for @wheelResultTitle.
  ///
  /// In en, this message translates to:
  /// **'Today\'s Suggestion!'**
  String get wheelResultTitle;

  /// No description provided for @wheelResultSubtitle.
  ///
  /// In en, this message translates to:
  /// **'We picked this delicious meal for you:'**
  String get wheelResultSubtitle;

  /// No description provided for @wheelSeeRecipe.
  ///
  /// In en, this message translates to:
  /// **'View Recipe & Details'**
  String get wheelSeeRecipe;

  /// No description provided for @wheelSpinAgain.
  ///
  /// In en, this message translates to:
  /// **'Spin Again'**
  String get wheelSpinAgain;

  /// No description provided for @wheelFilterCuisine.
  ///
  /// In en, this message translates to:
  /// **'Filter by Cuisine'**
  String get wheelFilterCuisine;

  /// No description provided for @wheelAllCuisines.
  ///
  /// In en, this message translates to:
  /// **'All Cuisines'**
  String get wheelAllCuisines;

  /// No description provided for @cuisineTitle.
  ///
  /// In en, this message translates to:
  /// **'World Cuisines'**
  String get cuisineTitle;

  /// No description provided for @cuisineSubtitle.
  ///
  /// In en, this message translates to:
  /// **'Explore delicious recipes from around the globe'**
  String get cuisineSubtitle;

  /// No description provided for @cuisineFoodsCount.
  ///
  /// In en, this message translates to:
  /// **'{count} dishes'**
  String cuisineFoodsCount(int count);

  /// No description provided for @cuisinePremiumBadge.
  ///
  /// In en, this message translates to:
  /// **'PREMIUM'**
  String get cuisinePremiumBadge;

  /// No description provided for @cuisineUnlock.
  ///
  /// In en, this message translates to:
  /// **'Unlock Cuisine'**
  String get cuisineUnlock;

  /// No description provided for @detailIngredients.
  ///
  /// In en, this message translates to:
  /// **'Ingredients'**
  String get detailIngredients;

  /// No description provided for @detailSteps.
  ///
  /// In en, this message translates to:
  /// **'Preparation Steps'**
  String get detailSteps;

  /// No description provided for @detailPrepTime.
  ///
  /// In en, this message translates to:
  /// **'Prep Time'**
  String get detailPrepTime;

  /// No description provided for @detailCookTime.
  ///
  /// In en, this message translates to:
  /// **'Cook Time'**
  String get detailCookTime;

  /// No description provided for @detailCalories.
  ///
  /// In en, this message translates to:
  /// **'Calories'**
  String get detailCalories;

  /// No description provided for @detailServings.
  ///
  /// In en, this message translates to:
  /// **'Servings'**
  String get detailServings;

  /// No description provided for @detailDifficulty.
  ///
  /// In en, this message translates to:
  /// **'Difficulty'**
  String get detailDifficulty;

  /// No description provided for @detailMinutes.
  ///
  /// In en, this message translates to:
  /// **'{min} min'**
  String detailMinutes(int min);

  /// No description provided for @detailCalorieUnit.
  ///
  /// In en, this message translates to:
  /// **'{cal} kcal'**
  String detailCalorieUnit(int cal);

  /// No description provided for @detailServingsCount.
  ///
  /// In en, this message translates to:
  /// **'{count} people'**
  String detailServingsCount(int count);

  /// No description provided for @difficultyEasy.
  ///
  /// In en, this message translates to:
  /// **'Easy'**
  String get difficultyEasy;

  /// No description provided for @difficultyMedium.
  ///
  /// In en, this message translates to:
  /// **'Medium'**
  String get difficultyMedium;

  /// No description provided for @difficultyHard.
  ///
  /// In en, this message translates to:
  /// **'Hard'**
  String get difficultyHard;

  /// No description provided for @favoritesTitle.
  ///
  /// In en, this message translates to:
  /// **'My Favorites'**
  String get favoritesTitle;

  /// No description provided for @favoritesEmptyTitle.
  ///
  /// In en, this message translates to:
  /// **'No Favorites Yet'**
  String get favoritesEmptyTitle;

  /// No description provided for @favoritesEmptyDesc.
  ///
  /// In en, this message translates to:
  /// **'Tap the heart icon on any recipe to save it here for quick access.'**
  String get favoritesEmptyDesc;

  /// No description provided for @favoritesRemoved.
  ///
  /// In en, this message translates to:
  /// **'Removed from favorites'**
  String get favoritesRemoved;

  /// No description provided for @favoritesAdded.
  ///
  /// In en, this message translates to:
  /// **'Added to favorites'**
  String get favoritesAdded;

  /// No description provided for @historyTitle.
  ///
  /// In en, this message translates to:
  /// **'Decision History'**
  String get historyTitle;

  /// No description provided for @historyEmptyTitle.
  ///
  /// In en, this message translates to:
  /// **'No History Yet'**
  String get historyEmptyTitle;

  /// No description provided for @historyEmptyDesc.
  ///
  /// In en, this message translates to:
  /// **'Spins you make on the wheel will be logged here.'**
  String get historyEmptyDesc;

  /// No description provided for @historyClear.
  ///
  /// In en, this message translates to:
  /// **'Clear History'**
  String get historyClear;

  /// No description provided for @historyClearConfirm.
  ///
  /// In en, this message translates to:
  /// **'Are you sure you want to clear your entire spin history?'**
  String get historyClearConfirm;

  /// No description provided for @historyCleared.
  ///
  /// In en, this message translates to:
  /// **'History cleared'**
  String get historyCleared;

  /// No description provided for @settingsTitle.
  ///
  /// In en, this message translates to:
  /// **'Settings'**
  String get settingsTitle;

  /// No description provided for @settingsLanguage.
  ///
  /// In en, this message translates to:
  /// **'Language'**
  String get settingsLanguage;

  /// No description provided for @settingsTheme.
  ///
  /// In en, this message translates to:
  /// **'Theme'**
  String get settingsTheme;

  /// No description provided for @settingsThemeDark.
  ///
  /// In en, this message translates to:
  /// **'Dark Mode'**
  String get settingsThemeDark;

  /// No description provided for @settingsSound.
  ///
  /// In en, this message translates to:
  /// **'Sound Effects'**
  String get settingsSound;

  /// No description provided for @settingsHaptic.
  ///
  /// In en, this message translates to:
  /// **'Haptic Feedback'**
  String get settingsHaptic;

  /// No description provided for @settingsPremium.
  ///
  /// In en, this message translates to:
  /// **'Premium Membership'**
  String get settingsPremium;

  /// No description provided for @settingsRestore.
  ///
  /// In en, this message translates to:
  /// **'Restore Purchases'**
  String get settingsRestore;

  /// No description provided for @settingsAbout.
  ///
  /// In en, this message translates to:
  /// **'About App'**
  String get settingsAbout;

  /// No description provided for @settingsVersion.
  ///
  /// In en, this message translates to:
  /// **'Version {version}'**
  String settingsVersion(String version);

  /// No description provided for @premiumTitle.
  ///
  /// In en, this message translates to:
  /// **'Unlock Full Access'**
  String get premiumTitle;

  /// No description provided for @premiumSubtitle.
  ///
  /// In en, this message translates to:
  /// **'Get all 10 world cuisines, unlimited spins, and ad-free experience!'**
  String get premiumSubtitle;

  /// No description provided for @premiumFeature1.
  ///
  /// In en, this message translates to:
  /// **'Unlock all 6 Premium World Cuisines'**
  String get premiumFeature1;

  /// No description provided for @premiumFeature2.
  ///
  /// In en, this message translates to:
  /// **'Access over 160+ detailed recipes'**
  String get premiumFeature2;

  /// No description provided for @premiumFeature3.
  ///
  /// In en, this message translates to:
  /// **'Custom filter & exclusion rules'**
  String get premiumFeature3;

  /// No description provided for @premiumFeature4.
  ///
  /// In en, this message translates to:
  /// **'Completely ad-free experience'**
  String get premiumFeature4;

  /// No description provided for @premiumBuyButton.
  ///
  /// In en, this message translates to:
  /// **'Get Premium Now'**
  String get premiumBuyButton;

  /// No description provided for @premiumRestore.
  ///
  /// In en, this message translates to:
  /// **'Restore Purchase'**
  String get premiumRestore;

  /// No description provided for @premiumSuccess.
  ///
  /// In en, this message translates to:
  /// **'Welcome to Premium!'**
  String get premiumSuccess;

  /// No description provided for @commonCancel.
  ///
  /// In en, this message translates to:
  /// **'Cancel'**
  String get commonCancel;

  /// No description provided for @commonConfirm.
  ///
  /// In en, this message translates to:
  /// **'Confirm'**
  String get commonConfirm;

  /// No description provided for @commonSave.
  ///
  /// In en, this message translates to:
  /// **'Save'**
  String get commonSave;

  /// No description provided for @commonClose.
  ///
  /// In en, this message translates to:
  /// **'Close'**
  String get commonClose;

  /// No description provided for @commonShare.
  ///
  /// In en, this message translates to:
  /// **'Share Recipe'**
  String get commonShare;

  /// No description provided for @commonShareText.
  ///
  /// In en, this message translates to:
  /// **'Look what I found on What to Eat app: {dishName}!'**
  String commonShareText(Object dishName);

  /// No description provided for @onboardingTitle1.
  ///
  /// In en, this message translates to:
  /// **'Can\'t Decide What to Eat?'**
  String get onboardingTitle1;

  /// No description provided for @onboardingSubtitle1.
  ///
  /// In en, this message translates to:
  /// **'Say goodbye to daily meal indecision with our fun decision wheel.'**
  String get onboardingSubtitle1;

  /// No description provided for @onboardingTitle2.
  ///
  /// In en, this message translates to:
  /// **'Spin the Wheel!'**
  String get onboardingTitle2;

  /// No description provided for @onboardingSubtitle2.
  ///
  /// In en, this message translates to:
  /// **'Let fate pick your next delicious meal with realistic sound and physics.'**
  String get onboardingSubtitle2;

  /// No description provided for @onboardingTitle3.
  ///
  /// In en, this message translates to:
  /// **'Discover World Cuisines'**
  String get onboardingTitle3;

  /// No description provided for @onboardingSubtitle3.
  ///
  /// In en, this message translates to:
  /// **'Over 160+ detailed recipes from 10 iconic world culinary traditions.'**
  String get onboardingSubtitle3;

  /// No description provided for @onboardingSkip.
  ///
  /// In en, this message translates to:
  /// **'Skip'**
  String get onboardingSkip;

  /// No description provided for @onboardingNext.
  ///
  /// In en, this message translates to:
  /// **'Next'**
  String get onboardingNext;

  /// No description provided for @onboardingStart.
  ///
  /// In en, this message translates to:
  /// **'Let\'s Get Started!'**
  String get onboardingStart;
}

class _AppLocalizationsDelegate
    extends LocalizationsDelegate<AppLocalizations> {
  const _AppLocalizationsDelegate();

  @override
  Future<AppLocalizations> load(Locale locale) {
    return SynchronousFuture<AppLocalizations>(lookupAppLocalizations(locale));
  }

  @override
  bool isSupported(Locale locale) =>
      <String>['de', 'en', 'es', 'tr'].contains(locale.languageCode);

  @override
  bool shouldReload(_AppLocalizationsDelegate old) => false;
}

AppLocalizations lookupAppLocalizations(Locale locale) {
  // Lookup logic when only language code is specified.
  switch (locale.languageCode) {
    case 'de':
      return AppLocalizationsDe();
    case 'en':
      return AppLocalizationsEn();
    case 'es':
      return AppLocalizationsEs();
    case 'tr':
      return AppLocalizationsTr();
  }

  throw FlutterError(
    'AppLocalizations.delegate failed to load unsupported locale "$locale". This is likely '
    'an issue with the localizations generation tool. Please file an issue '
    'on GitHub with a reproducible sample app and the gen-l10n configuration '
    'that was used.',
  );
}
