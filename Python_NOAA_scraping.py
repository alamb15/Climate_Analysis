#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://www.weather.gov/dtx/dtwtemp2000-2020'


# In[3]:


page = requests.get(url)


# In[4]:


soup = BeautifulSoup(page.text,'html')


# In[5]:


print(soup)


# In[8]:


table = soup.find(class_ = 'cms-content')
print(table)


# In[59]:


column_names = table.find_all('tr')
column_headers = column_names[1]
print(column_headers)


# In[63]:


final_column_headers = [item.text.strip() for item in column_headers]
print(final_column_headers)


# In[65]:


while("" in final_column_headers):
    final_column_headers.remove("")


# In[66]:


print(final_column_headers)


# In[67]:


import pandas as pd


# In[68]:


df = pd.DataFrame(columns = final_column_headers)


# In[69]:


df


# In[71]:


column_data = column_names[1:]
print(column_data)


# In[83]:


for row in column_names[1:]:
    row_data = row.find_all('td')
    final_data = [data.text.strip() for data in row_data]
    print(final_data)
    
    length = len(df)
    df.loc[length] = final_data
    
#so the problem with this, as in the last project i was working on, i did not indent my df.loc[length] = final data
#and did it outside of the loop, therfore it only looped through and grabbed one item to add to the df
#instead of keeping it in the loop by indenting, which i forgot about i did in the last one.


# In[90]:


df.drop(2, inplace=True)
df


# In[91]:


df = df.reset_index(drop=True)


# In[92]:


df


# In[93]:


df.to_csv('Detroit_weather_data.csv')


# In[ ]:


#grand_rapids data below, now I will use weather underground, a different site to retrieve
#historical monthly temperature averages from 2000-2020
#then once both converted into csv tables


# In[199]:


list_of_data = [[2000,25.3,34.1,44.2,47.2,62.0,67.2,71.0,72.4,64.7,56.1,37.0,16.0,49.8],
[2001,24.5,26.1,34.1,52.5,60.0,67.4,74.5,73.2,61.9,52.1,48.2,33.4,50.7],
[2002,31.9,32.1,34.5,49.9,55.2,70.9,77.0,73.1,67.3,49.7,37.6,30.1,50.8],
[2003,21.3,23.6,36.7,48.3,56.2,65.5,72.3,73.6,63.3,51.8,41.9,31.6,48.8],
[2004,20.3,27.4,41.1,50.4,60.0,67.1,71.2,67.5,66.5,53.9,43.7,28.9,49.8],
[2005,24.5,32.4,35.0,51.5,57.1,74.2,75.6,74.3,69.4,55.2,42.0,23.3,51.2],
[2006,35.8,28.2,38.3,53.1,59.6,68.3,76.5,74.3,62.4,49.0,42.8,33.8,51.8],
[2007,27.9,17.9,42.5,46.8,63.8,71.3,73.7,74.8,68.1,59.0,39.4,27.8,51.1],
[2008,23.5,23.0,34.9,49.4,55.5,70.8,74.0,72.7,66.1,52.6,39.3,22.9,48.7],
[2009,15.8,28.2,39.6,47.3,59.9,67.6,69.4,70.5,65.4,48.8,45.3,26.5,48.7],
[2010,21.9,26.7,41.7,54.6,61.7,71.2,77.6,76.7,65.1,56.0,41.5,22.5,51.4],
[2011,20.6,26.2,36.3,47.7,57.9,69.5,79.0,73.5,62.2,54.9,44.9,35.2,50.7],
[2012,30.2,32.9,53.5,50.7,65.6,74.0,81.0,73.3,64.1,51.5,40.5,36.1,54.5],
[2013,26.6,26.1,32.6,46.9,61.0,68.5,73.2,73.0,67.2,53.1,37.5,23.3,49.1],
[2014,15.7,17.3,31.7,48.6,60.4,70.9,70.4,73.7,63.9,52.0,33.6,32.0,47.5],
[2015,22.3,14.6,35.4,49.4,60.4,67.4,72.3,71.8,69.0,54.7,44.6,39.0,50.1],
[2016,24.7,30.4,43.3,47.8,59.7,71.6,75.5,75.8,69.6,56.9,46.8,25.0,52.3],
[2017,28.8,38.0,39.5,53.7,57.9,72.4,74.6,71.5,69.4,57.6,39.7,27.2,52.5],
[2018,24.6,28.8,36.9,41.2,66.1,71.5,76.2,76.3,68.9,52.7,34.6,33.2,50.9],
[2019,21.0,25.9,34.3,49.7,58.0,67.8,77.1,72.9,69.4,50.9,34.8,34.0,49.6],
[2020,30.1,30.2,42.8,48.4,59.9,74.0,79.2,76.8,66.3,51.5,47.4,32.8,53.3]
]


# In[200]:


chicago_df = pd.DataFrame(columns = final_column_headers)


# In[202]:


chicago_df


# In[205]:


for data in list_of_data:
    length_ = len(chicago_df)
    chicago_df.loc[length_] = data


# In[206]:


chicago_df


# In[207]:


chicago_df.to_csv('chicago_climate_dat.csv')


# In[ ]:


#now we have our detroit weather and our chicago weather

