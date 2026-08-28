import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';


import '../../core/theme/app_colors.dart';
import '../../core/theme/app_text_styles.dart';
import '../../core/widgets/food_image.dart';
import '../../core/widgets/frosted_glass_container.dart';
import '../../core/widgets/gradient_background.dart';
import '../../data/models/food_item.dart';
import '../../data/services/history_service.dart';
import '../../l10n/app_localizations.dart';
import '../recipe_detail/recipe_detail_screen.dart';

class HistoryScreen extends StatefulWidget {
  const HistoryScreen({super.key});

  @override
  State<HistoryScreen> createState() => _HistoryScreenState();
}

class _HistoryScreenState extends State<HistoryScreen> {
  List<(FoodItem, DateTime)> _historyItems = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadHistory();
  }

  Future<void> _loadHistory() async {
    final list = await HistoryService.instance.getHistoryWithFoods();
    if (!mounted) return;
    setState(() {
      _historyItems = list;
      _isLoading = false;
    });
  }

  Future<void> _clearHistory() async {
    final l10n = AppLocalizations.of(context);
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: AppColors.surface,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: Text(l10n?.historyClear ?? 'Geçmişi Temizle', style: const TextStyle(color: Colors.white)),
        content: Text(
          l10n?.historyClearConfirm ?? 'Tüm çark geçmişinizi silmek istediğinizden emin misiniz?',
          style: const TextStyle(color: AppColors.textSecondary),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(l10n?.commonCancel ?? 'İptal', style: const TextStyle(color: AppColors.textMuted)),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(backgroundColor: AppColors.primary),
            onPressed: () => Navigator.pop(context, true),
            child: Text(l10n?.commonConfirm ?? 'Onayla', style: const TextStyle(color: Colors.white)),
          ),
        ],
      ),
    );

    if (confirmed == true) {
      await HistoryService.instance.clearHistory();
      _loadHistory();
    }
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
                padding: const EdgeInsets.fromLTRB(20, 16, 20, 12),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      l10n?.historyTitle ?? 'Karar Geçmişi',
                      style: AppTextStyles.displaySmall.copyWith(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    if (_historyItems.isNotEmpty)
                      IconButton(
                        icon: const Icon(Icons.delete_sweep_rounded, color: AppColors.textMuted, size: 26),
                        onPressed: _clearHistory,
                        tooltip: l10n?.historyClear ?? 'Geçmişi Temizle',
                      ),
                  ],
                ),
              ).animate().fadeIn(duration: 400.ms),

              // ─── Liste ───
              Expanded(
                child: _isLoading
                    ? const Center(child: CircularProgressIndicator(color: AppColors.primary))
                    : _historyItems.isEmpty
                        ? _buildEmptyState(l10n)
                        : ListView.builder(
                            padding: const EdgeInsets.fromLTRB(20, 8, 20, 30),
                            physics: const BouncingScrollPhysics(),
                            itemCount: _historyItems.length,
                            itemBuilder: (context, index) {
                              final item = _historyItems[index];
                              final food = item.$1;
                              final date = item.$2;
                              return _buildHistoryCard(food, date, langCode, l10n, index);
                            },
                          ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildEmptyState(AppLocalizations? l10n) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 40),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: 90,
              height: 90,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: AppColors.frostedGlassDark,
              ),
              child: const Icon(
                Icons.history_rounded,
                color: AppColors.textMuted,
                size: 42,
              ),
            ),
            const SizedBox(height: 20),
            Text(
              l10n?.historyEmptyTitle ?? 'Henüz Geçmiş Yok',
              style: AppTextStyles.headlineSmall.copyWith(color: Colors.white),
            ),
            const SizedBox(height: 8),
            Text(
              l10n?.historyEmptyDesc ?? 'Çarkta yaptığınız seçimler burada listelenecektir.',
              style: AppTextStyles.bodySmall.copyWith(color: AppColors.textMuted, height: 1.4),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    ).animate().fadeIn(duration: 500.ms);
  }

  Widget _buildHistoryCard(
    FoodItem food,
    DateTime date,
    String langCode,
    AppLocalizations? l10n,
    int index,
  ) {
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => RecipeDetailScreen(food: food),
          ),
        );
      },
      child: FrostedGlassContainer(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.all(14),
        borderRadius: 18,
        child: Row(
          children: [
            FoodImage(
              food: food,
              width: 52,
              height: 52,
              borderRadius: BorderRadius.circular(15),
              emojiSize: 24,
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    food.getName(langCode),
                    style: AppTextStyles.titleMedium.copyWith(
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      Text(
                        food.cuisineId.toUpperCase(),
                        style: AppTextStyles.labelSmall.copyWith(
                          color: AppColors.primary,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                      const SizedBox(width: 8),
                      Text('•', style: TextStyle(color: AppColors.textMuted, fontSize: 10)),
                      const SizedBox(width: 8),
                      Text(
                        _formatTimestamp(date),
                        style: AppTextStyles.labelSmall.copyWith(color: AppColors.textMuted),
                      ),
                    ],
                  ),
                ],
              ),
            ),
            const Icon(Icons.arrow_forward_ios_rounded, color: AppColors.textMuted, size: 14),
          ],
        ),
      ),
    ).animate().fadeIn(delay: (40 * index).ms).slideX(begin: 0.1, end: 0);
  }

  String _formatTimestamp(DateTime dt) {
    final now = DateTime.now();
    final diff = now.difference(dt);

    if (diff.inMinutes < 1) return 'Az önce';
    if (diff.inMinutes < 60) return '${diff.inMinutes} dk önce';
    if (diff.inHours < 24) return '${diff.inHours} saat önce';
    if (diff.inDays < 7) return '${diff.inDays} gün önce';
    return '${dt.day}.${dt.month}.${dt.year}';
  }
}
