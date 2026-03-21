# user.py

# This is for managing users in this application

# Importing system files
import os

# Importing program files
from libs.Logging.logging import Logging

# Class users
class Users(Logging):
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

        # Check Users folder
        if not os.path.exists(self.users_dir):
            # Print warning
            self.printf(status="WARNING", msg="Users directory doesen't exists! Creating new.")

            # Create
            os.makedirs(self.users_dir)

        # Check defautl user folder 
        if not os.path.exists(self.default_dir):
            # Print warning
            self.printf(status="WARNING", msg="Default user doesen't exists! Creating new.")

            # Create
            os.makedirs(self.default_dir)

    '''
    Private functions.
    '''

    '''
    Public functions.
    '''
