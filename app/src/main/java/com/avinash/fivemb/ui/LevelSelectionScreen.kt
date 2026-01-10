package com.avinash.fivemb.ui

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material.icons.filled.Lock
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.avinash.fivemb.data.Category
import com.avinash.fivemb.data.Level

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LevelSelectionScreen(
    category: Category,
    isLevelUnlocked: (Int) -> Boolean,
    onLevelSelected: (Int) -> Unit,
    onBack: () -> Unit
) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("${category.name} Levels") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back")
                    }
                }
            )
        }
    ) { paddingValues ->
        LazyVerticalGrid(
            columns = GridCells.Fixed(3),
            contentPadding = PaddingValues(16.dp),
            horizontalArrangement = Arrangement.spacedBy(8.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp),
            modifier = Modifier.padding(paddingValues)
        ) {
            items(category.levels) { level ->
                val unlocked = isLevelUnlocked(level.id)
                LevelItem(level = level, isUnlocked = unlocked, onClick = {
                    if (unlocked) onLevelSelected(level.id)
                })
            }
        }
    }
}

@Composable
fun LevelItem(level: Level, isUnlocked: Boolean, onClick: () -> Unit) {
    Card(
        modifier = Modifier
            .aspectRatio(1f)
            .clickable(enabled = isUnlocked, onClick = onClick),
        colors = CardDefaults.cardColors(
            containerColor = if (isUnlocked) MaterialTheme.colorScheme.primaryContainer else MaterialTheme.colorScheme.surfaceVariant
        )
    ) {
        Box(
             modifier = Modifier.fillMaxSize(),
             contentAlignment = Alignment.Center
        ) {
             if (isUnlocked) {
                 Text(text = "${level.id}", style = MaterialTheme.typography.headlineMedium)
             } else {
                 Icon(Icons.Default.Lock, contentDescription = "Locked")
             }
        }
    }
}
