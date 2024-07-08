#!/usr/bin/env python
# coding: utf-8

# In[68]:


#Is the average temperature recorded for detroit significantly different 
#from the national average temperature?

#First, i'll import my CSV climate file and the necessary libraries i'll need
#to perform my hypothesis

from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

det_data = pd.read_csv('Detroit_weather_data.csv')
det_data.head()


# In[25]:


#Let's remove our Year and Avg columns to just get the recordings

parsed_data = det_data.iloc[:, 2:14]
print(parsed_data)


# In[50]:


#Now lets convert this data into a list
avg_temps = parsed_data.values.tolist()
print(avg_temps)


# In[51]:


#Our list seperated into smaller lists organized by Year, however we want just a list of all the 
#average recorded temperatures 

flat_list = []
for lists in avg_temps:
    for nums in lists:
        flat_list.append(nums)

print(flat_list)


# In[52]:


#Now let's get the mean from this list
sample_mean = np.mean(flat_list)


# In[69]:


#And now i'll visualize the data to check assumptions that my data is normally distrubted

plt.hist(flat_list)
plt.show()

#Notice that in our plot there is a presence of a bimodial distrubtion 
#that is not a normal bell curve. However for the sake of this project we will still 
#proceed with our test


# In[53]:


print(sample_mean)


# In[ ]:


#Annual average temperature in the U.S for 2023

2023_national_avg_temp = 54.41

#Source = 'https://www.statista.com/statistics/500472/annual-average-temperature-in-the-us/#:~:text=The%20average%20temperature%20in%20the,than%20the%2020th%20century%20average.'


# In[87]:


#Given that were comparing a sample average to a population value, i'll perform a one sample t-test
#to calculate the confidence interval with the following Null and Alternative hypothesis

#Null: the sample mean is not signifcantly different from the population mean
#Alternative: The sample mean is significantly different from the population mean

tstat, pval = ttest_1samp(flat_list,54.41)


# In[88]:


print(pval)


# In[ ]:


#our confidence interval is below 5% and therefore we can assume there is a significant 
#difference between the average temperature in detroit Michigan from 2000-2020 and the 
#national average temperature from 2023.

