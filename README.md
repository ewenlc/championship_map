# 📌 CHAMPIONSHIP basket MAP

L'objectif est de creer une carte interactive representant les perimetres englobant les différentes equipes d'un championnat. Donner une meilleure approche graphique des distances entre différentes équipes d'une meme competition.

The goal is to create an interactive map representing the perimeters encompassing the different teams in a championship. This provides a better graphical approach to the distances between different teams in the same competition.

## 🔗 Sommaire

- [🚀 Fonctionnalités (Features)](#-fonctionnalités)
- [🙋 Contact](#-contact)
- [🔧 Tester](#Tester)

---

## 🚀 Fonctionnalités

- Scrapping des pages de championnats ffbb (récuperer club/ville et classer celon poules)
- Creer carte intéractive + menu permettant d'observer chaque poule sur la carte.
-----------------------------------------------------------------------------------------------

- Scraping FFBB championship pages (retrieving clubs/cities and sorting them by group)
- Creating an interactive map + a menu allowing you to view each group on the map.
---

## 🔧 Tester 

Première partie : (Scrapping des pages de championnats ffbb (récuperer club/ville et classer celon poules)

Pour récuperer dans un fichier csv les équipes ainsi que l'adresse de leur salle de basket d'une poule (présente sur le site https://competitions.ffbb.com/). Il vous suffit de coller le lien de la page de la poule à analyser (exemple pour la poule F phase 2 D3 loire-atlantique : (https://competitions.ffbb.com/ligues/pdl/comites/0044/competitions/dm3/classement?phase=200000002864683&poule=200000003006254) dans l'espace réserver à celui ci dans le code scraper_ffbb_2.py.

exemple de rendu :

| Équipe                                           | Adresse                                  |
|--------------------------------------------------|-------------------------------------------|
| GROUPE ST VINCENT LE PALLET                     | RUE DES SPORTS, 44330 Le Pallet           |
| BASKET CLUB BASSE GOULAINE                      | SQUARE DE THELEY, 44115 Basse-Goulaine    |
| IE - CTC ERDRE CANAL - BASKET CLUB SUCE/ERDRE   | IMPASSE DU LEVANT, 44240 Sucé-sur-Erdre   |
| MONTBERT GENESTON LE BIGNON B.                  | Stade Municipal, 44140 Montbert           |
| ASPTT NANTES                                    | 38 RUE APPERT, 44100 Nantes               |
| USVR VARADES BASKET                             | 450 Rue du Parc, 44370 Varades            |



Deuxième partie : (Convertir les adresses en position GPS)

Ce projet utilise actuellement l’API Nominatim (OpenStreetMap) via la bibliothèque Python geopy pour convertir des adresses postales en coordonnées GPS (latitude / longitude).

Pourquoi ce choix ?
<br><br>
Gratuite et sans inscription.<br>
Basée sur OpenStreetMap, donc open source.

⚠️ Limites de Nominatim
Nominatim est très utile, mais présente des limitations :

Certaines adresses mal structurées ou incomplètes ne sont pas reconnues.<br>
Les adresses trop générales ou locales (ex : "Stade Municipal") sont souvent mal interprétées ou non géocodées, problème qu'on a résolu en remplacant l'adresse non exact par le nom de la commune uniquement. Ce changement nous permet d'avoir une adresse au détriement de la précision.

🚀 Évolution prévue : bascule vers une API plus robuste
Pour améliorer la précision et la couverture, une future version pourra utiliser l’API Google Maps Geocoding :

✅ Plus fiable pour les adresses incomplètes ou ambigües
✅ Renvoie un score de confiance et des types de lieux précis
❗️ Requiert une clé API et l’activation de la facturation (crédit gratuit de 200 $/mois)

🛠️ Améliorations possibles
Ajout d’un fallback automatique : Nominatim → Google Maps API
Enregistrement des adresses échouées pour correction manuelle
Cache local des géocodages pour éviter les appels répétés


---------------------------------------------------------------------------------------------

Part One: (Scraping the FFBB championship pages (retrieve club/city and sort by group))

To retrieve the teams and the address of their basketball venues from a group (available on the website https://competitions.ffbb.com/) in a csv file, simply paste the link to the group page to analyze (example for Group B Phase 2 D3 Loire-Atlantique: https://competitions.ffbb.com/ligues/pdl/comites/0044/competitions/dm3/classement?phase=200000002864683&poule=200000003006250) into the space provided in the scraper_ffbb_2.py code.





## 🙋 Contact

Tu peux me retrouver ici : 

- GitHub: @ewenlc
- LinkedIn: Ewen Le Callet (www.linkedin.com/in/ewen-le-callet-4b30282a8)
- Email: ewen.lecallet@gmail.com
