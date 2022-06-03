import os
from pprint import *
import pandas as pd
import numpy as np
import seaborn as sns
from dateutil import parser
import matplotlib.pyplot as plt
sns.set(rc={'figure.figsize':(11.7,8.27)})
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

channels = pd.read_csv('../csv/channels.csv', index_col=0)
videos = pd.read_csv('../csv/videos.csv', index_col = 0, sep =';')

channels = channels[channels.channelId != "UCCCPCZNChQdGa9EkATeye4g"]
videos = videos[videos.channelId != "UCCCPCZNChQdGa9EkATeye4g"]

videos_m = pd.merge(videos, channels, left_on="channelId", right_on="channelId", how="left")

videos_m = videos_m.rename(columns={
    'publishedAt_x': 'publishedAt_video',
    'title_x': 'title_video',
    'viewCount_x': 'viewCount_video',
    'title_y': 'title_channel',
    'viewCount_y': 'viewCount_channel'
}
)
videos_m = videos_m.assign(
    #engagement_1 = (((videos_m.likeCount + videos_m.commentCount) / videos_m.videoCount) / videos_m.subscriberCount) * 100,
    engagement = ((videos_m.likeCount + videos_m.commentCount) / videos_m.subscriberCount) * 100,
    #engagement_3 = (((videos_m.likeCount + videos_m.commentCount + videos_m.viewCount_video) / videos_m.videoCount) / videos_m.subscriberCount) * 100,
    #engagement_4 = ((videos_m.likeCount + videos_m.commentCount + videos_m.viewCount_video) / videos_m.subscriberCount) * 100,
    #engagement_5 = (videos_m.viewCount_video + videos_m.likeCount + videos_m.commentCount) / videos_m.subscriberCount
    
) 

videos_m
df = videos_m.groupby('channelId').mean()

df = df[['engagement']]
channels = pd.merge(channels, df, left_on="channelId", right_on="channelId", how="left")

channels.assign(
    viewPerSubs = channels.viewCount / channels.subscriberCount
)

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

sns.set(style = "darkgrid")

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = videos_m['color_1_r']
y = videos_m['color_1_g']
z = videos_m['color_1_b']

ax.scatter(x, y, z)

plt.show()