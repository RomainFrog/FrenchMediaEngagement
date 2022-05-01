#!/bin/python

import tweepy
import json

#Open json data
with open('tweets.json') as json_file:
	tweets = json.load(json_file)

print(tweets)