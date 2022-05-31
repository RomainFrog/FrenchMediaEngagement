#!/bin/python

import tweepy
import json

#Open json data
with open('tweets.json') as json_file:
	tweets_data = json.load(json_file)

with open('accounts.json') as json_file:
	author_data = json.load(json_file)

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

mean=[0,0,0,0,0]
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
	mean[0] += result[author][0]/a_data['public_metrics']['followers_count']/result[author][4]
	mean[1] += result[author][1]/a_data['public_metrics']['followers_count']/result[author][4]
	mean[2] += result[author][2]/a_data['public_metrics']['followers_count']/result[author][4]
	mean[3] += result[author][3]/a_data['public_metrics']['followers_count']/result[author][4]
	mean[4] += 1
	print(f"Retweet/Followers : {result[author][0]/a_data['public_metrics']['followers_count']/result[author][4]*100000}")
	print(f"Reply/Followers : {result[author][1]/a_data['public_metrics']['followers_count']/result[author][4]*100000}")
	print(f"Like/Followers : {result[author][2]/a_data['public_metrics']['followers_count']/result[author][4]*10000}")
	print(f"Quote/Followers : {result[author][3]/a_data['public_metrics']['followers_count']/result[author][4]*10000000}")
	print()

print(mean)
print(f"Mean Retweet/Followers : {mean[0]/mean[4]}")
print(f"Mean Reply/Followers : {mean[1]/mean[4]}")
print(f"Mean Like/Followers : {mean[2]/mean[4]}")
print(f"Mean Quote/Followers : {mean[3]/mean[4]}")

x=int(mean[4]/2)
retweet.sort()
print(f"Mediane Retweet {retweet[x]}")
reply.sort()
print(f"Mediane Reply {reply[x]}")
like.sort()
print(f"Mediane Like {like[x]}")
quote.sort()
print(f"Mediane Retweet {quote[x]}")
#Intégrer la manière de mesurer l'negagement:
#Normaliser l'engag