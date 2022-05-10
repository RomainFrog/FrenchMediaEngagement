import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from searchtweets import load_credentials
import tweepy
import json

#Création du dictionnaire KEYS
with open('KEY.env') as json_file:
	KEYS = json.load(json_file)

#Connection Client
client = tweepy.Client(KEYS['BEARER_TOKEN'],KEYS['API_KEY'], KEYS['API_KEY_SECRET'], KEYS['ACCES_TOKEN'], KEYS['ACCES_TOKEN_SECRET'])

#Création de la liste d'id des chaines twitter
list_chaine = ["lemondefr","franceinfo","France3TV","LeHuffPost","Le_Figaro","le_Parisien","LesEchos","lequipe","libe","LaCroix","humanite_fr","brutofficiel","BFMTV","MediavenirPress","lobs","journalmetro","LaTribune","Valeurs","OuestFrance","CNEWS","20Minutes","canardenchaine","HugoDecrypte","Europe1","Qofficiel","LCI","FRANCE24"]

#Obtention des données des chaines ["description","public_metrics","verified","location"]
chaines = client.get_users(usernames = list_chaine, user_fields=["description","public_metrics","verified","location"]).data
resultat_list = {x.username : {"id" : int(x.id), "description" : x.description, "public_metrics" : x.public_metrics, "verified" : x.verified, "location" : x.location} for x in chaines}
with open('accounts.json', 'w') as f:
    json.dump(resultat_list, f)

#tweepy get 5 tweets from account
#result = client.get_users_tweets(24744541, max_results=5, user_auth=False)
