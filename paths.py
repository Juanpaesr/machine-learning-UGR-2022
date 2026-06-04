"""Shared path configuration for ML notebooks (local + Colab)."""
import sys
from pathlib import Path


def find_project_root():
    candidates = [Path.cwd(), *Path.cwd().parents]
    try:
        from google.colab import drive  # noqa: F401

        candidates = [
            Path("/content/drive/MyDrive/AA"),
            Path("/content/drive/My Drive/AA"),
            Path("/content/AA"),
            *candidates,
        ]
    except ImportError:
        pass

    for p in candidates:
        if (p / "data").is_dir() and any(p.glob("P*.ipynb")):
            return p.resolve()
    return Path.cwd().resolve()


ROOT = find_project_root()
DATA_DIR = ROOT / "data"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def get_data(filename: str) -> str:
    return str(DATA_DIR / filename.replace("\\", "/"))
