# settingswindow.py

# Module for managing settings window

# Importing system files
from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QMainWindow, QMessageBox # type: ignore
from PySide6.QtCore import QTimer, QFile # type: ignore
from PySide6.QtUiTools import QUiLoader # type: ignore

# Importing program files
from libs.Logging.logging import Logging

# Class settings window
class SettingsWindow(Logging, QDialog):
    def __init__(self, app) -> None:
        '''
        Init parents, save app and print info message.
        '''
        # Init parents
        super().__init__()

        # Save application
        self.app = app

        # Print info message
        self.printf(status="INFO", msg="Opening settings menu")

        '''
        Load user interface file to settings window menu.
        '''

        # Load Ui file
        ui_file = QtCore.QFile("libs/QtGuiFiles/SettingsDialog.ui")

        # Read Ui file
        ui_file.open(QtCore.QFile.ReadOnly)

        # Load to settingsWindow
        self.ui = QUiLoader().load(ui_file, self)

        # Process events
        QtWidgets.QApplication.processEvents()

        # Close Ui file
        ui_file.close()

        '''
        Title, size and other settings.
        '''

        # Dialog properties like title, size and more
        self.setWindowTitle(f"WebScope | {self.app.version} | Settings")

        # Set size
        self.setFixedSize(800, 600)

        # Set window icon
        self.setWindowIcon(QtGui.QIcon("Application/assets/icons/icon.png"))

    '''
    Public functions.
    '''

    # Close event
    def closeEvent(self, event) -> None:
        # Print message
        self.printf(status="INFO", msg="Closing settings window")

        # Close window
        self.close()
