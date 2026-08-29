// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for English (`en`).
class AppLocalizationsEn extends AppLocalizations {
  AppLocalizationsEn([String locale = 'en']) : super(locale);

  @override
  String get appName => 'What to Eat?';

  @override
  String get appTagline => 'Decide what to eat with a spin of the wheel!';

  @override
  String get navWheel => 'Wheel';

  @override
  String get navCuisines => 'Cuisines';

  @override
  String get navFavorites => 'Favorites';

  @override
  String get navHistory => 'History';

  @override
  String get navSettings => 'Settings';

  @override
  String get wheelSpin => 'SPIN THE WHEEL';

  @override
  String get wheelSpinning => 'Deciding for you...';

  @override
  String get wheelResultTitle => 'Today\'s Suggestion!';

  @override
  String get wheelResultSubtitle => 'We picked this delicious meal for you:';

  @override
  String get wheelSeeRecipe => 'View Recipe & Details';

  @override
  String get wheelSpinAgain => 'Spin Again';

  @override
  String get wheelFilterCuisine => 'Filter by Cuisine';

  @override
  String get wheelAllCuisines => 'All Cuisines';

  @override
  String get cuisineTitle => 'World Cuisines';

  @override
  String get cuisineSubtitle =>
      'Explore delicious recipes from around the globe';

  @override
  String cuisineFoodsCount(int count) {
    return '$count dishes';
  }

  @override
  String get cuisinePremiumBadge => 'PREMIUM';

  @override
  String get cuisineUnlock => 'Unlock Cuisine';

  @override
  String get detailIngredients => 'Ingredients';

  @override
  String get detailSteps => 'Preparation Steps';

  @override
  String get detailPrepTime => 'Prep Time';

  @override
  String get detailCookTime => 'Cook Time';

  @override
  String get detailCalories => 'Calories';

  @override
  String get detailServings => 'Servings';

  @override
  String get detailDifficulty => 'Difficulty';

  @override
  String detailMinutes(int min) {
    return '$min min';
  }

  @override
  String detailCalorieUnit(int cal) {
    return '$cal kcal';
  }

  @override
  String detailServingsCount(int count) {
    return '$count people';
  }

  @override
  String get difficultyEasy => 'Easy';

  @override
  String get difficultyMedium => 'Medium';

  @override
  String get difficultyHard => 'Hard';

  @override
  String get favoritesTitle => 'My Favorites';

  @override
  String get favoritesEmptyTitle => 'No Favorites Yet';

  @override
  String get favoritesEmptyDesc =>
      'Tap the heart icon on any recipe to save it here for quick access.';

  @override
  String get favoritesRemoved => 'Removed from favorites';

  @override
  String get favoritesAdded => 'Added to favorites';

  @override
  String get historyTitle => 'Decision History';

  @override
  String get historyEmptyTitle => 'No History Yet';

  @override
  String get historyEmptyDesc =>
      'Spins you make on the wheel will be logged here.';

  @override
  String get historyClear => 'Clear History';

  @override
  String get historyClearConfirm =>
      'Are you sure you want to clear your entire spin history?';

  @override
  String get historyCleared => 'History cleared';

  @override
  String get settingsTitle => 'Settings';

  @override
  String get settingsLanguage => 'Language';

  @override
  String get settingsTheme => 'Theme';

  @override
  String get settingsThemeDark => 'Dark Mode';

  @override
  String get settingsSound => 'Sound Effects';

  @override
  String get settingsHaptic => 'Haptic Feedback';

  @override
  String get settingsPremium => 'Premium Membership';

  @override
  String get settingsRestore => 'Restore Purchases';

  @override
  String get settingsAbout => 'About App';

  @override
  String settingsVersion(String version) {
    return 'Version $version';
  }

  @override
  String get settingsPremiumDesc => 'Unlock all cuisines and recipes';

  @override
  String get settingsEula => 'Terms of Use (EULA)';

  @override
  String get settingsPrivacy => 'Privacy Policy';

  @override
  String get settingsSupport => 'Support & Feedback';

  @override
  String get settingsDeveloper => 'Developer';

  @override
  String get settingsDeveloperContact =>
      'Developer: kahramanapp • Contact: kahramandev01@gmail.com';

