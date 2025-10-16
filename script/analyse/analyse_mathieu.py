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

exploded = artists_subset.explode('tags')

top_n = 10

#Fréquence des tags
tag_counts_all = exploded['tags'].value_counts()
top_tags = tag_counts_all.head(top_n)

#Popularité totale (likes)
tag_popularity_all = exploded.groupby('tags')['artist_favorites'].sum().sort_values(ascending=False)
top_popularity = tag_popularity_all.head(top_n)

# Création des histogrammes
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Histogramme 1 : fréquence
axes[0].bar(
    top_tags.index,
    top_tags.values,
    color='skyblue',
    edgecolor='black'
)
axes[0].set_title('Most used Tag (Top 10)')
axes[0].set_ylabel('Number of Tags')
axes[0].set_xlabel('Tags')
axes[0].tick_params(axis='x', rotation=45)

# Histogramme 2 : popularité totale (likes)
axes[1].bar(
    top_popularity.index,
    top_popularity.values,
    color='salmon',
    edgecolor='black'
)
axes[1].set_title('Likes Distribution by Tag (Top 10)')
axes[1].set_ylabel('Number of Likes')
axes[1].set_xlabel('Tags')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
