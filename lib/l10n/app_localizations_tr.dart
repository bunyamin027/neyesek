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
  String get settingsPremiumDesc => 'Tüm mutfakları ve tarifleri açın';

  @override
  String get settingsEula => 'Kullanım Koşulları (EULA)';

  @override
  String get settingsPrivacy => 'Gizlilik Politikası';

  @override
  String get settingsSupport => 'Destek ve Geri Bildirim';

  @override
  String get settingsDeveloper => 'Geliştirici';

  @override
  String get settingsDeveloperContact =>
      'Geliştirici: kahramanapp • İletişim: kahramandev01@gmail.com';

  @override
  String get settingsCopyright =>
      '© 2026 Bugün Ne Yesek? — All rights reserved';

  @override
  String get premiumTitle => 'Tam Erişimi Aç';

  @override
  String get premiumSubtitle =>
      'Tüm 10 dünya mutfağına, sınırsız çark hakkına ve reklamsız deneyime sahip olun!';

  @override
  String get premiumHeaderTitle => 'Ne Yesek? Premium';

  @override
  String get premiumHeaderSubtitle =>
      '10 Dünya Mutfağı, 212+ Otantik Tarif ve Reklamsız Gurme Deneyimi';

  @override
  String get premiumFeature1 => 'Tüm 10 Dünya Mutfağına Tam Erişim';

  @override
  String get premiumFeature1Desc =>
      'Japon, Kore, Meksika, Fransız, Hint ve Çin mutfaklarının kilidini açın.';

  @override
  String get premiumFeature2 => '212+ Detaylı Otantik Yemek Tarifi';

  @override
  String get premiumFeature2Desc =>
      'Malzeme listeleri, kalori, süreler ve adım adım pişirme rehberleri.';

  @override
  String get premiumFeature3 => 'Akıllı Çark Filtreleri';

  @override
  String get premiumFeature3Desc =>
      'Vejetaryen, hızlı pişen, düşük kalorili veya zorluk filtrelerini dilediğince uygula.';

  @override
  String get premiumFeature4 => 'Sıfır Reklam, Kesintisiz Akış';

  @override
  String get premiumFeature4Desc =>
      'Hiçbir kesinti olmadan hızlı ve keyifli bir gurme deneyimi.';

  @override
  String get premiumPlanMonthly => 'Aylık Plan';

  @override
  String get premiumPlanYearly => 'Yıllık Plan';

  @override
  String get premiumPlanMonthlySubtitle =>
      'Esnek üyelik, dilediğin an iptal et';

  @override
  String get premiumPlanYearlySubtitle =>
      '12 ay sınırsız erişim • En avantajlı paket';

  @override
  String get premiumPlanSaveBadge => '%50 TASARRUF';

  @override
  String get premiumPerMonth => '/ ay';

  @override
  String get premiumPerYear => '/ yıl';

  @override
  String get premiumCtaYearly => 'Yıllık Premium\'a Geç';

  @override
  String get premiumCtaMonthly => 'Aylık Premium\'a Geç';

  @override
  String get premiumProcessing => 'İşlem yapılıyor...';

  @override
  String get premiumBuyButton => 'Hemen Premium\'a Geç';

  @override
  String get premiumRestore => 'Geri Yükle';

  @override
  String get premiumSuccess => 'Tebrikler! Premium üyelik aktif edildi! 🎉';

  @override
  String get premiumRestoreSuccess =>
      'Premium üyeliğiniz başarıyla geri yüklendi! 🎉';

  @override
  String get premiumRestoreNone =>
      'Satın alımlar kontrol edildi. Aktif abonelik bulunamadı.';

  @override
  String get premiumDisclosure =>
      'Ödeme, satın almayı onayladığınızda Apple ID hesabınızdan tahsil edilir. Abonelik, mevcut dönemin bitiminden en az 24 saat önce iptal edilmediği sürece otomatik olarak yenilenir. Yenileme ücreti, dönem bitiminden 24 saat önce hesabınızdan tahsil edilir. Aboneliğinizi satın aldıktan sonra Hesap Ayarları\'ndan yönetebilir veya iptal edebilirsiniz.';

  @override
  String get premiumEula => 'Kullanım Koşulları (EULA)';

  @override
  String get premiumPrivacy => 'Gizlilik Politikası';

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
