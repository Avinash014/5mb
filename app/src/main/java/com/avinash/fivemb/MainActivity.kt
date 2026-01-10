package com.avinash.fivemb

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier
import com.avinash.fivemb.data.QuizRepository
import com.avinash.fivemb.ui.QuizNavigation
import com.avinash.fivemb.ui.QuizViewModel
import com.avinash.fivemb.ui.QuizViewModelFactory
import com.avinash.fivemb.ui.theme.FiveMBTheme

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        val repository = QuizRepository(applicationContext)
        val factory = QuizViewModelFactory(repository)
        val viewModel = androidx.lifecycle.ViewModelProvider(this, factory)[QuizViewModel::class.java]

        setContent {
            FiveMBTheme {
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
