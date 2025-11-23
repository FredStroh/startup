#!/usr/bin/env python
"""
File selector widget for Jupyter notebooks using ipywidgets.
This module provides a simple file selection interface that starts in the current directory
and displays all files for selection. Optimized for Linux (Ubuntu) systems.
"""

import os
from pathlib import Path
import ipywidgets as widgets
from IPython.display import display


class FileSelector:
    """
    A file selector widget for Jupyter notebooks.
    
    This widget allows users to browse and select files from the file system.
    It starts in the current directory and displays all files and folders.
    
    Attributes:
        current_path (Path): Current directory path
        selected_file (str): Path of the selected file
    """
    
    def __init__(self, start_path=None):
        """
        Initialize the file selector.
        
        Args:
            start_path (str, optional): Starting directory path. Defaults to current directory.
        """
        self.current_path = Path(start_path) if start_path else Path.cwd()
        self.selected_file = None
        
        # Create widgets
        self.path_label = widgets.Label(value=f"Current path: {self.current_path}")
        self.file_list = widgets.Select(
            options=[],
            description='Files:',
            disabled=False,
            layout=widgets.Layout(width='80%', height='300px')
        )
        self.select_button = widgets.Button(
            description='Select File',
            button_style='success',
            tooltip='Select the highlighted file',
            icon='check'
        )
        self.parent_button = widgets.Button(
            description='Parent Directory',
            button_style='info',
            tooltip='Go to parent directory',
            icon='arrow-up'
        )
        self.output = widgets.Output()
        
        # Set up event handlers
        self.file_list.observe(self._on_item_selected, names='value')
        self.select_button.on_click(self._on_select_clicked)
        self.parent_button.on_click(self._on_parent_clicked)
        
        # Populate initial file list
        self._update_file_list()
        
        # Create layout
        self.container = widgets.VBox([
            self.path_label,
            widgets.HBox([self.parent_button]),
            self.file_list,
            self.select_button,
            self.output
        ])
    
    def _update_file_list(self):
        """Update the file list with contents of current directory."""
        try:
            # Get all items in current directory
            items = []
            
            # Add directories first (with / suffix)
            for item in sorted(self.current_path.iterdir()):
                if item.is_dir():
                    items.append(f"📁 {item.name}/")
                elif item.is_file():
                    items.append(f"📄 {item.name}")
            
            self.file_list.options = items
            self.path_label.value = f"Current path: {self.current_path}"
            
        except PermissionError:
            with self.output:
                print(f"Permission denied: {self.current_path}")
    
    def _on_item_selected(self, change):
        """Handle item selection in the file list."""
        if change['new']:
            selected_item = change['new']
            # Remove emoji prefix
            item_name = selected_item.split(' ', 1)[1] if ' ' in selected_item else selected_item
            item_path = self.current_path / item_name.rstrip('/')
            
            # If it's a directory, navigate into it
            if selected_item.startswith('📁'):
                self.current_path = item_path
                self._update_file_list()
    
    def _on_select_clicked(self, button):
        """Handle the select button click."""
        if self.file_list.value:
            selected_item = self.file_list.value
            # Remove emoji prefix
            item_name = selected_item.split(' ', 1)[1] if ' ' in selected_item else selected_item
            item_path = self.current_path / item_name.rstrip('/')
            
            if item_path.is_file():
                self.selected_file = str(item_path)
                with self.output:
                    self.output.clear_output()
                    print(f"✓ Selected file: {self.selected_file}")
            else:
                with self.output:
                    self.output.clear_output()
                    print("⚠ Please select a file, not a directory")
    
    def _on_parent_clicked(self, button):
        """Handle the parent directory button click."""
        parent = self.current_path.parent
        if parent != self.current_path:  # Check we're not at root
            self.current_path = parent
            self._update_file_list()
    
    def display(self):
        """Display the file selector widget."""
        display(self.container)
    
    def get_selected(self):
        """
        Get the path of the selected file.
        
        Returns:
            str: Path of the selected file, or None if no file is selected.
        """
        return self.selected_file


def create_file_selector(start_path=None):
    """
    Create and display a file selector widget.
    
    This is a convenience function to quickly create and display a file selector.
    
    Args:
        start_path (str, optional): Starting directory path. Defaults to current directory.
    
    Returns:
        FileSelector: The created file selector instance.
    
    Example:
        >>> selector = create_file_selector()
        >>> # After user selects a file
        >>> selected_file = selector.get_selected()
        >>> print(f"You selected: {selected_file}")
    """
    selector = FileSelector(start_path=start_path)
    selector.display()
    return selector


if __name__ == "__main__":
    print("This module is designed to be used in Jupyter notebooks.")
    print("Import it and use create_file_selector() to create a file selector widget.")
