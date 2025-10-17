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

X = df[df.columns[1:7]]
temp = X.sub(X.mean())
X_scaled = temp.div(X.std())
print(X)

# Entrainement du modèle
n_components = 6
pca = PCA(n_components=n_components)
pca_res = pca.fit_transform(X_scaled)
print(pca_res)

dimensions = ["Acousticness", "Danceability", "Energy", "Instrumentalness", "Liveness", "Speechiness"]

# Tableau de valeurs singulières + % variance

eig = pd.DataFrame ({
    "Dimension" : dimensions,
    "Valeur propre" : pca.explained_variance_,
    "% valeur propre" :
        np.round(pca.explained_variance_ratio_ * 100),
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
biplot(score=pca_res[:6,0:2],
coeff=np.transpose(pca.components_[0:2,:6]),
cat=y1[0:1], density=True, coeff_labels = list(range(6)))
# [print(i, dimensions[i]) for i in range(len(dimensions))]
plt.show()

# Visualisation avec plan factoriel
# Corrélation négative entre Danceability et Instrumentalness
pca_df = pd.DataFrame({
"Dim3 (Instrumentalness)" : pca_res[: , 3],
"Dim1 (Danceability)" : pca_res[ : , 1] 
})
pca_df.plot.scatter("Dim1 (Danceability)", "Dim3 (Instrumentalness)")
# Droite pour séparer les deux nuages de points
ax = plt.gca()
x_min, x_max = ax.get_xlim()
y_min, y_max = ax.get_ylim()
x0, y0 = -1.5, -2.0
m = 0.8
lo = x0
hi = max(x_max, y_max)
x = np.linspace(lo, hi, 100)
y = m * (x - x0) + y0
ax.plot(x, y, color='red', linestyle='--', linewidth=1)
plt.xlabel("Dimension 1 (Danceability)")
plt.ylabel("Dimension 3 (Instrumentalness)")
plt.suptitle ("First factorial plane")
plt.show()

# Corrélation négative entre Danceability et Speechiness
pca_df = pd.DataFrame({
"Dim1 (Danceability)" : pca_res[: , 1],
"Dim6 (Speechiness)" : pca_res[ : , 5]
})
pca_df.plot.scatter("Dim1 (Danceability)", "Dim6 (Speechiness)")
plt.xlabel("Dimension 1 (Danceability)")
plt.ylabel("Dimension 6 (Speechiness)")
plt.suptitle ("Second factorial plane")
plt.show()

# Corrélation négative entre Acousticness et Energy
pca_df = pd.DataFrame({
"Dim1 (Acousticness)" : pca_res[: , 0],
"Dim2 (Energy)" : pca_res[ : , 2]
})
pca_df.plot.scatter("Dim1 (Acousticness)", "Dim2 (Energy)")
plt.xlabel("Dimension 1 (Acousticness)")
plt.ylabel("Dimension 2 (Energy)")
plt.suptitle ("Third factorial plane")
plt.show()

# Corrélation négative entre Danceability et Instrumentalness
pca_df = pd.DataFrame({
"Dim1 (Danceability)" : pca_res[: , 1],
"Dim5 (Instrumentalness)" : pca_res[ : , 3]
})
pca_df.plot.scatter("Dim1 (Danceability)", "Dim5 (Instrumentalness)")
plt.xlabel("Dimension 1 (Danceability)")
plt.ylabel("Dimension 5 (Instrumentalness)")
plt.suptitle ("Fourth factorial plane")
plt.show()

# Corrélation négative entre Speechiness et Instrumentalness
pca_df = pd.DataFrame({
"Dim1 (Speechiness)" : pca_res[: , 5],
"Dim5 (Instrumentalness)" : pca_res[ : , 3]
})
pca_df.plot.scatter("Dim1 (Speechiness)", "Dim5 (Instrumentalness)")
plt.xlabel("Dimension 1 (Speechiness)")
plt.ylabel("Dimension 5 (Instrumentalness)")
plt.suptitle ("Fourth factorial plane")
plt.show()