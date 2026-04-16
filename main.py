# main.py

# Importing system files
import sys
import signal
import traceback

# Importing program files
from Application.Application import Application

from Application.Commands.Commands import Commands

# Ctrl+C signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Main class
class Main:

    def __init__(self) -> None:

        # Creating app
        self.Application = Application()

        # Running app
        sys.exit(self.Application.exec())

# Main block
if __name__ == "__main__":

    # Creating commands
    commands = Commands()

    # Try block for catching errors
    try:

        # Check num of args
        if len(sys.argv) > 1:

            # Store the first argument as a command
            command = sys.argv[1]

            # Store others arguments
            arguments = sys.argv[2::]

            # Check command
            if command not in commands.commands.keys():

                # Unknown commnad
                print("Unknown command! Try --help for help menu.")

                # Exit the script with an error status code
                sys.exit(1)
        
            # Run command for run application
            if command == "--run":

                # Assign main class
                main = Main
                
                # Run main class
                main()

            # Others variantions
            else:

                # Args errors
                try:

                    # Run command
                    commands.commands[command](arguments)

                except TypeError:

                    # Print missing argument error
                    print(f"{command}: Missing command operands")
                
                    # Print help command
                    print(f"Try --help {command[2::] + " " if command != "--help" else ""}for more information.")

        else:
            
            # Print help message
            print("Run \"python3 main.py --run\" to start application. Type \"--help\" for help menu.")
            
    # Catching errors
    except Exception as e:

        # Print defailed error
        traceback.print_exception(type(e), e, e.__traceback__)