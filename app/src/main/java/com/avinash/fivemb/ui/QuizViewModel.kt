package com.avinash.fivemb.ui

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewModelScope
import com.avinash.fivemb.data.Category
import com.avinash.fivemb.data.Level
import com.avinash.fivemb.data.Question
import com.avinash.fivemb.data.QuizRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class QuizViewModel(private val repository: QuizRepository) : ViewModel() {

    private val _categories = MutableStateFlow<List<Category>>(emptyList())
    val categories: StateFlow<List<Category>> = _categories.asStateFlow()

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
        return getCategory(categoryId)?.levels?.find { it.id == levelId }
    }
    
    fun isLevelUnlocked(categoryId: String, levelId: Int): Boolean {
        return repository.isLevelUnlocked(categoryId, levelId)
    }

    fun completeLevel(categoryId: String, levelId: Int, score: Int) {
        repository.saveHighScore(categoryId, levelId, score)
        // Unlock next logic is usually "if passed"
        // For this game, let's say > 0 score unlocks next? 
        // Or maybe just finishing it. Let's assume > 50% needed or just finish.
        // Simplified: Finish unlocks next.
        repository.unlockNextLevel(categoryId, levelId)
    }
}

class QuizViewModelFactory(private val repository: QuizRepository) : ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(QuizViewModel::class.java)) {
            @Suppress("UNCHECKED_CAST")
            return QuizViewModel(repository) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}
