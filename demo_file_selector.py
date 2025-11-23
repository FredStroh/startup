#!/usr/bin/env python
"""
Demo script showing the file selector widget structure.
Note: This script demonstrates the widget creation but won't display interactively
outside of a Jupyter notebook environment. Use file_selector_example.ipynb for 
interactive demonstration.
"""

from file_selector import FileSelector, create_file_selector
from pathlib import Path


def main():
    print("=" * 70)
    print("File Selector Widget Demo")
    print("=" * 70)
    print()
    
    # Create a file selector
    print("Creating file selector instance...")
    selector = FileSelector()
    
    print(f"✓ Current directory: {selector.current_path}")
    print(f"✓ Selected file: {selector.selected_file}")
    print()
    
    # Show available files in current directory
    print("Files and directories in current location:")
    print("-" * 70)
    items = []
    for item in sorted(selector.current_path.iterdir()):
        if item.is_dir():
            items.append(f"  📁 {item.name}/")
        elif item.is_file():
            items.append(f"  📄 {item.name}")
    
    for item in items[:10]:  # Show first 10 items
        print(item)
    
    if len(items) > 10:
        print(f"  ... and {len(items) - 10} more items")
    
    print()
    print("=" * 70)
    print("Widget Features:")
    print("=" * 70)
    print("✓ Browse directories with folder icons (📁)")
    print("✓ View files with file icons (📄)")
    print("✓ Navigate to parent directory with button")
    print("✓ Select files with confirmation button")
    print("✓ Visual feedback on selection")
    print()
    print("To use this widget interactively:")
    print("1. Open file_selector_example.ipynb in Jupyter")
    print("2. Run the cells to see the interactive widget")
    print("3. Click on directories to navigate")
    print("4. Click on files and press 'Select File' to choose")
    print()
    print("Or use it programmatically in your notebook:")
    print("  from file_selector import create_file_selector")
    print("  selector = create_file_selector()")
    print("  # ... interact with widget ...")
    print("  selected = selector.get_selected()")
    print()


if __name__ == "__main__":
    main()
