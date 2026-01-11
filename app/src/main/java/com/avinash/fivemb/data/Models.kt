package com.avinash.fivemb.data

data class QuizData(
    val categories: List<Category>
)

data class Category(
    val id: String,
    val name: String,
    val levels: List<Level>
)

data class Level(
    val id: Int,
    val questions: List<Question>
)

data class Question(
    val id: String,
    val text: String,
    val options: List<String>,
    val correctIndex: Int,
    val difficulty: Int = 1, // 1=Easy, 2=Medium, 3=Hard
    val explanation: String? = null
)

data class GameStats(
    val totalScore: Int = 0,
    val unlockedLevels: Map<String, Int> = mapOf()
)
