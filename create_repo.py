import os
import json
from pyvirtualdisplay import Display
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton, QGridLayout
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon, QFont, QBrush
from PyQt5.QtCore import Qt, QByteArray
from PyQt5.QtTest import QTest
from datetime import datetime

# Set QT_QPA_PLATFORM to 'offscreen'
os.environ["QT_QPA_PLATFORM"] = "offscreen"

class ThemeLoader:
    def __init__(self):
        self.theme = {}

    def load_theme_from_file(self, file_path, app):
        if not os.path.exists(file_path):
            print(f"Theme file '{file_path}' not found. Loading default 'Dark.json' instead.")
            file_path = "themes/Dark.json"
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Default theme file '{file_path}' not found.")

        with open(file_path, "r") as file:
            self.theme = json.load(file)

        if "palette" not in self.theme:
            raise ValueError("JSON theme must contain a 'palette' section.")

        palette_config = self.theme["palette"]
        palette = QPalette()
        role_map = {
            "Window": QPalette.Window,
            "WindowText": QPalette.WindowText,
            "Base": QPalette.Base,
            "AlternateBase": QPalette.AlternateBase,
            "ToolTipBase": QPalette.ToolTipBase,
            "ToolTipText": QPalette.ToolTipText,
            "Text": QPalette.Text,
            "Button": QPalette.Button,
            "ButtonText": QPalette.ButtonText,
            "BrightText": QPalette.BrightText,
            "Link": QPalette.Link,
            "Highlight": QPalette.Highlight,
            "HighlightedText": QPalette.HighlightedText,
        }

        for role_name, color_code in palette_config.items():
            if role_name in role_map:
                palette.setColor(role_map[role_name], QColor(color_code))
            else:
                print(f"Warning: '{role_name}' is not a recognized palette role.")
        
        app.setPalette(palette)

        if "stylesheet" in self.theme:
            stylesheet = self.theme["stylesheet"]
            app.setStyleSheet(stylesheet)
        else:
            print("No 'stylesheet' section found in the theme file.")

        return self.theme

class PicoDulceLauncher(QWidget):
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('PicoDulce Launcher')
        current_date = datetime.now()
        if (current_date.month == 12 and current_date.day >= 8) or (current_date.month == 1 and current_date.day <= 1):
            self.setWindowIcon(QIcon('holiday.ico'))
        else:
            self.setWindowIcon(QIcon('launcher_icon.ico'))

        self.setGeometry(100, 100, 400, 250)
        QApplication.setStyle("Fusion")

        if self.theme.get("background_image_base64", False):
            theme_background_base64 = self.theme.get("background_image_base64", "")
            if theme_background_base64:
                try:
                    background_image_data = QByteArray.fromBase64(theme_background_base64.encode())
                    pixmap = QPixmap()
                    if pixmap.loadFromData(background_image_data):
                        self.setAutoFillBackground(True)
                        palette = self.palette()
                        palette.setBrush(QPalette.Window, QBrush(pixmap.scaled(
                            self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
                        )))
                        self.setPalette(palette)
                    else:
                        print("Error: Failed to load background image from base64 string.")
                except Exception as e:
                    print(f"Error: Failed to decode and set background image. {e}")
            else:
                print("No background image base64 string found in the theme file.")

        title_label = QLabel('PicoDulce Launcher')
        title_label.setFont(QFont("Arial", 24, QFont.Bold))

        installed_versions_label = QLabel('Installed Versions:')
        installed_versions_label.setFont(QFont("Arial", 14))
        self.installed_version_combo = QComboBox()
        self.installed_version_combo.setMinimumWidth(200)
        self.installed_version_combo.addItem("Version 1.0")

        buttons_layout = QVBoxLayout()

        self.play_button = QPushButton('Play')
        self.play_button.setFocusPolicy(Qt.NoFocus)
        self.play_button.clicked.connect(self.play_instance)
        highlight_color = self.palette().color(QPalette.Highlight)
        self.play_button.setStyleSheet(f"background-color: {highlight_color.name()}; color: white;")
        buttons_layout.addWidget(self.play_button)

        self.open_menu_button = QPushButton('Version Manager')
        self.open_menu_button.clicked.connect(self.open_mod_loader_and_version_menu)
        buttons_layout.addWidget(self.open_menu_button)

        self.manage_accounts_button = QPushButton('Manage Accounts')
        self.manage_accounts_button.clicked.connect(self.manage_accounts)
        buttons_layout.addWidget(self.manage_accounts_button)

        self.open_marroc_button = QPushButton('Marroc Mod Manager')
        self.open_marroc_button.clicked.connect(self.open_marroc_script)
        buttons_layout.addWidget(self.open_marroc_button)

        grid_layout = QGridLayout()
        self.settings_button = QPushButton('Settings')
        self.settings_button.clicked.connect(self.open_settings_dialog)
        self.about_button = QPushButton('About')
        self.about_button.clicked.connect(self.show_about_dialog)
        
        grid_layout.addWidget(self.settings_button, 0, 0)
        grid_layout.addWidget(self.about_button, 0, 1)

        buttons_layout.addLayout(grid_layout)
        buttons_layout.setAlignment(Qt.AlignTop)
        buttons_layout.setSpacing(10)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(installed_versions_label)
        main_layout.addWidget(self.installed_version_combo)
        main_layout.addLayout(buttons_layout)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(20)

        self.setLayout(main_layout)

    def play_instance(self):
        print("Play button clicked")

    def open_mod_loader_and_version_menu(self):
        print("Version Manager button clicked")

    def manage_accounts(self):
        print("Manage Accounts button clicked")

    def open_marroc_script(self):
        print("Marroc Mod Manager button clicked")

    def open_settings_dialog(self):
        print("Settings button clicked")

    def show_about_dialog(self):
        print("About button clicked")

