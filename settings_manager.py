import json
import os

DEFAULT_SETTINGS = {"appearance": "System", 
                    "color_theme": "blue", 
                    "name_color": "Blue",
                    "number_color": 0}

SETTINGS_PATH = "data/settings.json"
DEFAULT_FONT = ("Arial", 12, "bold")
DEFAULT_TITLE_FONT = ("Arial", 24, "bold")

APP_TITLE = "To-Do List"
ICONPATH = "asset/icon.ico"

class SettingsManager:
    # load settings changes.
    def load_settings(self):
        try:
            with open(SETTINGS_PATH, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return DEFAULT_SETTINGS
 
    # save settings changes.
    def save_settings(self, data):
        try:
            os.mkdir('data')
        except FileExistsError:
            pass
        with open(SETTINGS_PATH, "w") as file:
            json.dump(data, file)