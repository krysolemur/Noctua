# main.py

import sys
import traceback
import Application.Commands.Commands as actions

def main() -> None:
    try:
        # Check for input
        if len(sys.argv) > 1:
            cmd = sys.argv[1]
            args = sys.argv[2:]

            # 1. Validate command
            if cmd not in actions.commands:
                print(f"Error: Unknown command '{cmd}'. Use --help for info.")
                sys.exit(1)

            # 2. GUI Path
            if cmd == "--run" or cmd in actions.GUI_COMMANDS:
                from Application.Application import Application
                app = Application()
                
                # Execute command before starting the window
                if cmd in actions.GUI_COMMANDS:
                    actions.commands[cmd](*args)
                
                # Start app loop
                sys.exit(app.exec())

            # 3. CLI Path
            else:
                try:
                    actions.commands[cmd](*args)
                except TypeError as e:
                    # Handle argument errors
                    if "arguments" in str(e) or "positional" in str(e):
                        print(f"Error: Invalid arguments for '{cmd}'.")
                    else:
                        raise 
        else:
            # Welcome message
            print("WebScope: Use --run to start or --help for options.")

    except KeyboardInterrupt:
        # Clean exit on Ctrl+C
        print("\nApplication stopped.")
        sys.exit(0)
        
    except Exception:
        # Log unexpected errors
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()