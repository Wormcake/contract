#!/usr/bin/env python
# coding: utf-8

# In[204]:


import requests as rq
from bs4 import BeautifulSoup as biso
import random

url = "https://en.wikipedia.org/wiki/Wikipedia:List_of_English_contractions"

page = rq.get(url)
soup = biso(page.content,'html.parser')

reviews = soup.find_all('td')
funn = soup.find_all('tr')

chug = random.randint(1, 190)
chud = chug*2
chup = chug+1
print(" " + str(chug) + " / 190")

for review in reviews[chud]:
    text = review.get_text().strip()
print(text)

for review in funn[chup]:
    text = review.get_text().strip()
print(text)

print("\nSource:\thttps://en.wikipedia.org/wiki/Wikipedia:List_of_English_contractions")

