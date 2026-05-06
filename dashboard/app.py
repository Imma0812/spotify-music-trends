"""Dashboard Streamlit : Spotify Music Trends."""
from __future__ import annotations

import sys
from pathlib import Path

# rend le package src importable depuis ce sous-dossier
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.analysis import (
    compare_genres,
    correlation_matrix,
    quick_stats,
    top_genres,
    top_tracks,
)
from src.config import AUDIO_FEATURES, RADAR_FEATURES
from src.data_loader import load_dataset
from src.transform import clean


st.set_page_config(
    page_title="Spotify Music Trends",
    layout="wide",
)


@st.cache_data(show_spinner="Chargement du dataset...")
def get_data() -> pd.DataFrame:
    return clean(load_dataset())


df = get_data()

st.title("Spotify Music Trends")
st.caption(
    "Analyse de plus de 100 000 morceaux Spotify et de leurs caracteristiques audio."
)

# ------------------------------ sidebar ------------------------------
st.sidebar.header("Filtres")
genres_all = sorted(df["track_genre"].unique())
default_genres = [g for g in ["pop", "rock", "jazz"] if g in genres_all] or genres_all[:3]

selected_genres = st.sidebar.multiselect(
    "Genres a comparer (radar)",
    options=genres_all,
    default=default_genres,
)
min_pop = st.sidebar.slider("Popularite minimale", 0, 100, 0)
df_view = df[df["popularity"] >= min_pop]

# ------------------------------ kpis ---------------------------------
stats = quick_stats(df_view)
c1, c2, c3, c4 = st.columns(4)
c1.metric("Morceaux", f"{stats['tracks']:,}".replace(",", " "))
c2.metric("Artistes", f"{stats['artists']:,}".replace(",", " "))
c3.metric("Genres", stats["genres"])
c4.metric("Duree moyenne", f"{stats['avg_duration_min']:.1f} min")

st.divider()

# ------------------------------ top genres ---------------------------
st.subheader("Top genres par popularite moyenne")
top = top_genres(df_view, n=15)
fig_top = px.bar(
    top,
    x="popularite_moyenne",
    y="track_genre",
    orientation="h",
    text="popularite_moyenne",
)
fig_top.update_layout(yaxis={"categoryorder": "total ascending"}, margin=dict(l=10, r=10, t=10, b=10))
fig_top.update_traces(texttemplate="%{text:.1f}", textposition="outside")
st.plotly_chart(fig_top, use_container_width=True)

# ------------------------------ comparateur radar --------------------
st.subheader("Comparateur de genres (features audio)")
if selected_genres:
    comp = compare_genres(df_view, selected_genres)
    feats = [f for f in RADAR_FEATURES if f in comp.columns]
    radar_fig = go.Figure()
    for _, row in comp.iterrows():
        radar_fig.add_trace(
            go.Scatterpolar(
                r=[row[f] for f in feats],
                theta=feats,
                fill="toself",
                name=row["track_genre"],
            )
        )
    radar_fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        margin=dict(l=10, r=10, t=10, b=10),
    )
    st.plotly_chart(radar_fig, use_container_width=True)
else:
    st.info("Selectionne au moins un genre dans la barre laterale.")

# ------------------------------ correlations -------------------------
st.subheader("Correlations entre features audio")
corr = correlation_matrix(df_view)
fig_corr = px.imshow(
    corr,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
)
fig_corr.update_layout(margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_corr, use_container_width=True)

# ------------------------------ distribution -------------------------
st.subheader("Distribution d une feature audio")
feat = st.selectbox("Feature", AUDIO_FEATURES, index=0)
fig_dist = px.histogram(df_view, x=feat, nbins=60)
fig_dist.update_layout(margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_dist, use_container_width=True)

# ------------------------------ top tracks ---------------------------
st.subheader("Top 20 morceaux les plus populaires")
st.dataframe(top_tracks(df_view, n=20), use_container_width=True, hide_index=True)
