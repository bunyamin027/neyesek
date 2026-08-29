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
  String get settingsPremiumDesc => 'Desbloquea todas las cocinas y recetas';

  @override
  String get settingsEula => 'Términos de Uso (EULA)';

  @override
  String get settingsPrivacy => 'Política de Privacidad';

  @override
  String get settingsSupport => 'Soporte y Comentarios';

  @override
  String get settingsDeveloper => 'Desarrollador';

  @override
  String get settingsDeveloperContact =>
      'Desarrollador: kahramanapp • Contacto: kahramandev01@gmail.com';

  @override
  String get settingsCopyright =>
      '© 2026 ¿Qué Comemos? — Todos los derechos reservados';

  @override
  String get premiumTitle => 'Desbloquear Acceso Total';

  @override
  String get premiumSubtitle =>
      '¡Consigue las 10 cocinas del mundo, giros ilimitados y experiencia sin anuncios!';

  @override
  String get premiumHeaderTitle => '¿Qué Comemos? Premium';

  @override
  String get premiumHeaderSubtitle =>
      '10 Cocinas del Mundo, 212+ Recetas Auténticas y Experiencia Gourmet Sin Anuncios';

  @override
  String get premiumFeature1 => 'Acceso completo a las 10 cocinas del mundo';

  @override
  String get premiumFeature1Desc =>
      'Desbloquea cocinas japonesa, coreana, mexicana, francesa, india y china.';

  @override
  String get premiumFeature2 => '212+ Recetas auténticas detalladas';

  @override
  String get premiumFeature2Desc =>
      'Listas de ingredientes, calorías, tiempos y guías paso a paso.';

  @override
  String get premiumFeature3 => 'Filtros inteligentes de ruleta';

  @override
  String get premiumFeature3Desc =>
      'Aplica filtros vegetarianos, cocción rápida, bajo en calorías o dificultad libremente.';

  @override
  String get premiumFeature4 => 'Sin anuncios, flujo ininterrumpido';

  @override
  String get premiumFeature4Desc =>
      'Una experiencia gourmet rápida y agradable sin interrupciones.';

  @override
  String get premiumPlanMonthly => 'Plan Mensual';

  @override
  String get premiumPlanYearly => 'Plan Anual';

  @override
  String get premiumPlanMonthlySubtitle =>
      'Membresía flexible, cancela cuando quieras';

  @override
  String get premiumPlanYearlySubtitle =>
      '12 meses acceso ilimitado • Mejor oferta';

  @override
  String get premiumPlanSaveBadge => 'AHORRA 50%';

  @override
  String get premiumPerMonth => '/ mes';

  @override
  String get premiumPerYear => '/ año';

  @override
  String get premiumCtaYearly => 'Obtener Premium Anual';

  @override
  String get premiumCtaMonthly => 'Obtener Premium Mensual';

  @override
  String get premiumProcessing => 'Procesando...';

  @override
  String get premiumBuyButton => 'Obtener Premium Ahora';

  @override
  String get premiumRestore => 'Restaurar';

  @override
  String get premiumSuccess => '¡Bienvenido a Premium! 🎉';

  @override
  String get premiumRestoreSuccess =>
      '¡Tu membresía premium ha sido restaurada! 🎉';

  @override
  String get premiumRestoreNone =>
      'Compras verificadas. No se encontró suscripción activa.';

  @override
  String get premiumDisclosure =>
      'El pago se carga a tu cuenta de Apple ID tras la confirmación. La suscripción se renueva automáticamente a menos que se cancele al menos 24 horas antes del final del período actual. El cargo de renovación se realiza dentro de las 24 horas previas al final del período actual. Puedes gestionar o cancelar tu suscripción en Configuración de Cuenta después de la compra.';

  @override
  String get premiumEula => 'Términos de Uso (EULA)';

  @override
  String get premiumPrivacy => 'Política de Privacidad';

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
