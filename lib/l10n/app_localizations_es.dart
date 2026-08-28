// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for Spanish Castilian (`es`).
class AppLocalizationsEs extends AppLocalizations {
  AppLocalizationsEs([String locale = 'es']) : super(locale);

  @override
  String get appName => '¿Qué Comemos?';

  @override
  String get appTagline => '¡Decide qué comer con un giro de la ruleta!';

  @override
  String get navWheel => 'Ruleta';

  @override
  String get navCuisines => 'Cocinas';

  @override
  String get navFavorites => 'Favoritos';

  @override
  String get navHistory => 'Historial';

  @override
  String get navSettings => 'Ajustes';

  @override
  String get wheelSpin => 'GIRAR RULETA';

  @override
  String get wheelSpinning => 'Decidiendo por ti...';

  @override
  String get wheelResultTitle => '¡Sugerencia de Hoy!';

  @override
  String get wheelResultSubtitle => 'Elegimos este delicioso plato para ti:';

  @override
  String get wheelSeeRecipe => 'Ver Receta y Detalles';

  @override
  String get wheelSpinAgain => 'Girar de Nuevo';

  @override
  String get wheelFilterCuisine => 'Filtrar por Cocina';

  @override
  String get wheelAllCuisines => 'Todas las Cocinas';

  @override
  String get cuisineTitle => 'Cocinas del Mundo';

  @override
  String get cuisineSubtitle => 'Explora deliciosas recetas de todo el mundo';

  @override
  String cuisineFoodsCount(int count) {
    return '$count platos';
  }

  @override
  String get cuisinePremiumBadge => 'PREMIUM';

  @override
  String get cuisineUnlock => 'Desbloquear Cocina';

  @override
  String get detailIngredients => 'Ingredientes';

  @override
  String get detailSteps => 'Pasos de Preparación';

  @override
  String get detailPrepTime => 'Preparación';

  @override
  String get detailCookTime => 'Cocción';

  @override
  String get detailCalories => 'Calorías';

  @override
  String get detailServings => 'Porciones';

  @override
  String get detailDifficulty => 'Dificultad';

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
    return '$count personas';
  }

  @override
  String get difficultyEasy => 'Fácil';

  @override
  String get difficultyMedium => 'Medio';

  @override
  String get difficultyHard => 'Difícil';

  @override
  String get favoritesTitle => 'Mis Favoritos';

  @override
  String get favoritesEmptyTitle => 'Aún no hay favoritos';

  @override
  String get favoritesEmptyDesc =>
      'Toca el icono del corazón en cualquier receta para guardarla aquí.';

  @override
  String get favoritesRemoved => 'Eliminado de favoritos';

  @override
  String get favoritesAdded => 'Añadido a favoritos';

  @override
  String get historyTitle => 'Historial de Giros';

  @override
  String get historyEmptyTitle => 'Aún no hay historial';

  @override
  String get historyEmptyDesc =>
      'Los giros que realices en la ruleta se guardarán aquí.';

  @override
  String get historyClear => 'Borrar Historial';

  @override
  String get historyClearConfirm =>
      '¿Estás seguro de que deseas borrar todo el historial?';

  @override
  String get historyCleared => 'Historial borrado';

  @override
  String get settingsTitle => 'Ajustes';

  @override
  String get settingsLanguage => 'Idioma';

  @override
  String get settingsTheme => 'Tema';

  @override
  String get settingsThemeDark => 'Modo Oscuro';

  @override
  String get settingsSound => 'Efectos de Sonido';

  @override
  String get settingsHaptic => 'Vibración Háptica';

  @override
  String get settingsPremium => 'Membresía Premium';

  @override
  String get settingsRestore => 'Restaurar Compras';

  @override
  String get settingsAbout => 'Acerca de la App';

  @override
  String settingsVersion(String version) {
    return 'Versión $version';
  }

  @override
  String get premiumTitle => 'Desbloquear Acceso Total';

  @override
  String get premiumSubtitle =>
      '¡Consigue las 10 cocinas del mundo, giros ilimitados y experiencia sin anuncios!';

  @override
  String get premiumFeature1 => 'Desbloquea las 6 Cocinas Premium del Mundo';

  @override
  String get premiumFeature2 => 'Acceso a más de 160 recetas detalladas';

  @override
  String get premiumFeature3 => 'Filtros y reglas de exclusión personalizadas';

  @override
  String get premiumFeature4 => 'Experiencia totalmente sin anuncios';

  @override
  String get premiumBuyButton => 'Obtener Premium Ahora';

  @override
  String get premiumRestore => 'Restaurar Compra';

  @override
  String get premiumSuccess => '¡Bienvenido a Premium!';

  @override
  String get commonCancel => 'Cancelar';

  @override
  String get commonConfirm => 'Confirmar';

  @override
  String get commonSave => 'Guardar';

  @override
  String get commonClose => 'Cerrar';

  @override
  String get commonShare => 'Compartir Receta';

  @override
  String commonShareText(Object dishName) {
    return '¡Mira lo que encontré en la app ¿Qué Comemos?: $dishName!';
  }

  @override
  String get onboardingTitle1 => '¿No Sabes Qué Comer?';

  @override
  String get onboardingSubtitle1 =>
      '¡Dile adiós a la indecisión diaria a la hora de comer!';

  @override
  String get onboardingTitle2 => '¡Gira la Ruleta!';

  @override
  String get onboardingSubtitle2 =>
      'Deja la decisión en manos de la suerte con sonidos y física realista.';

  @override
  String get onboardingTitle3 => 'Descubre Cocinas del Mundo';

  @override
  String get onboardingSubtitle3 =>
      'Más de 160 recetas de 10 grandes tradiciones culinarias.';

  @override
  String get onboardingSkip => 'Saltar';

  @override
  String get onboardingNext => 'Siguiente';

  @override
  String get onboardingStart => '¡Empecemos!';
}
