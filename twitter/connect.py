#!/bin/python

#Connect to twitter using the API
import tweepy
import pickle
import json

config = {}
with open('.env') as json_file:
	data = json.load(json_file)
	config['bearer_token'] = data['BEARER_TOKEN']

#print(config)
client = tweepy.Client(config['bearer_token'])

#tweepy get 5 tweets from account
result = client.get_users_tweets(24744541, max_results=5, user_auth=False)

data = []
for tweet in result[0]:
	data.append(tweet.data)

#save data json to file
with open('tweets.json', 'w') as f:
	json.dump(data, f)