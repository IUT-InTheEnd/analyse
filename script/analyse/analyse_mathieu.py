import matplotlib.pyplot as plt
import pandas as pd
import ast

source = '../../cleaned_dataset/'
artists_fichier = 'clean_artist.csv'

chemin_artists = source+artists_fichier

artists_subset = pd.read_csv(chemin_artists)


artists_subset['tags'] = artists_subset['tags'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

artists_subset['nb_tags'] = artists_subset['tags'].apply(len)

# Corrélation ou non entre le nombre de tag d'un artiste et le nombre like
plt.figure(figsize=(8,6))
plt.scatter(artists_subset['nb_tags'], artists_subset['artist_favorites'], alpha=0.5)
plt.title("Correlation between the numbers of artist's tag and likes")
plt.xlabel('Number of tags')
plt.ylabel('Number of likes')
plt.tight_layout()
plt.show()

