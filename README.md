# startup
To play and memorize

Hi All,

these are the very first steps ...

## File Selector Widget for Jupyter Notebooks

This repository includes a file selector widget that allows you to browse and select files directly within Jupyter notebooks.

### Features

- 📁 Browse directories starting from the current directory
- 📄 Select any file from the file system
- 🔼 Navigate up to parent directories
- 🐧 Optimized for Linux (Ubuntu) systems
- ✨ User-friendly interface with visual indicators

### Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install ipywidgets jupyter
```

### Quick Start

```python
from file_selector import create_file_selector

# Create and display the file selector
selector = create_file_selector()

# After selecting a file, retrieve the path
selected_file = selector.get_selected()
print(f"Selected: {selected_file}")
```

### Example Notebook

See `file_selector_example.ipynb` for a complete working example with detailed usage instructions.

### Usage in Jupyter

1. Import the module: `from file_selector import create_file_selector`
2. Create a selector: `selector = create_file_selector()`
3. Use the widget to navigate and select files
4. Retrieve the selection: `selected_file = selector.get_selected()`

The file selector will display:
- Folders with 📁 icon (click to navigate)
- Files with 📄 icon (click to select)
- A "Parent Directory" button to go up one level
- A "Select File" button to confirm your selection
