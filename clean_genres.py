import pandas as pd
genres = pd.read_csv("./dataset/genres.csv")

# rename des columns pour que ça soit plus clair en database
genres = genres.rename(columns={'parent': 'genre_parent_id', 'title': 'genre_title'})
print(genres)
