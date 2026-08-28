import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:url_launcher/url_launcher.dart';

import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../core/widgets/gradient_background.dart';
import '../../data/services/locale_service.dart';
import '../../data/services/sound_service.dart';
import '../../l10n/app_localizations.dart';
import '../premium/premium_screen.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  bool _soundEnabled = SoundService.instance.isEnabled;
  bool _hapticEnabled = true;

  @override
  void initState() {
    super.initState();
    _soundEnabled = SoundService.instance.isEnabled;
  }

  void _openPremiumScreen() {
    HapticFeedback.mediumImpact();
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => const PremiumScreen(),
      ),
    );
  }

  void _showLanguageSelector() {
    final l10n = AppLocalizations.of(context);
    final service = LocaleService.instance;

    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (context) => Container(
        padding: const EdgeInsets.fromLTRB(20, 20, 20, 30),
        decoration: BoxDecoration(
          color: AppColors.surface,
          borderRadius: const BorderRadius.vertical(top: Radius.circular(28)),
          border: Border.all(color: AppColors.glassBorder, width: 1.5),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Center(
              child: Container(
                width: 40,
                height: 4,
                decoration: BoxDecoration(
                  color: AppColors.textMuted.withValues(alpha: 0.3),
                  borderRadius: BorderRadius.circular(2),
                ),
              ),
            ),
            const SizedBox(height: 16),
            Text(
              l10n?.settingsLanguage ?? 'Dil Seçimi',
              style: AppTextStyles.titleLarge.copyWith(color: Colors.white, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),
            ...LocaleService.supportedLocales.map((locale) {
              final code = locale.languageCode;
              final isSelected = service.currentLanguageCode == code;
              return GestureDetector(
                onTap: () {
                  HapticFeedback.selectionClick();
                  service.setLocale(code);
                  Navigator.pop(context);
                },
                child: FrostedGlassContainer(
                  margin: const EdgeInsets.only(bottom: 10),
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                  borderRadius: 16,
                  child: Row(
                    children: [
                      Text(service.getLanguageFlag(code), style: const TextStyle(fontSize: 24)),
                      const SizedBox(width: 14),
                      Expanded(
                        child: Text(
                          service.getLanguageName(code),
                          style: AppTextStyles.bodyMedium.copyWith(
                            color: Colors.white,
                            fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                          ),
                        ),
                      ),
                      if (isSelected)
                        const Icon(Icons.check_circle_rounded, color: AppColors.primary, size: 22),
                    ],
                  ),
                ),
              );
            }),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final localeService = LocaleService.instance;

    return Scaffold(
      body: GradientBackground(
        child: SafeArea(
          child: ListView(
            padding: const EdgeInsets.fromLTRB(20, 16, 20, 30),
            physics: const BouncingScrollPhysics(),
            children: [
              Text(
                l10n?.settingsTitle ?? 'Ayarlar',
                style: AppTextStyles.displaySmall.copyWith(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ).animate().fadeIn(duration: 300.ms),

              const SizedBox(height: 20),

              // ─── Premium Kartı ───
              GestureDetector(
                onTap: _openPremiumScreen,
                child: FrostedGlassContainer(
                  padding: const EdgeInsets.all(18),
                  borderRadius: 22,
                  child: Row(
                    children: [
                      Container(
                        width: 52,
                        height: 52,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          color: AppColors.gold.withValues(alpha: 0.2),
                          border: Border.all(color: AppColors.gold, width: 1.5),
                        ),
                        child: const Icon(Icons.star_rounded, color: AppColors.gold, size: 28),
                      ),
                      const SizedBox(width: 16),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              l10n?.settingsPremium ?? 'Premium Üyelik',
                              style: AppTextStyles.titleMedium.copyWith(
                                color: Colors.white,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                            const SizedBox(height: 2),
                            Text(
                              'Tüm mutfakları ve tarifleri açın',
                              style: AppTextStyles.labelSmall.copyWith(color: AppColors.textMuted),
                            ),
                          ],
                        ),
                      ),
                      const Icon(Icons.arrow_forward_ios_rounded, color: AppColors.gold, size: 16),
                    ],
                  ),
                ),
              ).animate().fadeIn(delay: 100.ms),

              const SizedBox(height: 24),

              // ─── Dil Ayarı ───
              _buildSettingTile(
                icon: Icons.language_rounded,
                title: l10n?.settingsLanguage ?? 'Dil',
                trailingText: '${localeService.getLanguageFlag(localeService.currentLanguageCode)} ${localeService.getLanguageName(localeService.currentLanguageCode)}',
                onTap: _showLanguageSelector,
              ),

              // ─── Ses Efektleri ───
              _buildSwitchTile(
                icon: Icons.volume_up_rounded,
                title: l10n?.settingsSound ?? 'Ses Efektleri',
                value: _soundEnabled,
                onChanged: (val) {
                  setState(() => _soundEnabled = val);
                  SoundService.instance.setEnabled(val);
                },
              ),

              // ─── Titreşim ───
              _buildSwitchTile(
                icon: Icons.vibration_rounded,
                title: l10n?.settingsHaptic ?? 'Titreşim Geri Bildirimi',
                value: _hapticEnabled,
                onChanged: (val) => setState(() => _hapticEnabled = val),
              ),

              // ─── Satın Alımları Geri Yükle ───
              _buildSettingTile(
                icon: Icons.restore_rounded,
                title: l10n?.settingsRestore ?? 'Satın Alımları Geri Yükle',
                onTap: () {
                  HapticFeedback.lightImpact();
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text(l10n?.settingsRestore ?? 'Geri yükleme kontrol edildi'),
                      backgroundColor: AppColors.surfaceLight,
                    ),
                  );
                },
              ),

              // ─── Kullanım Koşulları (EULA) ───
              _buildSettingTile(
                icon: Icons.description_rounded,
                title: 'Kullanım Koşulları (EULA)',
                onTap: () async {
                  HapticFeedback.selectionClick();
                  final uri = Uri.parse('https://www.apple.com/legal/internet-services/itunes/dev/stdeula/');
                  try {
                    await launchUrl(uri, mode: LaunchMode.externalApplication);
                  } catch (_) {}
                },
              ),

              // ─── Gizlilik Politikası ───
              _buildSettingTile(
                icon: Icons.privacy_tip_rounded,
                title: 'Gizlilik Politikası',
                onTap: () async {
                  HapticFeedback.selectionClick();
                  final uri = Uri.parse('https://www.kahramanapp.com/privacy');
                  try {
                    await launchUrl(uri, mode: LaunchMode.externalApplication);
                  } catch (_) {}
                },
              ),

              // ─── Destek ve Geri Bildirim ───
              _buildSettingTile(
                icon: Icons.mail_outline_rounded,
                title: 'Destek ve Geri Bildirim',
                trailingText: 'kahramandev01@gmail.com',
                onTap: () async {
                  HapticFeedback.selectionClick();
                  final uri = Uri.parse('mailto:kahramandev01@gmail.com?subject=Bugun%20Ne%20Yesek%20Destek%20ve%20Geri%20Bildirim');
                  try {
                    await launchUrl(uri, mode: LaunchMode.externalApplication);
                  } catch (_) {}
                },
              ),

              // ─── Geliştirici ───
              _buildSettingTile(
                icon: Icons.code_rounded,
                title: 'Geliştirici',
                trailingText: 'kahramanapp',
                onTap: () async {
                  HapticFeedback.selectionClick();
                  final uri = Uri.parse('https://www.kahramanapp.com');
                  try {
                    await launchUrl(uri, mode: LaunchMode.externalApplication);
                  } catch (_) {}
                },
              ),

              const SizedBox(height: 30),

              // ─── Versiyon ve Telif ───
              Center(
                child: Column(
                  children: [
                    Text(
                      l10n?.settingsVersion('1.0.0') ?? 'Sürüm 1.0.0',
                      style: AppTextStyles.labelSmall.copyWith(color: AppColors.textMuted),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      'Geliştirici: kahramanapp • İletişim: kahramandev01@gmail.com',
                      style: AppTextStyles.labelSmall.copyWith(color: AppColors.textMuted.withValues(alpha: 0.8), fontSize: 11),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      '© 2026 Bugün Ne Yesek? — All rights reserved',
                      style: AppTextStyles.labelSmall.copyWith(color: AppColors.textMuted.withValues(alpha: 0.6), fontSize: 10),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildSettingTile({
    required IconData icon,
    required String title,
    String? trailingText,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: onTap,
      child: FrostedGlassContainer(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
        borderRadius: 18,
        child: Row(
          children: [
            Icon(icon, color: AppColors.primary, size: 22),
            const SizedBox(width: 14),
            Expanded(
              child: Text(
                title,
                style: AppTextStyles.bodyMedium.copyWith(color: Colors.white, fontWeight: FontWeight.w500),
              ),
            ),
            if (trailingText != null) ...[
              Text(
                trailingText,
                style: AppTextStyles.bodySmall.copyWith(color: AppColors.textSecondary),
              ),
              const SizedBox(width: 8),
            ],
            const Icon(Icons.arrow_forward_ios_rounded, color: AppColors.textMuted, size: 14),
          ],
        ),
      ),
    );
  }

  Widget _buildSwitchTile({
    required IconData icon,
    required String title,
    required bool value,
    required ValueChanged<bool> onChanged,
  }) {
    return FrostedGlassContainer(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      borderRadius: 18,
      child: Row(
        children: [
          Icon(icon, color: AppColors.primary, size: 22),
          const SizedBox(width: 14),
          Expanded(
            child: Text(
              title,
              style: AppTextStyles.bodyMedium.copyWith(color: Colors.white, fontWeight: FontWeight.w500),
            ),
          ),
          Switch.adaptive(
            value: value,
            activeTrackColor: AppColors.primary,
            onChanged: (v) {
              HapticFeedback.selectionClick();
              onChanged(v);
            },
          ),
        ],
      ),
    );
  }
}
