from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import json
from database import save_last_read
from khatma import update_khatma
from achievements import check_achievements
from plyer import notification
from datetime import datetime

class NoorApp(App):

    def build(self):
        self.load_theme()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.ayah_label = Label(
            text="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
            font_size=24
        )

        btn_read = Button(text="حفظ آخر قراءة")
        btn_read.bind(on_press=self.save_read)

        btn_notify = Button(text="إشعار أذكار")
        btn_notify.bind(on_press=self.send_notification)

        btn_khatma = Button(text="زيادة صفحة")
        btn_khatma.bind(on_press=self.add_page)

        layout.add_widget(self.ayah_label)
        layout.add_widget(btn_read)
        layout.add_widget(btn_notify)
        layout.add_widget(btn_khatma)

        return layout

    def load_theme(self):
        try:
            with open("theme.json") as f:
                theme = json.load(f)
                if theme["dark"]:
                    Window.clearcolor = (0.1, 0.1, 0.1, 1)
                else:
                    Window.clearcolor = (1, 1, 1, 1)
        except:
            Window.clearcolor = (1, 1, 1, 1)

    def save_read(self, instance):
        save_last_read("الفاتحة", 1)

    def send_notification(self, instance):
        notification.notify(
            title="أذكار",
            message="لا تنس ذكر الله",
            timeout=10
        )

    def add_page(self, instance):
        update_khatma(1)
        check_achievements()

if __name__ == "__main__":
    NoorApp().run()