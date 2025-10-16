import pandas as pd
import matplotlib.pyplot as plt

'''
Analyse à traiter :
    - track_duration : nombre d'écoutes du morceau
    - track_interest : score d'intérêt du morceau (FMA)
'''

# import from csv
df = pd.read_csv("./cleaned_dataset/clean_raw_tracks.csv")

df = df[["track_duration","track_interest"]]

def duration_to_seconds(duration_str):
    try:
        parts = duration_str.split(":")
        if len(parts) == 2:
            minutes, seconds = map(int, parts)
            return minutes * 60 + seconds
        elif len(parts) == 3:
            # Format H:MM:SS, on convertit aussi
            hours, minutes, seconds = map(int, parts)
            return hours * 3600 + minutes * 60 + seconds
        else:
            return None  # format non reconnu
    except:
        return None  # erreur de conversion


df["duration_seconds"] = df["track_duration"].apply(duration_to_seconds)

bins = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 900, 1800, 3600]
labels = ["00:00 - 01:00", "01:00 - 02:00", "02:00 - 03:00", "03:00 - 04:00", "04:00 - 05:00", "05:00 - 06:00", "06:00 - 07:00", "07:00 - 08:00", "08:00 - 09:00", "09:00 - 10:00", "10:00 - 15:00", "15:00 - 30:00", "30:00 - 1:00:00"]

df["duration_range"] = pd.cut(df["duration_seconds"], bins=bins, labels=labels, right=False)

count_per_bin = df["duration_range"].value_counts().sort_index()

plt.figure(figsize=(10,6))
bars = plt.bar(count_per_bin.index.astype(str), count_per_bin.values, color="blue")
plt.xticks(rotation=45)
plt.xlabel("Track duration range")
plt.ylabel("Number of tracks")
plt.title("Number of tracks by duration range")
plt.tight_layout()

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             height + 5,
             str(int(height)),
             ha='center', va='bottom', fontsize=12)
    
plt.savefig("images/analyse1_cyp.png")
plt.clf()

################

favorites_per_bin = df.groupby("duration_range")["track_interest"].mean()

plt.figure(figsize=(10,6))
bars = plt.bar(favorites_per_bin.index.astype(str), favorites_per_bin.values, color="blue")
plt.xlabel("Track duration range")
plt.ylabel("Average interest score (FMA)")
plt.title("Average interest score by track duration range")
plt.xticks(rotation=45)

# Ajouter les valeurs au-dessus de chaque barre
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2,
             height + 5,
             str(int(height)),
             ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.savefig("images/analyse2_cyp.png")