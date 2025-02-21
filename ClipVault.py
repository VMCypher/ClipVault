from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.core.clipboard import Clipboard
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import Config
import threading
import yt_dlp
import re
import os

# Define o ícone da janela com um PNG em vez de ICO
Window.set_icon("C:/meusProgramas/BaixadorYoutube/ClipVault/assets/icon.png")

KV = '''
ScreenManager:
    MainScreen:

<MainScreen>:
    name: "main"

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)

        MDTextField:
            id: url_input
            hint_text: "Cole a URL do vídeo aqui"
            mode: "rectangle"
            on_text_validate: app.baixar_video("mp4")
            size_hint_y: None
            height: dp(50)
            font_size: "18sp"
            hint_text_color: 0.7, 0.7, 0.7, 1
            foreground_color: 1, 1, 1, 1

        MDRaisedButton:
            id: resolution_button
            text: "Escolher Resolução"
            on_release: app.abrir_dropdown()
            md_bg_color: 0.1, 0.5, 0.8, 1
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1

        MDLabel:
            id: resolution_label
            text: "Resolução selecionada: 1080p"
            halign: "center"
            theme_text_color: "Secondary"

        BoxLayout:
            orientation: "horizontal"
            spacing: dp(10)
            size_hint_y: None
            height: dp(48)

            Image:
                source: "C:/meusProgramas/BaixadorYoutube/ClipVault/assets/play.png"
                size_hint: None, None
                size: dp(48), dp(48)

            MDRaisedButton:
                text: "Baixar MP4"
                on_release: app.baixar_video("mp4")
                md_bg_color: 0.1, 0.5, 0.8, 1
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

        MDLabel:
            id: status_label
            text: "Status: Aguardando..."
            halign: "center"
            theme_text_color: "Secondary"

        MDProgressBar:
            id: progress_bar
            value: 0
            max: 100
'''

class MainScreen(Screen):
    pass

class ClipVaultApp(MDApp):
    def build(self):
        self.title = "ClipVault"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.menu = None
        return Builder.load_string(KV)

    def abrir_dropdown(self):
        resolutions = ["4K", "1440p", "1080p", "720p", "480p"]
        menu_items = [
            {"viewclass": "MDRaisedButton", "text": res, "on_release": lambda x=res: self.set_resolution(x)}
            for res in resolutions
        ]
        self.menu = MDDropdownMenu(
            caller=self.root.get_screen("main").ids.resolution_button,
            items=menu_items,
            width_mult=3,
            background_color=(0.1, 0.1, 0.1, 1)
        )
        self.menu.open()

    def set_resolution(self, resolution):
        self.root.get_screen("main").ids.resolution_label.text = f"Resolução selecionada: {resolution}"
        self.menu.dismiss()

    def baixar_video(self, formato):
        url = self.root.get_screen("main").ids.url_input.text.strip()
        if not url:
            self.update_status("Insira uma URL válida!")
            return

        resolution = self.root.get_screen("main").ids.resolution_label.text.replace("Resolução selecionada: ", "").strip()
        self.update_status("Iniciando download...")
        threading.Thread(target=self.download_thread, args=(url, resolution), daemon=True).start()

    def download_thread(self, url, resolution):
        try:
            pasta_download = os.path.join(os.path.expanduser("~"), "Downloads")
            ydl_opts = {
                'outtmpl': os.path.join(pasta_download, '%(title)s.%(ext)s'),
                'progress_hooks': [self.log_progresso],
                'quiet': True,
                'noprogress': True,
                'no_warnings': True,
                'logger': self.LoggerFix(),
                'format': f'bestvideo[ext=mp4][height<={resolution}]+bestaudio[ext=m4a]/b[ext=mp4]'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.update_status(f"Download concluído! Arquivo salvo em {pasta_download}")

        except Exception as e:
            self.update_status(f"Erro: {str(e)}")

    def log_progresso(self, d):
        if d['status'] == 'downloading':
            self.update_status(f"Baixando: {d['_percent_str']} ({d['_eta_str']} restantes)")
        elif d['status'] == 'finished':
            self.update_status("Download finalizado, processando...")

    def update_status(self, text):
        Clock.schedule_once(lambda dt: setattr(self.root.get_screen("main").ids.status_label, "text", text), 0)

    class LoggerFix:
        def debug(self, msg): pass
        def warning(self, msg): pass
        def error(self, msg): pass

if __name__ == "__main__":
    ClipVaultApp().run()
