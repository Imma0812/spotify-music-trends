# Briefing Claude - Immaculé KONOU

> Ce document est un briefing structure pour reprendre une conversation avec Claude sans perdre de contexte. Il regroupe profil, projets en cours, decisions techniques, et fichiers livres.
> Date du dernier update : mai 2026.

---

## 1. Identite et positionnement

**Nom** : Mahougnon Siméon Immaculé KONOU
**Pseudo** : Lydia (prenom utilise dans le chat) / Imma0812 (GitHub)
**Email pro** : immaculekonou@gmail.com
**Email Cowork** : lililylygu@gmail.com
**Telephone** : +33 7 48 60 65 45
**Localisation** : Rennes, France (35700)

**Parcours actuel** :
- L3 MIAGE - Universite de Rennes 1 (ISTIC) - depuis sept. 2025
- Admis en M1 *Master Valorisation et Protection des Donnees de l Entreprise* - Universite Paris Cite - rentree sept. 2026

**Recherche** : ALTERNANCE Data a partir de septembre 2026.
Rythme : M1 = 3j ecole / 2j entreprise · M2 = 2j ecole / 3j entreprise.

**Positionnement strategique** :
- Pivot **Dev experimente (4+ ans freelance et entreprise) vers Data Engineering**
- Angle gagnant : "Dev experimente qui pivote Data" plutot que "junior data"
- Cible : Data Engineer / Analytics Engineer junior
- Titre LinkedIn / GitHub :
  `Data Engineering & Analytics · ETL · Pipelines · Analytics Engineering | Python · SQL · PySpark · Power BI | Open to Data Alternance 09/2026`

**Liens publics** :
- GitHub : https://github.com/Imma0812
- LinkedIn : https://www.linkedin.com/in/immaculé-konou/
- Certifications : https://certifs.vercel.app

---

## 2. Stack technique (CV de reference)

### Maitrise

| Domaine | Technos |
|---|---|
| Data, BDD, IA | SQL (PostgreSQL, MySQL, Oracle), MongoDB, Power BI, R, Python (Streamlit, NumPy, Pandas), Matplotlib, Seaborn, Plotly, PySpark, Kafka, PyTorch |
| Frontend | React.js, Next.js, Tailwind, JavaScript ES6+, HTML5/CSS3, Figma |
| Backend | PHP/Symfony, Node.js, API REST |
| Ops | Docker, Git/GitHub, WordPress, LucidChart, UML, SEO |

### En cours d apprentissage (a mentionner sur portfolio)
- dbt-core, Prefect, Airflow, Great Expectations, DuckDB
- TensorFlow, scikit-learn avance, Hugging Face
- BigQuery, Snowflake, AWS (S3, Lambda), Spark Streaming

### Certifications
- Udemy - Data Science avec Python (en cours)
- OpenClassrooms - Python, Power BI, Excel, SQL (en attente)
- freeCodeCamp - Python (en cours)
- Lien : https://certifs.vercel.app

### Langues
- Francais : maternel
- Anglais : intermediaire

### Engagement
- Adjoint au pole academique - Association BIG (Bretagne Information de Gestion), MIAGE Rennes

---

## 3. Repos GitHub existants

