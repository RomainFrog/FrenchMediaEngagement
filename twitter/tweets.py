#!/bin/python

import tweepy
import pickle

#Unpickle tweets.pickle
with open('tweets.pickle', 'rb') as f:
	tweets = pickle.load(f)

