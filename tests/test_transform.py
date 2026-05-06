"""Tests unitaires sur le module de nettoyage."""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.transform import clean, features_by_genre


def _fake_df(n: int = 50) -> pd.DataFrame:
    rng = np.random.default_rng(0)
    return pd.DataFrame(
        {
            "Unnamed: 0": range(n),
            "track_id": [f"t{i}" for i in range(n)],
            "artists": ["A"] * n,
            "album_name": ["alb"] * n,
            "track_name": ["t"] * n,
            "popularity": rng.integers(0, 100, n),
            "duration_ms": rng.integers(60_000, 400_000, n),
            "explicit": rng.choice([True, False], n),
            "danceability": rng.random(n),
            "energy": rng.random(n),
            "loudness": rng.uniform(-30, 0, n),
            "speechiness": rng.random(n),
            "acousticness": rng.random(n),
            "instrumentalness": rng.random(n),
            "liveness": rng.random(n),
            "valence": rng.random(n),
            "tempo": rng.uniform(60, 200, n),
            "mode": rng.choice([0, 1], n),
            "key": rng.integers(0, 12, n),
            "time_signature": rng.choice([3, 4, 5], n),
            "track_genre": rng.choice(["pop", "rock", "jazz"], n),
        }
    )


def test_clean_drops_unnamed_column() -> None:
    df = clean(_fake_df())
    assert "Unnamed: 0" not in df.columns


def test_clean_adds_duration_min() -> None:
    df = clean(_fake_df())
    assert "duration_min" in df.columns
    assert (df["duration_min"] > 0).all()


def test_clean_normalizes_genre_case() -> None:
    raw = _fake_df()
    raw.loc[0, "track_genre"] = "POP "
    df = clean(raw)
    assert df["track_genre"].str.islower().all()


def test_features_by_genre_columns() -> None:
    df = clean(_fake_df())
    grouped = features_by_genre(df)
    for col in ["track_genre", "danceability", "energy", "popularity", "track_count"]:
        assert col in grouped.columns
