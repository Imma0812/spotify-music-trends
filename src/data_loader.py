"""Telechargement et chargement du dataset Spotify."""
from __future__ import annotations

import shutil
from pathlib import Path

import pandas as pd

from src.config import DATASET_SLUG, RAW_CSV_NAME, RAW_DIR


def _load_env() -> None:
    # charge le .env du projet pour exposer KAGGLE_USERNAME / KAGGLE_KEY
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        try:
            from dotenv import load_dotenv

            load_dotenv(env_path)
        except ImportError:
            pass


def download_dataset() -> Path:
    """Telecharge le dataset si absent et retourne le chemin du csv."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    target = RAW_DIR / RAW_CSV_NAME
    if target.exists():
        return target

    _load_env()

    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError as exc:
        raise RuntimeError(
            "Le package kaggle n est pas installe. "
            "Lance `pip install -r requirements.txt`."
        ) from exc

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(DATASET_SLUG, path=str(RAW_DIR), unzip=True)

    # certains datasets posent leur csv dans un sous-dossier
    if not target.exists():
        candidates = list(RAW_DIR.rglob("*.csv"))
        if not candidates:
            raise FileNotFoundError(
                f"Aucun csv trouve apres le telechargement dans {RAW_DIR}"
            )
        shutil.move(str(candidates[0]), target)

    return target


def load_dataset() -> pd.DataFrame:
    """Charge le csv brut, le telecharge si besoin."""
    path = RAW_DIR / RAW_CSV_NAME
    if not path.exists():
        path = download_dataset()
    return pd.read_csv(path)
