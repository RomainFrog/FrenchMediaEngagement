#!/bin/python

#Connect to twitter using the API
import tweepy
import pickle
import json


config = {}
with open('.env') as json_file:
	data = json.load(json_file)
	config['bearer_token'] = data['BEARER_TOKEN']

client = tweepy.Client(config['bearer_token'])

#Generating a list of account:
usernames = ["lemondefr","franceinfo","France3tv","LeHuffPost","Le_Figaro","le_Parisien","LesEchos","lequipe","libe","LaCroix","humanite_fr","brutofficiel","BFMTV","mediavenir", "MediavenirPress","lobs","journalmetro","LaTribune","Valeurs","OuestFrance","CNEWS","20Minutes","canardenchaine","HugoDecrypte","Europe1","Qofficiel","LCI","FRANCE24"]
user_data = client.get_users(usernames = usernames, user_fields=['id', 'description', 'public_metrics', 'verified', 'location']).data
results = {}
for x in user_data:
	results[x.id] = {'username' : x.username, 'description' : x.description, 'public_metrics' : x.public_metrics, 'verified' : x.verified, 'location' : x.location}
with open('accounts.json', 'w') as f:
	json.dump(results, f)

#tweepy get MAX_RESULTS tweets from accounts
MAX_RESULTS = 100
tweets = {}
for user_id, user in results.items():
	tweets[user_id] = client.get_users_tweets(user_id, max_results=MAX_RESULTS, media_fields=['type', 'public_metrics'], tweet_fields=['created_at', 'geo', 'public_metrics', 'referenced_tweets'], user_auth=False)[0]

data = {}
for user_id, user in tweets.items():
	data[user_id] = []
	for tweet in user:
		data[user_id].append(tweet.data)

#save data json to file
with open('tweets.json', 'w') as f:
	json.dump(data, f)
