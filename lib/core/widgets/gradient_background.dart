import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/app_colors.dart';

/// Animasyonlu mesh gradient arka plan.
/// Koyu tonlarda hareketli renk geçişleri ile derinlik hissi yaratır.
class GradientBackground extends StatefulWidget {
  final Widget child;

  const GradientBackground({super.key, required this.child});

  @override
  State<GradientBackground> createState() => _GradientBackgroundState();
}

class _GradientBackgroundState extends State<GradientBackground>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 8),
    )..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return Container(
          decoration: const BoxDecoration(
            gradient: AppColors.backgroundGradient,
          ),
          child: Stack(
            children: [
              // Animasyonlu glow efekti 1
              Positioned(
                top: -100 + 50 * math.sin(_controller.value * 2 * math.pi),
                right: -50 + 30 * math.cos(_controller.value * 2 * math.pi),
                child: Container(
                  width: 300,
                  height: 300,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    gradient: RadialGradient(
                      colors: [
                        AppColors.primary.withValues(alpha: 0.08),
                        AppColors.primary.withValues(alpha: 0.0),
                      ],
                    ),
                  ),
                ),
              ),
              // Animasyonlu glow efekti 2
              Positioned(
                bottom: -80 + 40 * math.cos(_controller.value * 2 * math.pi),
                left: -60 + 35 * math.sin(_controller.value * 2 * math.pi),
                child: Container(
                  width: 250,
                  height: 250,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    gradient: RadialGradient(
                      colors: [
                        AppColors.accent.withValues(alpha: 0.06),
                        AppColors.accent.withValues(alpha: 0.0),
                      ],
                    ),
                  ),
                ),
              ),
              // Animasyonlu glow efekti 3
              Positioned(
                top: MediaQuery.of(context).size.height * 0.4 +
                    20 * math.sin(_controller.value * 3 * math.pi),
                left: MediaQuery.of(context).size.width * 0.5 +
                    25 * math.cos(_controller.value * 2.5 * math.pi),
                child: Container(
                  width: 200,
                  height: 200,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    gradient: RadialGradient(
                      colors: [
                        AppColors.primaryDark.withValues(alpha: 0.05),
                        AppColors.primaryDark.withValues(alpha: 0.0),
                      ],
                    ),
                  ),
                ),
              ),
              // İçerik
              child!,
            ],
          ),
        );
      },
      child: widget.child,
    );
  }
}
