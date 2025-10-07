import pandas as pd
chemin_to_csv = "./Dataset/raw_genres.csv"

df = pd.read_csv(chemin_to_csv)

# Colonnes supprimées car genre color n'a aucun intéret et genre handle est redondant avec genre title
df = df.drop(columns=["genre_color","genre_handle"])

df.to_csv("./Cleaned_Dataset/clean_raw_genres.csv",index=False)