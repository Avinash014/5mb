package com.avinash.fivemb.data

import android.content.Context
import com.google.gson.Gson
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import java.io.InputStreamReader

class QuizRepository(private val context: Context) {

    private val gson = Gson()
    private val sharedPreferences = context.getSharedPreferences("5mb_prefs", Context.MODE_PRIVATE)

    suspend fun loadQuizData(): QuizData? = withContext(Dispatchers.IO) {
        try {
            val categories = mutableListOf<com.avinash.fivemb.data.Category>()
            val files = listOf("math.json", "puzzle.json", "treasure.json")
            
            for (file in files) {
                try {
                    val inputStream = context.assets.open(file)
                    val reader = InputStreamReader(inputStream)
                    val category = gson.fromJson(reader, com.avinash.fivemb.data.Category::class.java)
                    categories.add(category)
                } catch (e: Exception) {
                     e.printStackTrace()
                }
            }
            if (categories.isEmpty()) null else com.avinash.fivemb.data.QuizData(categories)
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }

    fun isLevelUnlocked(categoryId: String, levelId: Int): Boolean {
        // Level 1 is always unlocked
        if (levelId == 1) return true
        val maxUnlocked = sharedPreferences.getInt("unlock_$categoryId", 1)
        return levelId <= maxUnlocked
    }

    fun unlockNextLevel(categoryId: String, currentLevelId: Int) {
        val currentMax = sharedPreferences.getInt("unlock_$categoryId", 1)
        if (currentLevelId >= currentMax) {
            sharedPreferences.edit().putInt("unlock_$categoryId", currentLevelId + 1).apply()
        }
    }
    
    fun saveHighScore(categoryId: String, levelId: Int, score: Int) {
        val key = "score_${categoryId}_$levelId"
        val currentHigh = sharedPreferences.getInt(key, 0)
        if (score > currentHigh) {
            sharedPreferences.edit().putInt(key, score).apply()
        }
    }

    fun getHighScore(categoryId: String, levelId: Int): Int {
         return sharedPreferences.getInt("score_${categoryId}_$levelId", 0)
    }
}
