#!/usr/bin/env python
"""
Simple tests for the file selector widget.
"""

import os
import sys
from pathlib import Path
from file_selector import FileSelector, create_file_selector


def test_file_selector_initialization():
    """Test FileSelector initialization."""
    selector = FileSelector()
    assert selector.current_path == Path.cwd(), "Should start in current directory"
    assert selector.selected_file is None, "Should have no file selected initially"
    print("✓ Initialization test passed")


def test_file_selector_with_custom_path():
    """Test FileSelector with custom start path."""
    test_path = "/tmp"
    selector = FileSelector(start_path=test_path)
    assert selector.current_path == Path(test_path), f"Should start in {test_path}"
    print("✓ Custom path test passed")


def test_file_selector_widgets_exist():
    """Test that all widgets are created."""
    selector = FileSelector()
    assert selector.path_label is not None, "Path label should exist"
    assert selector.file_list is not None, "File list should exist"
    assert selector.select_button is not None, "Select button should exist"
    assert selector.parent_button is not None, "Parent button should exist"
    assert selector.output is not None, "Output widget should exist"
    assert selector.container is not None, "Container should exist"
    print("✓ Widget creation test passed")


def test_create_file_selector_function():
    """Test the convenience function."""
    selector = create_file_selector()
    assert isinstance(selector, FileSelector), "Should return FileSelector instance"
    assert selector.current_path == Path.cwd(), "Should start in current directory"
    print("✓ Convenience function test passed")


def test_get_selected_returns_none_initially():
    """Test get_selected returns None when no file is selected."""
    selector = FileSelector()
    assert selector.get_selected() is None, "Should return None when no file selected"
    print("✓ Get selected initial state test passed")


def test_invalid_path_raises_error():
    """Test that invalid path raises ValueError."""
    try:
        selector = FileSelector(start_path="/nonexistent/path/that/does/not/exist")
        print("❌ Should have raised ValueError for nonexistent path")
        return False
    except ValueError as e:
        assert "does not exist" in str(e).lower(), "Error message should mention path doesn't exist"
        print("✓ Invalid path validation test passed")
        return True


def test_file_path_raises_error():
    """Test that file path (not directory) raises ValueError."""
    # Create a temporary file
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        temp_file = tf.name
    
    try:
        try:
            selector = FileSelector(start_path=temp_file)
            print("❌ Should have raised ValueError for file path")
            return False
        except ValueError as e:
            assert "not a directory" in str(e).lower(), "Error message should mention it's not a directory"
            print("✓ File path validation test passed")
            return True
    finally:
        # Clean up
        if os.path.exists(temp_file):
            os.unlink(temp_file)


def run_tests():
    """Run all tests."""
    print("Running file selector tests...\n")
    
    try:
        test_file_selector_initialization()
        test_file_selector_with_custom_path()
        test_file_selector_widgets_exist()
        test_create_file_selector_function()
        test_get_selected_returns_none_initially()
        
        # Validation tests
        if not test_invalid_path_raises_error():
            return 1
        if not test_file_path_raises_error():
            return 1
        
        print("\n✅ All tests passed!")
        return 0
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(run_tests())
