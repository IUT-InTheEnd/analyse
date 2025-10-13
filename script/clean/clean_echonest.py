import pandas as pd
import os
import numpy as np

# On utilise echonest.csv parce que les lignes avec de la data vide est supprimé
# J'ai esssayé de récupérer la donnée via l'API spotify mais impossible car les musics ne sont pas sur la platforme.


#,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest,echonest
#,audio_features,audio_features,audio_features,audio_features,audio_features,audio_features,audio_features,audio_features,metadata,metadata,metadata,metadata,metadata,metadata,metadata,ranks,ranks,ranks,ranks,ranks,social_features,social_features,social_features,social_features,social_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features,temporal_features
#,acousticness,danceability,energy,instrumentalness,liveness,speechiness,tempo,valence,album_date,album_name,artist_latitude,artist_location,artist_longitude,artist_name,release,artist_discovery_rank,artist_familiarity_rank,artist_hotttnesss_rank,song_currency_rank,song_hotttnesss_rank,artist_discovery,artist_familiarity,artist_hotttnesss,song_currency,song_hotttnesss,000,001,002,003,004,005,006,007,008,009,010,011,012,013,014,015,016,017,018,019,020,021,022,023,024,025,026,027,028,029,030,031,032,033,034,035,036,037,038,039,040,041,042,043,044,045,046,047,048,049,050,051,052,053,054,055,056,057,058,059,060,061,062,063,064,065,066,067,068,069,070,071,072,073,074,075,076,077,078,079,080,081,082,083,084,085,086,087,088,089,090,091,092,093,094,095,096,097,098,099,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223
#,track_id,,,,,,,,,,,,,,,,,,,,,,,
def fusion_headers(df):
    "fusionne les quatres premières lignes du fichier en un seul header"
    "echonest_audio_features_acousticness"
    # fusionne les quatres premières lignes du fichier en un seul header
    if df.shape[0] < 4:
        return df

    new_header = []
    for i in range(df.shape[1]):
        vals = [df.iat[r, i] for r in range(4)]
        # vérifier si les 4 valeurs sont non-nulles et identiques après strip
        cleaned = [str(v).strip() for v in vals]
        non_null = [c for c, v in zip(cleaned, vals) if not pd.isna(v) and c != ""]
        all_equal = (len(non_null) == 4) and (len(set(cleaned)) == 1)
        if all_equal:
            header = cleaned[0]
        else:
            # ne garder que les parties non-nulles pour éviter des underscores inutiles
            if non_null:
                header = "_".join(non_null)
            else:
                header = ""
        new_header.append(header)

    df.columns = new_header
    df = df.iloc[4:].reset_index(drop=True)

    # regrouper les colonnes numériques (000..223) en une seule colonne 'echonest_vector'
    vector_cols = [c for c in df.columns if str(c).strip().isdigit()]
    if vector_cols:
        # trier par valeur numérique pour garder l'ordre
        vector_cols = sorted(vector_cols, key=lambda x: int(str(x)))
        # convertir les valeurs en float/NaN et créer des listes
        df['echonest_vector'] = df[vector_cols].apply(
            lambda row: [ (float(x) if (not pd.isna(x) and str(x).strip() != "") else np.nan) for x in row.values ],
            axis=1
        )
        df = df.drop(columns=vector_cols)

    return df    

