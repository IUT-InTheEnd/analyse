import pandas as pd

# import from csv
df = pd.read_csv("./dataset/raw_tracks.csv")

# track date recorded : 103283 / 109727 qui sont NaN
# Les attributs suivants ne sont pas intéressantes à traiter ou manque de données
df = df.drop(columns=["album_title","album_url","artist_name","artist_url","artist_website",
                      "license_image_file","track_image_file","license_url","tags","track_bit_rate",
                      "track_comments","track_copyright_c","track_copyright_p","track_disc_number",
                      "track_explicit_notes","track_url","track_file","track_information",
                      "track_lyricist","track_number","track_publisher","license_image_file_large",
                      "track_date_recorded", "license_title","track_composer"
                ])

'''
Attributs retenus :
    - track_id : identifiant unique de la musique
    - album_id : identifiant unique de l'album
    - artist_id : identifiant unique de l'artiste
    - license_parent_id : identifiant de la licence
    - track_language_code : code de la langue du morceau
    - track_date_created : date d'ajout du morceau sur la plateforme
    - track_duration : durée du morceau
    - track_explicit : indique si le morceau est explicite ou non (valeurs possibles : "Radio-Safe", "Radio-Unsafe","Adults-Only")
    - track_favorites : nombre de favoris sur le morceau
    - track_genres : genres associés au morceau
    - track_instrumental : indique si le morceau est instrumental ou non (valeurs possibles : 0 ou 1)
    - track_interest : score d'intérêt du morceau (FMA)
    - track_listens : nombre d'écoutes du morceau
    - track_title : titre du morceau
'''

# track_explicit treatment (NaN -> Radio-Safe)
df_temp = df["track_explicit"].fillna("Radio-Safe")
df["track_explicit"] = df_temp

# export to csv
df.to_csv("./cleaned_dataset/clean_raw_tracks.csv",index=False)
