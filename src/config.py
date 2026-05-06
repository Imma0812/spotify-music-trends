"""Constantes du projet : chemins et liste des features audio."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# slug du dataset Kaggle utilise par defaut
DATASET_SLUG = "maharshipandya/-spotify-tracks-dataset"
RAW_CSV_NAME = "dataset.csv"

# colonnes audio fournies par Spotify
AUDIO_FEATURES = [
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo",
]

# sous-ensemble utilise pour les radars (echelles 0-1)
RADAR_FEATURES = [
    "danceability",
    "energy",
    "valence",
    "acousticness",
    "speechiness",
    "liveness",
]
