import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:confetti/confetti.dart';
import 'dart:async';

import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/animated_button.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../core/widgets/gradient_background.dart';
import '../../data/models/cuisine.dart';
import '../../data/models/food_item.dart';
import '../../data/models/wheel_filter.dart';
import '../../data/services/cuisine_service.dart';
import '../../data/services/food_service.dart';
import '../../data/services/history_service.dart';
import '../../data/services/purchase_service.dart';
import '../../data/services/sound_service.dart';
import '../../l10n/app_localizations.dart';
import '../result/result_screen.dart';
import 'widgets/food_wheel.dart';
import 'widgets/wheel_filter_bottom_sheet.dart';

/// Ana Ekran — Çarkıfelek, dinamik mutfak filtreleme, konfeti ve detaylı filtreler
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen>
    with TickerProviderStateMixin {
  final StreamController<int> _selectedController = StreamController<int>();
  bool _isSpinning = false;
  bool _isLoading = true;
  int _selectedIndex = 0;

  List<Cuisine> _cuisines = [];
  String _selectedCuisineId = 'all';
  WheelFilter _currentFilter = const WheelFilter();
  List<FoodItem> _foods = [];



  late AnimationController _glowController;
  late ConfettiController _confettiController;

  @override
  void initState() {
    super.initState();
    _glowController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 2),
    )..repeat(reverse: true);

    _confettiController = ConfettiController(
      duration: const Duration(seconds: 2),
    );

    _loadData();
  }

  Future<void> _loadData() async {
    final cuisines = await CuisineService.instance.getAllCuisines();
    final foods = await FoodService.instance.getFoodsForWheel(
      filter: _currentFilter.copyWith(cuisineId: _selectedCuisineId),
    );

    if (!mounted) return;
    setState(() {
      _cuisines = cuisines;
      _foods = _prepareWheelFoods(foods);
      _isLoading = false;
    });
  }

  List<FoodItem> _prepareWheelFoods(List<FoodItem> fullList) {
    if (fullList.length <= 10) return fullList;
    final list = List<FoodItem>.from(fullList)..shuffle();
    return list.take(10).toList();
  }

  Future<void> _onSelectCuisine(String cuisineId) async {
    if (_isSpinning) return;
    HapticFeedback.selectionClick();

    setState(() {
      _selectedCuisineId = cuisineId;
      _currentFilter = _currentFilter.copyWith(cuisineId: cuisineId);
      _isLoading = true;
    });

    final foods = await FoodService.instance.getFoodsForWheel(
      filter: _currentFilter,
    );

    if (!mounted) return;
    setState(() {
      _foods = _prepareWheelFoods(foods);
      _isLoading = false;
    });
  }

  void _openFilterModal() {
    if (_isSpinning) return;
    HapticFeedback.lightImpact();

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => WheelFilterBottomSheet(
        currentFilter: _currentFilter.copyWith(cuisineId: _selectedCuisineId),
        onApply: (newFilter) async {
          setState(() {
            _currentFilter = newFilter;
            _isLoading = true;
          });
          final foods = await FoodService.instance.getFoodsForWheel(
            filter: newFilter,
          );
          if (!mounted) return;
          setState(() {
            _foods = _prepareWheelFoods(foods);
            _isLoading = false;
          });
        },
      ),
    );
  }

  @override
  void dispose() {
    _selectedController.close();
    _glowController.dispose();
    _confettiController.dispose();
    super.dispose();
  }



  void _spinWheel() {
    if (_isSpinning || _foods.isEmpty) return;

    setState(() => _isSpinning = true);
    HapticFeedback.heavyImpact();

    final random = math.Random();
    _selectedIndex = random.nextInt(_foods.length);
    _selectedController.add(_selectedIndex);

    _startHapticSequence();
  }

  void _startHapticSequence() {
    int count = 0;
    Timer.periodic(const Duration(milliseconds: 200), (timer) {
      if (count > 15 || !_isSpinning) {
        timer.cancel();
        return;
      }
      HapticFeedback.selectionClick();
      SoundService.instance.playTick();
      count++;
    });
  }

  void _onWheelStopped() {
    setState(() => _isSpinning = false);
    HapticFeedback.heavyImpact();
    SoundService.instance.playWin();
    _confettiController.play();

    final selectedFood = _foods[_selectedIndex];
    HistoryService.instance.addHistory(selectedFood.id);

    Future.delayed(const Duration(milliseconds: 600), () {
      if (!mounted) return;
      _showResult(selectedFood);
    });
  }

  void _showResult(FoodItem food) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => ResultScreen(
        food: food,
        onSpinAgain: () {
          Navigator.pop(context);
          Future.delayed(const Duration(milliseconds: 300), _spinWheel);
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final screenSize = MediaQuery.of(context).size;
    final l10n = AppLocalizations.of(context);
    final langCode = Localizations.localeOf(context).languageCode;

    return Scaffold(
      body: GradientBackground(
        child: SafeArea(
          child: Stack(
            children: [
              Column(
                children: [
                  // ─── Üst Bar (Frosted Glass) ─────────────────
                  Padding(
                    padding: const EdgeInsets.fromLTRB(20, 12, 20, 0),
                    child: FrostedGlassContainer(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 20,
                        vertical: 14,
                      ),
                      borderRadius: 16,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  l10n?.appName ?? 'Ne Yesek?',
                                  style: AppTextStyles.headlineMedium,
                                ),
                                Text(
                                  l10n?.appTagline ?? 'Bugün ne yiyeceğine çarkı çevirerek karar ver!',
                                  style: AppTextStyles.bodySmall,
                                  maxLines: 2,
                                  overflow: TextOverflow.ellipsis,
                                ),
                              ],
                            ),
                          ),
                          // Filtre Butonu
                          GestureDetector(
                            onTap: _openFilterModal,
                            child: Container(
                              padding: const EdgeInsets.all(10),
                              decoration: BoxDecoration(
                                color: _currentFilter.hasActiveFilters
                                    ? AppColors.primary.withValues(alpha: 0.3)
                                    : AppColors.frostedGlassDark,
                                borderRadius: BorderRadius.circular(14),
                                border: Border.all(
                                  color: _currentFilter.hasActiveFilters
                                      ? AppColors.primary
                                      : AppColors.glassBorder,
                                  width: 1.5,
                                ),
                              ),
                              child: Stack(
                                clipBehavior: Clip.none,
                                children: [
                                  Icon(
                                    Icons.tune_rounded,
                                    color: _currentFilter.hasActiveFilters
                                        ? AppColors.primary
                                        : Colors.white,
                                    size: 22,
                                  ),
                                  if (_currentFilter.hasActiveFilters)
                                    Positioned(
                                      top: -4,
                                      right: -4,
                                      child: Container(
                                        width: 10,
                                        height: 10,
                                        decoration: const BoxDecoration(
                                          color: AppColors.gold,
                                          shape: BoxShape.circle,
                                        ),
                                      ),
                                    ),
                                ],
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  )
                      .animate()
                      .fadeIn(duration: 500.ms)
                      .slideY(begin: -0.3, end: 0),

                  const SizedBox(height: 12),

                  // ─── Mutfak Filtre Barı ───────────────────────
                  SizedBox(
                    height: 42,
                    child: ListView.builder(
                      scrollDirection: Axis.horizontal,
                      padding: const EdgeInsets.symmetric(horizontal: 16),
                      itemCount: _cuisines.length + 1,
                      itemBuilder: (context, index) {
                        if (index == 0) {
                          final isSelected = _selectedCuisineId == 'all';
                          return _buildCuisineChip(
                            id: 'all',
                            label: l10n?.wheelAllCuisines ?? 'Tüm Mutfaklar',
                            emoji: '🌍',
                            isSelected: isSelected,
                          );
                        }
                        final cuisine = _cuisines[index - 1];
                        final isSelected = _selectedCuisineId == cuisine.id;
                        return _buildCuisineChip(
                          id: cuisine.id,
                          label: cuisine.getName(langCode),
                          emoji: cuisine.emoji,
                          isSelected: isSelected,
                          isPremium: cuisine.isPremium,
                        );
                      },
                    ),
                  ).animate().fadeIn(delay: 200.ms, duration: 400.ms),

                  const Spacer(flex: 1),

                  // ─── Çarkıfelek ──────────────────────────────
                  if (_isLoading)
                    const Center(
                      child: CircularProgressIndicator(color: AppColors.primary),
                    )
                  else if (_foods.isEmpty)
                    Center(
                      child: Padding(
                        padding: const EdgeInsets.all(24.0),
                        child: Text(
                          'Filtrelerinize uygun yemek bulunamadı. Lütfen filtreleri gevşetin.',
                          style: AppTextStyles.bodyMedium,
                          textAlign: TextAlign.center,
                        ),
                      ),
                    )
                  else
                    SizedBox(
                      height: screenSize.width * 0.85,
                      width: screenSize.width * 0.85,
                      child: Stack(
                        alignment: Alignment.center,
                        children: [
                          // Glow efekti
                          AnimatedBuilder(
                            animation: _glowController,
                            builder: (context, child) {
                              return Container(
                                width: screenSize.width * 0.8,
                                height: screenSize.width * 0.8,
                                decoration: BoxDecoration(
                                  shape: BoxShape.circle,
                                  boxShadow: [
                                    BoxShadow(
                                      color: AppColors.primary.withValues(
                                        alpha: 0.15 + 0.1 * _glowController.value,
                                      ),
                                      blurRadius: 60 + 20 * _glowController.value,
                                      spreadRadius: 5,
                                    ),
                                  ],
                                ),
                              );
                            },
                          ),
                          // Çark
                          FoodWheel(
                            foods: _foods,
                            selectedStream: _selectedController.stream,
                            onAnimationEnd: _onWheelStopped,
                          ),
                        ],
                      ),
                    )
                        .animate()
                        .scale(
                          begin: const Offset(0.8, 0.8),
                          end: const Offset(1.0, 1.0),
                          duration: 600.ms,
                          curve: Curves.easeOutBack,
                        )
                        .fadeIn(duration: 500.ms),

                  const Spacer(flex: 1),

                  // ─── Çevir Butonu ────────────────────────────
                  Padding(
                    padding: const EdgeInsets.fromLTRB(40, 0, 40, 16),
                    child: AnimatedButton(
                      text: _isSpinning
                          ? (l10n?.wheelSpinning ?? 'Senin için seçiliyor...')
                          : (l10n?.wheelSpin ?? 'ÇARKI ÇEVİR'),
                      onPressed: _isSpinning || _foods.isEmpty ? null : _spinWheel,
                      width: double.infinity,
                      height: 60,
                      icon: _isSpinning ? null : Icons.casino_rounded,
                    ),
                  )
                      .animate()
                      .fadeIn(delay: 300.ms, duration: 500.ms)
                      .slideY(begin: 0.3, end: 0),

                  // Alt metin
                  Padding(
                    padding: const EdgeInsets.only(bottom: 20),
                    child: Text(
                      _isSpinning ? '' : '🎲 ${l10n?.appTagline ?? 'Çarkı çevir, kararı biz verelim!'}',
                      style: AppTextStyles.bodySmall,
                      textAlign: TextAlign.center,
                    ),
                  ).animate().fadeIn(delay: 500.ms, duration: 400.ms),
                ],
              ),

              // ─── Konfeti Kutlama Katmanı ───
              Align(
                alignment: Alignment.topCenter,
                child: ConfettiWidget(
                  confettiController: _confettiController,
                  blastDirectionality: BlastDirectionality.explosive,
                  maxBlastForce: 25,
                  minBlastForce: 10,
                  emissionFrequency: 0.05,
                  numberOfParticles: 35,
                  gravity: 0.2,
                  colors: const [
                    AppColors.primary,
                    AppColors.accent,
                    AppColors.gold,
                    Colors.greenAccent,
                    Colors.pinkAccent,
                    Colors.blueAccent,
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildCuisineChip({
    required String id,
    required String label,
    required String emoji,
    required bool isSelected,
    bool isPremium = false,
  }) {
    return GestureDetector(
      onTap: () => _onSelectCuisine(id),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        margin: const EdgeInsets.only(right: 8),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
        decoration: BoxDecoration(
          color: isSelected
              ? AppColors.primary
              : AppColors.frostedGlassDark,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: isSelected
                ? AppColors.primaryLight
                : AppColors.glassBorder,
            width: 1.5,
          ),
          boxShadow: isSelected
              ? [
                  BoxShadow(
                    color: AppColors.primary.withValues(alpha: 0.35),
                    blurRadius: 10,
                    offset: const Offset(0, 3),
                  ),
                ]
              : null,
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(emoji, style: const TextStyle(fontSize: 14)),
            const SizedBox(width: 6),
            Text(
              label,
              style: AppTextStyles.bodySmall.copyWith(
                color: isSelected
                    ? Colors.white
                    : AppColors.textSecondary,
                fontWeight: isSelected ? FontWeight.bold : FontWeight.w500,
              ),
            ),
            if (isPremium) ...[
              const SizedBox(width: 4),
              const Icon(
                Icons.star_rounded,
                color: AppColors.gold,
                size: 14,
              ),
            ],
          ],
        ),
      ),
    );
  }
}