def suppr_colonne_inutile(df):
    column_a_supprimer_csv = 'echonest_metadata_album_date,echonest_metadata_album_name,echonest_metadata_artist_latitude,echonest_metadata_artist_location,echonest_metadata_artist_longitude,echonest_metadata_artist_name,echonest_metadata_release,echonest_ranks_artist_discovery_rank,echonest_ranks_artist_familiarity_rank,echonest_ranks_artist_hotttnesss_rank,echonest_ranks_song_currency_rank,echonest_ranks_song_hotttnesss_rank,echonest_temporal_features_000,echonest_temporal_features_001,echonest_temporal_features_002,echonest_temporal_features_003,echonest_temporal_features_004,echonest_temporal_features_005,echonest_temporal_features_006,echonest_temporal_features_007,echonest_temporal_features_008,echonest_temporal_features_009,echonest_temporal_features_010,echonest_temporal_features_011,echonest_temporal_features_012,echonest_temporal_features_013,echonest_temporal_features_014,echonest_temporal_features_015,echonest_temporal_features_016,echonest_temporal_features_017,echonest_temporal_features_018,echonest_temporal_features_019,echonest_temporal_features_020,echonest_temporal_features_021,echonest_temporal_features_022,echonest_temporal_features_023,echonest_temporal_features_024,echonest_temporal_features_025,echonest_temporal_features_026,echonest_temporal_features_027,echonest_temporal_features_028,echonest_temporal_features_029,echonest_temporal_features_030,echonest_temporal_features_031,echonest_temporal_features_032,echonest_temporal_features_033,echonest_temporal_features_034,echonest_temporal_features_035,echonest_temporal_features_036,echonest_temporal_features_037,echonest_temporal_features_038,echonest_temporal_features_039,echonest_temporal_features_040,echonest_temporal_features_041,echonest_temporal_features_042,echonest_temporal_features_043,echonest_temporal_features_044,echonest_temporal_features_045,echonest_temporal_features_046,echonest_temporal_features_047,echonest_temporal_features_048,echonest_temporal_features_049,echonest_temporal_features_050,echonest_temporal_features_051,echonest_temporal_features_052,echonest_temporal_features_053,echonest_temporal_features_054,echonest_temporal_features_055,echonest_temporal_features_056,echonest_temporal_features_057,echonest_temporal_features_058,echonest_temporal_features_059,echonest_temporal_features_060,echonest_temporal_features_061,echonest_temporal_features_062,echonest_temporal_features_063,echonest_temporal_features_064,echonest_temporal_features_065,echonest_temporal_features_066,echonest_temporal_features_067,echonest_temporal_features_068,echonest_temporal_features_069,echonest_temporal_features_070,echonest_temporal_features_071,echonest_temporal_features_072,echonest_temporal_features_073,echonest_temporal_features_074,echonest_temporal_features_075,echonest_temporal_features_076,echonest_temporal_features_077,echonest_temporal_features_078,echonest_temporal_features_079,echonest_temporal_features_080,echonest_temporal_features_081,echonest_temporal_features_082,echonest_temporal_features_083,echonest_temporal_features_084,echonest_temporal_features_085,echonest_temporal_features_086,echonest_temporal_features_087,echonest_temporal_features_088,echonest_temporal_features_089,echonest_temporal_features_090,echonest_temporal_features_091,echonest_temporal_features_092,echonest_temporal_features_093,echonest_temporal_features_094,echonest_temporal_features_095,echonest_temporal_features_096,echonest_temporal_features_097,echonest_temporal_features_098,echonest_temporal_features_099,echonest_temporal_features_100,echonest_temporal_features_101,echonest_temporal_features_102,echonest_temporal_features_103,echonest_temporal_features_104,echonest_temporal_features_105,echonest_temporal_features_106,echonest_temporal_features_107,echonest_temporal_features_108,echonest_temporal_features_109,echonest_temporal_features_110,echonest_temporal_features_111,echonest_temporal_features_112,echonest_temporal_features_113,echonest_temporal_features_114,echonest_temporal_features_115,echonest_temporal_features_116,echonest_temporal_features_117,echonest_temporal_features_118,echonest_temporal_features_119,echonest_temporal_features_120,echonest_temporal_features_121,echonest_temporal_features_122,echonest_temporal_features_123,echonest_temporal_features_124,echonest_temporal_features_125,echonest_temporal_features_126,echonest_temporal_features_127,echonest_temporal_features_128,echonest_temporal_features_129,echonest_temporal_features_130,echonest_temporal_features_131,echonest_temporal_features_132,echonest_temporal_features_133,echonest_temporal_features_134,echonest_temporal_features_135,echonest_temporal_features_136,echonest_temporal_features_137,echonest_temporal_features_138,echonest_temporal_features_139,echonest_temporal_features_140,echonest_temporal_features_141,echonest_temporal_features_142,echonest_temporal_features_143,echonest_temporal_features_144,echonest_temporal_features_145,echonest_temporal_features_146,echonest_temporal_features_147,echonest_temporal_features_148,echonest_temporal_features_149,echonest_temporal_features_150,echonest_temporal_features_151,echonest_temporal_features_152,echonest_temporal_features_153,echonest_temporal_features_154,echonest_temporal_features_155,echonest_temporal_features_156,echonest_temporal_features_157,echonest_temporal_features_158,echonest_temporal_features_159,echonest_temporal_features_160,echonest_temporal_features_161,echonest_temporal_features_162,echonest_temporal_features_163,echonest_temporal_features_164,echonest_temporal_features_165,echonest_temporal_features_166,echonest_temporal_features_167,echonest_temporal_features_168,echonest_temporal_features_169,echonest_temporal_features_170,echonest_temporal_features_171,echonest_temporal_features_172,echonest_temporal_features_173,echonest_temporal_features_174,echonest_temporal_features_175,echonest_temporal_features_176,echonest_temporal_features_177,echonest_temporal_features_178,echonest_temporal_features_179,echonest_temporal_features_180,echonest_temporal_features_181,echonest_temporal_features_182,echonest_temporal_features_183,echonest_temporal_features_184,echonest_temporal_features_185,echonest_temporal_features_186,echonest_temporal_features_187,echonest_temporal_features_188,echonest_temporal_features_189,echonest_temporal_features_190,echonest_temporal_features_191,echonest_temporal_features_192,echonest_temporal_features_193,echonest_temporal_features_194,echonest_temporal_features_195,echonest_temporal_features_196,echonest_temporal_features_197,echonest_temporal_features_198,echonest_temporal_features_199,echonest_temporal_features_200,echonest_temporal_features_201,echonest_temporal_features_202,echonest_temporal_features_203,echonest_temporal_features_204,echonest_temporal_features_205,echonest_temporal_features_206,echonest_temporal_features_207,echonest_temporal_features_208,echonest_temporal_features_209,echonest_temporal_features_210,echonest_temporal_features_211,echonest_temporal_features_212,echonest_temporal_features_213,echonest_temporal_features_214,echonest_temporal_features_215,echonest_temporal_features_216,echonest_temporal_features_217,echonest_temporal_features_218,echonest_temporal_features_219,echonest_temporal_features_220,echonest_temporal_features_221,echonest_temporal_features_222,echonest_temporal_features_223'
    colonnes_a_supprimer = column_a_supprimer_csv.split(',')
    df = df.drop(columns=colonnes_a_supprimer, errors='ignore')
    return df

