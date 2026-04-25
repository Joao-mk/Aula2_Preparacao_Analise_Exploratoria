import pandas as pd

artistas = pd.read_csv("spotify_artists_info_edited.csv", delimiter="\t")

# mostra colunas com lihnas vazias

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


#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------

#tratar dados atipicos
Q1 = artistas['followers'].quantile(0.75)
Q3 = artistas['followers'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - (1.5 * IQR)
limite_superior = Q3 + (1.5 * IQR)

print(f"Range normal de seguidores (IQR): {limite_inferior:.0f} a {limite_superior:.0f}")

outliers = artistas[(artistas['followers']< limite_inferior) | (artistas['followers']> limite_superior)]
print(f"\nEncontrados {len(outliers)} outliers na coluna 'followers'.\n")

if len(outliers) >0:
    print("Top 5 artistas mais seguidos (outliers): ")
    print(outliers.nlargest(5, 'followers')[['name', 'followers']])

#dados duplicados
ID_Duplicados = artistas.duplicated(subset=['artist_id']).sum()

if ID_Duplicados > 0:
    print(f"Encontrados {ID_Duplicados} duplicados na coluna 'artist_id'")
    artistas = artistas.drop.duplicatas(subnet=['artist_id'], keep='firts')
else:
    print("Não há duplicatas na coluna 'artist_id'")
print(f"Formato após a remoção de duplicatas: {artistas.shape}\n")
