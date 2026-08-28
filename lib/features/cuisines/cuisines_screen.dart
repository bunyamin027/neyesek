import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';

import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../core/widgets/gradient_background.dart';
import '../../data/models/cuisine.dart';
import '../../data/services/cuisine_service.dart';
import '../../data/services/purchase_service.dart';
import '../../l10n/app_localizations.dart';
import '../premium/premium_screen.dart';
import 'cuisine_dishes_screen.dart';

class CuisinesScreen extends StatefulWidget {
  const CuisinesScreen({super.key});

  @override
  State<CuisinesScreen> createState() => _CuisinesScreenState();
}

class _CuisinesScreenState extends State<CuisinesScreen> {
  List<Cuisine> _cuisines = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadCuisines();
  }

  Future<void> _loadCuisines() async {
    final list = await CuisineService.instance.getAllCuisines();
    if (!mounted) return;
    setState(() {
      _cuisines = list;
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context);
    final langCode = Localizations.localeOf(context).languageCode;

    return Scaffold(
      body: GradientBackground(
        child: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // ─── Üst Başlık ───
              Padding(
                padding: const EdgeInsets.fromLTRB(20, 16, 20, 8),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      l10n?.cuisineTitle ?? 'Dünya Mutfakları',
                      style: AppTextStyles.displaySmall.copyWith(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      l10n?.cuisineSubtitle ?? 'Dünyanın dört bir yanından nefis tarifleri keşfedin',
                      style: AppTextStyles.bodySmall.copyWith(color: AppColors.textSecondary),
                    ),
                  ],
                ),
              ).animate().fadeIn(duration: 400.ms),

              const SizedBox(height: 12),

              // ─── Mutfak Izgarası (Grid) ───
              Expanded(
                child: _isLoading
                    ? const Center(child: CircularProgressIndicator(color: AppColors.primary))
                    : GridView.builder(
                        padding: const EdgeInsets.fromLTRB(16, 8, 16, 30),
                        physics: const BouncingScrollPhysics(),
                        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                          crossAxisCount: 2,
                          childAspectRatio: 0.85,
                          crossAxisSpacing: 14,
                          mainAxisSpacing: 14,
                        ),
                        itemCount: _cuisines.length,
                        itemBuilder: (context, index) {
                          final cuisine = _cuisines[index];
                          return _buildCuisineCard(cuisine, langCode, l10n, index);
                        },
                      ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildCuisineCard(Cuisine cuisine, String langCode, AppLocalizations? l10n, int index) {
    return GestureDetector(
      onTap: () {
        if (cuisine.isPremium && !PurchaseService.instance.isPremium) {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => const PremiumScreen(),
            ),
          );
        } else {
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => CuisineDishesScreen(cuisine: cuisine),
            ),
          );
        }
      },
      child: FrostedGlassContainer(
        padding: const EdgeInsets.all(16),
        borderRadius: 22,
        child: Stack(
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                // Flag and Emoji
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Container(
                      width: 50,
                      height: 50,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        color: cuisine.primaryColor.withValues(alpha: 0.2),
                        border: Border.all(
                          color: cuisine.primaryColor.withValues(alpha: 0.5),
                          width: 1.5,
                        ),
                      ),
                      child: Center(
                        child: Text(cuisine.emoji, style: const TextStyle(fontSize: 26)),
                      ),
                    ),
                    Text(cuisine.flag, style: const TextStyle(fontSize: 22)),
                  ],
                ),

                // Name & Food Count
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      cuisine.getName(langCode),
                      style: AppTextStyles.titleLarge.copyWith(
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      cuisine.getDescription(langCode),
                      style: AppTextStyles.bodySmall.copyWith(
                        color: AppColors.textMuted,
                        fontSize: 11,
                        height: 1.3,
                      ),
                      maxLines: 2,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ],
                ),

                // Bottom badge
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      l10n?.cuisineFoodsCount(cuisine.foodCount) ?? '${cuisine.foodCount} yemek',
                      style: AppTextStyles.labelSmall.copyWith(
                        color: AppColors.primary,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const Icon(
                      Icons.arrow_forward_ios_rounded,
                      color: AppColors.textMuted,
                      size: 12,
                    ),
                  ],
                ),
              ],
            ),

            // Premium badge
            if (cuisine.isPremium)
              Positioned(
                top: 0,
                right: 32,
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                  decoration: BoxDecoration(
                    color: AppColors.gold.withValues(alpha: 0.2),
                    borderRadius: BorderRadius.circular(6),
                    border: Border.all(color: AppColors.gold, width: 1),
                  ),
                  child: Text(
                    l10n?.cuisinePremiumBadge ?? 'PREMIUM',
                    style: const TextStyle(
                      color: AppColors.gold,
                      fontSize: 9,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
          ],
        ),
      ),
    ).animate().fadeIn(delay: (60 * index).ms).scale(begin: const Offset(0.9, 0.9), end: const Offset(1, 1));
  }
}
