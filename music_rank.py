
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
import sys, urllib.request
import requests
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from collections import Counter
get_ipython().magic('matplotlib inline')


# In[2]:

rank_no=[]
artist=[]
music=[]
twitter=[]


# In[3]:

def get_single_item_data(item_url, number_start =0,num_end =100):
        source_code = urllib.request.urlopen(item_url)  # get all source code
        source_text = source_code.read()
        #plain_text = source_text.decode('utf-8')
        #output = open('plain_text','w+')
        #output.write(plain_text)
        #output.close()
        soup = BeautifulSoup(source_text,"html.parser")
        #toplist = soup.find_all('table',{'class':'smv'}).find_all("tr")[0].find_all("td")td[3]
        toplist = soup.find_all('table',{'class':'smv'})
        Top_Emerging = toplist[0]
        Top_Trending = toplist[1] #updating fast in 6 seconds
        Top_Overall = toplist[2]
        #print(toplist[2])
        rank_list = toplist[1].find_all('tr')
        for rank in rank_list[number_start:num_end]:
            rank_no.append(rank.find_all('td')[0].text)
            artist.append(rank.find_all('td')[1].text)
            music_text = rank.find_all('td')[2].text
            music.append(music_text[0:(music_text.find("\n"))-1])
            twitter.append(rank.find_all('td')[1].find('a').get("href"))
        #for i in np.arange(len(artist)).tolist()[0:5]:
            #print("ranking No:"+str(i+1)+"   artist:"+artist[i]+"  music:"+music[i]+'\n')
            #print(twitter[i]+'\n')


# In[4]:

#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  Top Five song and Singers   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
get_single_item_data("http://realtime.billboard.com/?chart=trending140", 70, 90)


# In[5]:

Top_Overall_df = pd.DataFrame({'No.':rank_no, 'artist': artist, 'music':music, 'Twitter':twitter})


# In[6]:

#Top_Overall_df.describe()


# In[7]:

count = dict(Counter(artist))
#print(count)

xVals = list(count.keys())
yVals = list(count.values())
#print("------------top 20 songs------"+str(len(np.unique(xVals)))+" singers in total---------")
print(np.unique(xVals))
x = tuple(np.arange(len(xVals)))
width = 0.4
ax = plt.subplot(111)
ax.set_position([5,2,2.5,1])
ax.bar(x, yVals, width)
ax.set_xticks([i+width/2 for i in x])
ax.set_xticklabels(xVals)
plt.rcParams['font.size'] = 80


# In[8]:

#sns.factorplot(y='artist', data=Top_Overall_df, kind='count',size=10,linewidth=1)


# In[ ]:




# In[35]:

#import threading

#def printit():
#  threading.Timer(10.0, printit).start()
#  %run music_rank_animation.py

#printit()


# In[ ]:



