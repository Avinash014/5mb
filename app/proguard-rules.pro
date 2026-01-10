# Add project-specific strict rules here.
# By default, the flags in this file are appended to flags specified
# in 'proguard-android-optimize.txt' releases of Android SDK.

# Keeps the Questions model valid for Gson reflection
-keep class com.avinash.fivemb.data.** { *; }
