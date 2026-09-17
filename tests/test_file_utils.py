from pathlib import Path
import pytest
from utils.file_utils import validate_input, ensure_dir

def test_validate_input(tmp_path):
    p = tmp_path / "sample.txt"
    p.write_text("hello")
    assert validate_input(p) == p

def test_validate_missing_input(tmp_path):
    with pytest.raises(FileNotFoundError):
        validate_input(tmp_path / "missing.txt")

def test_ensure_dir(tmp_path):
    p = ensure_dir(tmp_path / "new")
    assert p.exists()