| Repo | Description | Categorie |
|---|---|---|
| [ETL-pipeline-e-commerce](https://github.com/Imma0812/ETL-pipeline-e-commerce) | Pipeline ETL Python sur 500k+ transactions e-commerce, RFM | Data |
| [stock-predicator](https://github.com/Imma0812/stock-predicator) | Dashboard prediction boursiere Streamlit | Data |
| [certifs](https://github.com/Imma0812/certifs) | Vitrine Next.js des certifications, deployee sur Vercel | Web |
| [spotify-music-trends](https://github.com/Imma0812/spotify-music-trends) | (a pousser) Analyse 100k+ morceaux Spotify - Streamlit dashboard | Data |
| [crypto-pipeline](https://github.com/Imma0812/crypto-pipeline) | (a pousser) Pipeline ELT moderne CoinGecko + dbt + Metabase | Data |
| [Suivi_depense](https://github.com/Imma0812/Suivi_depense) | Application web suivi de depenses | Web |
| [IQ-master-Quiz](https://github.com/Imma0812/IQ-master-Quiz) | Test de QI interactif React | Web |
| [puissance4_python](https://github.com/Imma0812/puissance4_python) | Jeu Puissance 4 Python | Mini |
| [Morpions.py](https://github.com/Imma0812/Morpions.py) | Jeu Morpion Python | Mini |
| [ChatBot](https://github.com/Imma0812/ChatBot) | Chatbot Python | Mini |

### Projets non publies sur GitHub mais a mentionner
- **AgriChain** : Marketplace agricole Node/React/MongoDB (V2 en cours)
- **Plateforme cadastre** : SIG pour parcelles foncieres (Vue.js, Leaflet, SQL) - Djougou
- **Dashboard LCS** : Outil admin pour ecole, collaboration Nexa SMN
- **App gestion immobiliere** : Type conciergerie, Nantes
- **Systeme reservation Symfony 7** : Algo anti-collision + calendrier interactif
- **Generateur factures Symfony 7** : Service oriente, KnpSnappy
- **Programme analyse de sentiment** : NLP Python

---

## 4. Charte graphique (a respecter sur tous les supports)

- Fond noir : `#0A0A0A`
- Accent orange : `#FF800D`
- Texte blanc : `#FAFAFA`
- Font : Inter (sans-serif), JetBrains Mono (mono)
- Style : sobre, moderne, minimaliste, glassmorphism subtil
- **Aucun emoji** dans le code et les contenus pro
- **Aucun sticker** type IA
- Animations Framer Motion uniquement la ou ca apporte de la valeur (pas partout)

---

## 5. Projets livres pendant les conversations

### 5.1 Projet : `spotify-music-trends`
**Localisation locale** : `~/Documents/spotify-music-trends/`
**Statut** : Code complet, 5/5 tests passent, pret a pousser sur GitHub

**Stack** : Python 3.10+, Pandas, NumPy, Plotly, Streamlit, Kaggle API, python-dotenv

**Architecture** :
```
src/data_loader.py  -> download Kaggle + load CSV
src/transform.py    -> nettoyage du dataset
src/analysis.py     -> agregations metiers
dashboard/app.py    -> Streamlit (KPIs, top genres, radar comparateur, correlations, distributions)
notebooks/exploration.ipynb -> EDA
tests/test_transform.py -> 4 tests unitaires
```

**Dataset** : `maharshipandya/-spotify-tracks-dataset` (Kaggle, 114k tracks, 125 genres)

**Setup local** :
```bash
cd ~/Documents/spotify-music-trends
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# config Kaggle : ~/.kaggle/kaggle.json (Legacy API Key - bouton "Create Legacy API Key" sur kaggle.com/settings)
chmod 600 ~/.kaggle/kaggle.json
python scripts/download_data.py
streamlit run dashboard/app.py
```

**Push GitHub** :
```bash
cd ~/Documents/spotify-music-trends
git init && git add . && git commit -m "init: spotify music trends pipeline + dashboard"
git branch -M main
git remote add origin https://github.com/Imma0812/spotify-music-trends.git
git push -u origin main
```

---

### 5.2 Projet : `crypto-pipeline`
**Localisation locale** : `~/Documents/crypto-pipeline/`
**Statut** : Code complet, 5/5 tests passent, pret a pousser sur GitHub

**Stack moderne (le flagship Data Engineering)** :
- Python + Prefect (ingestion + orchestration)
- PostgreSQL 16 (stockage)
- dbt-core 1.7 (transformations staging -> marts)
- Metabase (visualisation)
- Docker Compose (tout en 1 commande)
- GitHub Actions (CI : pytest + dbt build sur Postgres service)

**Source de donnees** : CoinGecko API (free tier, sans cle, top 100 cryptos)

**Architecture** :
```
CoinGecko -> [Prefect flow] -> PostgreSQL raw.coin_snapshots
                                       v
                                [dbt staging]
                                       v
                                [dbt marts] mart_top_movers, mart_coin_daily, mart_volatility
                                       v
                                  Metabase
```

**Modeles dbt** :
- `stg_coin_snapshots` : view, cast + uppercase symbol + filtre nulls
- `mart_top_movers` : table, top gainers/losers 24h
- `mart_coin_daily` : table, agg journaliere prix/volume
- `mart_volatility` : table, stddev pct_change_24h par coin

**Demarrage** :
```bash
cd ~/Documents/crypto-pipeline
cp .env.example .env
make up                # Postgres + Metabase
make ingest            # premiere ingestion (top 100 cryptos)
make seed              # 6 snapshots espaces de 1 min (historique minimal)
make dbt               # build staging + marts + tests
open http://localhost:3000  # Metabase
```

**Push GitHub** :
```bash
git init && git add . && git commit -m "init: pipeline elt crypto coingecko + dbt + prefect + docker"
git branch -M main
git remote add origin https://github.com/Imma0812/crypto-pipeline.git
git push -u origin main
```

---

### 5.3 Projet : `immacule-portfolio`
**Localisation locale** : `~/Documents/immacule-portfolio/`
**Statut** : Refonte complete, tout pret, prochaine etape = npm install + config Supabase/Resend

**Stack** : Next.js 15 (App Router), Tailwind 3.4, Framer Motion 11, React Hook Form, next-themes, lucide-react, Supabase, Resend

**Sections du site** :
1. Hero (titre + photo + CTA + status alternance)
2. About (parcours + stats + recherche alternance)
3. Skills (2 onglets : Maitrise / En cours d apprentissage)
4. Projects (4 filtres : Tous / Data / Web / Mini - 16 projets reels)
5. Experience (timeline 5 jobs)
6. Certifications (link vers certifs.vercel.app)
7. Contact (formulaire + Supabase log + Resend email)
8. Footer

**Features** :
- FR/EN toggle (i18n custom dans `lib/translations.js`)
- Dark/Light toggle (`next-themes`)
- Header sticky glassmorphism
- Menu mobile responsive
- Compteur de visites (Supabase RPC `increment_visit`)
- Formulaire validation React Hook Form + API route `/api/contact`
- Rate limiting in-memory sur l API contact
- Animations mesurees (entrees de sections + menu mobile uniquement)

**Setup local** :
```bash
cd ~/Documents/immacule-portfolio
npm install
cp .env.local.example .env.local
# remplir Supabase + Resend
npm run dev
```

**Supabase setup** :
1. Creer projet sur supabase.com (free tier)
2. Settings > API : copier URL, anon key, service_role key dans .env.local
3. SQL Editor : coller `supabase/schema.sql` + Run

**Resend setup** :
1. Compte sur resend.com
2. API key -> RESEND_API_KEY
3. RESEND_TO = immaculekonou@gmail.com

**Deploiement Vercel** :
1. Push sur GitHub
2. Vercel > Add Project > Import
3. Coller env vars
4. Deploy

**Fichiers obsoletes a nettoyer manuellement** :
```bash
rm app/components/sections/{TestimonialsSection,ServicesSection,ProcessSection}.js
rm app/components/ui/{TestimonialCard,ServiceCard,SkillCard,Card,ParticleAnimation}.js
rm app/components/layout/Navigation.js
rm app/components/common/SectionWrapper.js
rm hooks/{useFormValidation,useIntersectionObserver,useScrollAnimation}.js
rm utils/{animations,helpers,constants}.js
rm data/{services,testimonials,process}.js
```

---

## 6. README profil GitHub a coller

A coller integralement dans `Imma0812/Imma0812/README.md` (le repo special qui s affiche en haut du profil GitHub) :

```markdown
<h1 align="center">Hello, je suis Siméon Immaculé KONOU 👋</h1>

<p align="center">
  <b>Data Engineering & Analytics · ETL · Data Pipelines · Analytics Engineering</b><br/>
  <code>Python</code> · <code>SQL</code> · <code>PySpark</code> · <code>Power BI</code> · <code>Pandas</code><br/>
  <b>Open to Data Alternance · Septembre 2026</b>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/immaculé-konou/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="mailto:immaculekonou@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  <a href="https://certifs.vercel.app">
    <img src="https://img.shields.io/badge/Certifications-2E8B57?style=for-the-badge&logo=verifiedby&logoColor=white" alt="Certifs"/>
  </a>
</p>

---

## A propos

Je pivote vers la Data Engineering & Analytics : ce qui m interesse, c est la chaine complete de la donnee - de la collecte brute jusqu a la decision business.

> Mon profil hybride Dev + Data est un atout : je ne me contente pas d analyser la donnee, je sais aussi construire les pipelines, les bases et les applications qui la produisent et la consomment.

**Recherche** : alternance Data Engineer / Analytics Engineer a partir de septembre 2026.

---

## Stack technique

### Data, BDD & IA
| Categorie | Technologies |
|---|---|
| Langages Data | Python, SQL, R |
| Bibliotheques Python | Pandas, NumPy, Streamlit, Matplotlib, Seaborn, Plotly, PyTorch |
| Bases SQL | PostgreSQL, MySQL, Oracle |
| Bases NoSQL | MongoDB |
| Big Data & Streaming | PySpark, Kafka |
| BI & Visualisation | Power BI |

### Frontend
React.js · Next.js · Tailwind CSS · JavaScript (ES6+) · HTML5 · CSS3 · Figma

### Backend
PHP (Symfony) · Node.js · API REST

### Ops & Outils
Docker · Git/GitHub · WordPress · LucidChart · UML · SEO

---

## Projets Data & IA

### [ETL-pipeline-e-commerce](https://github.com/Imma0812/ETL-pipeline-e-commerce)
Pipeline ETL complet en Python analysant 500 000+ transactions e-commerce reelles.
- Stack : Python 3.10+ · Pandas · SQLite · SQL avance
- Concepts : Window Functions, CTE, agregations, segmentation client RFM

### [crypto-pipeline](https://github.com/Imma0812/crypto-pipeline)
Pipeline ELT moderne CoinGecko + Postgres + dbt + Metabase, conteneurise Docker, CI GitHub Actions.
- Stack : Python · Prefect · PostgreSQL · dbt · Metabase · Docker

### [spotify-music-trends](https://github.com/Imma0812/spotify-music-trends)
Dashboard Streamlit analysant 100 000+ morceaux Spotify et leurs features audio.
- Stack : Python · Pandas · Plotly · Streamlit · Kaggle API

### [stock-predicator](https://github.com/Imma0812/stock-predicator)
Dashboard de prediction boursiere - modele predictif + interface decisionnelle.
- Stack : Python · Streamlit · Pandas

### [certifs](https://github.com/Imma0812/certifs)
Vitrine Next.js centralisant mes certifications data & dev - https://certifs.vercel.app

---

## Projets Web & Logiciel

- AgriChain - Marketplace agricole (Node.js, React, MongoDB)
- Outil d administration etudiant - collaboration Nexa SMN
- Application de gestion immobiliere (conciergerie Nantes)
- Plateforme d information geospatiale type Cadastre (Vue.js, Leaflet)
- Systeme de reservation de salles - Symfony 7 avec algo anti-collision
- Mini-projets : Puissance 4, Morpion, IQ Master Quiz, Chatbot

---

## Certifications

| Plateforme | Certification | Statut |
|---|---|---|
| Udemy | Data Science avec Python | En cours |
| OpenClassrooms | Python · Power BI · Excel · SQL | En attente |
| freeCodeCamp | Python | En cours |

Toutes mes certifications : https://certifs.vercel.app

---

## Langues

- Francais : maternel
- Anglais : intermediaire

---

## Contact

> Disponible pour une alternance Data a partir de septembre 2026.

- LinkedIn : [Immaculé Konou](https://www.linkedin.com/in/immaculé-konou/)
- Email : immaculekonou@gmail.com
```

**Bio sidebar GitHub (160 char max)** :
```
Aspirant Data Engineer · ETL · Analytics | Python · SQL · PySpark · Power BI | L3 MIAGE Rennes 1 | Open to Data Alternance 09/2026
```

**A remplir aussi sur le profil GitHub** :
- Pronouns : He/Him
- Location : Rennes, France
- Website : https://www.linkedin.com/in/immaculé-konou/

**Topics a ajouter sur chaque repo** :
- ETL-pipeline-e-commerce : `etl` `data-engineering` `python` `pandas` `sqlite` `sql` `rfm-analysis` `data-pipeline`
- crypto-pipeline : `data-engineering` `elt` `dbt` `prefect` `postgresql` `docker` `metabase` `python` `pipeline` `coingecko` `modern-data-stack` `ci-cd`
- spotify-music-trends : `data-analysis` `python` `streamlit` `pandas` `plotly` `spotify` `music` `kaggle` `data-visualization`
- stock-predicator : `python` `machine-learning` `dashboard` `prediction` `data-science`
- certifs : `nextjs` `portfolio` `certifications` `vercel`

---

## 7. Idees de projets futurs (au cas ou)

### Projets ecartes mais bons en backup
- F1 : 75 ans de courses analysees (dataset Kaggle Formula 1) - DataAnalysis
- DVF : marche immobilier francais (15M+ lignes, DuckDB + Power BI) - DataAnalysis
- Marche alternance Data : meta-projet (API France Travail) - DataAnalysis
- Pipeline SNCF retards trains : Modern Data Stack - Data Engineering

### A boucler en priorite avant alternance
1. Pousser `spotify-music-trends` sur GitHub + deployer sur Streamlit Cloud
2. Pousser `crypto-pipeline` sur GitHub + ajouter badge CI
3. Mettre le portfolio en ligne sur Vercel
4. Ajouter screenshots reels dans `/public/images/projects/` du portfolio

---

## 8. Regles importantes pour les futures conversations

1. **Pas d emojis dans le code, jamais.** Ni dans les commentaires, ni dans les print, ni dans les noms.
2. **Commentaires courts en francais** (style dev, pas paragraphes).
3. **Pas de stickers / traces IA** dans les contenus livres.
4. **"vazy" = signal pour demander acces a un dossier** (request_cowork_directory).
5. **Charte graphique** : noir + orange `#FF800D`. Toujours.
6. **Cible** : alternance Data 09/2026 (pas stage). Toujours preciser.
7. **Photo de profil** : `/public/images/profile1.png` dans le portfolio.
8. **Logos** : `/public/images/Logo1.png` et `LogoR.png`.

---

## 9. Comment utiliser ce briefing

Au debut d une nouvelle conversation Claude, dis :

> Voici le briefing complet de mes projets et de mon profil. Lis-le avant de me repondre. Ensuite je te dis ce dont j ai besoin aujourd hui.

Puis joins ce fichier (`CLAUDE_BRIEFING.md`).

Claude aura alors :
- Mon identite et positionnement
- Mes liens, repos, stack
- L etat de mes 3 gros projets (Spotify, Crypto Pipeline, Portfolio)
- La charte graphique a respecter
- Les regles a suivre
- Les prochaines actions

---

## 10. Quick checklist (etat au moment de l export)

- [ ] Push `spotify-music-trends` sur GitHub
- [ ] Push `crypto-pipeline` sur GitHub
- [ ] Configurer Kaggle API (kaggle.json dans ~/.kaggle/)
- [ ] Configurer Supabase pour le portfolio
- [ ] Configurer Resend pour le portfolio
- [ ] Deployer le portfolio sur Vercel
- [ ] Mettre les screenshots reels dans `/public/images/projects/` du portfolio
- [ ] Re-pinner les repos GitHub dans le bon ordre (ETL > Crypto > Spotify > Portfolio > Certifs)
- [ ] Ajouter description + topics sur les nouveaux repos GitHub
- [ ] Mettre a jour le README profil GitHub (`Imma0812/Imma0812/README.md`)
- [ ] Adapter le LinkedIn avec le nouveau titre "Data Engineering & Analytics"
- [ ] Supprimer les fichiers obsoletes du portfolio (cf section 5.3)

---

*Fin du briefing. Garde ce fichier en lieu sur, c est ta memoire externe.*
