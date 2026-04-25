import pandas as pd

artistas = pd.read_csv("spotify_artists_info_edited.csv", delimiter="\t")

print(artistas["genres"].isna().sum())
#Limpar Ruidos
import ast

try:
    #artistas["genres"] = artistas["genres"].apply(ast.literal_eval)
    artistas["genres"] = artistas["genres"].apply(
        lambda x: ast.literal_eval(x) if pd.notna(x) else []
    )
    print("Coluna 'genres' string para lista python com sucesso. ")
    print(f"Exemplo de tipo de dados em 'genres' após a conversão: {type(artistas['genres'].iloc[0])}")
except Exception as e:
    print(f"Erro ao converter 'genres'. {e}")
print("")    