def generate_screenshots():
    display = Display(visible=0, size=(800, 600))
    display.start()

    app = QApplication([])

    theme_loader = ThemeLoader()
    themes_folder = "themes"
    previews_folder = "previews"

    if not os.path.exists(themes_folder):
        print(f"Themes folder '{themes_folder}' not found.")
        return

    if not os.path.exists(previews_folder):
        os.makedirs(previews_folder)
        print(f"Created previews folder '{previews_folder}'.")

    for theme_file in os.listdir(themes_folder):
        if theme_file.endswith(".json"):
            theme_path = os.path.join(themes_folder, theme_file)
            theme = theme_loader.load_theme_from_file(theme_path, app)

            launcher = PicoDulceLauncher(theme)
            launcher.show()
            QTest.qWait(100)

            screenshot_path = os.path.join(previews_folder, f"{os.path.splitext(theme_file)[0]}.png")
            screenshot = launcher.grab()
            screenshot.save(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

            launcher.close()

    app.quit()
    display.stop()

def extract_theme_info(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if 'manifest' in data:
            manifest = data['manifest']
            theme_name = os.path.splitext(os.path.basename(filename))[0]
            return {
                "name": manifest.get("name", ""),
                "description": manifest.get("description", ""),
                "author": manifest.get("author", ""),
                "license": manifest.get("license", ""),
                "link": f"https://raw.githubusercontent.com/nixietab/picodulce-themes/refs/heads/main/{filename}".replace("\\",'/'),
                "preview": f"https://raw.githubusercontent.com/nixietab/picodulce-themes/refs/heads/main/previews/{theme_name}.png"
            }
    return None

themes = []

themes_dir = 'themes'
for filename in os.listdir(themes_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(themes_dir, filename)
        theme_info = extract_theme_info(filepath)
        if theme_info:
            themes.append(theme_info)

themes.sort(key=lambda theme: theme['name'])

repo_data = {
    "themes": themes
}

with open('repo.json', 'w', encoding='utf-8') as outfile:
    json.dump(repo_data, outfile, indent=2)

print("repo.json has been generated and sorted alphabetically.")

generate_screenshots()
