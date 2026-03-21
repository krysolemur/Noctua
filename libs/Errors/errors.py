# errors.py

# Importing 
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication # type: ignore
from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore

from libs.Logging.logging import Logging

# Class for displaying errors for users

# Main class Errors 
class Error(Logging):
    def __init__(self):
        # Init parents
        super().__init__()

    # User error definition
    def userError(self):
        # Load Ui file
        ui_file = QtCore.QFile("Application/QtGuiFiles/Error.ui")

        # Read Ui file
        ui_file.open(QtCore.QFile.ReadOnly)

        # Load to setupWindow
        self.errorWindow = QtUiTools.QUiLoader().load(ui_file)

        # Process events
        QtWidgets.QApplication.processEvents()

        # Close Ui file
        ui_file.close()

        # # Dialog properties like title, size and more
        # self.errorWindow.setWindowTitle(f"WebScope | {self.version}")

        # Set size
        self.errorWindow.setFixedSize(600, 75)

        # Set window icon
        self.errorWindow.setWindowIcon(QtGui.QIcon("Application/assets/icons/icon.png"))

        # Exec setupWindow
        self.errorWindow.show()
