package com.avinash.fivemb.ui.theme

import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color

// Basic Materials
val Purple80 = Color(0xFFD0BCFF)
val PurpleGrey80 = Color(0xFFCCC2DC)
val Pink80 = Color(0xFFEFB8C8)

val Purple40 = Color(0xFF6650a4)
val PurpleGrey40 = Color(0xFF625b71)
val Pink40 = Color(0xFF7D5260)

val GreenSuccess = Color(0xFF00E676) // Brighter Green
val RedError = Color(0xFFFF1744) // Brighter Red
val AlertYellow = Color(0xFFFFC400)

val OffWhite = Color(0xFFF5F5F5)
val DarkText = Color(0xFF121212)
val LightText = Color(0xFFEEEEEE)

// Neural Neon Palette
val NeonBlue = Color(0xFF2979FF)
val NeonPurple = Color(0xFFD500F9)
val NeonCyan = Color(0xFF00E5FF)
val DeepBgStart = Color(0xFF121212)
val DeepBgEnd = Color(0xFF240046) // Deep Indigo

val MainBackgroundBrush = Brush.verticalGradient(
    colors = listOf(DeepBgStart, DeepBgEnd)
)

val CardGradient = Brush.linearGradient(
    colors = listOf(
        Color.White.copy(alpha = 0.1f),
        Color.White.copy(alpha = 0.05f)
    )
)
