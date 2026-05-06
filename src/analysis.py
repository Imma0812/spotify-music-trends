"""Fonctions d agregation pour le dashboard et les notebooks."""
from __future__ import annotations

import pandas as pd

from src.config import AUDIO_FEATURES


def top_genres(df: pd.DataFrame, n: int = 15) -> pd.DataFrame:
    """Top n genres par popularite moyenne."""
    return (
        df.groupby("track_genre")["popularity"]
        .mean()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
        .rename(columns={"popularity": "popularite_moyenne"})
    )


def top_tracks(df: pd.DataFrame, n: int = 20) -> pd.DataFrame:
    """Les n morceaux les plus populaires."""
    cols = ["track_name", "artists", "track_genre", "popularity"]
    return df.sort_values("popularity", ascending=False).head(n)[cols].reset_index(drop=True)


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Matrice de correlation entre features audio et popularite."""
    cols = [c for c in AUDIO_FEATURES if c in df.columns] + ["popularity"]
    return df[cols].corr()


def compare_genres(df: pd.DataFrame, genres: list[str]) -> pd.DataFrame:
    """Moyenne des features audio pour les genres choisis."""
    sub = df[df["track_genre"].isin(genres)]
    cols = [c for c in AUDIO_FEATURES if c in sub.columns]
    return sub.groupby("track_genre")[cols].mean().reset_index()


def quick_stats(df: pd.DataFrame) -> dict:
    """Statistiques rapides pour les KPI du dashboard."""
    return {
        "tracks": len(df),
        "artists": df["artists"].nunique(),
        "genres": df["track_genre"].nunique(),
        "avg_duration_min": float(df["duration_min"].mean()),
        "avg_popularity": float(df["popularity"].mean()),
    }
