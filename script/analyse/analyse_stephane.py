#@title         : analyse_stephane.py
#@description   : Analyse des données nettoyées des albums
#@author        : Antoine Stéphane
#@date          : 2025-10-13 

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import prince  

# import des fichiers csv nécessaures
df_tracks = pd.read_csv("../../cleaned_dataset/clean_raw_tracks.csv")
df_albums = pd.read_csv("../../cleaned_dataset/clean_albums.csv")



#######   AFC entre les artistes et les types d'albums   #######

# table de contingence
data_crosstab = pd.crosstab(df_albums["artist_name"], df_albums["album_type"])

# suppression des types 'unknown'
data_crosstab = data_crosstab.drop(columns='unknown', errors='ignore')

# suppression des tables vides
data_crosstab = data_crosstab.loc[
    data_crosstab.sum(axis=1) > 0,
    data_crosstab.sum(axis=0) > 0
]

afc = prince.CA(n_components=2, random_state=42)
afc = afc.fit(data_crosstab)

# récupération des coordonnées
row_coords = afc.row_coordinates(data_crosstab)  # artistes
col_coords = afc.column_coordinates(data_crosstab)  # alubms

# visualisation par un scatter plot
plt.figure(figsize=(10, 7))
plt.scatter(row_coords[0], row_coords[1], color="#f5a61d", label="Artists")
plt.scatter(col_coords[0], col_coords[1], color="#095372", label="Album Types")

# ajout des labels pour les albums 
for i, txt in enumerate(col_coords.index):
    plt.text(
        col_coords.iloc[i, 0] + 0.02,
        col_coords.iloc[i, 1] + 0.02,
        txt,
        color="#095372",
        fontsize=10,
        fontweight='bold'
    )

plt.axhline(0, color='grey', lw=1)
plt.axvline(0, color='grey', lw=1)
plt.title("Correspondence analysis between artists and album types")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




#######   Etude de la corrélation entre la popularité des morceaux et leur album   #######

# selection des colonnes nécessaires
df_tracks = df_tracks[['track_id', 'album_id', 'track_favorites', 'track_listens']]
df_albums = df_albums[['album_id', 'album_favorites', 'album_listens']]

# regroupement des deux dataframes
df_merged = pd.merge(df_tracks, df_albums, on='album_id', how='left').dropna()

# calcul de la corrélation
correlation = df_merged[['track_favorites', 'album_favorites', 'track_listens', 'album_listens']].corr()

# visualisation de la matrice de corrélation
custom_cmap = LinearSegmentedColormap.from_list("custom", ["#7dd0ff", "#095372"])
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap=custom_cmap,
    fmt=".2f",
    linewidths=0.5,
    cbar_kws={'label': 'Correlation Coefficient'},
)
plt.title("Correlation between the Popularity of a track and its album")
plt.tight_layout()
plt.show()
