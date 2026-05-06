"""Nettoyage du dataset et preparation pour l analyse."""
from __future__ import annotations

import pandas as pd

from src.config import AUDIO_FEATURES


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie le dataset brut Spotify."""
    df = df.copy()

    # supprime la colonne d index si elle existe
    first = df.columns[0]
    if first.lower().startswith("unnamed"):
        df = df.drop(columns=first)

    df = df.drop_duplicates(subset=["track_id"])
    df = df.dropna(subset=["track_name", "artists", "track_genre"])

    # types
    df["explicit"] = df["explicit"].astype(bool)
    df["popularity"] = df["popularity"].astype(int)
    df["duration_min"] = df["duration_ms"] / 60_000

    # certains genres reviennent en majuscule, on uniformise
    df["track_genre"] = df["track_genre"].str.lower().str.strip()

    return df.reset_index(drop=True)


def features_by_genre(df: pd.DataFrame) -> pd.DataFrame:
    """Moyenne des features audio + popularite par genre."""
    cols = [c for c in AUDIO_FEATURES if c in df.columns]
    grouped = df.groupby("track_genre")[cols].mean()
    grouped["popularity"] = df.groupby("track_genre")["popularity"].mean()
    grouped["track_count"] = df.groupby("track_genre").size()
    return grouped.reset_index().sort_values("popularity", ascending=False)
