package `in`.wisegears.fivemb

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Modifier
import `in`.wisegears.fivemb.data.QuizRepository
import `in`.wisegears.fivemb.data.SettingsRepository
import `in`.wisegears.fivemb.ui.QuizNavigation
import `in`.wisegears.fivemb.ui.QuizViewModel
import `in`.wisegears.fivemb.ui.QuizViewModelFactory
import `in`.wisegears.fivemb.ui.theme.FiveMBTheme

import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        installSplashScreen()
        super.onCreate(savedInstanceState)
        
        val repository = QuizRepository(applicationContext)
        val settingsRepository = SettingsRepository(applicationContext)
        val soundManager = `in`.wisegears.fivemb.utils.SoundManager(applicationContext)
        val factory = QuizViewModelFactory(repository, settingsRepository, soundManager)
        val viewModel = androidx.lifecycle.ViewModelProvider(this, factory)[QuizViewModel::class.java]

        setContent {
            val settings = viewModel.settings.collectAsState().value
            // Observe Dark Mode setting (or simple system default if settings not set to strict override which we haven't implemented logic for 'system vs manual')
            // For now, let's treat the boolean as the manual override.
            
            FiveMBTheme(darkTheme = settings.isDarkMode) {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                   QuizNavigation(viewModel = viewModel)
                }
            }
        }
    }
}
