# Logger.py

from datetime import datetime
import traceback
import inspect
import json
import sys
import os

from Application.AppContext import ctx

# Default configuration
DEFAULT_CONFIG = {
    "cb_console_time": "Yes",
    "cb_console_colors": "Yes",
    "btn_console_info": True,
    "btn_console_warning": True,
    "btn_console_success": True,
    "btn_console_error": True,
    "btn_console_debug": True,
    "cb_file_enabled": "Yes",
    "btn_file_info": True,
    "btn_file_warning": True,
    "btn_file_success": True,
    "btn_file_error": True,
    "btn_file_debug": True,
    "sb_file_rotation": 10,
    "sb_file_retention": 7,
    "le_file_path": "./Logs",
    "cb_file_compression": "zip"
}

class Logger:

    # Logs dir
    LOG_PATH = "Logs/app.log"

    def __init__(self, config:dict) -> None:

        # Get c_levels and f_levels
        self.c_levels = {
            "INFO": config["btn_console_info"],
            "WARN": config["btn_console_warning"],
            "SUCCESS": config["btn_console_success"],
            "ERROR": config["btn_console_error"],
            "DEBUG": config["btn_console_debug"],
            "CRITICAL": True
        }

        if config["cb_file_enabled"] == "Yes":
            self.f_levels = {
                "INFO": config["btn_file_info"],
                "WARN": config["btn_file_warning"],
                "SUCCESS": config["btn_file_success"],
                "ERROR": config["btn_file_error"],
                "DEBUG": config["btn_file_debug"],
                "CRITICAL": True
            }
        else:
            self.f_levels = {
                "INFO": False,
                "WARN": False,
                "SUCCESS": False,
                "ERROR": False,
                "DEBUG": False,
                "CRITICAL": True
            }

        # Get time
        self.time = bool(config["cb_console_time"])

        # Log init
        self.info("Logger initialized")

    # Write to console and file methods for high efectivity
    def _cout(self, level, msg, func="", row="", filename="") -> None:
        # Check level
        if not self.c_levels.get(level, False):
            return
        
        # Get timestamp
        if self.time:
            timestamp = datetime.now().strftime("%H:%M:%S")

        # Create msg
        path = f"{filename}{":" if filename else ""}{func}{":" if func else ""}{row}"
        msg = f"{timestamp} {level:^10} {path}{" - " if path else ""}{msg}"
        print(msg)
    
    def _fout(self, level, msg, func="", row="", filename="") -> None:
        # Check level
        if not self.f_levels.get(level, False):
            return
        
        # Get timestamp
        if self.time:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create msg
        path = f"{filename}{":" if filename else ""}{func}{":" if func else ""}{row}"
        msg = f"{timestamp} {level:^10} {path}{" - " if path else ""}{msg}"
    
    # Info log
    def info(self, msg) -> None:
        self._cout("INFO", msg)
        self._fout("INFO", msg)

    # Warning log
    def warn(self, msg) -> None:
        self._cout("WARN", msg)
        self._fout("WARN", msg)

    # Success log
    def success(self, msg) -> None:
        self._cout("SUCCESS", msg)
        self._fout("SUCCESS", msg)

    # Error log
    def error(self, msg) -> None:
        # Get info about where was func calling

        # Filename, row and func
        caller_frame = inspect.stack()[1]

        filename = os.path.basename(caller_frame.filename)
        row = caller_frame.lineno
        func = caller_frame.function

        # Output
        self._cout("ERROR", msg, row=row, func=func, filename=filename)
        self._fout("ERROR", msg, row=row, func=func, filename=filename)

    # Debug log
    def debug(self, msg) -> None:
        self._cout("DEBUG", msg)
        self._fout("DEBUG", msg)

    # Critical -> Not in settings
    def critical(self, exception) -> None:
        # Get details from exception
        msg = self._error_details(exception=exception)

        # Output
        self._cout("CRITICAL", msg)
        self._fout("CRITICAL", msg)

    # Get error details
    def _error_details(self, exception) -> dict:
        # Full traceback of error
        full_traceback = traceback.format_exc()
        
        # Error location
        _, _, exc_tb = sys.exc_info()
        tb_last = traceback.extract_tb(exc_tb)[-1] if exc_tb else None
        
        # Details dictonary
        details = {
            # Type and message
            "type": type(exception).__name__,
            "message": str(exception),
            
            # Localize error
            "file": tb_last.filename if tb_last else "Unknown",
            "line": tb_last.lineno if tb_last else "N/A",
            "function": tb_last.name if tb_last else "N/A",
            "code": tb_last.line if tb_last else "N/A",
            
            # Full trackeback
            "full_traceback": "\n" + full_traceback,
        }

        # Specific errors data
        if isinstance(exception, OSError):
            details["extra_info"]["errno"] = exception.errno
            details["extra_info"]["path"] = exception.filename

        # Format details
        json_string = json.dumps(details, indent=4, ensure_ascii=False)

        ident = " " * 6

        clean_json = json_string.replace('\\n', '\n' + ident)
        clean_json = clean_json.replace('\\"', '"')

        return clean_json

# Init logger
logger = Logger(ctx.config.get("LoggingPage", DEFAULT_CONFIG))

