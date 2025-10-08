import pandas as pd
import matplotlib.pyplot as plt

path = "/home/etudiant/Documents/SAE/Dataset/"
ls = ["echonest.csv",
      "feature.csv",
      "genres.csv",
      "raw_albums.csv",
      "raw_artists.csv",
      "raw_echonest.csv",
      "raw_genres.csv",
      "raw_track.csv",
      "tracks.csv"]

ls = [path+fich for fich in ls]

# selection du fichier raw_albums.csv
df = pd.read_csv(ls[3]) #lecture des 10 premières lignes 

# affichage des différents attributs de la table
print("Attributs : ", df.columns)

# selection des attributs pertinents
df = df.drop(columns=['album_engineer', 'album_producer', 'album_handle', 'album_information', 'album_url', 'album_image_file', 'album_images', 'artist_url'])

'''
Attributs retenus :
    - album_id : identifiant unique de l'album
    - album_title : nom de l'album
    - album_type : type d'album (album, single, compilation)
    - album_date_released : date de sortie de l'album
    - album_date_created : date d'ajout de l'album sur la plateforme
    - album_comments : nombre de commentaires sur l'album
    - album_favorites : nombre de favoris sur l'album
    - album_listens : nombre d'écoutes de l'album
    - album_tracks : nombre de morceaux dans l'album
    - tags : tags associés à l'album
    - artist_name : artiste principal
'''

# nombre d'albums
print("\nNombre d'albums : ", len(df))# 15234 

# affichage des valeurs manquantes pour chaque attribut
print("\nAffichage du nombre de valeurs manquantes")
print(df.isnull().sum())


count = 0
for tag in df["tags"]:
    if tag != "[]":
        count+=1
print("\nNombre de tags vides : ", count)


# il y a 2701 instances avec des tags associés donc les données obtenues auparavant avec la somme des valeurs nulles n'est pas correcte pour les tags

# après analyse des valeurs des tags 
# on remarque que les valeurs ne sont pas pertinentes 

df = df.drop(columns=['tags']) # on supprime donc la colonne


## on s'intéresse maintenant aux dates de sortie et de publication sur la plateforme des albums 

# Conversion en datetime
df["album_date_created"] = pd.to_datetime(df["album_date_created"], errors="coerce")
df["album_date_released"] = pd.to_datetime(df["album_date_released"], errors="coerce")

# Extraction des années
year_created = df["album_date_created"].dt.year
year_released = df["album_date_released"].dt.year

#calcul de la différence entre les années
diff = year_created - year_released
print("\nDifférence années de publication sur la plateforme et de sortie de l'album")
print("Moyenne : ", diff.mean()) # moyenne de la différence entre les années  ->  1.66 donc en moyenne les album ont été ajoutés à la plateforme 1 an et demi après leur sortie
print("Maximum : ", diff.max()) # différence maximale entre les années -> il existe un album qui a été ajouté à la plateforme 112 ans après sa sortie
print("Minimum : ", diff.min()) # différence minimale entre les années -> il existe un album qui a été ajouté à la platforme 6 ans avant sa sortie 

# il y a 5491 valeurs manquantes sur 15234 pour l'année de sortie

# on aurait pu se dire que vu que l'album est publié sur la plateforme en moyenne 1 an et demi après sa sortie, on pourrait combler les valeurs manquantes de l'année de sortie par l'année de création - 1 ou 2
# cependant avec les valeurs min et max on voit que ce n'est pas du tout représentatif de l'ensemble des données
# si un album est sorti en 1920 et qu'il a été ajouté à la plateforme en 2020, on ne peut pas estimer son année de sortie à 2019 ou 2018
# on va donc remplacer les valeurs manquantes par des valeurs nulles 

# Mise sous le meme format
df["album_date_created"] = df["album_date_created"].dt.strftime('%d-%m-%Y')
df["album_date_released"] = df["album_date_released"].dt.strftime('%d-%m-%Y')

# Remplacement des valeurs manquantes par des valeurs nulles
for elt in df["album_date_released"]:
    if pd.isnull(elt):
        df["album_date_released"].replace(elt, '00-00-0000', inplace=True)
        
# il y a 464 valeurs nulles pour la variable album_type
# on remplace les valeurs nulles par "unknown"
for elt in df["album_type"]:
    if pd.isnull(elt):
        df["album_type"].replace(elt, "unknown", inplace=True)

#il y a une valeur de la colonne artist_name qui est nulle
for elt in df["artist_name"]:
    if pd.isnull(elt):
        df["artist_name"].replace(elt, "unknown", inplace=True)

# on vérifie qu'il n'y a plus de valeurs manquantes
print("\nVérification valeurs manquantes après premier nettoyage : ")
print(df.isnull().sum())


# c'est bon toutes les valeurs manquantes ont été gérées


# maintenant on va vérifier la validité des valeurs en vérifiant s'il n'y a pas de données corrompues 
# (nombre d'écoutes de favoris positifs, données uniques pour les identifiants...)

nb_ecoutes_false = 0
for elt in df["album_listens"]:
    if elt < 0:
        nb_ecoutes_false+=1

nb_favoris_false = 0
for elt in df["album_favorites"]:
    if elt < 0:
        nb_favoris_false+=1

nb_comments_false = 0
for elt in df["album_comments"]:
    if elt < 0:
        nb_comments_false+=1

nb_tracks_false = 0
for elt in df["album_tracks"]:
    if elt < 0:
        nb_tracks_false+=1

print("\nErreurs nombre écoutes : ", nb_ecoutes_false)
print("Erreurs nombre de favoris : ", nb_favoris_false)
print("Erreurs nombre de commentaires : ", nb_comments_false)
print("Erreurs nombre de morceaux : ", nb_tracks_false)

# pas d'erreur sur les stats d'écoutes de favoris et de commentaires

# vérification de la validité des album_id
d = {}
for elt in df["album_id"]:
    if elt not in d:
        d[elt] = 1
    else:
        d[elt] += 1

print("\nVérification des album_id : ")
# parcourir le dictionnaire d pour voir s'il n'y a pas une clé avec une valeur présente deux fois ou plus
count_duplicates = 0
for cle, valeur in d.items():
    if valeur > 1 :
        count_duplicates += 1
        print("Erreur album_id : ", cle, " apparait ", valeur, " fois")
    
if count_duplicates == 0:
    print("Tous les id sont uniques") # c'est le cas

count_negatives = 0
for elt in df["album_id"]:
    if elt < 0:
        count_negatives += 1

print("Erreurs id négatifs : ", count_negatives) # pas d'erreur


# on créé un nouveau fichier csv avec les données nettoyées
# df.to_csv("clean_albums.csv", index=False) 