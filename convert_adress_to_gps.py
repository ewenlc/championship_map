import pandas as pd
import time

#API pour convertir adresse en gps
from geopy.geocoders import Nominatim

# 1. Charger le fichier CSV d'entrée
df = pd.read_csv("adresses_clubs.csv", sep=';')

# 2. Initialiser le géocodeur
geolocator = Nominatim(user_agent="geo_app")

# 3. Créer les colonnes latitude et longitude
latitudes = []
longitudes = []

for adresse in df["Adresse"]:
    latitude = None
    longitude = None
    try:
        location = geolocator.geocode(adresse)
        if not location:
            # Première tentative : ajouter ", France"
            location = geolocator.geocode(adresse + ", France")

        if not location:
            # Dernière tentative : n'utiliser que la ville (ON UTILISE f DANS PRINT => {} pour variable)
            print(f"❌ Échec : {adresse} → tentative avec ville uniquement")
            ville_seule = adresse.split(',')[-1].strip() + ", France"

            #test voir si nom ville cohérent
            print(ville_seule)

            location = geolocator.geocode(ville_seule)

        if location:
            latitude = location.latitude
            longitude = location.longitude
            print(f"✅ Géocodé : {adresse} → {latitude}, {longitude}")
        else:
            print(f"🚫 Échec total : {adresse}")

    except Exception as e:
        print(f"❌ Erreur : {adresse} → {e}")

    # Ajouter les coordonnées (ou None) aux listes
    latitudes.append(latitude)
    longitudes.append(longitude)

    time.sleep(1)  # Respect des limites API (1 requête/sec)

# 4. Ajouter les coordonnées au DataFrame
df["latitude"] = latitudes
df["longitude"] = longitudes

# 5. Supprimer les lignes non géocodées
df_clean = df.dropna(subset=["latitude", "longitude"])

# 6. Sauvegarder dans un nouveau fichier
df_clean[["Equipe", "latitude", "longitude"]].to_csv("positions_avec_coords.csv", index=False)
print("✅ Fichier généré : positions_avec_coords.csv")
