#!/bin/python

import tweepy
import json
from statistics import mean

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Open json data
with open('tweets.json') as json_file:
	tweets_data = json.load(json_file)

with open('accounts.json') as json_file:
	author_data = json.load(json_file)

'''
#Somme des likes par médias, avec infos sur lui
result = {}
for author, tweets in tweets_data.items():
	result[author] = [0, 0, 0, 0, 0]
	for t in tweets:
		if int(t['created_at'].split("-")[2].split("T")[0]) == 10:
			result[author][0] += t['public_metrics']['retweet_count']
			result[author][1] += t['public_metrics']['reply_count']
			result[author][2] += t['public_metrics']['like_count']
			result[author][3] += t['public_metrics']['quote_count']
			result[author][4] += 1

average=[0,0,0,0,0]
retweet=[]
reply=[]
like=[]
quote=[]

for author, a_data in author_data.items():
	if(result[author][4] == 0 or a_data['username'] == "Mediavenir"): continue
	print(a_data['username'] + ": \t" + str(result[author]))
	# print(f"\tFollowers :\t{a_data['public_metrics']['followers_count']}")
	# print(f"\tListed :\t{a_data['public_metrics']['listed_count']}")
	# print(f"Retweet/Followers : {result[author][0]/a_data['public_metrics']['followers_count']}")
	# print(f"Reply/Followers : {result[author][1]/a_data['public_metrics']['followers_count']}")
	# print(f"Like/Followers : {result[author][2]/a_data['public_metrics']['followers_count']}")
	# print(f"Quote/Followers : {result[author][3]/a_data['public_metrics']['followers_count']}")
	print("Today")
	retweet.append(result[author][0]/a_data['public_metrics']['followers_count']/result[author][4])
	reply.append(result[author][1]/a_data['public_metrics']['followers_count']/result[author][4])
	like.append(result[author][2]/a_data['public_metrics']['followers_count']/result[author][4])
	quote.append(result[author][3]/a_data['public_metrics']['followers_count']/result[author][4])
	average[0] += result[author][0]/a_data['public_metrics']['followers_count']/result[author][4]
	average[1] += result[author][1]/a_data['public_metrics']['followers_count']/result[author][4]
	average[2] += result[author][2]/a_data['public_metrics']['followers_count']/result[author][4]
	average[3] += result[author][3]/a_data['public_metrics']['followers_count']/result[author][4]
	average[4] += 1
	print(f"Retweet/Followers : {result[author][0]/a_data['public_metrics']['followers_count']/result[author][4]*100000}")
	print(f"Reply/Followers : {result[author][1]/a_data['public_metrics']['followers_count']/result[author][4]*100000}")
	print(f"Like/Followers : {result[author][2]/a_data['public_metrics']['followers_count']/result[author][4]*10000}")
	print(f"Quote/Followers : {result[author][3]/a_data['public_metrics']['followers_count']/result[author][4]*10000000}")
	print()

print(average)
print(f"average Retweet/Followers : {average[0]/average[4]}")
print(f"average Reply/Followers : {average[1]/average[4]}")
print(f"average Like/Followers : {average[2]/average[4]}")
print(f"average Quote/Followers : {average[3]/average[4]}")

x=int(average[4]/2)
retweet.sort()
print(f"Mediane Retweet {retweet[x]}")
print(f"Max Retweet {retweet[average[4]-1]}")
reply.sort()
print(f"Mediane Reply {reply[x]}")
print(f"Max Reply {reply[average[4]-1]}")
like.sort()
print(f"Mediane Like {like[x]}")
print(f"Max Like {like[average[4]-1]}")
quote.sort()
print(f"Mediane Quote {quote[x]}")
print(f"Max Quote {quote[average[4]-1]}")

#Intégrer la manière de mesurer l'negagement:
#Normaliser l'engag

#( Retweet+ likes\number of tweets)\ Total number of followers))* 100= engagement rate 
'''
#engagement
engagement={}
for author, tweets in tweets_data.items():
	engagement[author] = []
	for t in tweets:
		engagement[author].append( (t['public_metrics']['retweet_count']+t['public_metrics']['like_count']+t['public_metrics']['reply_count']+t['public_metrics']['quote_count']) / author_data[author]['public_metrics']['followers_count'] * 100 )
	
result={}
authors=[]
eng=[]
for author, r in engagement.items():
	print(author_data[author]['username'])
	authors.append(author_data[author]['username'])

	print(mean(engagement[author]))
	result[author_data[author]['username']] = mean(engagement[author])
	eng.append(mean(engagement[author]))

print(result)
df = pd.DataFrame({'media': authors, 'engagement': eng})
print(df)

sns.barplot(y='media', x="engagement", data=df)
plt.title("Engagement par media")
plt.show()
#print(engagement)