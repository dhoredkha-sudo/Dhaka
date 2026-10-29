[app]
# Title shown on the phone.
title = Python Starter
# Package name: lowercase, no spaces.
package.name = pythonstarter
# Reverse-domain style identifier for the APK.
package.domain = org.example.pythonstarter
# Where the code lives.
source.dir = .
source.include_exts = py
# App version.
version = 0.1
# Python libraries used by main.py. Add more here, comma separated,
# e.g. requests, pillow - but keep this list small for the first build.
requirements = python3,kivy
# Portrait, like the phone apps you have built before.
orientation = portrait
# Android target. Buildozer downloads the SDK/NDK on the GitHub
# runner on the first build, so you do not install them on your phone.
android.api = 33
android.minapi = 21
android.ndk = 25b
android.gradle_dependencies =
# Do not change this unless you know why: it is the entry file.
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
log_level = 2
warn_on_root = 1
