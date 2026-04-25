# Globals.py

from Application.ConfigManager.ConfigManager import ConfigManager

class Globals:

    def __init__(self) -> None:
        # Config module
        self.ConfigManager = ConfigManager()
