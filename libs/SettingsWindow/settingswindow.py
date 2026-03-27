# settingswindow.py

# Module for managing settings window

# Importing system files
import re
import os

from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import QFile 
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon 

# Importing program files
from libs.Logging.logging import Logging
from Config.configmanager import ConfigManager

# Class settings window
class SettingsWindow(QDialog, Logging):
    def __init__(self, app) -> None:
        '''
        Init parents, save app and print info message.
        '''
        # Init parents
        super().__init__()

        # Save application
        self.app = app

        # Print info message
        self.printi(msg="Opening settings window")

        '''
        Usefull variables.
        '''

        # Config module
        self.config = ConfigManager()

        '''
        Load user interface file to settings window menu.
        '''

        # Load Ui file
        ui_file = QFile("libs/QtGuiFiles/SettingsDialog.ui")

        # Read Ui file
        ui_file.open(QFile.ReadOnly)

        # Load to settingsWindow
        self.ui = QUiLoader().load(ui_file)

        # Create layout
        self.layout = QVBoxLayout()

        # Load ui and add it to layout
        self.layout.addWidget(self.ui)

        # Delete edges from layout
        self.layout.setContentsMargins(0, 0, 0, 0) 

        # Set layout to settings dialog
        self.setLayout(self.layout)

        # Close Ui file
        ui_file.close()

        '''
        Title, size, other settings and actions.
        '''

        # Dialog properties like title, size and more
        self.setWindowTitle(f"{self.app.name} | {self.app.version} | Settings")

        # Set window icon
        self.setWindowIcon(QIcon("icon.svg"))

        # Set size
        self.setFixedSize(632, 560)

        # Add profiles into combobox
        self._loadProfiles()

        # Add profile action
        self.ui.addProfileButton.clicked.connect(self._addProfile)

        # Remove profile action
        self.ui.removeProfileButton.clicked.connect(self._removeProfile)

    # Load profiles
    def _loadProfiles(self) -> None:
        # Add all items to combobox
        self.ui.profilesComboBox.addItems(self.config.all_profiles)

    # Add profile
    def _addProfile(self) -> None:
        # Load Ui file
        ui_file = QFile("libs/QtGuiFiles/ProfileDialog.ui")

        # Read Ui file
        ui_file.open(QFile.ReadOnly)

        # Load to settingsWindow
        self.profileName = QUiLoader().load(ui_file)

        # Adjust size
        self.profileName.adjustSize()

        # Create button action
        self.profileName.createButton.clicked.connect(self._checkProfile)

        # Cancel button action
        self.profileName.cancelButton.clicked.connect(self.profileName.reject)

        # Show dialog
        self.profileName.exec()

    # Check profile function
    def _checkProfile(self) -> None:
        # Get name
        name = self.profileName.profileNameLineEdit.text().strip()

        # Set error styles
        self.profileName.statusLabel.setStyleSheet(
            "color: #ff0000"
        )

        # Check if profile is not None
        if not name or not bool(re.fullmatch(r'^[a-zA-Z0-9_\- ]+$', name)):
            # Set error label
            self.profileName.statusLabel.setText("Enter valid name!")

            return

        # Check if profile does not exists
        if os.path.exists(os.path.join(self.config.config_dir, f"{name}.json")):
            # Set error label
            self.profileName.statusLabel.setText(f"Profile with name {name} already exists!")
            
            return
        
        # Set success styles
        self.profileName.statusLabel.setStyleSheet(
            "color: #00ff00"
        )

        # Set succes label text
        self.profileName.statusLabel.setText(f"Profile with name {name} created successfully.")

        # Add profile
        self.config.addProfile(name)

        # Close dialog
        self.profileName.close()

        # Actualize profiles list
        self._loadProfiles()

    # Remove profile
    def _removeProfile(self) -> None:
        # Get name
        name = self.ui.profilesComboBox.currentText()

        # Call config function
        self.config.removeProfile(name)

    '''
    Public functions.
    '''

    # Close event
    def closeEvent(self, event) -> None:
        # Print message
        self.printi(msg="Closing settings window")

        # Close window
        event.accept()
