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

X = df[df.columns[:8]]
temp = X.sub(X.mean())
X_scaled = temp.div(X.std())

# Entrainement du modèle
n_components = 8
pca = PCA(n_components=n_components)
pca_res = pca.fit_transform(X_scaled)
print(pca_res)

dimensions = ["Acousticness", "Danceability", "Energy", "Instrumentalness", "Liveness", "Speechiness", "Tempo", "Valence"]

# Tableau de valeurs singulières + % variance

eig = pd.DataFrame ({
    "Dimension" : dimensions,
    "Valeur propre" : pca.explained_variance_,
    "% valeur propre" :
        np.round (pca.explained_variance_ratio_ * 100),
    "% cum. val. prop." :
        np.round(np.cumsum(pca.explained_variance_ratio_) * 100)
})
print(eig)

y1 = list(pca.explained_variance_ratio_)
fig, ax = plt.subplots()
labels = [str(i+1).zfill(1) for i in range(n_components)]
ax.bar(labels, y1, label = labels)
ax.set_xlabel("PCA dimension")
ax.set_ylabel("Explained variance percentage")
plt.show()

# Je prends que les 4 premières valeurs car avec elles on atteint +50% de valeur propre 
biplot(score=pca_res[:4,0:2],
coeff=np.transpose(pca.components_[0:2,:4]),
cat=y1[0:1], density=False, coeff_labels = list(range(4)))
# [print(i, dimensions[i]) for i in range(len(dimensions))]
plt.show()

# Visualisation avec plan factoriel
pca_df = pd.DataFrame({
"Dim3 (Instrumentalness)" : pca_res[: , 3],
"Dim1 (Danceability)" : pca_res[ : , 1] 
})
pca_df.plot.scatter("Dim1 (Danceability)", "Dim3 (Instrumentalness)")
plt.xlabel("Dimension 1 (Danceability)")
plt.ylabel("Dimension 3 (Instrumentalness)")
plt.suptitle ("Premier plan factoriel")
plt.show()

pca_df = pd.DataFrame({
"Dim0 (Acousticness)" : pca_res[: , 0],
"Dim2 (Energy)" : pca_res[ : , 2]
})
pca_df.plot.scatter("Dim1 (Danceability)", "Dim2 (Energy)")
plt.xlabel("Dimension 1 (Danceability)")
plt.ylabel("Dimension 2 (Energy)")
plt.suptitle ("Premier plan factoriel")
plt.show()
