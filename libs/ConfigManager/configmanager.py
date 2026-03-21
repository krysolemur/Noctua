# configmanager.py

# This modules are used for managing settings and other configuration
import json
import sys
import os

# Import program files
from libs.Logging.logging import Logging

# Main class Config:
class Config(Logging):
    def __init__(self):
        # Init parents
        super().__init__()

        # Defautl settings
        self.defautl_config = {
            
        }

        # Config folder path
        self.config_dir = "Users/Default/Config"

        # Condif file path
        self.config_file = "Users/Default/Config/config.json" 

        # Check if config folder exists
        if not os.path.exists(self.config_dir):
            # Print warning
            self.printf(status="WARNING", msg="Config directory doesen't exists! Creating new.")

            # Create
            os.makedirs(self.config_dir)

        # Check if config file exists
        if not os.path.exists(self.config_file):
            # Print warning
            self.printf(status="WARNING", msg="Config file doesen't exists! Creating new.")

            # Creating
            with open(self.config_file, "w") as config:
                json.dump(self.defautl_config, config, indent=4)