import pandas as pd
import matplotlib.pyplot as plt
import ast

echonest = pd.read_csv("./cleaned_dataset/clean_echonest.csv")
tracks = pd.read_csv("./cleaned_dataset/clean_raw_tracks.csv")

def genre(x):
    try:
        g = ast.literal_eval(x)
        if g and isinstance(g, list):
            return g[0].get("genre_title")
    except:
        return None

tracks["genre"] = tracks["track_genres"].apply(genre)
df = pd.merge(
    echonest[["track_id", "echonest_audio_features_tempo"]],
    tracks[["track_id", "genre"]],
    on="track_id"
)
df = df.dropna()
# df = df[df["echonest_audio_features_tempo"] < 300] 
# counts = df["genre"].value_counts()
# df = df[df["genre"].isin(counts[counts >= 10].index)]

genres = sorted(df["genre"].unique())
data = []
for g in genres:
    genre_data = df[df["genre"] == g]["echonest_audio_features_tempo"]
    data.append(genre_data)
moy = []
medi = []
for d in data:
    moy.append(d.mean())
    medi.append(d.median())

test = plt.violinplot(data, showmeans=True, showmedians=True, showextrema=True)
plt.xticks(range(1, len(genres) + 1), genres, rotation=90)
plt.xlabel("Genre")
plt.ylabel("Tempo (BPM)")
plt.title("Tempo distribution by genre")
i = 1
for moy, med in zip(moy, medi):
    plt.text(i, moy + 3, f"{moy:.1f}",fontsize=7)
    plt.text(i, med - 6, f"{med:.1f}",fontsize=7)
    i = i + 1
plt.show()
