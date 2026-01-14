package `in`.wisegears.fivemb.utils

import android.content.Context
import android.media.AudioAttributes
import android.media.SoundPool
import android.os.Build
import android.os.VibrationEffect
import android.os.Vibrator
import android.os.VibratorManager

class SoundManager(private val context: Context) {
    private val soundPool: SoundPool
    private var correctSoundId: Int = 0
    private var wrongSoundId: Int = 0
    private val vibrationHelper = VibrationHelper(context)

    init {
        val audioAttributes = AudioAttributes.Builder()
            .setUsage(AudioAttributes.USAGE_GAME)
            .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
            .build()
            
        soundPool = SoundPool.Builder()
            .setMaxStreams(2)
            .setAudioAttributes(audioAttributes)
            .build()
            
        // Load sounds from Resources
        correctSoundId = soundPool.load(context, `in`.wisegears.fivemb.R.raw.correct, 1)
        wrongSoundId = soundPool.load(context, `in`.wisegears.fivemb.R.raw.wrong, 1)
    }

    fun playCorrectSound() {
        if (correctSoundId != 0) {
            soundPool.play(correctSoundId, 1f, 1f, 1, 0, 1f)
        }
    }

    fun playWrongSound() {
        if (wrongSoundId != 0) {
            soundPool.play(wrongSoundId, 0.6f, 0.6f, 1, 0, 1f)
        }
    }
    
    fun vibrateCorrect() {
        vibrationHelper.vibrate(50)
    }
    
    fun vibrateWrong() {
        vibrationHelper.vibrate(200)
    }
}

class VibrationHelper(context: Context) {
    private val vibrator = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
        val vibratorManager = context.getSystemService(Context.VIBRATOR_MANAGER_SERVICE) as VibratorManager
        vibratorManager.defaultVibrator
    } else {
        @Suppress("DEPRECATION")
        context.getSystemService(Context.VIBRATOR_SERVICE) as Vibrator
    }

    fun vibrate(duration: Long) {
        if (vibrator.hasVibrator()) {
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                vibrator.vibrate(VibrationEffect.createOneShot(duration, VibrationEffect.DEFAULT_AMPLITUDE))
            } else {
                @Suppress("DEPRECATION")
                vibrator.vibrate(duration)
            }
        }
    }
}
