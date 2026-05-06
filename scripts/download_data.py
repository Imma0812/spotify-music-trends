"""Script CLI pour telecharger le dataset Kaggle."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_loader import download_dataset


def main() -> None:
    path = download_dataset()
    print(f"dataset disponible : {path}")


if __name__ == "__main__":
    main()
