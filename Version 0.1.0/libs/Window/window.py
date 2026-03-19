# window.py

# Importing system files
from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QMainWindow, QMessageBox # type: ignore
from PySide6.QtCore import QTimer, QFile # type: ignore
from PySide6.QtUiTools import QUiLoader # type: ignore

# Imporing program files
from libs.Logging.logging import Logging
from libs.SettingsWindow.settingswindow import SettingsWindow

# Main class window for managing window and loading GUI
class Window(QMainWindow, Logging):
    def __init__(self, app) -> None:
        # Init QMainWindow
        super().__init__()

        # Save parent 
        self.app = app

        '''
        Load user interface 
        '''

        # Load QtUi file 
        ui_file = QFile("QtGuiFiles/MainWindow.ui")

        # Open for reading
        ui_file.open(QFile.ReadOnly)

        # Load Ui
        self.ui = QUiLoader().load(ui_file)

        # Set central widget
        self.setCentralWidget(self.ui)

        # Close file
        ui_file.close()

        # Process events
        QtWidgets.QApplication.processEvents()

        '''
        Set actions for all menu in tool bar like settings, help and more...
        '''

        self.ui.actionSettings.triggered.connect(self._openSettings)

        '''
        Other windows settings like size, title and more...
        '''

        # Title
        self.setWindowTitle(f"WebScope | {self.app.version}")  

        # Size
        self.resize(800, 600) 

        # Go to center of screen
        self._center()

    '''
    Private functions.
    '''

    # Center function
    # No logging
    def _center(self) -> None:
        # Get screen size
        screen = QApplication.primaryScreen()

        # Get geometry
        screen_geometry = screen.geometry()

        # Count half of creen
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        # Move to center
        self.move(x, y)

    # Settings function
    def _openSettings(self):
        # Create settings window object
        self.settingsWindow = SettingsWindow(app=self.app)

        # Exec settings window
        self.settingsWindow.exec()

    '''
    Public functions.
    '''
    
    # Close event
    def closeEvent(self, event):
        # Get reply by user
        reply = QMessageBox.question(
            self,
            "Confirm",               
            "Do you really want quit application?", 
            QMessageBox.Yes | QMessageBox.No,  
            QMessageBox.No             
        )

        # Check reply
        if reply == QMessageBox.Yes:
            # If yes print info
            self.printf(status="INFO", msg="Quiting application")

            # Quit app
            self.app.quit()
        else:
            # Ignore and close just the dialog, keep main window opened
            event.ignore()




