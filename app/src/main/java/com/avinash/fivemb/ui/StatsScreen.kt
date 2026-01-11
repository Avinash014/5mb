package com.avinash.fivemb.ui

import androidx.compose.foundation.layout.*
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.avinash.fivemb.data.AdConfig
import com.avinash.fivemb.ui.theme.NeonCyan
import com.avinash.fivemb.ui.theme.NeonPurple

@Composable
fun StatsScreen(
    score: Int,
    totalQuestions: Int,
    timeTakenMillis: Long,
    onHome: () -> Unit,
    onReplay: () -> Unit
) {
    GameBackground {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // Ad Banner
            if (AdConfig.SHOW_STATS_BANNER) {
                GlassCard(modifier = Modifier.fillMaxWidth().height(50.dp)) {
                    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                         Text("Ad Banner", color = Color.White.copy(alpha=0.5f))
                    }
                }
                Spacer(modifier = Modifier.height(32.dp))
            }
        
            Text(
                text = "Level Complete!",
                style = MaterialTheme.typography.displaySmall,
                fontWeight = FontWeight.Bold,
                color = NeonCyan
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
                        color = Color.White.copy(alpha=0.7f),
                        letterSpacing = 2.sp
                    )
                    Text(
                        text = "$score / $totalQuestions",
                        style = MaterialTheme.typography.displayMedium,
                        fontWeight = FontWeight.Black,
                        color = Color.White
                    )
                    
                    Spacer(modifier = Modifier.height(24.dp))
                    
                    Text(
                        text = "TIME TAKEN",
                        style = MaterialTheme.typography.labelMedium,
                        color = Color.White.copy(alpha=0.7f),
                        letterSpacing = 2.sp
                    )
                    val seconds = timeTakenMillis / 1000
                    Text(
                        text = "${seconds}s",
                        style = MaterialTheme.typography.headlineMedium,
                        color = NeonPurple,
                        fontWeight = FontWeight.Bold
                    )
                }
            }
            
            Spacer(modifier = Modifier.height(48.dp))
            
            BouncyButton(
                onClick = onReplay,
                modifier = Modifier.fillMaxWidth(0.8f),
                containerColor = NeonPurple
            ) {
                Text("Replay Level", style = MaterialTheme.typography.titleMedium)
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            BouncyButton(
                onClick = onHome,
                modifier = Modifier.fillMaxWidth(0.8f),
                containerColor = Color.White.copy(alpha=0.2f)
            ) {
                Text("Back to Menu", style = MaterialTheme.typography.titleMedium)
            }
        }
    }
}
