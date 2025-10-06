import pandas as pd
import os
import numpy as np
import dotenv

# environnement clé api spotify depuis .env
dotenv.load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_SECRET = os.getenv('SPOTIFY_SECRET')

# Fonction pour trouver les cases vides dans le but de compléter avec l'api spotify
def trouver_case_vide(chemin_fichier):
    try:
        liste_vide = []
        df = pd.read_csv(chemin_fichier, low_memory=False)
        col_1a9 = df.columns[:9]        
        df[col_1a9] = df[col_1a9].replace(np.nan, '', regex=True)
        for index, row in df.iterrows():
            for col in col_1a9:
                if str(row[col]).strip() == '':
                    liste_vide += [[index+2, col]] # On ajoute 2 pour compenser l'indexation et l'en-tête
        return liste_vide
    except Exception as e:
        print(f"Erreur : {e}")

repertoire = './dataset'
nom_fichier = 'raw_echonest.csv'
chemin_fichier = os.path.join(repertoire, nom_fichier)

liste_vide_final = trouver_case_vide(chemin_fichier)

#retire les valeurs inférieurs ou égales à 4
for item in liste_vide_final[:]:
    if item[0] <= 4:
        liste_vide_final.remove(item)
    else:
        break
    
# Dictionnaire echonest pour remplacer les noms de colonnes
echonest_dict = {
    'echonest.1' : 'danceability',
    'echonest.2' : 'energy',
    'echonest.3' : 'instrumentalness',
    'echonest.4' : 'liveness',
    'echonest.5' : 'speechiness',
    'echonest.6' : 'tempo',
    'echonest.7' : 'valence'
}

# Remplace les noms de colonnes dans la liste
for item in liste_vide_final:
    if item[1] in echonest_dict:
        item[1] = echonest_dict[item[1]]

# On récupère le nom de la musique dans raw_tracks.csv et l'artist id
nom_fichier = 'raw_tracks.csv'
chemin_fichier = os.path.join(repertoire, nom_fichier)
df_tracks = pd.read_csv(chemin_fichier, low_memory=False)
# filtre les lignes avec les tracks id de liste vide final
track_ids = df_tracks['track_id'].tolist()
track_ids_vide = []
for item in liste_vide_final:
    track_ids_vide.append(track_ids[item[0]-2]) # On retire 2 pour compenser l'indexation et l'en-tête