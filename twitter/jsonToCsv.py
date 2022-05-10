import pandas as pd
import json
from datetime import datetime
from datetime import timezone

df = pd.read_json("tweets.json")
dataFrame = pd.DataFrame(df)
print(dataFrame.iloc[1,3]['id'])


print(dataFrame.shape)

array = []
nb = 0

for i in range(dataFrame.shape[0]):
    for j in range(dataFrame.shape[1]):
        array.append([])
        array[nb].append(dataFrame.columns[j]) #On met l'id du compte
        array[nb].append(int(dataFrame.iloc[i,j]['id'])) #On met l'id du Tweet
        array[nb].append(dataFrame.iloc[i,j]['created_at'][:10]) #Date
        array[nb].append(dataFrame.iloc[i,j]['created_at'][11:][:-5]) #heure en UTC+0
        array[nb].append(dataFrame.iloc[i,j]['text']) #Text du tweet
        array[nb].append(dataFrame.iloc[i,j]['public_metrics']['retweet_count']) #Nb de retweet
        array[nb].append(dataFrame.iloc[i,j]['public_metrics']['reply_count']) # Nb de reply
        array[nb].append(dataFrame.iloc[i,j]['public_metrics']['like_count']) #Nb de like
        array[nb].append(dataFrame.iloc[i,j]['public_metrics']['quote_count']) #Nb de quote
        nb = nb+1
#print(array)

new_dataFrame =  pd.DataFrame(data = array,columns = ["id_compte","id_tweet","date","heure_UTC0","text","retweet_count","reply_count","like_count","quote_count"])
print(new_dataFrame)
new_dataFrame.to_csv("Tweets.csv",sep=',')
