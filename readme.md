# 🏀 WNBA Player Clustering with Stats

## 📊 Overview
This project uses **All seasons of WNBA data** to cluster player-seasons into meaningful groups based on their per-100 possession statistics. The goal is to discover patterns and similarities in player performance using unsupervised learning techniques.

## 🔍 What It Does
- Loads and preprocesses WNBA player stats (per 100 possessions).
- Treats each player-season as a unique data point.
- Uses **Principal Component Analysis (PCA)** to reduce dimensionality.
- Applies **K-Means Clustering** and other techniques to group similar player profiles.
- Visualizes clusters and interprets them based on player roles or positions.

## 🧠 Techniques Used
- 📦 `tidyverse` for data wrangling
- 📊 `ggplot2` for visualizations
- 🤖 `FactoMineR` & `factoextra` for PCA
- 📈 `kmeans` for clustering

## 📌 Highlights
- 💡 Explores how players group based on play style, not just position.
- 🖼️ Includes 3D visualizations for PCA components and clusters.

## 📁 Data
The dataset includes WNBA player statistics from **2000 to 2024**, cleaned and transformed into per-100 possession metrics for better comparability.

## 🧪 Future Directions
- 🕵️‍♀️ Track individual players across clusters to study career evolution.
- 📆 Analyze how player archetypes have changed over time.
- 🏆 Compare clusters to real positions or accolades (e.g. All-Star selections).
---

📎 *This was a fun deep dive into sports analytics using unsupervised learning!*
