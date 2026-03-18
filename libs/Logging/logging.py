# logging.py

# Importing
import traceback
import sys

# This python file will be using for logging into files if enabled

# Main class Logging 
class Logging:
    def __init__(self, *args, **kwargs):
        # Init arguments
        super().__init__(*args, **kwargs)

        # Accept types terminal
        self.accept_types_terminal = []

        # Accept types file
        self.accept_types_file = {
            
        }

        # Logging variable
        self.logging = True

    # Printf method do print
    def printf(self, status, msg=None, exception=None, function=None):
        # Check type
        if status in self.accept_types_terminal or not self.accept_types_terminal:
            if status == "ERROR":
                # Get info from error
                exc_type, exc_value, exc_tb = sys.exc_info()
                last_tb = traceback.extract_tb(exc_tb)[-1]

                # Print error    
                print(f"[  \033[31mERROR\033[0m   ] {msg if msg else "ERROR"} at line {last_tb.lineno} in {last_tb.filename}!")
            elif status == "OK":
                # Print ok
                print(f"[    \033[32mOK\033[0m    ] {msg if msg else f"{function}() run successfully"}.")
            elif status == "WARNING":
                # Print warning
                print(f"[  \033[33mWARNING\033[0m ] {msg}.")
            elif status == "DEBUG":
                # Print debug
                print(f"[   \033[35mDEBUG\033[0m  ] {msg}.")
            elif status == "INFO":
                # Print info
                print(f"[   \033[34mINFO\033[0m   ] {msg}.")
            elif status == "CRITICAL":
                # Print info
                print(f"[ \033[1m\033[31mCRITICAL\033[0m ] {msg + "! " if msg else ""}Exiting program.")

                # Exit program
                sys.exit(1)
            else:
                None