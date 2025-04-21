# Import des bibliothèques
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests

#pour eviter de surcharger de requete
import time


# pour supprimer indésirable dans acquisition de données (ici numéros et "-")
import re

######################################################################################################################################

# URL Ciblée
url = 'https://competitions.ffbb.com/ligues/pdl/comites/0044/competitions/dm3/classement?phase=200000002864683&poule=200000003006256'

######################################################################################################################################

#AVEC CETTE COMMANDE NE DETECTE PAS DE USER-AGENT faux
#page_hw = urlopen(url)
#soup = BeautifulSoup(page_hw, 'html.parser')

#POUR ETRE CONSIDERER COMME UTILISATEUR
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

# Initialisation de BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')


######################################################################################################################################

# Récupération des infos de la poule (nom equipe + url page équipe)



# Création des listes vides
teams = []

#constante pour le début de chaque url de ce site (ffbb)
base_url = "https://competitions.ffbb.com"


#divs=balise pour les équipes d'une poule sur la page de classement
divs = soup.find_all('div', attrs={'class': 'min-w-[228px]'})

#TEST POUR VOIR SI BIEN 6 éléments trouvés (nb d'équipes)
#print(f"Nombre de divs trouvés : {len(divs)}")


for item in soup.find_all('div', attrs={'class': 'min-w-[228px]'}):
    text = item.text.replace("\n", "").strip()#ici on prend le nom de l'équipe
    clean_text = re.sub(r"\s*-\s*\d+$", "", text)
    
    parent_a = item.find_parent('a')#ici on prend le lien vers la page de l'équipe dans la balise parents
    href = parent_a.get('href') if parent_a else None

    if href:
        link = base_url + href  # ici on garde bien le https
        teams.append((clean_text, link))
    else:
        print(f"⚠️ Aucun lien pour l'équipe : {clean_text}")

for team in teams:
    print(team)


######################################################################################################################################

# Pour chaque équipe : aller sur la page, trouver club, aller sur page club, prendre l'adresse


# Liste pour stocker résultats finaux
results = []



for team_name, team_url in teams:
    print(f"Traitement de l’équipe : {team_name}")

    try:
        team_resp = requests.get(team_url, headers=headers)#permet de se rendre sur l'url
        team_soup = BeautifulSoup(team_resp.text, 'html.parser')#permet de se rendre sur l'url

        # Trouver tous les liens avec la classe 'capitalize'
        club_links = team_soup.find_all('a', class_='capitalize')

        # Vérifier que nous avons suffisamment de liens
        if len(club_links) >= 4:
            # Sélectionner le quatrième lien (index 3) ON A REMARQUE QUE TOUJOURS LE 4e lien
            club_link_tag = club_links[3]
            club_url = base_url + club_link_tag.get('href')
            print(f"Lien vers le club : {club_url}")
        else:
            print(f"❌ Aucun lien vers le club trouvé pour {team_name}")

        # Aller sur la page info du club

        club_info_url = club_url + "#informations"#structure de l'url pour infos
        club_resp = requests.get(club_info_url, headers=headers)
        club_soup = BeautifulSoup(club_resp.text, 'html.parser')


        # Trouver l'adresse dans les balises (car beaucoup avec meme classe donc on filtre)

        blocks = club_soup.select('div.flex.flex-col.gap-\\[10px\\]')

        # Parcourir pour trouver celui qui contient le mot "Salle"
        for block in blocks:
            title = block.find('div', class_='text-base font-bold')
            if title and 'Salle' in title.text:
                salle_block = block
                break


        # Chercher le span qui contient "Adresse"
        adresse_label = salle_block.find('span', string='Adresse')

        if adresse_label:
            # L'adresse est probablement dans le span frère suivant
            adresse_span = adresse_label.find_next('span')
            adresse = adresse_span.text.strip()
            print("Adresse trouvée :", adresse)
        else:
            print("Adresse non trouvée")

        results.append((team_name, adresse))

        # Petit délai pour éviter d’être bloqué par le serveur
        time.sleep(1)

    except Exception as e:
        print(f"⚠️ Erreur pour {team_name} : {e}")
        continue


######################################################################################################################################

# Création d'un dataframe, puis export en csv

df_address = pd.DataFrame(results, columns=['Equipe', 'Adresse'])
df_address.to_csv('adresses_clubs.csv', index=False, sep=';', encoding='utf-8', quoting=1)

######################################################################################################################################


#TEST QU'ON CAPTE BIEN DES CHOSES (cas où dynamique)

#print(response.status_code)
#print(soup.prettify()[:2000])  # Les 2000 premiers caractères du HTML récupéré