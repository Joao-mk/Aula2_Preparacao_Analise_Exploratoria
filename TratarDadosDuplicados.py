import pandas as pd

artistas = pd.read_csv("spotify_artists_info_edited.csv", delimiter="\t")

Q1 = artistas['followers'].quantile(0.25)
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