  @override
  String get settingsCopyright => '© 2026 What to Eat? — All rights reserved';

  @override
  String get premiumTitle => 'Unlock Full Access';

  @override
  String get premiumSubtitle =>
      'Get all 10 world cuisines, unlimited spins, and ad-free experience!';

  @override
  String get premiumHeaderTitle => 'What to Eat? Premium';

  @override
  String get premiumHeaderSubtitle =>
      '10 World Cuisines, 212+ Authentic Recipes & Ad-Free Gourmet Experience';

  @override
  String get premiumFeature1 => 'Full Access to All 10 World Cuisines';

  @override
  String get premiumFeature1Desc =>
      'Unlock Japanese, Korean, Mexican, French, Indian and Chinese cuisines.';

  @override
  String get premiumFeature2 => '212+ Detailed Authentic Recipes';

  @override
  String get premiumFeature2Desc =>
      'Ingredient lists, calories, timing and step-by-step cooking guides.';

  @override
  String get premiumFeature3 => 'Smart Wheel Filters';

  @override
  String get premiumFeature3Desc =>
      'Apply vegetarian, quick cook, low calorie or difficulty filters freely.';

  @override
  String get premiumFeature4 => 'Zero Ads, Uninterrupted Flow';

  @override
  String get premiumFeature4Desc =>
      'A fast and enjoyable gourmet experience without any interruptions.';

  @override
  String get premiumPlanMonthly => 'Monthly Plan';

  @override
  String get premiumPlanYearly => 'Yearly Plan';

  @override
  String get premiumPlanMonthlySubtitle =>
      'Flexible membership, cancel anytime';

  @override
  String get premiumPlanYearlySubtitle =>
      '12 months unlimited access • Best value';

  @override
  String get premiumPlanSaveBadge => 'SAVE 50%';

  @override
  String get premiumPerMonth => '/ month';

  @override
  String get premiumPerYear => '/ year';

  @override
  String get premiumCtaYearly => 'Get Yearly Premium';

  @override
  String get premiumCtaMonthly => 'Get Monthly Premium';

  @override
  String get premiumProcessing => 'Processing...';

  @override
  String get premiumBuyButton => 'Get Premium Now';

  @override
  String get premiumRestore => 'Restore';

  @override
  String get premiumSuccess => 'Welcome to Premium! 🎉';

  @override
  String get premiumRestoreSuccess =>
      'Your premium membership has been restored! 🎉';

  @override
  String get premiumRestoreNone =>
      'Purchases checked. No active subscription found.';

  @override
  String get premiumDisclosure =>
      'Payment is charged to your Apple ID account upon confirmation. Subscription automatically renews unless cancelled at least 24 hours before the end of the current period. Renewal is charged within 24 hours prior to the end of the current period. You can manage or cancel your subscription in Account Settings after purchase.';

  @override
  String get premiumEula => 'Terms of Use (EULA)';

  @override
  String get premiumPrivacy => 'Privacy Policy';

  @override
  String get commonCancel => 'Cancel';

  @override
  String get commonConfirm => 'Confirm';

  @override
  String get commonSave => 'Save';

  @override
  String get commonClose => 'Close';

  @override
  String get commonShare => 'Share Recipe';

  @override
  String commonShareText(Object dishName) {
    return 'Look what I found on What to Eat app: $dishName!';
  }

  @override
  String get onboardingTitle1 => 'Can\'t Decide What to Eat?';

  @override
  String get onboardingSubtitle1 =>
      'Say goodbye to daily meal indecision with our fun decision wheel.';

  @override
  String get onboardingTitle2 => 'Spin the Wheel!';

  @override
  String get onboardingSubtitle2 =>
      'Let fate pick your next delicious meal with realistic sound and physics.';

  @override
  String get onboardingTitle3 => 'Discover World Cuisines';

  @override
  String get onboardingSubtitle3 =>
      'Over 160+ detailed recipes from 10 iconic world culinary traditions.';

  @override
  String get onboardingSkip => 'Skip';

  @override
  String get onboardingNext => 'Next';

  @override
  String get onboardingStart => 'Let\'s Get Started!';
}
