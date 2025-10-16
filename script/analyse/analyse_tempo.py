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
df = pd.merge(echonest[["track_id","echonest_audio_features_tempo"]],tracks[["track_id","genre"]],on="track_id")
df = df.dropna()
df = df[df["echonest_audio_features_tempo"] < 300]

counts = df["genre"].value_counts()
df = df[df["genre"].isin(counts[counts>=10].index)]
genres = sorted(df["genre"].unique())
data = [df[df["genre"]==g]["echonest_audio_features_tempo"] for g in genres]

plt.violinplot(data, showmeans=True, showmedians=True, showextrema=True)
plt.xlabel("genre")
plt.ylabel("tempo")
plt.title("Tempo distribution by genre")
plt.show()
