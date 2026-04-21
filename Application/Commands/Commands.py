# Commands.py

import sys

from Application.ConfigManager.ConfigManager import ConfigManager
from Application.Application import Application as app
from Application.ThemeManager.ThemeCreator import ThemeCreator
from Application.Logger.Logger import Logger

CLI_COMMANDS = ["--help", "--version", "--reset-settings", "--clear-logs"]
GUI_COMMANDS = ["--run", "--theme-creator", "--style-creator"]
ALL_COMMANDS = ["run", "help", "reset-settings", "create-settings", "version"]
COMMANDS_DESCRIPTIONS = {
    "--run": "Run application.",
    "--help": "Display help message.",
    "--reset-settings": "Reset program configuration.",
    "--create-settings": "Create new settings if previous was deleted or renamed.",
    "--version": "Show actual version of application.",
    "--create-theme": "Show dialog for creating own theme.",
    "--clear-logs": "Clear all logs."
}
COMMANDS_ARGS = {
    "--run": "",
    "--help": "<command>",
    "--reset-settings": None,
    "--version": None,
    "--create-settings": None,
    "--create-theme": None,
    "--clear-logs": None
}

# Help menu
def show_help(*args) -> None:
    # Get user input if exists
    raw_input = args[0] if args else None
    
    # 1. Show all commands
    if not raw_input:
        # Align text based on longest command name
        padding = len(max(COMMANDS_DESCRIPTIONS.keys(), key=len))
        
        print("Available commands:")
        for name, desc in COMMANDS_DESCRIPTIONS.items():
            print(f"  {name:<{padding}}  {desc}")
        return

    # 2. Process specific command
    # Remove dashes to normalize input
    clean_name = raw_input.lstrip("-")
    cmd_key = f"--{clean_name}"

    # 3. Validation
    if cmd_key not in commands:
        print(f"Error: Unknown command '{clean_name}'.")
        return

    # 4. Show detail
    cmd_args = COMMANDS_ARGS.get(cmd_key, "")
    description = COMMANDS_DESCRIPTIONS.get(cmd_key, "No description.")

    # Only add space if there are arguments
    args_display = f" {cmd_args}" if cmd_args else ""

    print(f"Usage: python3 main.py {cmd_key}{args_display}")
    print(f"Description: {description}")

# Version function
def show_version(*args) -> None:
    # Import tools to check system
    import platform
    import PySide6 # type: ignore
    
    # 1. Show app version
    print(f"WebScope v{app.version}")
    
    # 2. Show system info for debugging
    print(f"Python {platform.python_version()}")
    print(f"PySide6 {PySide6.__version__}")

# Reset settings function
def resetSettings(*args) -> None:
    # Reset settings
    ConfigManager().resetSettings()

# Create configuration
def createSettings(*args) -> None:
    # Create settings file
    ConfigManager()._checkConfigFile()

# TODO: Create theme
def createTheme(*args) -> None:
    # Init theme creator
    ThemeCreator().exec()

# Clear logs
def clearLogs()-> None:
    # Clear
    Logger.clearLogs()

commands = {
    "--run": None,
    "--help": show_help,
    "--reset-settings": resetSettings,
    "--create-settings": createSettings,
    "--version": show_version,
    "--create-theme": createTheme,
    "--clear-logs": clearLogs
}