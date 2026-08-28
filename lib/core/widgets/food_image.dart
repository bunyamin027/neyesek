import 'package:flutter/material.dart';
import 'package:cached_network_image/cached_network_image.dart';
import '../../data/models/food_item.dart';

/// Akıllı ve Nefis Yemek Tarifleri Tarzı Yemek Görseli / Emoji Widget'ı
/// CachedNetworkImage ile yüksek performanslı disk & bellek önbellekleme ve pürüzsüz geçiş sunar.
class FoodImage extends StatelessWidget {
  final FoodItem food;
  final double? width;
  final double? height;
  final BorderRadius? borderRadius;
  final BoxFit fit;
  final double emojiSize;

  const FoodImage({
    super.key,
    required this.food,
    this.width,
    this.height,
    this.borderRadius,
    this.fit = BoxFit.cover,
    this.emojiSize = 32,
  });

  @override
  Widget build(BuildContext context) {
    final br = borderRadius ?? BorderRadius.circular(16);
    final imgPath = food.imagePath.trim();

    if (imgPath.isEmpty) {
      return _buildEmojiFallback(br);
    }

    Widget imageWidget;
    if (imgPath.startsWith('http://') || imgPath.startsWith('https://')) {
      imageWidget = CachedNetworkImage(
        imageUrl: imgPath,
        width: width,
        height: height,
        fit: fit,
        fadeInDuration: const Duration(milliseconds: 300),
        placeholder: (context, url) => _buildLoading(br),
        errorWidget: (context, url, error) => _buildEmojiFallback(br),
      );
    } else {
      final fullAssetPath = imgPath.startsWith('assets/')
          ? imgPath
          : 'assets/images/$imgPath';
      imageWidget = Image.asset(
        fullAssetPath,
        width: width,
        height: height,
        fit: fit,
        errorBuilder: (context, error, stackTrace) => _buildEmojiFallback(br),
      );
    }

    return ClipRRect(
      borderRadius: br,
      child: imageWidget,
    );
  }

  Widget _buildLoading(BorderRadius br) {
    return Container(
      width: width,
      height: height,
      decoration: BoxDecoration(
        color: food.color.withValues(alpha: 0.15),
        borderRadius: br,
      ),
      child: Center(
        child: SizedBox(
          width: 24,
          height: 24,
          child: CircularProgressIndicator(
            strokeWidth: 2,
            color: food.color,
          ),
        ),
      ),
    );
  }

  Widget _buildEmojiFallback(BorderRadius br) {
    return Container(
      width: width,
      height: height,
      decoration: BoxDecoration(
        gradient: RadialGradient(
          colors: [
            food.color.withValues(alpha: 0.35),
            food.color.withValues(alpha: 0.12),
          ],
        ),
        borderRadius: br,
        border: Border.all(
          color: food.color.withValues(alpha: 0.45),
          width: 1.5,
        ),
      ),
      child: Center(
        child: Text(
          food.emoji,
          style: TextStyle(fontSize: emojiSize),
        ),
      ),
    );
  }
}
