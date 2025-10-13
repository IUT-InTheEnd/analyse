# Analyse ACP NEVOT Pierre

import csv
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from biplot import *

# Standardisation

fichier = "./cleaned_dataset/clean_echonest.csv"
df = pd.read_csv(fichier)

acousticness = df["echonest_audio_features_acousticness"]
danceability = df["echonest_audio_features_danceability"]
energy = df["echonest_audio_features_energy"]
instrumentalness = df["echonest_audio_features_instrumentalness"]
liveness = df["echonest_audio_features_liveness"]
speechiness = df["echonest_audio_features_speechiness"]
tempo = df["echonest_audio_features_tempo"]
valence = df["echonest_audio_features_valence"]
artist_discovery = df["echonest_social_features_artist_discovery"]
artist_familiarity = df["echonest_social_features_artist_familiarity"]
artist_hotttnesss = df["echonest_social_features_artist_hotttnesss"]
song_currency = df["echonest_social_features_song_currency"]
song_hotttnesss = df["echonest_social_features_song_hotttnesss"]

valeur = np.stack(
    (
        acousticness,
        danceability,
        energy,
        instrumentalness,
        liveness,
        speechiness,
        tempo,
        valence,
        artist_discovery,
        artist_familiarity,
        artist_hotttnesss,
        song_currency,
        song_hotttnesss,
    ),
    axis=1
)

dimensions = [
    "acousticness",
    "danceability",
    "energy",
    "instrumentalness",
    "liveness",
    "speechiness",
    "tempo",
    "valence",
    "artist_discovery",
    "artist_familiarity",
    "artist_hotttnesss",
    "song_currency",
    "song_hotttnesss",
]

scaler = StandardScaler()
scaler.fit(valeur)
valeur_scaled = scaler.transform(valeur)

# Entrainement du modèle
pca = PCA()
pca_res = pca.fit_transform(valeur_scaled)
print(pca_res)

# Tableau de valeurs singulières + % variance

eig = pd.DataFrame ({
    "Dimension" :
        dimensions,
    "Valeur propre" : pca.explained_variance_,
    "% valeur propre" :
        np.round (pca.explained_variance_ratio_ * 100),
    "% cum. val. prop." :
        np.round(np.cumsum(pca.explained_variance_ratio_) * 100)
})
print(eig)

y1 = list(pca.explained_variance_ratio_)
x1 = range(len(y1))
plt.bar(x1, y1)
plt.show()
