# theme.py

# Import system modules
import os

from PySide6.QtWidgets import QDialog, QFileDialog # type: ignore

# Import profram files
from libs.Logging.logging import Logging

from libs.QtGuiFiles.PyFiles.ThemeDialog import Ui_ThemeDialog

# Class Theme
class Theme(Logging):
    def __init__(self) -> None:
        '''
        Init parents and set imoprtant variables.
        '''

        # Init parents
        super().__init__()

        # Theme directory
        self.theme_dir = "resources/Themes"

        # Defautl themes
        self.default_themes = {
            "Default": None,
            "Dark": None,
            "Light": None
        }

        # All themes
        self.themes = self._getThemes

        # Get themes
        self.themes()

    '''
    Private functions.
    '''

    # Browse button function
    def _browseThemes(self) -> None:
        # Get filename from QFileDialog
        filename, _ = QFileDialog.getOpenFileName(
            self,
            # Title
            "Choose file",
            # Default folder
            "",  
            # Accept types
            "Python files (*.py);;"
        )

        # Set to QLineEdit
        self.ui.addLineEdit.setText(filename)

    # Get all themes
    def _getThemes(self) -> list:
        # Create new list
        themes = []

        # List through themes direcotyr
        for theme in os.listdir(self.theme_dir):
            # Check if its not directory
            if not os.path.isdir(f"{self.theme_dir}/{theme}") and theme != "theme.py":
                # Check python type
                if theme.endswith(".py"):
                    # Append it to the theme list
                    themes.append(str(theme))

        # Return themes
        return themes

    # Add theme
    def _addTheme(self, path) -> None:
        # Set statusLabel stylesheet
        self.ui.statusLabel.setStyleSheet("color: #ff0000")

        # Check path
        if not path:
            # Set error text
            self.ui.statusLabel.setText("Enter path!")

            return

        # Check if path exists
        if not os.path.exists(path):
            # Set error text
            self.ui.statusLabel.setText("Path does not exists!")

            return 

        # Accept
        self.close()

    '''
    Public functions.
    '''

    # Add theme dialog
    def themeDialog(self) -> None:
        '''
        Create dialog, load ui and setup it.
        '''

        ThemeDialog = QDialog()

        # Load ui
        ThemeDialogUi = Ui_ThemeDialog()

        # Setup ui
        ThemeDialogUi.setupUi(ThemeDialog = QDialog())

        '''
        Setup window like title, size and more.
        '''

        # Title
        ThemeDialog.setWindowTitle("Add theme")

        # Minimum size
        ThemeDialog.setMinimumSize(ThemeDialog.sizeHint())

        # Resize
        ThemeDialog.resize(ThemeDialog.sizeHint())

        '''
        Button actions.
        '''

        # Browse button action
        ThemeDialog.ui.browseButton.clicked.connect(self._browseThemes)

        # Add theme button action
        ThemeDialog.ui.addButton.clicked.connect(lambda: self._addTheme(ThemeDialogUi.addLineEdit.text()))