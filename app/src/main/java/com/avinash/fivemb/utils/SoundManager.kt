package com.avinash.fivemb.utils

import android.content.Context
import android.media.AudioAttributes
import android.media.SoundPool
import android.os.Build
import android.os.VibrationEffect
import android.os.Vibrator
import android.os.VibratorManager
import java.io.File
import java.io.FileOutputStream
import java.nio.ByteBuffer
import java.nio.ByteOrder
import kotlin.math.PI
import kotlin.math.exp
import kotlin.math.sin

class SoundManager(private val context: Context) {
    private val soundPool: SoundPool
    private val correctSoundId: Int
    private val wrongSoundId: Int
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
            
        // Generate and load sounds
        val correctFile = File(context.cacheDir, "correct.wav")
        if (!correctFile.exists()) {
             createWavFile(correctFile, Frequency.HIGH_SUCCESS)
        }
        
        val wrongFile = File(context.cacheDir, "wrong.wav")
        if (!wrongFile.exists()) {
             createWavFile(wrongFile, Frequency.LOW_ERROR)
        }
        
        correctSoundId = soundPool.load(correctFile.absolutePath, 1)
        wrongSoundId = soundPool.load(wrongFile.absolutePath, 1)
    }

    fun playCorrectSound() {
        soundPool.play(correctSoundId, 1f, 1f, 1, 0, 1f)
    }

    fun playWrongSound() {
        soundPool.play(wrongSoundId, 0.6f, 0.6f, 1, 0, 1f)
    }
    
    fun vibrateCorrect() {
        vibrationHelper.vibrate(50)
    }
    
    fun vibrateWrong() {
        vibrationHelper.vibrate(200)
    }
    
    // --- Audio Generation Logic ---
    
    private enum class Frequency(val freq: Double, val duration: Double) {
        HIGH_SUCCESS(880.0, 0.6), // A5, Bell-like
        LOW_ERROR(220.0, 0.4)     // A3, Dull
    }

    private fun createWavFile(file: File, type: Frequency) {
        val sampleRate = 44100
        val numSamples = (type.duration * sampleRate).toInt()
        val generatedSnd = ByteArray(2 * numSamples)
        
        val buffer = ByteBuffer.allocate(2 * numSamples)
        buffer.order(ByteOrder.LITTLE_ENDIAN)
        
        for (i in 0 until numSamples) {
            val t = i.toDouble() / sampleRate
            
            // Generate standard sine wave
            var sample = 0.0
            
            if (type == Frequency.HIGH_SUCCESS) {
                // Bell-like: Fundamental + Harmonic, Exponential Decay
                val envelope = exp(-3.0 * t) // Decay 
                sample = (sin(2 * PI * type.freq * t) + 0.5 * sin(2 * PI * type.freq * 2 * t)) * envelope
            } else {
                // Error: Sawtooth-ish or just low sine with fast decay
                val envelope = exp(-10.0 * t) 
                sample = sin(2 * PI * type.freq * t) * envelope
            }

            // Scale to 16-bit PCM range
            val maxAmp = 32767
            val valInt = (sample * maxAmp).toInt().coerceIn(-maxAmp, maxAmp).toShort()
            buffer.putShort(valInt)
        }
        
        writeWavHeader(file, buffer.array(), sampleRate)
    }
    
    private fun writeWavHeader(file: File, data: ByteArray, sampleRate: Int) {
        val header = ByteArray(44)
        val totalDataLen = data.size + 36
        val byteRate = sampleRate * 2
        
        // RIFF header
        header[0] = 'R'.code.toByte(); header[1] = 'I'.code.toByte(); header[2] = 'F'.code.toByte(); header[3] = 'F'.code.toByte()
        // File size
        header[4] = (totalDataLen and 0xff).toByte()
        header[5] = ((totalDataLen shr 8) and 0xff).toByte()
        header[6] = ((totalDataLen shr 16) and 0xff).toByte()
        header[7] = ((totalDataLen shr 24) and 0xff).toByte()
        // WAVE
        header[8] = 'W'.code.toByte(); header[9] = 'A'.code.toByte(); header[10] = 'V'.code.toByte(); header[11] = 'E'.code.toByte()
        // fmt chunk
        header[12] = 'f'.code.toByte(); header[13] = 'm'.code.toByte(); header[14] = 't'.code.toByte(); header[15] = ' '.code.toByte()
        // fmt chunk size (16 for PCM)
        header[16] = 16; header[17] = 0; header[18] = 0; header[19] = 0
        // Audio format (1 for PCM)
        header[20] = 1; header[21] = 0
        // Num channels (1 for Mono)
        header[22] = 1; header[23] = 0
        // Sample rate
        header[24] = (sampleRate and 0xff).toByte()
        header[25] = ((sampleRate shr 8) and 0xff).toByte()
        header[26] = ((sampleRate shr 16) and 0xff).toByte()
        header[27] = ((sampleRate shr 24) and 0xff).toByte()
        // Byte rate
        header[28] = (byteRate and 0xff).toByte()
        header[29] = ((byteRate shr 8) and 0xff).toByte()
        header[30] = ((byteRate shr 16) and 0xff).toByte()
        header[31] = ((byteRate shr 24) and 0xff).toByte()
        // Block align (2 bytes)
        header[32] = 2; header[33] = 0
        // Bits per sample
        header[34] = 16; header[35] = 0
        // data chunk
        header[36] = 'd'.code.toByte(); header[37] = 'a'.code.toByte(); header[38] = 't'.code.toByte(); header[39] = 'a'.code.toByte()
        // data size
        header[40] = (data.size and 0xff).toByte()
        header[41] = ((data.size shr 8) and 0xff).toByte()
        header[42] = ((data.size shr 16) and 0xff).toByte()
        header[43] = ((data.size shr 24) and 0xff).toByte()

        val fos = FileOutputStream(file)
        fos.write(header)
        fos.write(data)
        fos.close()
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
