import pandas as pd
genres = pd.read_csv("./dataset/genres.csv")

# rename des columns pour que ça soit plus clair en database
genres = genres.rename(columns={'parent': 'genre_parent_id', 'title': 'genre_title'})

# replace des valeurs de top_level par un bool
genres['top_level'] = (genres['genre_parent_id'] == 0)
print(genres)



genres.to_csv('./cleaned_dataset/clean_genres.csv', index=False)