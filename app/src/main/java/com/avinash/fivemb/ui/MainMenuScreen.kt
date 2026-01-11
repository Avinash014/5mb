package com.avinash.fivemb.ui

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material.icons.filled.Star
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.avinash.fivemb.R
import com.avinash.fivemb.data.Category
import com.avinash.fivemb.ui.theme.NeonBlue
import com.avinash.fivemb.ui.theme.NeonCyan
import com.avinash.fivemb.ui.theme.NeonPurple

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MainMenuScreen(
    categories: List<Category>,
    onCategorySelected: (String) -> Unit,
    onSettingsClick: () -> Unit
) {
    GameBackground {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.End
            ) {
                IconButton(onClick = onSettingsClick) {
                    Icon(Icons.Default.Settings, contentDescription = "Settings", tint = Color.White)
                }
            }
            
            Spacer(modifier = Modifier.height(32.dp))
            
            Image(
                painter = painterResource(id = R.drawable.logo_512),
                contentDescription = null,
                modifier = Modifier.size(100.dp)
            )
            
            Spacer(modifier = Modifier.height(16.dp))
            
            Text(
                text = stringResource(id = R.string.app_name) + " QUIZ",
                style = MaterialTheme.typography.displayMedium,
                fontWeight = FontWeight.ExtraBold,
                color = NeonCyan,
                letterSpacing = 4.sp
            )
            
            Text(
                text = stringResource(id = R.string.app_tagline),
                style = MaterialTheme.typography.bodyLarge,
                color = Color.White.copy(alpha = 0.7f)
            )
            
            Spacer(modifier = Modifier.height(48.dp))
            
            if (categories.isEmpty()) {
                CircularProgressIndicator(color = NeonBlue)
            } else {
                LazyColumn(
                    verticalArrangement = Arrangement.spacedBy(16.dp),
                    contentPadding = PaddingValues(bottom = 32.dp)
                ) {
                    items(categories) { category ->
                        GlassCard(
                            modifier = Modifier
                                .fillMaxWidth()
                                .height(100.dp),
                            onClick = { onCategorySelected(category.id) }
                        ) {
                            Row(
                                modifier = Modifier
                                    .fillMaxSize()
                                    .padding(24.dp),
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.SpaceBetween
                            ) {
                                Column {
                                    Text(
                                        text = category.name,
                                        style = MaterialTheme.typography.headlineSmall,
                                        fontWeight = FontWeight.Bold,
                                        color = Color.White
                                    )
                                    Text(
                                        text = "${category.levels.size} Levels",
                                        style = MaterialTheme.typography.bodyMedium,
                                        color = Color.White.copy(alpha = 0.6f)
                                    )
                                }
                                Icon(
                                    Icons.Default.Star, 
                                    contentDescription = null, 
                                    tint = NeonPurple,
                                    modifier = Modifier.size(32.dp)
                                )
                            }
                        }
                    }
                }
            }
        }
    }
}
