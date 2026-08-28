import 'package:flutter/material.dart';

/// Uygulama renk paleti
/// Sıcak tonlar (iştah açıcı) + koyu arka plan + frosted glass
class AppColors {
  AppColors._();

  // ─── Birincil Renkler ─────────────────────────────────────
  static const Color primary = Color(0xFFFF6B35);
  static const Color primaryLight = Color(0xFFFF8F5E);
  static const Color primaryDark = Color(0xFFE55A2B);

  // ─── Vurgu Renkleri ───────────────────────────────────────
  static const Color accent = Color(0xFFFFB347);
  static const Color accentLight = Color(0xFFFFCC80);
  static const Color accentDark = Color(0xFFE5983F);

  // ─── Arka Plan ────────────────────────────────────────────
  static const Color background = Color(0xFF0D0D0D);
  static const Color backgroundLight = Color(0xFF1A1A2E);
  static const Color surface = Color(0xFF16213E);
  static const Color surfaceLight = Color(0xFF1E2A4A);

  // ─── Metin Renkleri ───────────────────────────────────────
  static const Color textPrimary = Color(0xFFF5F5F5);
  static const Color textSecondary = Color(0xFFB0B0B0);
  static const Color textMuted = Color(0xFF707070);

  // ─── Çark Renkleri ────────────────────────────────────────
  static const List<Color> wheelColors = [
    Color(0xFFFF6B35), // Turuncu
    Color(0xFFE84545), // Kırmızı
    Color(0xFFFFB347), // Amber
    Color(0xFF2ECC71), // Yeşil
    Color(0xFF3498DB), // Mavi
    Color(0xFF9B59B6), // Mor
    Color(0xFFE67E22), // Koyu turuncu
    Color(0xFF1ABC9C), // Teal
    Color(0xFFF39C12), // Altın
    Color(0xFFE74C3C), // Crimson
  ];

  // ─── Gradient'ler ─────────────────────────────────────────
  static const LinearGradient primaryGradient = LinearGradient(
    colors: [primary, accent],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );

  static const LinearGradient backgroundGradient = LinearGradient(
    colors: [background, backgroundLight, surface],
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
  );

  static const RadialGradient glowGradient = RadialGradient(
    colors: [
      Color(0x40FF6B35),
      Color(0x20FF6B35),
      Color(0x00FF6B35),
    ],
    radius: 0.8,
  );

  static const LinearGradient meshGradient = LinearGradient(
    colors: [
      Color(0xFF0D0D0D),
      Color(0xFF1A1A2E),
      Color(0xFF16213E),
      Color(0xFF0F3460),
    ],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    stops: [0.0, 0.3, 0.6, 1.0],
  );

  // ─── Frosted Glass ────────────────────────────────────────
  static const Color frostedGlass = Color(0x30FFFFFF);
  static const Color frostedGlassBorder = Color(0x20FFFFFF);
  static const Color frostedGlassDark = Color(0x15FFFFFF);
  static const Color glassBorder = Color(0x20FFFFFF);

  // ─── Özel Renkler ─────────────────────────────────────────
  static const Color gold = Color(0xFFFFD700);
  static const Color goldLight = Color(0xFFFFE082);
  static const Color error = Color(0xFFE53935);
  static const Color surfaceDark = Color(0xFF12121E);
}

