# Logger.py

from datetime import datetime
import traceback
import sys
import queue
import threading
import json
import inspect
import os

from noctua.context import ctx

# Default configuration
DEFAULT_CONFIG = {
    "cb_console_time": "Yes",
    "cb_console_colors": "Yes",
    "btn_console_info": True,
    "btn_console_warning": True,
    "btn_console_success": True,
    "btn_console_error": True,
    "btn_console_debug": False,
    "cb_file_enabled": "Yes",
    "btn_file_info": False,
    "btn_file_warning": False,
    "btn_file_success": False,
    "btn_file_error": True,
    "btn_file_debug": False,
    "sb_file_rotation": 10,
    "sb_file_retention": 7,
    "le_file_path": "./Logs",
    "cb_file_compression": "zip"
}

class Logger:

    # Logs dir
    DEFAULT_LOG_DIR = "Logs"
    
    # Logs filepath
    DEFAULT_LOG_FILE = "app.log"

    # Level colors
    LEVEL_COLORS = {
        "INFO": "\033[94m", "WARN": "\033[93m", "SUCCESS": "\033[92m",
        "ERROR": "\033[91m", "DEBUG": "\033[95m", "CRITICAL": "\033[1;41;97m",
        "RESET": "\033[0m", "GRAY": "\033[90m", "WHITE_BOLD": "\033[1;97m"
    }
    
    # Initialization
    def __init__(self, config:dict) -> None:
        # Console levels
        self.console_levels = {}

        # File levels
        self.file_levels = {}

        # File writer thread
        self.file_writer_thread = None

        # Stop flag for thread
        self.stop_writer = False

        # File queue
        self.file_write_queue = queue.Queue()

        # Threading lock for synchronization
        self.logging_lock = threading.Lock()
        # Create paths
        self.log_dir = config.get("le_file_path", DEFAULT_CONFIG.get("le_file_path", self.DEFAULT_LOG_DIR))
        self.log_path = os.path.join(self.log_dir, self.DEFAULT_LOG_FILE)

        # Start file writer thread
        self._start_file_writer_thread()

        # Start
        self.update(config)
        
    # Thread management
    def _start_file_writer_thread(self):
        if self.file_writer_thread is None or not self.file_writer_thread.is_alive():
            self.stop_writer = False
            self.file_writer_thread = threading.Thread(target=self._file_writer_loop, daemon=True)
            self.file_writer_thread.start()
    
    def _file_writer_loop(self):
        while not self.stop_writer:
            try:
                # Get item from queue with timeout
                item = self.file_write_queue.get(timeout=1.0)
                if item is None:  # Stop signal
                    break
                level, msg, caller = item
                self._write_to_file_sync(level, msg, **caller)
                self.file_write_queue.task_done()
            except queue.Empty:
                continue

    # Config helpers
    def _set_console_levels(self, config: dict) -> None:
        self.console_levels = {
            "INFO": config.get("btn_console_info", True),
            "WARN": config.get("btn_console_warning", True),
            "SUCCESS": config.get("btn_console_success", True),
            "ERROR": config.get("btn_console_error", True),
            "DEBUG": config.get("btn_console_debug", True),
            "CRITICAL": True
        }

    def _set_file_levels(self, config: dict) -> None:
        if config.get("cb_file_enabled") == "Yes":
            # Set levels for file logging
            self.file_levels = {
                "INFO": config.get("btn_file_info", False),
                "WARN": config.get("btn_file_warning", False),
                "SUCCESS": config.get("btn_file_success", False),
                "ERROR": config.get("btn_file_error", True),
                "DEBUG": config.get("btn_file_debug", False),
                "CRITICAL": True
            }

            # File handling
            try:
                # Check logging directory
                if self.log_dir:
                    os.makedirs(self.log_dir, exist_ok=True)
                self.log_file = open(self.log_path, "a", encoding="utf-8")
                # Restart file writer thread
                self._start_file_writer_thread()
            except OSError as e:
                print(f"LOG_ERROR: {e}")
                self.log_file = None

        else:
            self.file_levels = {
                "INFO": False,
                "WARN": False,
                "SUCCESS": False,
                "ERROR": False,
                "DEBUG": False,
                "CRITICAL": True
            }
        
    def _write_to_console(self, level, msg, func="", row="", filename="") -> None:
        # Get timestamp and colors      
        timestamp = datetime.now().strftime("%H:%M:%S") if self.include_timestamp else ""
        color = self.LEVEL_COLORS.get(level, "")
        reset = self.LEVEL_COLORS["RESET"]
        
        # Format message
        if self.use_colors:
            path = f"{filename}:{func}:{self.LEVEL_COLORS['WHITE_BOLD']}{row}{reset}"
            formatted_msg = f"{self.LEVEL_COLORS['GRAY']}{timestamp}{reset} {color}{level:^10}{reset} {path} - {msg}"
        else:
            formatted_msg = f"{timestamp} {level:^10} {filename}:{func}:{row} - {msg}"
        
        # Print to console
        print(formatted_msg)
    
    # Writing to file
    def _write_to_file(self, level, msg, func="", row="", filename="") -> None:
        # Add to queue for async writing
        self.file_write_queue.put((level, msg, {"func": func, "row": row, "filename": filename}))
    
    # Synchronous file writing (for thread)
    def _write_to_file_sync(self, level, msg, func="", row="", filename="") -> None:
        # Timestamp, path and msg
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if self.include_timestamp else ""
        path = f"{filename}:{func}:{row}"
        formatted_msg = f"{timestamp} {level:^10} {path} - {msg}\n"
        
        # Log to file
        try:
            self.log_file.write(formatted_msg)
            self.log_file.flush()
        except OSError:
            pass

    # Log to file and console
    def _log_message(self, level, msg, is_exception=False, caller=None) -> None:
        # Get caller if not provided
        if caller is None:
            caller = self._get_caller_details()
        
        # Lock threads
        with self.logging_lock:
            # Write to console
            if self.console_levels.get(level, False):
                self._write_to_console(level, msg, **caller)
            
            # Write to file
            if self.log_file and self.file_levels.get(level, False):
                self._write_to_file(level, msg, **caller)
            
    # Lifecycle
    def update(self, config:dict) -> None:
        # Close old log
        self.close()
        
        # Set console and file levels
        self._set_console_levels(config)
        self._set_file_levels(config)
        
        # Get time and colors
        self.include_timestamp = config.get("cb_console_time") == "Yes"
        self.use_colors = config.get("cb_console_colors") == "Yes"

        # Log init
        self.info("Logger initialized")

    # Close log file
    def close(self) -> None:
        # Stop file writer thread
        self.stop_writer = True
        self.file_write_queue.put(None)  # Stop signal
        if self.file_writer_thread and self.file_writer_thread.is_alive():
            self.file_writer_thread.join(timeout=5.0)
        
        # With threading
        with self.logging_lock:
            if self.log_file:
                try:
                    # Log closing and close 
                    self.info("Logger is shutting down...")
                    self.log_file.flush()
                    self.log_file.close()
                except Exception as e:
                    # Print error
                    print(f"Error during logger shutdown: {e}")
                finally:
                    # Set log file to None
                    self.log_file = None

    # Public API
    def info(self, msg):
        self._log_message("INFO", msg)
    
    def warn(self, msg):
        self._log_message("WARN", msg)
    
    def success(self, msg):
        self._log_message("SUCCESS", msg)
    
    def debug(self, msg):
        self._log_message("DEBUG", msg)
    
    def error(self, msg):
        self._log_message("ERROR", msg)
    
    def critical(self, exception):
        # Get details and log
        details = self._format_error_details(exception)
        self._log_message("CRITICAL", details)

    # Utils
    @staticmethod
    def _get_caller_details() -> dict:
        frame = inspect.currentframe().f_back.f_back.f_back
        if frame:
            return {
                "filename": os.path.basename(frame.f_code.co_filename),
                "func": frame.f_code.co_name,
                "row": frame.f_lineno
            }
        return {"filename": "unknown", "func": "unknown", "row": 0}
        
    # Get error details
    @staticmethod
    def _format_error_details(exception) -> str:
        tb_lines = traceback.format_exc().splitlines()
        
        # Error location
        _, _, exc_tb = sys.exc_info()
        tb_last = traceback.extract_tb(exc_tb)[-1] if exc_tb else None
        
        # Details
        details = {
            "type": type(exception).__name__,
            "message": str(exception),
            "location": {
                "file": tb_last.filename if tb_last else "Unknown",
                "line": tb_last.lineno if tb_last else "N/A",
                "function": tb_last.name if tb_last else "N/A"
            },
            "full_traceback": tb_lines, 
            "extra_info": {}
        }

        # Specific errors data
        if isinstance(exception, OSError):
            details["extra_info"]["errno"] = exception.errno
            details["extra_info"]["path"] = exception.filename

        # Return formated details
        return json.dumps(details, indent=4, ensure_ascii=False)



