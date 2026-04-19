# ThemeCreator.py

# Importing system files
from pathlib import Path
import importlib.util
import re
import json
import os

from PySide6.QtWidgets import QDialog, QColorDialog, QMessageBox, QFileDialog # type: ignore
from PySide6.QtGui import QColor, QPalette, QIcon, QPixmap # type: ignore
from PySide6.QtCore import Qt # type: ignore

from Application.QtFiles.ThemeCreator import Ui_ThemeCreator
from Application.QtFiles.ThemePreview import Ui_ThemePreview

# Main class ThemeCreator
class ThemeCreator(QDialog):
        
    # Constructor
    def __init__(self) -> None:
        
        # Init parents
        super().__init__()

        # Color Role mapping
        self.roleMapping = {
            "Window": QPalette.ColorRole.Window,
            "WindowText": QPalette.ColorRole.WindowText,
            "Base": QPalette.ColorRole.Base,
            "AlternateBase": QPalette.ColorRole.AlternateBase,
            "Text": QPalette.ColorRole.Text,
            "Button": QPalette.ColorRole.Button,
            "ButtonText": QPalette.ColorRole.ButtonText,
            "BrightText": QPalette.ColorRole.BrightText,
            "Light": QPalette.ColorRole.Light,
            "Midlight": QPalette.ColorRole.Midlight,
            "Dark": QPalette.ColorRole.Dark,
            "Mid": QPalette.ColorRole.Mid,
            "Shadow": QPalette.ColorRole.Shadow,
            "Highlight": QPalette.ColorRole.Highlight,
            "HighlightedText": QPalette.ColorRole.HighlightedText,
            "Link": QPalette.ColorRole.Link,
            "LinkVisited": QPalette.ColorRole.LinkVisited,
            "PlaceholderText": QPalette.ColorRole.PlaceholderText,
            "ToolTipBase": QPalette.ColorRole.ToolTipBase,
            "ToolTipText": QPalette.ColorRole.ToolTipText
        }

        # Create empty default palette
        self.custom_theme = {
            "Active": {}, 
            "Inactive": {},
            "Disabled": {}
        }

        # Preview window
        self.previewWindow = None

        # Load Ui
        self.ui = Ui_ThemeCreator()
        
        # Setup ui
        self.ui.setupUi(self)

        # Actions
        self.ui.btn_full_preview.clicked.connect(self._show_preview)
        self.ui.btn_set_color.clicked.connect(self._color_picker)
        self.ui.cb_state.currentIndexChanged.connect(self._update_table)
        self.ui.btn_reset.clicked.connect(self._reset_role)
        self.ui.btn_export.clicked.connect(self._export_theme)
        self.ui.btn_import.clicked.connect(self._import_theme)

    # Make icon function
    def _make_icon(self, color: QColor) -> QIcon:
        pixmap = QPixmap(24, 14)
        pixmap.fill(color)

        # Return pixmap as icon
        return QIcon(pixmap)

    # Pick color function
    def _color_picker(self) -> None:
        # Get selected item
        selectedItem = self.ui.tw_palette_roles.selectedItems()

        # Checkk selected
        if not selectedItem:
            return
        
        item = selectedItem[0]
        roleName = item.text(0)
        currentState = self.ui.cb_state.currentText().split(" ")[0]

        currentHex = item.text(1)
        initialColor = QColor(currentHex) if currentHex else QColor(Qt.GlobalColor.white)

        color = QColorDialog.getColor(initialColor, self, f"Pick Color for {roleName} ({currentState})")

        # Check if color is valid
        if color.isValid():
            # Get new color
            newHex = color.name().upper()
            
            self.custom_theme[currentState][roleName] = color
            
            # Actualize Ui of table
            item.setText(1, newHex) 
            item.setIcon(2, self._make_icon(color))

            # Apply to preview
            self._apply_to_preview()
            
    # Update table
    def _update_table(self) -> None:
        # Get current state
        currentState = self.ui.cb_state.currentText().split(" ")[0]

        # Get root
        root = self.ui.tw_palette_roles.invisibleRootItem()

        # Block updating
        self.ui.tw_palette_roles.setUpdatesEnabled(False)

        # Browse all childs
        for i in range(root.childCount()):
            # Get item
            item = root.child(i)
            
            # Get role name
            roleName = item.text(0)
            
            # Get roleName
            if roleName in self.custom_theme[currentState]:
                # Get color
                color = self.custom_theme[currentState][roleName]

                # Set text from color name
                item.setText(1, color.name().upper())

                # Set icon
                item.setIcon(2, self._make_icon(color))
            else:
                # Set none text
                item.setText(1, "")

                # Set none icon
                item.setIcon(2, QIcon())

        # Update preview
        self._apply_to_preview

        # Cancle block updating
        self.ui.tw_palette_roles.setUpdatesEnabled(True)

    # Reset role function
    def _reset_role(self) -> None:
        # Get selected
        selectedItem = self.ui.tw_palette_roles.selectedItems()

        # Check selected
        if not selectedItem:
            return

        # Get item
        item = selectedItem[0]

        # Get role name
        roleName = item.text(0)
        
        # Get current state
        currentState = self.ui.cb_state.currentText().split(" ")[0]


        # Removing from data structure
        if roleName in self.custom_theme[currentState]:
            # Remove
            del self.custom_theme[currentState][roleName]

        # Clear table
        item.setText(1, "")           

        # Icon
        item.setIcon(2, QIcon()) 
        
        # Actualize preview
        self._apply_to_preview()

    # Applying to preview
    def _apply_to_preview(self) -> None:
        # Check if it has that atribute
        if hasattr(self, 'previewWindow') and self.previewWindow is not None:
            # Set palette
            self.previewWindow.setPalette(self._build_palette())

    # Building palette
    def _build_palette(self) -> QPalette:
        # Create new palette
        palette = QPalette()
        
        # Set state map
        stateMap = {
            "Active": QPalette.ColorGroup.Active,
            "Inactive": QPalette.ColorGroup.Inactive,
            "Disabled": QPalette.ColorGroup.Disabled
        }
        
        # Browse all states names and roles
        for stateName, roles in self.custom_theme.items():
            # Get group
            group = stateMap[stateName]

            # Browse all role name and their colors
            for roleName, color in roles.items():
                # If is role name in mapping
                if roleName in self.roleMapping:
                    # Set color
                    palette.setColor(group, self.roleMapping[roleName], color)
        
        # Return palette
        return palette
    
    # Show preview function
    def _show_preview(self) -> None:
        # Check if window exists
        if not hasattr(self, 'previewWindow') or self.previewWindow is None:
            try:
                # Create dialog
                self.previewWindow = QDialog(self)

                # Load ui
                self.previewUi = Ui_ThemePreview()

                # Setup ui
                self.previewUi.setupUi(self.previewWindow)
            except Exception as e:
                # Show error
                QMessageBox.critical(self, "Error", f"Could not load Preview Dialog: {e}")
                return

        # Create current palette
        currentPalette = self._build_palette()

        # Apply palette
        # Teď už voláme setPalette na QDialog, který tuto metodu má
        self.previewWindow.setPalette(currentPalette)
        
        # Repain preview
        self.previewWindow.update()

        # Show window is its hiden
        if not self.previewWindow.isVisible():
            self.previewWindow.show()
        else:
            # If is open, just raise it and set as active window
            self.previewWindow.raise_()
            self.previewWindow.activateWindow()

    # Import method
    def _import_theme(self) -> None:
        # Open file dialog and return path
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Import theme",
            "resources/Themes", 
            "JSON File (*.json);;Qt Stylesheet (*.qss);;Python Dict (*.py)"
        )

        # Check file path
        if not file_path:
            return

        # Get type
        _, extension = os.path.splitext(file_path)
        type = extension.lower()

        try:
            if "json" in type:
                self._import_from_json(file_path)
            elif "qss" in type:
                self._import_from_qss(file_path)
            elif "py" in type:
                self._import_from_py(file_path)
        except Exception as e:
            print(e)

        # Reset table
        self._update_table()

        # Update preview
        self._apply_to_preview()

    # Import from *.json
    def _import_from_json(self, file_path) -> None:
        # Open file
        with open(file_path, "r") as theme:
            exported_data = json.load(theme)

        # Groups
        for group, roles in exported_data.items():
            # Check existing group
            if group in self.custom_theme:
                for role, hex_color in roles.items():
                    # Parse color back to QColor
                    self.custom_theme[group][role] = QColor(hex_color)

        # Build new palette
        self._build_palette()

    # Import from *.qss
    def _import_from_qss(self, file_path) -> None:
        # Open file
        with open(file_path, "r") as theme:
            exported_data = theme.read()

        # Pattern
        pattern = r'qproperty-(active|inactive|disabled)-([\w-]+):\s*(#[a-fA-F0-9]{6});'

        # Find patterns
        matches = re.findall(pattern, exported_data)

        # Check matches
        if not matches:
            return

        # Browse groups, roles and colors in matches
        for group_raw, role, hex_color in matches:
            # Get group
            group = group_raw.capitalize()
            
            # Set it to custom theme
            self.custom_theme[group][role] = QColor(hex_color)

        # Build palette
        self._build_palette()

    # Import from *.py
    def _import_from_py(self, file_path) -> None:
        # Preparing dynamic imort
        file_path = Path(file_path)

        # Module name without type
        module_name = file_path.stem 

        # Create path for import
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        theme_module = importlib.util.module_from_spec(spec)
        
        # Run module
        spec.loader.exec_module(theme_module)

        # Check if module has THEME_DATA
        if hasattr(theme_module, "THEME_DATA"):
            # Load data
            data = theme_module.THEME_DATA
            
            # Load like from json
            for group_name, roles in data.items():
                # Normalize group 
                group = group_name.capitalize()

                # Role name and color
                for role_name, hex_color in roles.items():
                    self.custom_theme[group][role_name] = QColor(hex_color)

            # 4. Aplikace
            self._build_palette()

    # Export as *.json
    def _export_as_json(self, file_path) -> None:
        # Parsed data
        export_data = {}

        # Groups
        for group, roles in self.custom_theme.items():
            # Empty dict for each group
            export_data[group] = {} 
            
            # Roles and colors
            for role, color in roles.items():
                # Make string from QColor
                hex_color = color.name().upper()
                
                # Save to new dict
                export_data[group][role] = hex_color

        # Open file
        with open(file_path, "w") as theme:
            # Write it 
            json.dump(export_data, theme, indent=4)

    # Export as *.py
    def _export_as_py(self, file_path) -> None:
        # Parsed data
        export_data = {}

        # Groups
        for group, roles in self.custom_theme.items():
            # Empty dict for each group
            export_data[group] = {} 
            
            # Roles and colors
            for role, color in roles.items():
                # Make string from QColor
                hex_color = color.name().upper()
                
                # Save to new dict
                export_data[group][role] = hex_color

        file_content = f"THEME_DATA = {export_data}"

        # Open file
        with open(file_path, "w") as theme:
            # Write it 
            theme.write(file_content)

    # Export as *.qss
    def _export_as_qss(self, file_path) -> None:
        # Line start
        lines = ["#ThemeData {"]
        
        # Groups
        for group, roles in self.custom_theme.items():
            group_name = group.lower()
            # Roles, colors
            for role, color in roles.items():
                hex_val = color.name().upper()
                # Line with property
                lines.append(f"    qproperty-{group_name}-{role}: {hex_val};")
        
        lines.append("}")

        # Create full text
        full_text = "\n".join(lines)

        # Open file
        with open(file_path, "w") as theme:
            theme.write(str(full_text))

    # Save theme method
    def _export_theme(self) -> None:
        # Get decode type
        decode_type = self.ui.cb_format.currentText()

        # Open file dialog and return path
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save theme",
            "resources/Themes/theme", 
            str(decode_type)
        )

        # Close dialog and return empty string
        if not file_path:
            return
        
        # Repair types
        if "(*.json)" in decode_type and not file_path.endswith(".json"):
            file_path += ".json"
        elif "(*.qss)" in decode_type and not file_path.endswith(".qss"):
            file_path += ".qss"
        elif "(*.py)" in decode_type and not file_path.endswith(".py"):
            file_path += ".py"

        try:
            # Check if its is json, python or qss
            if "json" in decode_type:
                self._export_as_json(file_path)
            elif "qss" in decode_type:
                self._export_as_qss(file_path)
            elif "py" in decode_type:
                self._export_as_py(file_path)
        except Exception as e:
            print(e) 