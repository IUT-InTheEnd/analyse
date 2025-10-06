import pandas as pd
import math
import re

source = './dataset/'
artists_fichier = 'raw_artists.csv'

chemin_artists = source+artists_fichier

artists = pd.read_csv(chemin_artists)

"""
colonnes gardées : identifiant de l'artiste, l'année de début d'activité et de fin, la popularité de l'artiste

"""

colonnes = ["artist_id","artist_active_year_begin","artist_active_year_end","artist_favorites"]

artists_subset = artists[colonnes]

#remplacer les années de débuts d'activités par l'année d'ajout ou dans la bio 
def extract_year(date_str):
    match = re.search(r'\d{4}', str(date_str))
    return int(match.group()) if match else None

def fill_year():
    annee_ajout = artists["artist_bio"].apply(extract_year);
    artists_subset["artist_active_year_begin"].fillna(annee_ajout,inplace=True)
    if(artists_subset["artist_active_year_begin"].isnull().values.any()):
        annee_ajout = artists["artist_date_created"].apply(extract_year);
        artists_subset["artist_active_year_begin"].fillna(annee_ajout,inplace=True)

fill_year()

#remplacer les années supérieures à aujourd'hui par autre chose
artists_subset.loc[artists_subset["artist_active_year_end"]>2025,"artist_active_year_end"]=0000
artists_subset = artists_subset.sort_values('artist_active_year_end',ascending=False)

print(artists_subset)

