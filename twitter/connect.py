#!/bin/python

#Connect to twitter using the API
import tweepy
import pickle
import json

class config:
	def __init__(self):
		with open('.env') as json_file:
			data = json.load(json_file)
			self.bearer_token = data['BEARER_TOKEN']

config = {}
with open('.env') as json_file:
	data = json.load(json_file)
	config['bearer_token'] = data['BEARER_TOKEN']

#print(config)
client = tweepy.Client(config['bearer_token'])

#tweepy get 50 tweets from account
#tweets = client.user_timeline("@realDonaldTrump", count=50)

result = client.get_users_tweets(24744541, max_results=5, user_auth=False)


#save result Pickle
with open('tweets.pickle', 'wb') as f:
	pickle.dump(result[0], f)


#save result pickle