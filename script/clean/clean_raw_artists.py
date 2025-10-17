import pandas as pd
from bs4 import BeautifulSoup

source = './dataset/'
artists_fichier = 'raw_artists.csv'

chemin_artists = source+artists_fichier

artists = pd.read_csv(chemin_artists)

"""
colonnes gardées : identifiant de l'artiste, nom d'artiste,bio d'artiste,la popularité de l'artiste par like, l'image de l'artiste 

certaines colonnes étaient pertinantes mais par un trop grand manque de données ne sont pas gardées.

"""
colonnes = ["artist_id","artist_name","artist_bio","artist_favorites","artist_image_file","tags"]

artists_subset = artists[colonnes]


#remplir les bio vides et retirer les balises html
artists_subset["artist_bio"].fillna("No bio available",inplace=True)
artists_subset["artist_bio"] = artists_subset["artist_bio"].apply(lambda x: BeautifulSoup(x, 'html.parser').get_text())


print(artists.isnull().sum()/len(artists)*100)
print(artists_subset.isnull().sum()/len(artists_subset)*100)

#exporter le dataframe clean en csv 
dossier_export = './cleaned_dataset/'
nom_fichier = 'clean_artist.csv'
chemin_export = dossier_export + nom_fichier


artists_subset.to_csv(chemin_export,index=False)
