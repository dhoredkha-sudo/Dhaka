"""Minimal Kivy starter app - proves the GitHub -> APK route works.
Run on a PC/phone Python with Kivy installed:  python main.py
For Android, do NOT build on the phone - see README.md and
.github/workflows/build-apk.yml (GitHub Actions builds the APK).
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 20
        self.count = 0

        self.title = Label(
            text="Hello from Python!",
            font_size=32,
            size_hint_y=0.4,
        )
        self.counter = Label(
            text="Count: 0",
            font_size=28,
            size_hint_y=0.3,
        )
        self.button = Button(
            text="Tap me",
            font_size=26,
            size_hint_y=0.3,
        )
        self.button.bind(on_press=self.on_tap)
        self.add_widget(self.title)
        self.add_widget(self.counter)
        self.add_widget(self.button)

    def on_tap(self, _instance):
        self.count += 1
        self.counter.text = f"Count: {self.count}"


class StarterApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    StarterApp().run()
