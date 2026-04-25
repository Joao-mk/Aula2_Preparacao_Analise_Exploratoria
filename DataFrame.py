import pandas as pd

artistas = pd.read_csv("spotify_artists_info_edited.csv", delimiter="\t")

#cria um dataframe para fazer um print bonito
num_ausente = artistas.isna(). sum()
porc = artistas.isna().sum() * 100/len(artistas)

df_artistas = pd.DataFrame(
    {
        "soma " : num_ausente,
        "porcentagem" : porc
    }
)

print(df_artistas)