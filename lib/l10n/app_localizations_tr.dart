// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for Turkish (`tr`).
class AppLocalizationsTr extends AppLocalizations {
  AppLocalizationsTr([String locale = 'tr']) : super(locale);

  @override
  String get appName => 'Ne Yesek?';

  @override
  String get appTagline => 'Bugün ne yiyeceğine çarkı çevirerek karar ver!';

  @override
  String get navWheel => 'Çark';

  @override
  String get navCuisines => 'Mutfaklar';

  @override
  String get navFavorites => 'Favoriler';

  @override
  String get navHistory => 'Geçmiş';

  @override
  String get navSettings => 'Ayarlar';

  @override
  String get wheelSpin => 'ÇARKI ÇEVİR';

  @override
  String get wheelSpinning => 'Senin için seçiliyor...';

  @override
  String get wheelResultTitle => 'Günün Önerisi!';

  @override
  String get wheelResultSubtitle => 'Senin için bu lezzetli yemeği seçtik:';

  @override
  String get wheelSeeRecipe => 'Tarifi ve Detayları Gör';

  @override
  String get wheelSpinAgain => 'Tekrar Çevir';

  @override
  String get wheelFilterCuisine => 'Mutfağa Göre Filtrele';

  @override
  String get wheelAllCuisines => 'Tüm Mutfaklar';

  @override
  String get cuisineTitle => 'Dünya Mutfakları';

  @override
  String get cuisineSubtitle =>
      'Dünyanın dört bir yanından nefis tarifleri keşfedin';

  @override
  String cuisineFoodsCount(int count) {
    return '$count yemek';
  }

  @override
  String get cuisinePremiumBadge => 'PREMIUM';

  @override
  String get cuisineUnlock => 'Mutfağı Aç';

  @override
  String get detailIngredients => 'Malzemeler';

  @override
  String get detailSteps => 'Hazırlanış Adımları';

  @override
  String get detailPrepTime => 'Hazırlık';

  @override
  String get detailCookTime => 'Pişirme';

  @override
  String get detailCalories => 'Kalori';

  @override
  String get detailServings => 'Porsiyon';

  @override
  String get detailDifficulty => 'Zorluk';

  @override
  String detailMinutes(int min) {
    return '$min dk';
  }

  @override
  String detailCalorieUnit(int cal) {
    return '$cal kcal';
  }

  @override
  String detailServingsCount(int count) {
    return '$count kişilik';
  }

  @override
  String get difficultyEasy => 'Kolay';

  @override
  String get difficultyMedium => 'Orta';

  @override
  String get difficultyHard => 'Zor';

  @override
  String get favoritesTitle => 'Favorilerim';

  @override
  String get favoritesEmptyTitle => 'Henüz Favori Yok';

  @override
  String get favoritesEmptyDesc =>
      'Hızlıca erişmek istediğiniz tariflerin kalp simgesine dokunarak buraya kaydedin.';

  @override
  String get favoritesRemoved => 'Favorilerden çıkarıldı';

  @override
  String get favoritesAdded => 'Favorilere eklendi';

  @override
  String get historyTitle => 'Karar Geçmişi';

  @override
  String get historyEmptyTitle => 'Henüz Geçmiş Yok';

  @override
  String get historyEmptyDesc =>
      'Çarkta yaptığınız seçimler burada listelenecektir.';

  @override
  String get historyClear => 'Geçmişi Temizle';

  @override
  String get historyClearConfirm =>
      'Tüm çark geçmişinizi silmek istediğinizden emin misiniz?';

  @override
  String get historyCleared => 'Geçmiş temizlendi';

  @override
  String get settingsTitle => 'Ayarlar';

  @override
  String get settingsLanguage => 'Dil';

  @override
  String get settingsTheme => 'Tema';

  @override
  String get settingsThemeDark => 'Karanlık Mod';

  @override
  String get settingsSound => 'Ses Efektleri';

  @override
  String get settingsHaptic => 'Titreşim Geri Bildirimi';

  @override
  String get settingsPremium => 'Premium Üyelik';

  @override
  String get settingsRestore => 'Satın Alımları Geri Yükle';

  @override
  String get settingsAbout => 'Uygulama Hakkında';

  @override
  String settingsVersion(String version) {
    return 'Sürüm $version';
  }

  @override
  String get premiumTitle => 'Tam Erişimi Aç';

  @override
  String get premiumSubtitle =>
      'Tüm 10 dünya mutfağına, sınırsız çark hakkına ve reklamsız deneyime sahip olun!';

  @override
  String get premiumFeature1 => '6 Premium Dünya Mutfağının Kilidini Açın';

  @override
  String get premiumFeature2 => '160+ detaylı tarife sınırsız erişim';

  @override
  String get premiumFeature3 => 'Özel filtreleme ve hariç tutma kuralları';

  @override
  String get premiumFeature4 => 'Tamamen reklamsız deneyim';

  @override
  String get premiumBuyButton => 'Hemen Premium\'a Geç';

  @override
  String get premiumRestore => 'Satın Alımı Geri Yükle';

  @override
  String get premiumSuccess => 'Premium\'a Hoş Geldiniz!';

  @override
  String get commonCancel => 'İptal';

  @override
  String get commonConfirm => 'Onayla';

  @override
  String get commonSave => 'Kaydet';

  @override
  String get commonClose => 'Kapat';

  @override
  String get commonShare => 'Tarifi Paylaş';

  @override
  String commonShareText(Object dishName) {
    return 'Bugün Ne Yesek uygulamasında harika bir tarif buldum: $dishName!';
  }

  @override
  String get onboardingTitle1 => 'Ne Yiyeceğine Karar Veremiyor musun?';

  @override
  String get onboardingSubtitle1 =>
      'Her gün \'Bugün ne yesek?\' derdine eğlenceli çarkımızla son verin!';

  @override
  String get onboardingTitle2 => 'Çarkı Çevir!';

  @override
  String get onboardingSubtitle2 =>
      'Kararı şansa bırak, günün lezzetini çark belirlesin.';

  @override
  String get onboardingTitle3 => 'Dünya Mutfaklarını Keşfet';

  @override
  String get onboardingSubtitle3 =>
      '10 farklı mutfaktan 160+ detaylı tarif parmaklarının ucunda.';

  @override
  String get onboardingSkip => 'Atla';

  @override
  String get onboardingNext => 'İleri';

  @override
  String get onboardingStart => 'Hemen Başla';
}
