import pandas as pd

artistas = pd.read_csv("spotify_artists_info_edited.csv", delimiter="\t")

ID_Duplicados = artistas.duplicated(subset=['artist_id']).sum()

if ID_Duplicados > 0:
    print(f"Encontrados {ID_Duplicados} duplicados na coluna 'artist_id'")
    artistas = artistas.drop.duplicatas(subnet=['artist_id'], keep='firts')
else:
    print("Não há duplicatas na coluna 'artist_id'")
print(f"Formato após a remoção de duplicatas: {artistas.shape}\n")
