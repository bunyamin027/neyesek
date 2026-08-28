import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'app.dart';
import 'data/services/locale_service.dart';
import 'data/services/purchase_service.dart';
import 'data/services/sound_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Servisleri başlat
  await LocaleService.instance.init();
  await SoundService.instance.init();
  await PurchaseService.instance.init();

  // Status bar stilini ayarla — karanlık tema
  SystemChrome.setSystemUIOverlayStyle(
    const SystemUiOverlayStyle(
      statusBarBrightness: Brightness.dark,
      statusBarIconBrightness: Brightness.light,
      statusBarColor: Colors.transparent,
    ),
  );

  // Ekran yönelimini dikey olarak kilitle
  SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);

  runApp(const NeYesekApp());
}

