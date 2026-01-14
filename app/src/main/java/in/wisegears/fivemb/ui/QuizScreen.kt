package `in`.wisegears.fivemb.ui

import androidx.compose.animation.*
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Close
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.filled.Info
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Dialog
import `in`.wisegears.fivemb.data.AdConfig
import `in`.wisegears.fivemb.data.Level
import `in`.wisegears.fivemb.ui.theme.GreenSuccess
import `in`.wisegears.fivemb.ui.theme.RedError
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun QuizScreen(
    level: Level,
    timerDuration: Int,
    isLivesMode: Boolean,
    isShowExplanation: Boolean,
    onCorrectAnswer: () -> Unit,
    onWrongAnswer: () -> Unit,
    onQuizFinished: (Int, Int, Long, List<`in`.wisegears.fivemb.data.Question>) -> Unit,
    onBack: () -> Unit
) {
    val totalTimeSeconds = timerDuration
    var currentQuestionIndex by remember { mutableIntStateOf(0) }
    var selectedOptionIndex by remember { mutableStateOf<Int?>(null) }
    var score by remember { mutableIntStateOf(0) }
    var lives by remember { mutableIntStateOf(3) }
    var timeLeft by remember { mutableLongStateOf(totalTimeSeconds * 1000L) } 
    var isProcessing by remember { mutableStateOf(false) } 
    var showExplanation by remember { mutableStateOf(false) }
    val wrongAnswers = remember { mutableListOf<`in`.wisegears.fivemb.data.Question>() }
    
    // Fix: Ensure currentQuestion is stable and only derived from index
    val currentQuestion = remember(currentQuestionIndex, level) {
         level.questions.getOrNull(currentQuestionIndex)
    }
    
    LaunchedEffect(key1 = "timer") {
        // Fix: Use a loop that respects the pause
        while (timeLeft > 0 && currentQuestion != null && (!isLivesMode || lives > 0)) {
            val start = System.currentTimeMillis()
            delay(100)
            val end = System.currentTimeMillis()
            
            // Only decrement if not showing explanation and not processing answer transition
            if (!isProcessing && !showExplanation) {
                 val elapsed = end - start 
                 // Safeguard against large drifts, but simplistic subtraction is fine here
                 timeLeft = (timeLeft - elapsed).coerceAtLeast(0)
            }
        }
        if (timeLeft <= 0) {
             onQuizFinished(score, level.questions.size, (totalTimeSeconds * 1000L), wrongAnswers)
        }
    }
    
    val coroutineScope = rememberCoroutineScope()


    if (showExplanation && currentQuestion?.explanation != null) {
        Dialog(onDismissRequest = { /* Prevent dismiss */ }) {
            // Darker background for readability
            Box(
                modifier = Modifier
                    .background(MaterialTheme.colorScheme.surfaceVariant, RoundedCornerShape(16.dp))
                    .padding(1.dp) // Border effect
            ) {
                 GlassCard(modifier = Modifier.padding(0.dp)) {
                    Column(
                        modifier = Modifier.padding(24.dp),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Icon(Icons.Default.Info, contentDescription = null, tint = MaterialTheme.colorScheme.secondary, modifier = Modifier.size(48.dp))
                        Spacer(modifier = Modifier.height(16.dp))
                        Text("Did You Know?", style = MaterialTheme.typography.headlineSmall, color = MaterialTheme.colorScheme.onSurface, fontWeight = FontWeight.Bold)
                        Spacer(modifier = Modifier.height(8.dp))
                        Text(
                            text = currentQuestion.explanation,
                            style = MaterialTheme.typography.bodyLarge,
                            color = MaterialTheme.colorScheme.onSurface, 
                            textAlign = TextAlign.Center
                        )
                        Spacer(modifier = Modifier.height(24.dp))
                        BouncyButton(
                            onClick = {
                                showExplanation = false
                                 coroutineScope.launch {
                                    // Resume Logic
                                    if (currentQuestionIndex < level.questions.size - 1) {
                                        currentQuestionIndex++
                                        selectedOptionIndex = null
                                        isProcessing = false
                                    } else {
                                        val timeTaken = (totalTimeSeconds * 1000L) - timeLeft
                                        onQuizFinished(score, level.questions.size, timeTaken, wrongAnswers)
                                    }
                                }
                            },
                            containerColor = MaterialTheme.colorScheme.primary
                        ) {
                            Text("Got it!", color = MaterialTheme.colorScheme.onPrimary)
                        }
                    }
                }
            }
        }
    }

    GameBackground {
        Column(
            modifier = Modifier.fillMaxSize()
        ) {
            // Header
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                IconButton(onClick = onBack) {
                    Icon(Icons.Default.Close, contentDescription = "Exit", tint = MaterialTheme.colorScheme.onSurface)
                }
                
                if (isLivesMode) {
                    Row {
                         repeat(3) { index ->
                             Icon(
                                 Icons.Default.Favorite, 
                                 contentDescription = null, 
                                 tint = if (index < lives) RedError else MaterialTheme.colorScheme.onSurface.copy(alpha=0.3f),
                                 modifier = Modifier.size(24.dp)
                             )
                         }
                    }
                }
                
                Text(
                    text = "${timeLeft / 1000}s",
                    style = MaterialTheme.typography.titleLarge,
                    color = if (timeLeft < 10000) RedError else MaterialTheme.colorScheme.primary,
                    fontWeight = FontWeight.Bold
                )
            }

            if (currentQuestion != null) {
                Column(
                    modifier = Modifier.padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                     // Ad Placeholder Configurable
                    if (AdConfig.SHOW_QUIZ_BANNER) {
                        AdMobBanner()
                        Spacer(modifier = Modifier.height(24.dp))
                    } else {
                        Spacer(modifier = Modifier.height(74.dp)) // Maintain spacing
                    }

                    
                    Spacer(modifier = Modifier.height(32.dp))
                    
                    AnimatedContent(
                        targetState = currentQuestion,
                        transitionSpec = {
                            fadeIn() + slideInHorizontally { width -> width } togetherWith
                            fadeOut() + slideOutHorizontally { width -> -width }
                        }, label = "questionAnim"
                    ) { question ->
                        Text(
                            text = question.text,
                            style = MaterialTheme.typography.headlineSmall,
                            textAlign = TextAlign.Center,
                            color = MaterialTheme.colorScheme.onSurface,
                            fontWeight = FontWeight.Bold,
                            minLines = 3
                        )
                    }

                    Spacer(modifier = Modifier.weight(1f))
                    
                    currentQuestion.options.forEachIndexed { index, text ->
                        val isSelected = selectedOptionIndex == index
                        
                        val containerColor = if (selectedOptionIndex != null) {
                            if (index == currentQuestion.correctIndex) GreenSuccess
                            else if (isSelected) RedError
                            else MaterialTheme.colorScheme.surfaceVariant
                        } else {
                            MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.5f)
                        }
                        
                        val contentColor = if (selectedOptionIndex != null && (index == currentQuestion.correctIndex || isSelected)) Color.White else MaterialTheme.colorScheme.onSurface

                        BouncyButton(
                            onClick = {
                                if (selectedOptionIndex == null) {
                                    isProcessing = true
                                    selectedOptionIndex = index
                                    val isCorrect = index == currentQuestion.correctIndex
                                    
                                    if (isCorrect) {
                                        score++
                                        onCorrectAnswer()
                                    } else {
                                        onWrongAnswer()
                                        if (currentQuestion != null) wrongAnswers.add(currentQuestion)
                                        if (isLivesMode) {
                                            lives--
                                        }
                                    }
                                    
                                    coroutineScope.launch {
                                        delay(1000)
                                        // LOGIC UPDATE: Show explanation ONLY on WRONG answer if explanation exists AND setting is ON
                                        val showExplanationDialog = !isCorrect && isShowExplanation && currentQuestion.explanation != null
                                        
                                        if (isLivesMode && lives == 0) {
                                             val timeTaken = (totalTimeSeconds * 1000L) - timeLeft
                                             onQuizFinished(score, level.questions.size, timeTaken, wrongAnswers)
                                        } else {
                                            if (showExplanationDialog) {
                                                showExplanation = true
                                            } else {
                                                if (currentQuestionIndex < level.questions.size - 1) {
                                                    currentQuestionIndex++
                                                    selectedOptionIndex = null
                                                    isProcessing = false
                                                } else {
                                                    val timeTaken = (totalTimeSeconds * 1000L) - timeLeft
                                                    onQuizFinished(score, level.questions.size, timeTaken, wrongAnswers)
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(vertical = 6.dp),
                            containerColor = containerColor,
                            contentColor = contentColor
                        ) {
                             Text(
                                text = text,
                                style = MaterialTheme.typography.bodyLarge,
                                fontWeight = FontWeight.SemiBold
                            )
                        }
                    }
                    Spacer(modifier = Modifier.height(32.dp))
                }
            }
        }
    }
}
