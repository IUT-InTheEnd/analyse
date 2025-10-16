import matplotlib.pyplot as plt
import pandas as pd
import ast
import squarify
import numpy as np

source = './'
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

# Définir le nombre de barres
top_n = 10


tag_counts = exploded['tags'].value_counts().head(10)


tag_popularity = exploded.groupby('tags')['artist_favorites'].sum().sort_values(ascending=False).head(10)

# Création de la figure
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

def add_labels_with_contrast(ax, values, labels, colors):
    norm = plt.Normalize(np.min(values), np.max(values))
    cmap = plt.cm.Blues if 'Frequency' in ax.get_title() else plt.cm.Reds
    colors_mapped = cmap(norm(values))

    rects = squarify.normalize_sizes(values, 100, 100)
    rects = squarify.squarify(rects, 0, 0, 100, 100)
    squarify.plot(sizes=values, color=colors_mapped, ax=ax, alpha=0.9)

    for rect, label, color in zip(rects, labels, colors_mapped):
        x = rect['x'] + rect['dx']/2
        y = rect['y'] + rect['dy']/2
        brightness = np.dot(color[:3], [0.299, 0.587, 0.114])
        text_color = 'black' if brightness > 0.6 else 'white'
        ax.text(x, y, label, va='center', ha='center', fontsize=10, color=text_color, weight='bold')

    ax.axis('off')


axes[0].set_title('Treemap of Tag Frequency (Top 10)', fontsize=14)
add_labels_with_contrast(
    axes[0],
    tag_counts.values,
    [f"{tag}\n{count}" for tag, count in zip(tag_counts.index, tag_counts.values)],
    plt.cm.Blues(tag_counts.values / max(tag_counts.values))
)


axes[1].set_title('Treemap of Tag Popularity (Top 10 by Likes)', fontsize=14)
add_labels_with_contrast(
    axes[1],
    tag_popularity.values,
    [f"{tag}\n{int(likes)}" for tag, likes in zip(tag_popularity.index, tag_popularity.values)],
    plt.cm.Reds(tag_popularity.values / max(tag_popularity.values))
)

plt.tight_layout()
plt.show()
