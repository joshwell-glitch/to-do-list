import json
import os

DEFAULT_SETTINGS = {"appearance": "system", 
                    "color_theme": "blue", 
                    "name_color": "Blue",
                    "number_color": 0}

DEFAULT_FONT = ("Arial", 12, "bold")
DEFAULT_TITLE_FONT = ("Arial", 24, "bold")

APP_TITLE = "To-Do List"
SETTINGS_PATH = "data/settings.json"
ICONPATH = "asset/icon.ico"

class SettingsManager:
    # LOAD SAVED SETTINGS:
    def load_settings(self):
        try:
            with open(SETTINGS_PATH, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return DEFAULT_SETTINGS
 
    # SAVE NEW CHANGES IN SETTINGS:
    def save_settings(self, data):
        try:
            os.mkdir('data')
        except FileExistsError:
            pass
        with open(SETTINGS_PATH, "w") as file:
            json.dump(data, file)