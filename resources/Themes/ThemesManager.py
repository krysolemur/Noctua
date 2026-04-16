# theme.py

# Importing system files
import shutil
import json
import os

from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox # type: ignore
from PySide6.QtGui import QPalette, QColor # type: ignore
from PySide6.QtCore import Qt # type: ignore

# Import program files
from resources.Themes.ThemeCreator import ThemeCreator

# Main class ThemeManager
class ThemesManager:

    # Themes dir
    themeDir = "resources/Themes"

    # Initiator
    def __init__(self) -> None:

        # Init parents
        super().__init__()

        # Themes mapping
        self.defaultThemes = {
            "Dark": lambda: self.loadPalette("Dark"),
            "Light": lambda: self.loadPalette("Light")
        }



        self.themes = self._getThemes

        self.themes()

    def _getThemes(self) -> list:

        themes = []

        for theme in os.listdir(self.themeDir):

            if not os.path.isdir(f"{self.themeDir}/{theme}"):

                if theme.endswith(".json"):

                    # Add the verified filename string to our collection
                    themes.append(str(theme))

        return themes

    # Move file to theme dir
    @classmethod
    def addTheme(cls, path) -> bool:
        try:
            # Move that file to themes dir
            shutil.move(path, cls.themeDir)

            return True
        except Exception as e:
            print(e)
            return False

    # Theme creator
    def createTheme(self) -> None:
        # Init main theme creator class
        themeCreator = ThemeCreator()

        # Execute the class
        themeCreator.exec()
        
    # Transforms a JSON structure into a functional Qt color palette
    def parsePalette(self, palette):

        # Guard clause to ensure the file exists and has a JSON extension
        if not os.path.exists(f"{self.theme_dir}/{palette}") or not palette.endswith(".json"):

            # Log a critical error message via the Logging parent class
            self.printe(msg=f"Wrong palette {palette}", exception=None, function=self.parseJSONPalette.__name__)

            # Exit the method with a failure status
            return False
        
        # Open the filesystem resource in read-only mode
        with open(f"{self.theme_dir}/{palette}", "r") as theme:

            # Convert the raw JSON text into a Python dictionary
            data = json.load(theme)
            
        # Initialize a fresh QPalette instance to be populated
        palette = QPalette()


        # Safe block to catch missing keys in the JSON theme definition
        try:

            # Mapping text and label colors from the dictionary to the palette
            palette.setColor(QPalette.WindowText, data["QPalette.WindowText"])

            # Map the standard foreground color for text widgets
            palette.setColor(QPalette.Text, data["QPalette.Text"])

            # Map the color for text displayed on buttons
            palette.setColor(QPalette.ButtonText, data["QPalette.ButtonText"])

            # Map the color for highly contrasting or highlighted text
            palette.setColor(QPalette.BrightText, data["QPalette.BrightText"])

            # Map the color for non-interactive hint text in inputs
            palette.setColor(QPalette.PlaceholderText, data["QPalette.PlaceholderText"])


            # Mapping background and surface colors
            palette.setColor(QPalette.Window, data["QPalette.Window"])

            # Map the primary background for data entry fields
            palette.setColor(QPalette.Base, data["QPalette.Base"])

            # Map the secondary background for alternating row colors
            palette.setColor(QPalette.AlternateBase, data["QPalette.AlternateBase"])

            # Map the main background color for button elements
            palette.setColor(QPalette.Button, data["QPalette.Button"])

            # Map the background of hovering help tooltips
            palette.setColor(QPalette.ToolTipBase, data["QPalette.ToolTipBase"])

            # Map the text color inside help tooltips
            palette.setColor(QPalette.ToolTipText, data["QPalette.ToolTipText"])


            # Mapping decorative 3D effects and shadowing
            palette.setColor(QPalette.Shadow, data["QPalette.Shadow"])

            # Map the lightest color for 3D highlights
            palette.setColor(QPalette.Light, data["QPalette.Light"])

            # Map the mid-light shading level
            palette.setColor(QPalette.Midlight, data["QPalette.Midlight"])

            # Map the neutral middle shading level
            palette.setColor(QPalette.Mid, data["QPalette.Mid"])

            # Map the darkest shading level for deep shadows
            palette.setColor(QPalette.Dark, data["QPalette.Dark"])


            # Mapping interaction and link colors
            palette.setColor(QPalette.Highlight, data["QPalette.Highlight"])

            # Map the color of text inside selected areas
            palette.setColor(QPalette.HighlightedText, data["QPalette.HighlightedText"])

            # Map the default color for interactive hyperlinks
            palette.setColor(QPalette.Link, data["QPalette.Link"])

            # Map the color for links that have been visited
            palette.setColor(QPalette.LinkVisited, data["QPalette.LinkVisited"])


            # Mapping specific colors for inactive/disabled UI states
            palette.setColor(QPalette.Disabled, QPalette.WindowText, data["Disabled.WindowText"])

            # Map disabled general text
            palette.setColor(QPalette.Disabled, QPalette.Text, data["Disabled.Text"])

            # Map disabled button text
            palette.setColor(QPalette.Disabled, QPalette.ButtonText, data["Disabled.ButtonText"])

            # Map disabled field background
            palette.setColor(QPalette.Disabled, QPalette.Base, data["Disabled.Base"])


            # Successfully return the fully configured QPalette object
            return palette

        # Exception handler for malformed JSON theme files
        except KeyError as e:

            # Log the specific missing attribute that caused the failure
            self.printe(msg=f"Error while loading palette {palette}", exception=e, function=self.parseJSONPalette.__name__)

            # Return failure status to prevent application styling errors
            return False

    # Generates a standard hardcoded Dark or Light palette
    def loadPalette(self, palette):
        # Configuration for the high-contrast Dark theme
        if palette == "Dark":

            # Create a new palette instance for dark mode
            dark_palette = QPalette()

            # Load palette
            background_color = QColor(45, 45, 45)
            alternate_background = QColor(35, 35, 35)
            text_color = QColor(225, 225, 225)
            disabled_color = QColor(127, 127, 127)
            highlight_color = QColor(42, 130, 218) 
            dark_palette.setColor(QPalette.Window, background_color)
            dark_palette.setColor(QPalette.WindowText, text_color)
            dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.AlternateBase, alternate_background)
            dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, text_color)
            dark_palette.setColor(QPalette.Button, background_color)
            dark_palette.setColor(QPalette.ButtonText, text_color)
            dark_palette.setColor(QPalette.BrightText, Qt.red)
            dark_palette.setColor(QPalette.Link, highlight_color)
            dark_palette.setColor(QPalette.Highlight, highlight_color)
            dark_palette.setColor(QPalette.HighlightedText, Qt.black)
            dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, disabled_color)
            dark_palette.setColor(QPalette.Disabled, QPalette.Text, disabled_color)
            dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, disabled_color)
            dark_palette.setColor(QPalette.Disabled, QPalette.Base, background_color)

            # Return the fully defined dark mode palette
            return dark_palette

        # Configuration for the standard Light theme
        elif palette == "Light":

            # Create a new palette instance for light mode
            light_palette = QPalette()


            # Set the light gray standard background
            background_color = QColor(240, 240, 240)

            # Set a slightly darker gray for visual separation in UI
            alternate_background = QColor(225, 225, 225)

            # Set pure white for input areas
            base_color = QColor(255, 255, 255)

            # Set solid black for primary text
            text_color = QColor(0, 0, 0)

            # Set a soft gray for disabled text
            disabled_color = QColor(160, 160, 160)

            # Set the classic Windows blue for highlights
            highlight_color = QColor(0, 120, 215) 


            # Apply color constants to the light palette roles
            light_palette.setColor(QPalette.Window, background_color)

            # Assign main text color
            light_palette.setColor(QPalette.WindowText, text_color)

            # Assign white background for input fields
            light_palette.setColor(QPalette.Base, base_color)

            # Assign alternate background color
            light_palette.setColor(QPalette.AlternateBase, alternate_background)

            # Define tooltip appearance
            light_palette.setColor(QPalette.ToolTipBase, Qt.white)

            # Define tooltip text appearance
            light_palette.setColor(QPalette.ToolTipText, text_color)

            # Define general text color
            light_palette.setColor(QPalette.Text, text_color)

            # Define button color
            light_palette.setColor(QPalette.Button, background_color)

            # Define text on buttons
            light_palette.setColor(QPalette.ButtonText, text_color)

            # Define attention text color
            light_palette.setColor(QPalette.BrightText, Qt.red)

            # Define link appearance
            light_palette.setColor(QPalette.Link, highlight_color)

            # Define selection appearance
            light_palette.setColor(QPalette.Highlight, highlight_color)

            # Define selected text color
            light_palette.setColor(QPalette.HighlightedText, Qt.white)


            # Define visual rules for disabled widgets in light mode
            light_palette.setColor(QPalette.Disabled, QPalette.WindowText, disabled_color)

            # Set disabled foreground text
            light_palette.setColor(QPalette.Disabled, QPalette.Text, disabled_color)

            # Set disabled button text
            light_palette.setColor(QPalette.Disabled, QPalette.ButtonText, disabled_color)

            # Set disabled base background
            light_palette.setColor(QPalette.Disabled, QPalette.Base, background_color)


            # Return the complete light mode palette
            return light_palette

        # Return nothing if an unknown palette name is passed
        else: None

    # Export to python method
    def _exportToPython(self) -> None:
        """Exportuje paletu jako spustitelný Python skript (.py)."""
        import os

        # 1. Dialog pro výběr místa uložení
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export as Python Script",
            "theme_config.py",
            "Python Files (*.py)"
        )

        if not file_path:
            return

        try:
            # 2. Záhlaví souboru a importy
            py_code = [
                "from PySide6.QtGui import QPalette, QColor",
                "from PySide6.QtCore import Qt",
                "",
                "def get_custom_palette():",
                "    palette = QPalette()",
                ""
            ]

            # Mapování grup pro kód
            group_map = {
                "Active": "QPalette.ColorGroup.Active",
                "Inactive": "QPalette.ColorGroup.Inactive",
                "Disabled": "QPalette.ColorGroup.Disabled"
            }

            # 3. Generování příkazů pro každou barvu
            for state, roles in self.customPalette.items():
                group_str = group_map[state]
                if roles:
                    py_code.append(f"    # --- {state} State ---")
                    for role_name, color in roles.items():
                        role_enum = f"QPalette.ColorRole.{role_name}"
                        hex_val = color.name().upper()
                        # Vygenerujeme řádek: palette.setColor(skupina, role, QColor("#HEX"))
                        line = f"    palette.setColor({group_str}, {role_enum}, QColor('{hex_val}'))"
                        py_code.append(line)
                    py_code.append("")

            py_code.append("    return palette")

            # 4. Zápis do souboru
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("\n".join(py_code))

            QMessageBox.information(self, "Success", f"Python theme script generated:\n{file_path}")

        except Exception as e:
            QMessageBox.critical(self, "Export Error", f"Failed to generate Python file: {e}")
