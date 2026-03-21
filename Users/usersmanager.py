# usersmanager.py

# This is for managing users in this application

# Importing system files
import os

from PySide6 import QtWidgets, QtCore, QtUiTools, QtGui # type: ignore
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QMessageBox, QListView # type: ignore
from PySide6.QtCore import QTimer, QFile # type: ignore
from PySide6.QtUiTools import QUiLoader # type: ignore
from PySide6.QtGui import QStandardItemModel, QStandardItem

# Importing program files
from libs.Logging.logging import Logging

# Class users
class UsersManager(Logging):
    def __init__(self):
        '''
        Init parents, set class variables and other.
        '''

        # Init parents
        super().__init__()

        # Users folder path
        self.users_dir = "Users"

        # Default user path
        self.default_dir = "Users/Default"

        # Version variable
        self.version = "0.1.0"

        # Check Users folder
        if not os.path.exists(self.users_dir):
            # Print warning
            self.printw(msg="Users directory doesen't exists! Creating new.")

            # Create
            os.makedirs(self.users_dir)

        # Check defautl user folder 
        if not os.path.exists(self.default_dir):
            # Print warning
            self.printw(msg="Default user doesen't exists! Creating new.")

            # Create
            os.makedirs(self.default_dir)

    '''
    Private functions.
    '''

    # Load settings for user 
    def _loadSettings(self, user) -> None:
        # Try find user settings for that user 
        try:
            # Get settings path
            settings_path = f"Users/{user}/user_config.json"

            # Open that file with user config
            with open(settings_path, "r") as config:
                print("fsdfsd")
                
        except FileExistsError:
            None

    '''
    Public functions.
    '''

    # Users settings dialog
    def usersSettings(self) -> None:
        '''
        Load ui for custom restart dialog.
        '''

        # Load Ui file
        ui_file = QtCore.QFile("libs/QtGuiFiles/UsersDialog.ui")

        # Read Ui file
        ui_file.open(QtCore.QFile.ReadOnly)

        # Load to setupDialog
        self.usersDialog = QtUiTools.QUiLoader().load(ui_file)

        # Process events
        QtWidgets.QApplication.processEvents()

        # Close Ui file
        ui_file.close()

        '''
        Set window properties, title, size and more.
        '''

        # Dialog properties like title, size and more
        self.usersDialog.setWindowTitle(f"WebScope | {self.version} | Users settings")

        # Set size
        self.usersDialog.setFixedSize(400, 300)

        # Create model
        self.model = QStandardItemModel()

        # Set model for list view
        self.usersDialog.usersView.setModel(self.model)

        '''
        Append all users to list view, show settings for that user and other actions.
        '''

        # Using loop browse all users in /Users folder
        for user in os.listdir(self.users_dir):
            if os.path.isdir(f"{self.users_dir}/{user}") and not user == "__pycache__":
                # Append to usersView
                self.model.appendRow(QStandardItem(user))

        # Load settings when users is changet in list view
        self.usersDialog.usersView.selectionModel().currentChanged.connect(lambda current, prev: self._loadSettings(user=self.model.data(current)))

        '''
        Exec usersDialog.
        '''

        # Exec setupDialog
        self.usersDialog.exec()

    # Login function
    def login(self, username) -> bool:
        ...

    # Function that create user folder
    def addUser(self, name) -> None:
        # Try except block
        try:
            # Create
            os.makedirs(self.default_dir)

            # Print info
            self.printo(msg=f"Added user {name}")
        except Exception as e:
            # Print info
            self.printe(msg=f"Error while adding user {name}", exception=e, function=__name__)


