# application.py

# Importing
import requests # type: ignore
import sys
import os
import math
import json


from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QMessageBox # type: ignore
from PySide6.QtCore import QTimer, QFile # type: ignore
from PySide6.QtUiTools import QUiLoader # type: ignore

# Importing program files
from libs.Window.window import Window
from libs.ConfigManager.configmanager import Config
from libs.Logging.logging import Logging
from libs.Errors.errors import Error
from libs.Users.users import Users

# Class for managing whole application
class Application(Logging, QApplication):
    def __init__(self) -> None:
        '''
        Set application parametres, init parents and other.
        '''
        # Init parents
        super().__init__(sys.argv)

        # Start QTimer
        self.timer = QTimer()

        # Info message
        self.printf(msg="Creating application", status="INFO")

        '''
        Setting all applications variables.
        '''

        # Application version
        self.version = "0.1.0"

        # User variable
        self.user = "Default"

        '''
        Inicializing all neccessary modules.
        '''

        # Users module
        self.users = Users()

        # Config module
        self.config = Config()

        # Error module
        self.error = Error()

        # Window module
        self.window = Window(app=self)

        '''
        Running program.
        '''

        # Setup application
        self._setup()

    '''
    Private functions.
    '''

    # Setup function
    def _setup(self) -> None:
        # Print DEBUG
        self.printf(status="DEBUG", msg="Inicializing application")

        # Process index variable
        self.process_index = 0

        '''
        Load ui for custom restart dialog.
        '''

        # Load Ui file
        ui_file = QtCore.QFile("libs/QtGuiFiles/SetupDialog.ui")

        # Read Ui file
        ui_file.open(QtCore.QFile.ReadOnly)

        # Load to setupDialog
        self.setupDialog = QtUiTools.QUiLoader().load(ui_file)

        # Process events
        QtWidgets.QApplication.processEvents()

        # Close Ui file
        ui_file.close()

        '''
        Set window properties, title, size and more.
        '''

        # Dialog properties like title, size and more
        self.setupDialog.setWindowTitle(f"WebScope | {self.version} | Inicializing")

        # Set size
        self.setupDialog.setFixedSize(600, 75)

        # Exec setupDialog
        self.setupDialog.show()

        '''
        Set timer for loading bar.
        '''

        # Run all setup processes with pause
        self.timer.timeout.connect(self._run_next_process)

        # Small pause
        self.timer.start(500)

    # Run next proccess function
    def _run_next_process(self) -> None:
        # List of all proccesses with their labels
        all_proccess = [
            (self._checkNetworkConnection, "Checking internet connection..."),
            (self._checkForUpdates, "Checking for updates..."),
            (self._checkUserDir, "Checking user directory"),
            (self._checkConfigDir, "Checking config directory...")
        ]

        '''
        Close dialog, open main window and stop timer when loop ends.
        '''
        # Check if all process was runned
        if self.process_index == len(all_proccess):
            # Stop timer
            self.timer.stop()

            # Delete timer
            del(self.timer)

            # Close loading window
            self.setupDialog.close()

            # Delete setup window
            del(self.setupDialog)

            # Show main window
            self.window.show()

            # End loop 
            return

        '''
        Run all proccess with try except block for catching errors.
        '''

        # Get one process
        process = all_proccess[self.process_index]

        # Try-except for catching errors
        try:    
            # Check if process is call able
            if callable(process[0]):
                # Run process
                process[0]()

            '''
            Set label properties and loading bar actions.
            '''

            # Set loading label text
            self.setupDialog.loadingLabel.setText(process[1])

            # Set OK Color
            self.setupDialog.statusLabel.setStyleSheet("color: #00ff00")

            # Set OK status of function
            self.setupDialog.statusLabel.setText("OK")

            # Set progressBar value
            self.setupDialog.loadingBar.setValue(self.setupDialog.loadingBar.value() + (100 // len(all_proccess)))

            # OK message
            self.printf(status="OK", msg="", function=process[0].__name__)
        except Exception as e:
            '''
            Set error look.
            '''

            # Error message
            self.printf(status="ERROR", exception=e, msg="")

            # Set ERROR Color
            self.setupDialog.statusLabel.setStyleSheet("color: #ff0000")

            # Set ERROR status of function
            self.setupDialog.statusLabel.setText("ERROR")

            # Stop timer
            self.timer.stop()

        # Count + 1 process index
        self.process_index += 1

    # Checking internet connection
    def _checkNetworkConnection(self) -> None:
        None

    # Function that check for updates
    def _checkForUpdates(self) -> None:
        None

    # Check user directory
    def _checkUserDir(self) -> None:
        # Check Users folder
        if not os.path.exists(self.users.users_dir):
            # Print warning
            self.printf(status="WARNING", msg="Users directory doesen't exists! Creating new.")

            # Create
            os.makedirs(self.users.users_dir)

        # Check defautl user folder 
        if not os.path.exists(self.users.default_dir):
            # Print warning
            self.printf(status="WARNING", msg="Default user doesen't exists! Creating new.")

            # Create
            os.makedirs(self.users.default_dir)

    # Checking config files
    def _checkConfigDir(self) -> None:
        # Check if config folder exists
        if not os.path.exists(self.config.config_dir):
            # Print warning
            self.printf(status="WARNING", msg="Config directory doesen't exists! Creating new.")

            # Create
            os.makedirs(self.config_dir)

        # Check if config file exists
        if not os.path.exists(self.config.config_file):
            # Print warning
            self.printf(status="WARNING", msg="Config file doesen't exists! Creating new.")

            # Creating
            with open(self.config_file, "w") as config:
                json.dump(self.config.defautl_config, config, indent=4)

    '''
    Public functions.
    '''
