# Ne Yesek? (What to Eat?) 🍽️

**Ne Yesek?** is a beautifully designed, intuitive Flutter application that helps users decide what to cook or eat today. With a fun, interactive "Smart Food Wheel" and a rich database of over 212 authentic recipes from 10 different world cuisines, finding your next meal has never been easier or more delicious.

## 🌟 Key Features

*   🎡 **Smart Food Wheel:** Can't decide what to eat? Spin the interactive wheel to get a random recipe suggestion based on your preferences.
*   🌍 **10 Global Cuisines:** Explore culinary delights from Turkish, Italian, Japanese, Mexican, French, Indian, Chinese, Korean, Spanish, and American cuisines.
*   📖 **212+ Authentic Recipes:** Detailed recipes complete with high-quality images, prep time, difficulty, calorie counts, and step-by-step instructions.
*   ⏱️ **Advanced Filtering:** Filter recipes by:
    *   Maximum Preparation Time
    *   Maximum Calories
    *   Difficulty Level (Easy, Medium, Hard)
*   ❤️ **Favorites System:** Save your most-loved recipes to your personal cookbook for quick access later.
*   💎 **Premium Experience:** Unlock all cuisines and enjoy an ad-free experience with flexible monthly and yearly subscription plans (powered by In-App Purchases).
*   🌐 **Multi-Language Support:** Fully localized in multiple languages including English, Turkish, German, Spanish, and more.
*   🎨 **Modern UI/UX:** A visually stunning interface with glassmorphism effects, smooth animations, and sound effects for the interactive wheel.

## 📸 Screenshots

*(You can add screenshots here later by placing image links)*
<!-- 
<img src="screenshots/home.png" width="200"/>
<img src="screenshots/wheel.png" width="200"/>
<img src="screenshots/recipe.png" width="200"/> 
-->

## 🛠️ Tech Stack & Architecture

*   **Framework:** Flutter (Dart)
*   **Architecture:** Feature-first modular architecture
*   **State Management:** Provider
*   **Local Storage:** SharedPreferences (for favorites and settings)
*   **In-App Purchases:** `in_app_purchase` package for handling Apple App Store subscriptions.
*   **Localization:** Flutter's native `flutter_localizations` with `.arb` files.
*   **Audio:** `audioplayers` for wheel spinning sound effects.
*   **Animations:** Implicit animations and custom `AnimationController`s.

## 🚀 Getting Started

To run this project locally, follow these steps:

### Prerequisites

*   Flutter SDK (latest stable version recommended)
*   Dart SDK
*   Xcode (for iOS) or Android Studio (for Android)

### Installation

1.  **Clone the repository** (if applicable):
    ```bash
    git clone https://github.com/bunyamin027/neyesek.git
    cd neyesek
    ```

2.  **Install dependencies:**
    ```bash
    flutter pub get
    ```

3.  **Run the app:**
    ```bash
    flutter run
    ```

## 💰 In-App Purchases Setup (Developers)

This app uses Apple's native in-app purchase system for its Premium features. To test purchases in the sandbox environment:
1. Ensure your bundle ID matches the App Store Connect record (`com.kahramanapp.neyesek`).
2. Add your sandbox tester account in your device settings.
3. The current Product IDs used in the app are:
   - Monthly: `com.neyesek.app.premium.monthly`
   - Yearly: `com.neyesek.app.premium.yearly`

## 📄 License

This project is proprietary and confidential. Unauthorized copying of this file, via any medium, is strictly prohibited.
© 2024 Ne Yesek
