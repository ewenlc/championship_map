# Import des bibliothèques
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests

# pour supprimer indésirable dans acquisition de données (ici numéros et "-")
import re

######################################################################################################################################

# URL Ciblée
url = 'https://competitions.ffbb.com/ligues/pdl/comites/0044/competitions/dm3/classement?phase=200000002864683&poule=200000003006254'

######################################################################################################################################

#AVEC CETTE COMMANDE NE DETECTE PAS DE USER-AGENT
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

# Récupération des infos du site

#names = soup.find_all('a', attrs={'class': 'tw-leading-[1.625rem]'})
names = soup.find_all('div', attrs={'class': 'min-w-[228px]'})

# Création des listes vides
hw_title = []

# Peuplement des listes avec les résultats souhaités
for item in names:
    text = item.text.replace("\n", "").strip()
    # Supprimer les "- numéro" à la fin
    clean_text = re.sub(r"\s*-\s*\d+$", "", text)
    hw_title.append(clean_text)

######################################################################################################################################

# Création d'un dataframe, puis export en csv.
df = pd.DataFrame(list(zip(hw_title)), columns=['Equipes'])
df.to_csv('scraper_ffbb_1.csv', index=False, sep=';', encoding='utf-8', quoting=1)

######################################################################################################################################


#TEST QU'ON CAPTE BIEN DES CHOSES

print(response.status_code)
print(soup.prettify()[:2000])  # Les 2000 premiers caractères du HTML récupéré