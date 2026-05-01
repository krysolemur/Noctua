# main.py

import sys
import signal

from noctua.logger.logger import logger
from noctua.app import Application

def main() -> None:
    # Allow Ctrl+C to work properly with Qt
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    try:
        # Create and execute app
        app = Application()
        sys.exit(app.exec())

    except KeyboardInterrupt:
        # Clean exit on Ctrl+C
        print("\nApplication stopped.")
        sys.exit(0)
        
    except Exception as e:
        # Log error
        logger.critical(e)

        # Exit 
        sys.exit(1)


if __name__ == "__main__":
    main()