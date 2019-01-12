[app]

#        *** Naming ***
title = Firebase
source.dir = .
package.name = sampleapp
package.domain = sampleapp

#        *** Important ***
version = 0.01
requirements = kivy,hostpython2,android,requests,openssl
android.permissions = INTERNET
p4a.source_dir = ~/p4a
p4a.bootstrap = sdl2

p4a.branch = master

# (int) Android API to use
android.api = 27
# (int) Minimum API required
android.minapi = 21
# (int) Android SDK version to use
android.sdk = 23
# (str) Android NDK version to use
android.ndk = 17c
# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
android.arch = armeabi-v7a

#        *** Constant App Settings ***

orientation = portrait
fullscreen = 1

[buildozer]

log_level = 2
warn_on_root = 1
