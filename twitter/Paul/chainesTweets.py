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

#Chargement des données des chainesDict
with open("accounts.json") as json_data:
    chainesDict = json.load(json_data)

MAX_RESULTS = 5
tweets = {}
for chaines in chainesDict.values():

     userTweets = client.get_users_tweets(chaines["id"], max_results = MAX_RESULTS, media_fields=['alt_text','duration_ms','height','media_key','non_public_metrics','organic_metrics','preview_image_url','promoted_metrics','public_metrics','type','url','width'], user_auth=False).data
     #print(userTweets)
     for x in userTweets:

         #infoTweet = client.get_tweet(x.id,tweet_fields=["created_at","text","conversation_id","public_metrics","lang","geo"],expansions= ["author_id","attachments.media_keys"], user_auth=False).data
		 #https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id
         #print(infoTweet,"\n\n")

         #tweets[chaines['id']] ={ x.id :  {'text' : x.text,'alt_text' : x.alt_text}}
		 #tweets[chaines['id']] ={'text' : x.text}
		 #, 'duration_ms' : x.duration_ms, 'height' : x.height, 'media_key' : x.media_key, 'non_public_metrics' : x.non_public_metrics, 'organic_metrics' : x.organic_metrics,'preview_image_url' : x.preview_image_url,'promoted_metrics' : x.promoted_metrics,'public_metrics' : x.public_metrics,'type' : x.type,'url' : x.url,'width' : x.width
         """Pas plus d'info ? """


with open('tweets.json', 'w') as f:
    json.dump(tweets, f)
