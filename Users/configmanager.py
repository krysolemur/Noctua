# configmanager.py

# Import system files
import json
import sys
import os

# Import program files
from libs.Logging.logging import Logging
from Users.usersmanager import UsersManager

# Main class Config:
class ConfigManager(Logging):
    def __init__(self):
        '''
        Init parents, set variables.
        '''
        # Init parents
        super().__init__()

        # Default app config
        self.app_config = {}

        # Default user config
        self.user_config = {}

        # Default general config
        self.general_config = {}

        # Config folder path
        self.config_dir = "Users"

        # general.json path
        self.general_path = "general.json"

        '''
        Check all config files for all users.
        '''

        # List all users and check config files
        for user in os.listdir(self.config_dir):
            if os.path.isdir(f"{self.config_dir}/{user}") and not user == "__pycache__":
                # Check if config_app file exists
                if not os.path.exists(f"{self.config_dir}/{user}/app_config.json"):
                    # Print warning
                    self.printf(status="WARNING", msg=f"Config file for user {user} doesen't exists! Creating new.")

                    # Creating
                    with open(f"{self.config_dir}/{user}/app_config.json", "w") as config:
                        # Write default settings
                        json.dump(self.app_config, config, indent=4)

                        # Close file
                        config.close()

                    # Check if config_user file exists
                if not os.path.exists(f"{self.config_dir}/{user}/user_config.json"):
                    # Print warning
                    self.printf(status="WARNING", msg=f"Config file for user {user} doesen't exists! Creating new.")

                    # Creating
                    with open(f"{self.config_dir}/{user}/user_config.json", "w") as config:
                        # Write default settings
                        json.dump(self.user_config, config, indent=4)

                        # Close file
                        config.close()

        # Check general.json in main directory
        if not os.path.exists(self.general_path):
            # Print warning
            self.printf(status="WARNING", msg=f"General config doesen't exists! Creating new.")

            # Create general.json
            with open(self.general_path, "w") as config:
                # Write default settings
                json.dump(self.general_config, config, indent=4)

                # Close file
                config.close()