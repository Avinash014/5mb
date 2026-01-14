package com.avinash.fivemb.ui

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewModelScope
import com.avinash.fivemb.data.Category
import com.avinash.fivemb.data.Level
import com.avinash.fivemb.data.QuizRepository
import com.avinash.fivemb.data.SettingsRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class QuizViewModel(
    private val repository: QuizRepository,
    val settingsRepository: SettingsRepository,
    private val soundManager: com.avinash.fivemb.utils.SoundManager
) : ViewModel() {

    private val _categories = MutableStateFlow<List<Category>>(emptyList())
    val categories: StateFlow<List<Category>> = _categories.asStateFlow()
    
    val settings = settingsRepository.settings

    init {
        loadData()
    }

    private fun loadData() {
        viewModelScope.launch {
            val data = repository.loadQuizData()
            data?.let {
                _categories.value = it.categories
            }
        }
    }

    fun getCategory(categoryId: String): Category? {
        return _categories.value.find { it.id == categoryId }
    }
    
    fun getLevel(categoryId: String, levelId: Int): Level? {
        val level = getCategory(categoryId)?.levels?.find { it.id == levelId }
        return level?.copy(questions = level.questions.shuffled())
    }
    
    fun isLevelUnlocked(categoryId: String, levelId: Int): Boolean {
        return repository.isLevelUnlocked(categoryId, levelId)
    }

    fun getHighScore(categoryId: String, levelId: Int): Int {
        return repository.getHighScore(categoryId, levelId)
    }

    fun completeLevel(categoryId: String, levelId: Int, score: Int) {
        repository.saveHighScore(categoryId, levelId, score)
        repository.unlockNextLevel(categoryId, levelId)
    }
    
    // Feedback
    fun playCorrectEffect() {
        if (settings.value.isSoundEnabled) soundManager.playCorrectSound()
        if (settings.value.isVibrationEnabled) soundManager.vibrateCorrect()
    }
    
    fun playWrongEffect() {
        if (settings.value.isSoundEnabled) soundManager.playWrongSound()
        if (settings.value.isVibrationEnabled) soundManager.vibrateWrong()
    }
    
    // Settings Updates
    fun updateTimer(seconds: Int) = settingsRepository.updateTimerDuration(seconds)
    fun toggleSound(enabled: Boolean) = settingsRepository.toggleSound(enabled)
    fun toggleVibration(enabled: Boolean) = settingsRepository.toggleVibration(enabled)
    fun toggleLives(enabled: Boolean) = settingsRepository.toggleLivesMode(enabled)
    fun toggleDarkMode(enabled: Boolean) = settingsRepository.toggleDarkMode(enabled)
    fun toggleShowExplanation(enabled: Boolean) = settingsRepository.toggleShowExplanation(enabled)
}

class QuizViewModelFactory(
    private val repository: QuizRepository,
    private val settingsRepository: SettingsRepository,
    private val soundManager: com.avinash.fivemb.utils.SoundManager
) : ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(QuizViewModel::class.java)) {
            @Suppress("UNCHECKED_CAST")
            return QuizViewModel(repository, settingsRepository, soundManager) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}
