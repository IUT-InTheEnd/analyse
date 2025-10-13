import csv
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from biplot import *

input_file = "../../dataset/features.csv"
df = pd.read_csv(input_file)
values = df.iloc[3:, 1:]

scaler = StandardScaler()
scaler.fit(values)
values_scaled = scaler.transform(values)

pca = PCA()
pca_res = pca.fit_transform(values_scaled)

eig = pd.DataFrame ({
    "Dimension" :
        [f"Dim {i}." for i in range(len(pca.components_))],
    "Valeur propre" : pca.explained_variance_,
    "% valeur propre" :
        np.round (pca.explained_variance_ratio_ * 100),
    "% cum. val. prop." :
        np.round(np.cumsum(pca.explained_variance_ratio_) * 100)
})
print(eig.head(20))

y1 = list(pca.explained_variance_ratio_)
biplot(score=pca_res[:16,0:2],
coeff=np.transpose(pca.components_[0:2,:16]),
cat=y1[0:1], density=False, coeff_labels = list(range(16))) #dimensions[6:])
# [print(i, dimensions[i]) for i in range(len(dimensions))]
plt.show()