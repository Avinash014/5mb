package com.avinash.fivemb.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Close
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import com.avinash.fivemb.data.Level
import com.avinash.fivemb.data.Question
import com.avinash.fivemb.ui.theme.GreenSuccess
import com.avinash.fivemb.ui.theme.RedError
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun QuizScreen(
    level: Level,
    onQuizFinished: (Int, Int, Long) -> Unit,
    onBack: () -> Unit
) {
    // Game constants
    val totalTimeSeconds = 60
    
    // State
    var currentQuestionIndex by remember { mutableIntStateOf(0) }
    var selectedOptionIndex by remember { mutableStateOf<Int?>(null) }
    var score by remember { mutableIntStateOf(0) }
    var timeLeft by remember { mutableLongStateOf(totalTimeSeconds * 1000L) } // Milliseconds
    var isProcessing by remember { mutableStateOf(false) } // To prevent double clicks and timer during delay
    
    val currentQuestion = level.questions.getOrNull(currentQuestionIndex)
    
    // Timer
    LaunchedEffect(key1 = "timer") {
        while (timeLeft > 0 && currentQuestion != null) {
            delay(100)
            if (!isProcessing) {
                 timeLeft -= 100
            }
        }
        if (timeLeft <= 0) {
            // Time up!
             onQuizFinished(score, level.questions.size, (totalTimeSeconds * 1000L))
        }
    }
    
    val coroutineScope = rememberCoroutineScope()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Level ${level.id}") },
                actions = {
                    Text(
                        text = "${timeLeft / 1000}s",
                        style = MaterialTheme.typography.titleMedium,
                        color = if (timeLeft < 10000) RedError else MaterialTheme.colorScheme.onSurface,
                        modifier = Modifier.padding(end = 16.dp)
                    )
                },
                navigationIcon = {
                     IconButton(onClick = onBack) {
                        Icon(Icons.Default.Close, contentDescription = "Exit")
                    }
                }
            )
        }
    ) { paddingValues ->
        if (currentQuestion != null) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(paddingValues)
                    .padding(16.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                // Progress
                LinearProgressIndicator(
                    progress = (currentQuestionIndex + 1).toFloat() / level.questions.size,
                    modifier = Modifier.fillMaxWidth()
                )
                
                Spacer(modifier = Modifier.height(32.dp))
                
                // Question
                Text(
                    text = currentQuestion.text,
                    style = MaterialTheme.typography.headlineSmall,
                    textAlign = TextAlign.Center,
                    minLines = 3
                )
                
                Spacer(modifier = Modifier.height(32.dp))
                
                // Options
                currentQuestion.options.forEachIndexed { index, text ->
                    val isSelected = selectedOptionIndex == index
                    
                    // Button Colors
                    // Default: PrimaryContainer
                    // Selected & Correct: Green
                    // Selected & Wrong: Red
                    // Not Selected & isCorrect (Show Answer): Green (after selection)
                    
                    val buttonColors = if (selectedOptionIndex != null) {
                        if (index == currentQuestion.correctIndex) {
                            ButtonDefaults.buttonColors(containerColor = GreenSuccess)
                        } else if (isSelected) {
                            ButtonDefaults.buttonColors(containerColor = RedError)
                        } else {
                            ButtonDefaults.filledTonalButtonColors()
                        }
                    } else {
                        ButtonDefaults.filledTonalButtonColors()
                    }
                    
                    Button(
                        onClick = {
                            if (selectedOptionIndex == null) {
                                isProcessing = true
                                selectedOptionIndex = index
                                if (index == currentQuestion.correctIndex) score++
                                
                                coroutineScope.launch {
                                    delay(1000)
                                    // Move next
                                    if (currentQuestionIndex < level.questions.size - 1) {
                                        currentQuestionIndex++
                                        selectedOptionIndex = null
                                        isProcessing = false
                                    } else {
                                        // Finish
                                        val timeTaken = (totalTimeSeconds * 1000L) - timeLeft
                                        onQuizFinished(score, level.questions.size, timeTaken)
                                    }
                                }
                            }
                        },
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(vertical = 8.dp)
                            .height(56.dp),
                        colors = buttonColors,
                        shape = RoundedCornerShape(12.dp)
                    ) {
                        Text(
                            text = text,
                            style = MaterialTheme.typography.bodyLarge,
                            fontWeight = FontWeight.SemiBold
                        )
                    }
                }
            }
        }
    }
}
