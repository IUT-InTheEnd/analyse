import pandas as pd

df = pd.read_csv("./dataset/raw_tracks.csv")

# track date recorded : 103283 / 109727 qui sont NaN
# les autres attributs ne sont pas intéressantes à traiter ou manque de données
df = df.drop(columns=["album_title","album_url","artist_name","artist_url","artist_website",
                      "license_image_file","track_image_file","license_url","tags","track_bit_rate",
                      "track_comments","track_copyright_c","track_copyright_p","track_disc_number",
                      "track_explicit_notes","track_url","track_file","track_information","track_language_code",
                      "track_lyricist","track_number","track_publisher","license_image_file_large",
                      "track_date_recorded", "license_title","track_composer"
                ])

# track_explicit treatment (NaN -> Radio-Safe)
df_temp = df["track_explicit"].fillna("Radio-Safe")
df["track_explicit"] = df_temp

df.to_csv("./cleaned_dataset/clean_raw_tracks.csv",index=False)



