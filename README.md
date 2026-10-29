# Python Starter - GitHub to APK (phone-only route)

Yes - like NOVA EDU, you can upload to GitHub from your phone and
let GitHub's computer build the APK. The difference is only the
builder:

- NOVA EDU: GitHub Actions -> Expo / EAS -> APK (needed EXPO_TOKEN)
- This Python app: GitHub Actions -> Buildozer / Kivy -> APK
  (no token, no Expo account needed for a **debug** APK)

## Files in this starter

- `main.py` - a tiny Kivy app: a label, a counter, one button.
  Replace this file with your real app later.
- `buildozer.spec` - tells Buildozer the app name, package,
  requirements (`python3,kivy`) and Android API levels.
- `.github/workflows/build-apk.yml` - the GitHub Actions workflow.
  It runs on every push to `main`.

## Phone-only steps (GitHub web, no terminal)

1. Create a new public repo on GitHub from your phone browser.
2. Upload `main.py` and `buildozer.spec` to the repo root.
3. **Important - the same dotfolder trap as before:** uploading
   from mobile often skips folders starting with a dot, so
   `.github` may not upload. If it is missing after upload,
   create it manually on GitHub web:
   Add file -> Create new file -> type the full path
   `.github/workflows/build-apk.yml` -> paste the workflow
   file -> Commit directly to main.
4. Go to the repo's **Actions** tab. You should see a run
   called "Build Android APK". Tap it and wait.
5. When it turns green, scroll to **Artifacts** at the bottom
   and download `python-starter-apk`. Unzip it on your phone
   (the APK is inside) and install it - allow "Install unknown
   apps" for your browser/file manager when asked.

## Honest expectations - read before you start

- This workflow has **not** been run on GitHub yet in this chat,
  so the first build is untested. It is the standard Buildozer
  workflow, but a first build can still fail on a dependency
  version. If it fails, send me the exact error from the Actions
  log - do not guess.
- First build is slow: the runner downloads the Android SDK/NDK
  and compiles Python/Kivy for Android. Expect roughly 20-40
  minutes, sometimes longer. Later builds are faster because of
  caching on the runner - but this starter has no cache step yet,
  so budget for a long first run.
- The APK from this workflow is a **debug** APK, good for
  testing on your own phone. It is not a signed Play Store
  release. A release build needs your own keystore, which is a
  separate step - do not paste any keystore password in chat.
- Bengali text: Kivy's default font does not reliably render
  Bengali. This starter uses English on purpose. If your real
  app needs Bangla UI, that needs a Bengali font file bundled
  with the app - tell me and I will add that step, do not assume
  Bangla will just work in Kivy.
- Flet is easier for UI, but its GitHub APK build needs Flutter
  and is more complex than this Kivy/Buildozer route. That is
  why this starter uses Kivy.

## After this starter works

Replace `main.py` with your app, add any new libraries to
`requirements` in `buildozer.spec`, push again, and a new APK
is built automatically. One push = one new build.
