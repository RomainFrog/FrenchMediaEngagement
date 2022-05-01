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

usernames = ['lemondefr', 'mediavenir']
results = {x.username : [x.id, x.description, x.public_metrics, x.verified, x.location] for x in client.get_users(usernames = usernames, user_fields=['description', 'public_metrics', 'verified', 'location']).data}

with open('accounts.json', 'w') as f:
	json.dump(results, f)

#tweepy get 5 tweets from account
#Le Monde FR
#for user in results:
#	result[user] = []
#	result[user].append(client.get_users(24744541))
#info = client.get_users(24744541)

"""
result = client.get_users_tweets(24744541, max_results=5, user_auth=False)
data = []
for tweet in result[0]:
	data.append(tweet.data)

#save data json to file
with open('tweets.json', 'w') as f:
	json.dump(data, f)

"""