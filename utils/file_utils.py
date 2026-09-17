from pathlib import Path


def ensure_dir(path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def validate_input(path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file does not exist: {p}")
    if not p.is_file():
        raise ValueError(f"Input path is not a file: {p}")
    return p
