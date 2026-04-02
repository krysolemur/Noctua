# theme.py

# Import system modules
import os

from PySide6.QtWidgets import QDialog, QFileDialog # type: ignore

# Import profram files
from libs.Logging.logging import Logging

from libs.QtGuiFiles.PyFiles.ThemeDialog import Ui_ThemeDialog

# Class Theme
class Theme(QDialog, Logging):
    def __init__(self) -> None:
        '''
        Init parents and set imoprtant variables.
        '''

        # Init parents
        super().__init__()

        # Theme directory
        self.theme_dir = "resources/Themes"

        # All themes
        self.themes = self._getThemes

        # Get themes
        self.themes()

        '''
        Create dialog, load ui and setup it.
        '''

        # Load ui
        self.ui = Ui_ThemeDialog()

        # Setup ui
        self.ui.setupUi(self)

        '''
        Setup window like title, size and more.
        '''

        # Title
        self.setWindowTitle("Add theme")

        # Minimum size
        self.setMinimumSize(self.sizeHint())

        # Resize
        self.resize(self.sizeHint())

        '''
        Button actions.
        '''

        # Browse button action
        self.ui.browseButton.clicked.connect(self._browseThemes)

        # Add theme button action
        self.ui.addButton.clicked.connect(lambda: self._addTheme(self.ui.addLineEdit.text()))

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