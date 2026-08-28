import 'package:audioplayers/audioplayers.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SoundService {
  static final SoundService instance = SoundService._internal();
  SoundService._internal();

  final AudioPlayer _tickPlayer = AudioPlayer();
  final AudioPlayer _winPlayer = AudioPlayer();

  static const String _keySound = 'sound_effects_enabled';
  bool _isEnabled = true;
  bool get isEnabled => _isEnabled;

  Future<void> init() async {
    final prefs = await SharedPreferences.getInstance();
    _isEnabled = prefs.getBool(_keySound) ?? true;

    // Pre-configure players for low latency
    await _tickPlayer.setReleaseMode(ReleaseMode.stop);
    await _winPlayer.setReleaseMode(ReleaseMode.stop);
  }

  Future<void> setEnabled(bool enabled) async {
    _isEnabled = enabled;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_keySound, enabled);
  }

  Future<void> playTick() async {
    if (!_isEnabled) return;
    try {
      await _tickPlayer.stop();
      await _tickPlayer.play(AssetSource('sounds/wheel_tick.wav'), volume: 0.6);
    } catch (_) {}
  }

  Future<void> playWin() async {
    if (!_isEnabled) return;
    try {
      await _winPlayer.stop();
      await _winPlayer.play(AssetSource('sounds/win_chime.wav'), volume: 0.85);
    } catch (_) {}
  }

  void dispose() {
    _tickPlayer.dispose();
    _winPlayer.dispose();
  }
}
