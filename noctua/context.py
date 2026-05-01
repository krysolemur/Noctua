# Globals.py

from noctua.config_manager.config_manager import ConfigManager
from noctua.theme_manager.themes_manager import ThemesManager
from noctua.style_manager.style_manager import StyleManager
from noctua.logger.logger import Logger

class Context:

    def __init__(self) -> None:

        # Config module
        self.ConfigManager = ConfigManager()

        # Logger module
        self.logger = Logger()

        # Configuration
        self.config = self.ConfigManager.load_settings()
        
        # ThemeManager
        # self.ThemesManager = ThemesManager()

        # StyleManager
        self.StyleManager = StyleManager()

ctx = Context()


