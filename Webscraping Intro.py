#!/usr/bin/env python
# coding: utf-8

# In[6]:


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/id-en/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+card&N=-1&isNodeId=1'
#opening up the connection, grab the page
uClient = uReq(my_url)
page_html= uClient.read()
uClient.close()
#html Parsing
page_soup = soup(page_html,"html.parser")
page_soup.h1
page_soup.p
page_soup.body.span


# In[7]:


#grab each products
containers = page_soup.findAll("div",{"class":"item-container"})
len(containers)


# In[8]:


containers[0]


# In[ ]:




