package `in`.wisegears.fivemb.data

import android.content.Context
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

class SettingsRepository(context: Context) {
    private val prefs = context.getSharedPreferences("5mb_settings", Context.MODE_PRIVATE)

    private val _settings = MutableStateFlow(loadSettings())
    val settings: StateFlow<AppSettings> = _settings.asStateFlow()

    private fun loadSettings(): AppSettings {
        return AppSettings(
            timerDurationSeconds = prefs.getInt("timer_duration", 60),
            isSoundEnabled = prefs.getBoolean("sound_enabled", true),
            isVibrationEnabled = prefs.getBoolean("vibration_enabled", true),
            isDarkMode = prefs.getBoolean("dark_mode", false),
            isLivesMode = true, // Always enabled per user request
            isShowExplanation = prefs.getBoolean("show_explanation", true)
        )
    }

    fun updateTimerDuration(seconds: Int) {
        prefs.edit().putInt("timer_duration", seconds).apply()
        refresh()
    }

    fun toggleSound(enabled: Boolean) {
        prefs.edit().putBoolean("sound_enabled", enabled).apply()
        refresh()
    }

    fun toggleVibration(enabled: Boolean) {
        prefs.edit().putBoolean("vibration_enabled", enabled).apply()
        refresh()
    }
    
    fun toggleLivesMode(enabled: Boolean) {
        prefs.edit().putBoolean("lives_mode", enabled).apply()
        refresh()
    }
    
    fun toggleDarkMode(enabled: Boolean) {
        prefs.edit().putBoolean("dark_mode", enabled).apply()
        refresh()
    }

    fun toggleShowExplanation(enabled: Boolean) {
        prefs.edit().putBoolean("show_explanation", enabled).apply()
        refresh()
    }

    private fun refresh() {
        _settings.value = loadSettings()
    }
}

data class AppSettings(
    val timerDurationSeconds: Int,
    val isSoundEnabled: Boolean,
    val isVibrationEnabled: Boolean,
    val isDarkMode: Boolean,
    val isLivesMode: Boolean,
    val isShowExplanation: Boolean
)
