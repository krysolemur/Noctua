# Logger.py

# Importing system modules
import sys
import os

# Main class Logger
class Logger:

    # Logs dir
    LOGS_DIR = "Logs"

    # Initiator
    def __init__(self, config, serviceName) -> None:
        None
    
    # # Update settings
    # def update_config(self, newConfig) -> None:
    #     # Remove configuration
    #     logger.remove() 
        
    #     # Run constructor again with new config
    #     self.__init__(newConfig, self.serviceName)

    #     # Log successfully update
    #     logger.success("Logger configuration updated successfully.")

    # # Clear logs
    # @classmethod
    # def clear_logs(cls) -> None:
    #     # Clear log file by opening it in write mode
    #     with open(f"{cls.LOGS_DIR}/app.log", "w") as log:
    #         pass 
    #     print("Logs have been cleared.")

logger = Logger()
