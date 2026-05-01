from noctua.config_manager import ConfigManager
# from noctua.logger import Logger
# from noctua.theme_manager import ThemesManager
# from noctua.style_manager import StyleManager

class Context:

    def __init__(self) -> None:

        # Config module
        self.ConfigManager = ConfigManager()

        # Configuration
        self.config = self.ConfigManager.load_settings()

        # Logger module
        # self.logger = Logger(self.config.get("LoggingPage"))
        
        # ThemeManager
        # self.ThemesManager = ThemesManager()

        # StyleManager
        # self.StyleManager = StyleManager()

ctx = Context()


