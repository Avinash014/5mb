package com.avinash.fivemb.ui

import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument

@Composable
fun QuizNavigation(viewModel: QuizViewModel) {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = "menu") {
        composable("menu") {
            MainMenuScreen(
                categories = viewModel.categories.collectAsState().value,
                onCategorySelected = { categoryId ->
                    navController.navigate("levels/$categoryId")
                }
            )
        }
        
        composable(
            route = "levels/{categoryId}",
            arguments = listOf(navArgument("categoryId") { type = NavType.StringType })
        ) { backStackEntry ->
            val categoryId = backStackEntry.arguments?.getString("categoryId") ?: ""
            val category = viewModel.getCategory(categoryId)
            
            if (category != null) {
                LevelSelectionScreen(
                    category = category,
                    isLevelUnlocked = { levelId -> viewModel.isLevelUnlocked(categoryId, levelId) },
                    onLevelSelected = { levelId ->
                        navController.navigate("quiz/$categoryId/$levelId")
                    },
                    onBack = { navController.popBackStack() }
                )
            }
        }

        composable(
            route = "quiz/{categoryId}/{levelId}",
            arguments = listOf(
                navArgument("categoryId") { type = NavType.StringType },
                navArgument("levelId") { type = NavType.IntType }
            )
        ) { backStackEntry ->
            val categoryId = backStackEntry.arguments?.getString("categoryId") ?: ""
            val levelId = backStackEntry.arguments?.getInt("levelId") ?: 1
            val level = viewModel.getLevel(categoryId, levelId)

            if (level != null) {
                QuizScreen(
                    level = level,
                    onQuizFinished = { score, total, time ->
                         viewModel.completeLevel(categoryId, levelId, score)
                         navController.navigate("stats/$categoryId/$levelId/$score/$total/$time") {
                             popUpTo("levels/$categoryId") {
                                 inclusive = false
                             }
                         }
                    },
                    onBack = { navController.popBackStack() }
                )
            }
        }
        
        composable(
             route = "stats/{categoryId}/{levelId}/{score}/{total}/{time}",
             arguments = listOf(
                navArgument("categoryId") { type = NavType.StringType },
                navArgument("levelId") { type = NavType.IntType },
                navArgument("score") { type = NavType.IntType },
                navArgument("total") { type = NavType.IntType },
                navArgument("time") { type = NavType.LongType }
            )
        ) { backStackEntry ->
             val score = backStackEntry.arguments?.getInt("score") ?: 0
             val total = backStackEntry.arguments?.getInt("total") ?: 0
             val time = backStackEntry.arguments?.getLong("time") ?: 0L
             
             StatsScreen(
                 score = score,
                 totalQuestions = total,
                 timeTakenMillis = time,
                 onHome = {
                     navController.popBackStack("menu", inclusive = false)
                 },
                 onReplay = {
                      navController.popBackStack()
                 }
             )
        }
    }
}
