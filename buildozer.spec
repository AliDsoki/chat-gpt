[app]
# General
title = MyApp
package.name = myapp
package.domain = com.example

# Include extensions
source.include_exts = py,png,jpg,kv,atlas

# Requirements
requirements = python3,kivy

# Android specific settings
android.api = 33
android.ndk = 23b
android.archs = arm64-v8a

# Path for Android SDK (default path should work)
# android.sdk = /path/to/android-sdk
# android.ndk_path = /path/to/android-ndk

# Buildozer settings
# p4a.source_dir = /root/.cache/p4a  # Removed or commented this line to avoid issues
