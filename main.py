import pandas as pd

artistas = pd.read_csv("spotify_artists_info_edited.csv", delimiter="\t")

# mostra colunas com lihnas vazias
'''
print(artistas.isna())

#mostra a quantidade de linhas vazia em uma coluna expecifica, neste caso na coluna popularity
sumaVazio =sum((artistas['popularity'].isna()))
print(sumaVazio)
#-------------------------------

#cria um dataframe para fazer um print bonito
num_ausente = artistas.isna(). sum()
porc = artistas.isna().sum() * 100/len(artistas)

df_artistas = pd.DataFrame(
    {
        "soma " : num_ausente,
        "porcentagem" : porc
    }
)

#verifica o tipo de dados
print(artistas.dtypes)

#-----------------------------------------------------------------------------
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

'''
#-------------------------------------------------------------------------------

#Limpar Ruidos
import ast

try:
    artistas["genres"] = artistas["genres"].apply(ast.literal_eval)
    print("Coluna 'genres' string para lista python com sucesso. ")
    print(f"Exemplo de tipo de dados em 'genres' após a conversão: {type(artistas['genres'].iloc[0])}")
except Exception as e:
    print(f"Erro ao converter 'genres'. {e}")
print("")    

#-------------------------------------------------------------------------------

#tratar dados atipicos

#dados duplicados