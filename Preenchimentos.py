import pandas as pd

artistas = pd.read_csv("spotify_artists_info_edited.csv", delimiter="\t")

#isna faz a verificação das linhas vazias, no caso da coluna especifica popularity

sumaVazio =sum((artistas['popularity'].isna()))
print(sumaVazio)

#preenche colunas vazia com uma media

mediana_pop = artistas['popularity'].median()
artistas["popularity"] = artistas["popularity"].fillna(mediana_pop)
print(f"{sumaVazio} Nulos em 'popularity' preenchidos com mediana: {mediana_pop}")

artistas['genres'] = artistas["genres"].fillna("['Não classificado']")
sumaVazioGenres = sum(artistas["genres"].isna())
print(f"{sumaVazioGenres} Nulos em 'genres' preenchidos com a mensagem padrão '[\"Não classificado\"]'")

artistas['image_url'] = artistas["image_url"].fillna('URL indisponivel')
sumaVazioImagem = sum(artistas["image_url"].isna())
print(f"{sumaVazioImagem} Nulos em 'imagem_url' preenchidos com a imagem padrão 'URL indisponivel'")

vazioRestante = artistas.isna().sum()
print(f"{vazioRestante}")