def verifie_valeurs(df):
    # vérifie les colonnes qui ne sont pas track_id et echonest_audio_features_tempo si elles ont des valeurs entre 0 et 1
    for col in df.columns:
        if col not in ['track_id', 'echonest_audio_features_tempo']:
            for val in df[col]:
                try:
                    fval = float(val)
                    if fval < 0 or fval > 1:
                        print(f"Valeur hors de l'intervalle dans la colonne {col}: {val}")
                except ValueError:
                    print(f"Valeur non numérique dans la colonne {col}: {val}")
        # vérifie que la colonne echonest_audio_features_tempo n'a pas de valeur négative
        elif col == 'echonest_audio_features_tempo':
            for val in df[col]:
                try:
                    fval = float(val)
                    if fval < 0:
                        print(f"Valeur négative dans la colonne {col}: {val}")
                except ValueError:
                    print(f"Valeur non numérique dans la colonne {col}: {val}")

fichier = 'echonest.csv'
chemin = '../../dataset/'
chemin_clean = '../../cleaned_dataset/'

if os.path.exists(chemin + fichier):
    df = pd.read_csv(chemin + fichier, header=None, low_memory=False)
    df = fusion_headers(df)
    # enregistrer le fichier nettoyé
    df = suppr_colonne_inutile(df)
    verifie_valeurs(df)
    df.to_csv(chemin_clean + 'clean_' + fichier, index=False)
    
    
    
    

    

