"""Project paths relative to this file."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = PROJECT_ROOT / "data" / "raw"
CLEANED_DIR = PROJECT_ROOT / "data" / "cleaned"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
