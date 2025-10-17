import csv
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from biplot import *

DATASET_PATH = "../../dataset"

df_genres = pd.read_csv(DATASET_PATH + "/genres.csv")
df_tracks = pd.read_csv(DATASET_PATH + "/tracks.csv")

# print(df_tracks.head())

genre_listens = {}
genre_favorites = {}
genre_comments = {}
genre_number = {}

# print(df_tracks.head(2))
def flatten(col) :
    if col == "Unnamed: 0" : return "track_id"
    fcol = col.split('.')[0]
    for i, r in df_tracks.head(2).iterrows() :
        if isinstance(r[col], float) : continue
        fcol += '.' + r[col]
    return fcol
df_tracks.rename(flatten, axis='columns', inplace=True)
df_tracks.drop([0, 1], axis='rows', inplace=True)

for index, row in df_tracks.iterrows() :
    # for genre_id in eval(row["track.genres"]) :
    genre_id = row['track.genre_top']
    if isinstance(genre_id, float) : continue
    if genre_id in genre_listens :
        genre_listens[genre_id] += int(row["track.listens"])
        genre_favorites[genre_id] += int(row["track.favorites"])
        genre_comments[genre_id] += int(row["track.comments"])
        genre_number[genre_id] += 1
    else :
        genre_listens[genre_id] = int(row["track.listens"])
        genre_favorites[genre_id] = int(row["track.favorites"])
        genre_comments[genre_id] = int(row["track.comments"])
        genre_number[genre_id] = 1

# print(genre_listens)
# print(genre_favorites)
# print(genre_comments)
df_genres = df_genres.transpose()
df_genres.rename(lambda col : df_genres[col]["genre_id"], axis='columns', inplace=True)

ls_genre = []
ls_genre_number = []
ls_label = []

for id in genre_listens :
    ls_genre.append(genre_listens[id])
    ls_genre_number.append(genre_number[id])
    ls_label.append(id)

ls_avg = [i/j for i,j in zip(ls_genre, ls_genre_number)]


ls_avg, ls_label = zip(*[(avg, lab) for avg, lab in sorted(zip(ls_avg, ls_label))])


plt.barh(ls_label, ls_avg)
plt.title("Average number of listens for each genre")
plt.tight_layout()
plt.show()