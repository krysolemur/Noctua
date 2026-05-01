# Globals.py

from noctua.config_manager.ConfigManager import ConfigManager
from noctua.theme_manager.ThemesManager import ThemesManager
from noctua.style_manager.StyleManager import StyleManager

class AppContext:

    def __init__(self) -> None:

        # Config module
        self.ConfigManager = ConfigManager()

        # Configuration
        self.config = self.ConfigManager.load_settings()
        
        # ThemeManager
        self.ThemesManager = ThemesManager()

        # StyleManager
        self.StyleManager = StyleManager()

ctx = AppContext()


