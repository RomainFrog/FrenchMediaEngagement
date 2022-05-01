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
results = {x.username : {'id' : int(x.id), 'description' : x.description, 'public_metrics' : x.public_metrics, 'verified' : x.verified, 'location' : x.location} for x in client.get_users(usernames = usernames, user_fields=['description', 'public_metrics', 'verified', 'location']).data}

with open('accounts.json', 'w') as f:
	json.dump(results, f)

#tweepy get 5 tweets from account
tweets = {}
for user in results.values():
	tweets[user['id']] = client.get_users_tweets(user['id'], max_results=5, media_fields=['type', 'public_metrics'], tweet_fields=['created_at', 'geo', 'public_metrics', 'referenced_tweets'], user_auth=False)[0]


data = {}
for user_id, user in tweets.items():
	data[user_id] = []
	for tweet in user:
		data[user_id].append(tweet.data)

#save data json to file
with open('tweets.json', 'w') as f:
	json.dump(data, f)