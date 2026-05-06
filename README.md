# Spotify Music Trends

Analyse de **+100 000 morceaux Spotify** et de leurs caracteristiques audio. Le projet repond a une question simple : **qu est-ce qui differencie un genre musical d un autre du point de vue des donnees ?**

Pipeline complet : ingestion Kaggle, nettoyage, agregations, dashboard interactif.

## Architecture

```
Kaggle dataset
     |
     v
[ data_loader.py ]  ->  data/raw/dataset.csv
     |
     v
[ transform.py ]    ->  DataFrame nettoye (cache Streamlit)
     |
     v
[ analysis.py ]     ->  agregations metiers
     |
     v
[ dashboard/app.py ] (Streamlit)  +  notebooks/exploration.ipynb
```

## Stack

- Python 3.10+
- pandas, numpy
- plotly
- streamlit
- kaggle (telechargement dataset)
- python-dotenv

## Structure

```
spotify-music-trends/
|-- src/
|   |-- config.py         # chemins, constantes
|   |-- data_loader.py    # download + load Kaggle
|   |-- transform.py      # nettoyage
|   `-- analysis.py       # fonctions d agregation
|-- dashboard/
|   `-- app.py            # appli Streamlit
|-- scripts/
|   `-- download_data.py  # CLI de download
|-- notebooks/
|   `-- exploration.ipynb # EDA
|-- data/                 # csv brut + processed (ignore par git)
|-- requirements.txt
|-- .env.example
`-- README.md
```

## Installation

```bash
git clone https://github.com/Imma0812/spotify-music-trends.git
cd spotify-music-trends

python -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate            # Windows

pip install -r requirements.txt
```

## Configuration des credentials Kaggle

Le dataset est telecharge automatiquement via l API Kaggle. Deux options :

**Option A (recommandee) : fichier kaggle.json**
1. Va sur https://www.kaggle.com/settings -> *Create New Token*
2. Place le fichier telecharge dans `~/.kaggle/kaggle.json`
3. Sur macOS / Linux : `chmod 600 ~/.kaggle/kaggle.json`

**Option B : variables d environnement**

```bash
cp .env.example .env
# edite .env et renseigne KAGGLE_USERNAME et KAGGLE_KEY
```

## Usage

### Telecharger le dataset

```bash
python scripts/download_data.py
```

Le csv est ecrit dans `data/raw/dataset.csv` (~25 Mo).

### Lancer le dashboard

```bash
streamlit run dashboard/app.py
```

Le dashboard est dispo sur http://localhost:8501.

### Ouvrir le notebook d exploration

```bash
jupyter notebook notebooks/exploration.ipynb
```

## Ce que montre le dashboard

- **KPIs** : nombre de morceaux, d artistes, de genres, duree moyenne
- **Top 15 genres** par popularite moyenne
- **Comparateur de genres** (radar des features audio)
- **Matrice de correlation** entre features audio + popularite
- **Distribution** d une feature audio au choix
- **Top 20 morceaux** les plus populaires

## Dataset

[Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) - Maharshi Pandya, Kaggle.

114 000 morceaux, 125 genres, 20 colonnes dont les features audio Spotify (danceability, energy, valence, tempo, etc.).

## Licence

MIT
