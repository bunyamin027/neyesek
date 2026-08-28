import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

import 'core/theme/app_theme.dart';
import 'core/constants/app_strings.dart';
import 'data/services/locale_service.dart';
import 'features/onboarding/onboarding_screen.dart';
import 'features/navigation/main_nav_screen.dart';
import 'l10n/app_localizations.dart';

/// Ana uygulama widget'ı
class NeYesekApp extends StatelessWidget {
  const NeYesekApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: LocaleService.instance,
      builder: (context, child) {
        return MaterialApp(
          title: AppStrings.appName,
          debugShowCheckedModeBanner: false,
          theme: AppTheme.darkTheme,
          locale: LocaleService.instance.currentLocale,
          localizationsDelegates: const [
            AppLocalizations.delegate,
            GlobalMaterialLocalizations.delegate,
            GlobalWidgetsLocalizations.delegate,
            GlobalCupertinoLocalizations.delegate,
          ],
          supportedLocales: AppLocalizations.supportedLocales,
          home: const _AppStartScreen(),
        );
      },
    );
  }
}


/// Başlangıç ekranı — Onboarding tamamlanmış mı kontrol eder.
class _AppStartScreen extends StatefulWidget {
  const _AppStartScreen();

  @override
  State<_AppStartScreen> createState() => _AppStartScreenState();
}

class _AppStartScreenState extends State<_AppStartScreen> {
  bool _isLoading = true;
  bool _onboardingCompleted = false;

  @override
  void initState() {
    super.initState();
    _checkOnboarding();
  }

  Future<void> _checkOnboarding() async {
    final prefs = await SharedPreferences.getInstance();
    final completed = prefs.getBool('onboarding_completed') ?? false;
    if (!mounted) return;
    setState(() {
      _onboardingCompleted = completed;
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const Scaffold(
        body: Center(
          child: CircularProgressIndicator(),
        ),
      );
    }

    return _onboardingCompleted
        ? const MainNavScreen()
        : const OnboardingScreen();
  }
}
