package `in`.wisegears.fivemb.ui

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import `in`.wisegears.fivemb.data.AdConfig
import `in`.wisegears.fivemb.ui.theme.NeonCyan
import `in`.wisegears.fivemb.ui.theme.NeonPurple

@Composable
fun StatsScreen(
    score: Int,
    timeTakenMillis: Long,
    wrongQuestions: List<`in`.wisegears.fivemb.data.Question>,
    onHome: () -> Unit,
    onReplay: () -> Unit
) {
    GameBackground {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp)
                .verticalScroll(androidx.compose.foundation.rememberScrollState()),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Top // Changed from Center to accommodate scroll
        ) {
            Spacer(modifier = Modifier.height(32.dp)) // Top padding

            // Ad Banner
            if (AdConfig.SHOW_STATS_BANNER) {
                GlassCard(modifier = Modifier.fillMaxWidth().height(50.dp)) {
                    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                         Text("Ad Banner", color = MaterialTheme.colorScheme.onSurface.copy(alpha=0.5f))
                    }
                }
                Spacer(modifier = Modifier.height(32.dp))
            }
        
            Text(
                text = "Level Complete!",
                style = MaterialTheme.typography.displaySmall,
                fontWeight = FontWeight.Bold,
                color = MaterialTheme.colorScheme.primary
            )
            
            Spacer(modifier = Modifier.height(48.dp))
            
            GlassCard(modifier = Modifier.fillMaxWidth()) {
                Column(
                    modifier = Modifier.padding(24.dp).fillMaxWidth(),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        text = "SCORE",
                        style = MaterialTheme.typography.labelMedium,
                        color = MaterialTheme.colorScheme.onSurface.copy(alpha=0.7f),
                        letterSpacing = 2.sp
                    )
                    Text(
                        text = "$score",
                        style = MaterialTheme.typography.displayMedium,
                        fontWeight = FontWeight.Black,
                        color = MaterialTheme.colorScheme.onSurface
                    )
                    
                    Spacer(modifier = Modifier.height(24.dp))
                    
                    Text(
                        text = "TIME TAKEN",
                        style = MaterialTheme.typography.labelMedium,
                        color = MaterialTheme.colorScheme.onSurface.copy(alpha=0.7f),
                        letterSpacing = 2.sp
                    )
                    val seconds = timeTakenMillis / 1000
                    Text(
                        text = "${seconds}s",
                        style = MaterialTheme.typography.headlineMedium,
                        color = MaterialTheme.colorScheme.secondary,
                        fontWeight = FontWeight.Bold
                    )
                }
            }
            
            Spacer(modifier = Modifier.height(32.dp))
            
            BouncyButton(
                onClick = onReplay,
                modifier = Modifier.fillMaxWidth(0.8f),
                containerColor = MaterialTheme.colorScheme.primary
            ) {
                Text("Replay Level", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.onPrimary)
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            BouncyButton(
                onClick = onHome,
                modifier = Modifier.fillMaxWidth(0.8f),
                containerColor = MaterialTheme.colorScheme.surfaceVariant
            ) {
                Text("Back to Menu", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.onSurfaceVariant)
            }

            // Review Mistakes Section
            if (wrongQuestions.isNotEmpty()) {
                Spacer(modifier = Modifier.height(48.dp))
                
                Text(
                    text = "Review Mistakes",
                    style = MaterialTheme.typography.titleLarge,
                    color = MaterialTheme.colorScheme.error,
                    fontWeight = FontWeight.Bold
                )
                
                Spacer(modifier = Modifier.height(16.dp))
                
                wrongQuestions.forEach { question ->
                    GlassCard(modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp)) {
                         Column(modifier = Modifier.padding(16.dp)) {
                             Text(
                                 text = question.text,
                                 style = MaterialTheme.typography.titleMedium,
                                 color = MaterialTheme.colorScheme.onSurface,
                                 fontWeight = FontWeight.SemiBold
                             )
                             Spacer(modifier = Modifier.height(8.dp))
                             
                             Text(
                                 text = "Correct Answer:",
                                 style = MaterialTheme.typography.labelMedium,
                                 color = MaterialTheme.colorScheme.onSurface.copy(alpha=0.6f)
                             )
                             Text(
                                 text = question.options[question.correctIndex],
                                 style = MaterialTheme.typography.bodyLarge,
                                 color = `in`.wisegears.fivemb.ui.theme.GreenSuccess,
                                 fontWeight = FontWeight.Bold
                             )
                             
                             if (question.explanation != null) {
                                 Spacer(modifier = Modifier.height(8.dp))
                                 Text(
                                     text = "Explanation:",
                                     style = MaterialTheme.typography.labelMedium,
                                     color = MaterialTheme.colorScheme.onSurface.copy(alpha=0.6f)
                                 )
                                 Text(
                                     text = question.explanation,
                                     style = MaterialTheme.typography.bodyMedium,
                                     color = MaterialTheme.colorScheme.onSurface.copy(alpha=0.8f)
                                 )
                             }
                         }
                    }
                }
                Spacer(modifier = Modifier.height(32.dp))
            }
        }
    }
}
