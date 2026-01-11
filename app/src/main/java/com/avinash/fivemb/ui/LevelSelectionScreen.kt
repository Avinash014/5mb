package com.avinash.fivemb.ui

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.Lock
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.avinash.fivemb.data.Category
import com.avinash.fivemb.data.Level
import com.avinash.fivemb.ui.theme.NeonBlue
import com.avinash.fivemb.ui.theme.AlertYellow

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LevelSelectionScreen(
    category: Category,
    isLevelUnlocked: (Int) -> Boolean,
    getHighScore: (Int) -> Int,
    onLevelSelected: (Int) -> Unit,
    onBack: () -> Unit
) {
    GameBackground {
        Column(modifier = Modifier.fillMaxSize()) {
            TopAppBar(
                title = { Text(category.name, color = Color.White) },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back", tint = Color.White)
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = Color.Transparent)
            )
            
            LazyColumn(
                contentPadding = PaddingValues(16.dp),
                verticalArrangement = Arrangement.spacedBy(16.dp),
            ) {
                items(category.levels) { level ->
                    val unlocked = isLevelUnlocked(level.id)
                    val highScore = getHighScore(level.id)
                    
                    LevelListItem(
                        level = level, 
                        isUnlocked = unlocked, 
                        highScore = highScore,
                        onClick = { if (unlocked) onLevelSelected(level.id) }
                    )
                }
            }
        }
    }
}

@Composable
fun LevelListItem(level: Level, isUnlocked: Boolean, highScore: Int, onClick: () -> Unit) {
    val containerColor = if (isUnlocked) Color.White.copy(alpha = 0.1f) else Color.White.copy(alpha = 0.05f)
    val contentColor = if (isUnlocked) Color.White else Color.White.copy(alpha = 0.3f)

    GlassCard(
        modifier = Modifier.fillMaxWidth().height(80.dp),
        onClick = if (isUnlocked) onClick else null
    ) {
        Row(
            modifier = Modifier.fillMaxSize().padding(horizontal = 20.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                 if (isUnlocked) {
                     Text(
                        text = "Level ${level.id}", 
                        style = MaterialTheme.typography.titleLarge,
                        color = NeonBlue,
                        fontWeight = FontWeight.Bold
                     )
                 } else {
                     Icon(Icons.Default.Lock, contentDescription = "Locked", tint = contentColor)
                     Spacer(modifier = Modifier.width(16.dp))
                     Text(
                        text = "Level ${level.id}", 
                        style = MaterialTheme.typography.titleLarge,
                        color = contentColor
                     )
                 }
            }
            
            if (isUnlocked && highScore > 0) {
                Column(horizontalAlignment = Alignment.End) {
                    Text("Best", style = MaterialTheme.typography.labelSmall, color = Color.White.copy(alpha=0.6f))
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text("$highScore", style = MaterialTheme.typography.titleMedium, color = AlertYellow)
                        Spacer(modifier = Modifier.width(4.dp))
                        Icon(Icons.Default.Star, contentDescription = null, tint = AlertYellow, modifier = Modifier.size(16.dp))
                    }
                }
            }
        }
    }
}
