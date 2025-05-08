import pandas as pd

#Folium est une bibliothèque Python qui permet de créer des cartes interactives dans un navigateur en utilisant Leaflet.js, 
# une bibliothèque JavaScript populaire pour la cartographie interactive.
import folium


from shapely.geometry import MultiPoint, Polygon, mapping

#UTILISE POUR GEOjson
import json

# 1. Charger les données CSV
df = pd.read_csv("positions_avec_coords.csv")

# 2. Créer une carte centrée sur la moyenne des points
center = [df["latitude"].mean(), df["longitude"].mean()]
m = folium.Map(location=center, zoom_start=10)

# 3. Ajouter un marqueur stylisé pour chaque point
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=7,
        color='navy',
        fill=True,
        fill_color='skyblue',
        fill_opacity=0.9,
        popup=folium.Popup(row['Equipe'], max_width=250),
    ).add_to(m)

# 4. Calculer l’enveloppe convexe (polygone qui englobe les points extrêmes)
points = [(lon, lat) for lat, lon in zip(df.latitude, df.longitude)]
convex_hull = MultiPoint(points).convex_hull

# 5. Créer l'objet GeoJSON du polygone sans interaction
geojson_polygon = {
    "type": "Feature",
    "properties": {},
    "geometry": mapping(Polygon(convex_hull.exterior.coords))
}

# 6. Ajouter le polygone à la carte en désactivant toute interaction
folium.GeoJson(
    geojson_polygon,
    name="Zone",
    style_function=lambda x: {
        "fillColor": "limegreen",
        "color": "black",
        "weight": 3,
        "fillOpacity": 0.2,
        "interactive": False  # ✅ Pas d'interaction
    }
).add_to(m)

# 7. Sauvegarder dans un fichier HTML
m.save("map_sans_interference.html")
print("✅ Carte générée : map_sans_interference.html")
