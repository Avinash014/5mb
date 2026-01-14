package `in`.wisegears.fivemb.ui

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import `in`.wisegears.fivemb.data.AppSettings

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SettingsScreen(
    settings: AppSettings,
    onTimerChange: (Int) -> Unit,
    onSoundToggle: (Boolean) -> Unit,
    onVibrationToggle: (Boolean) -> Unit,
    onLivesToggle: (Boolean) -> Unit,
    onShowExplanationToggle: (Boolean) -> Unit,
    onDarkModeToggle: (Boolean) -> Unit,
    onBack: () -> Unit
) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Settings") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, contentDescription = "Back")
                    }
                }
            )
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(16.dp)
                .verticalScroll(rememberScrollState()),
            verticalArrangement = Arrangement.spacedBy(24.dp)
        ) {
            // Timer
            SettingsSection(title = "Timer Duration") {
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    listOf(60, 120, 300).forEach { seconds ->
                        FilterChip(
                            selected = settings.timerDurationSeconds == seconds,
                            onClick = { onTimerChange(seconds) },
                            label = { Text("${seconds / 60} min") }
                        )
                    }
                }
            }

            // Toggles
            SwitchSetting("Show Explanations", settings.isShowExplanation, onShowExplanationToggle)
            SwitchSetting("Sound Effects", settings.isSoundEnabled, onSoundToggle)
            SwitchSetting("Vibration", settings.isVibrationEnabled, onVibrationToggle)
            SwitchSetting("Dark Mode", settings.isDarkMode, onDarkModeToggle)
            
            Spacer(modifier = Modifier.height(32.dp))
            
            // About
            Text(
                text = "Version 1.1 (Phase 2)",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
    }
}

@Composable
fun SettingsSection(title: String, content: @Composable () -> Unit) {
    Column {
        Text(title, style = MaterialTheme.typography.titleMedium, modifier = Modifier.padding(bottom = 8.dp))
        content()
    }
}

@Composable
fun SwitchSetting(title: String, checked: Boolean, onCheckedChange: (Boolean) -> Unit) {
    Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.SpaceBetween,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Text(title, style = MaterialTheme.typography.bodyLarge)
        Switch(checked = checked, onCheckedChange = onCheckedChange)
    }
}
