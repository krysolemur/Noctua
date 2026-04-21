# Commands.py

CLI_COMMANDS = ["--help", "--version", "--reset-settings", "--clear-logs"]
GUI_COMMANDS = ["--run", "--theme-creator", "--style-creator"]
ALL_COMMANDS = ["run", "help", "reset-settings", "version", "--clear-logs", "--theme-creator", "--style-creator"]
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
    from Application.Application import Application as app
    import platform
    import PySide6 # type: ignore
    
    # 1. Show app version
    print(f"WebScope v{app.version}")
    
    # 2. Show system info for debugging
    print(f"Python {platform.python_version()}")
    print(f"PySide6 {PySide6.__version__}")

# Reset settings function
def reset_settings(*args) -> None:
    # 1. Import manager locally
    from Application.ConfigManager.ConfigManager import ConfigManager 
    
    # 2. Perform reset
    ConfigManager().reset_settings()
    
    # 3. Give feedback to user
    print("Settings have been reset to default values.")

# Create theme
def create_theme(*args) -> None:
    # Import theme manager
    from Application.ThemeManager.ThemesManager import ThemesManager

    # Init theme creator
    ThemesManager.create_theme()

# Create style
def create_style(*args) -> None:
    # Import style manager
    from Application.StyleManager.StyleManager import StyleManager

    # Init theme creator
    StyleManager.create_sheet()

# Clear logs
def clear_logs()-> None:
    # Import 
    from Application.Logger.Logger import Logger

    # Clear
    Logger.clear_logs()

commands = {
    "--run": "",
    "--help": show_help,
    "--reset-settings": reset_settings,
    "--version": show_version,
    "--theme-creator": create_theme,
    "--style-creator": create_style,
    "--clear-logs": clear_logs
}