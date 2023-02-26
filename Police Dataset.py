#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # Importing the data set

# In[2]:


data = pd.read_csv(r"C:\Users\user\Downloads\3. Police Data.csv")


# In[7]:


data


# # checking the null values

# In[9]:


data.isnull()


# In[10]:


data.isnull().sum()


# In[11]:


#as country_name column is blank, need to drop that


# In[12]:


data.drop(columns= 'country_name',inplace= True)


# In[13]:


data


# # for speeding how many persons was stopped 

# In[16]:


#will use filter and count to get the data
data[data.violation== 'Speeding'].driver_gender.value_counts()


# In[17]:


#search conducted for speeding


# In[32]:


data.search_conducted.value_counts()


# In[19]:


#will use groupby functions for both men and women for search_conducted


# In[22]:


affected_while_speeding= data.groupby('driver_gender').search_conducted.sum()


# In[23]:


affected_while_speeding


# # what is the avg time of stop_duration?

# In[26]:


data.head(5)


# In[29]:


#as the data type of stop_duration is string-object, need to convert into integer for calculating the mean


# In[34]:


data.stop_duration.value_counts()


# In[35]:


data['stop_duration']= data['stop_duration'].map({'0-15 Min': 7.5,'16-30 Min': 24,'30+ Min': 45 })


# In[36]:


data


# In[40]:


data['stop_duration'].mean()


# # compare the age distribution for each violation

# In[42]:


data.head(5)


# In[46]:


data.groupby('violation').driver_age.describe()


# # How many drivers was arrested

# In[47]:


data.head(5)


# In[50]:


data.is_arrested.value_counts()


# In[51]:


arrested= data.groupby('driver_gender').is_arrested.sum()


# In[54]:


arrested


# In[55]:


#arrested according of age


# In[56]:


arrested_age = data.groupby('driver_age').is_arrested.sum()


# In[57]:


arrested_age


# # How many cars was stopped and arrested for drugs case

# In[61]:


data.head(5)


# In[64]:


data.drugs_related_stop.value_counts()


# In[66]:


drug_age = data.groupby('driver_age').drugs_related_stop.sum()


# In[67]:


drug_age


# In[75]:


drug_gender = data.groupby('driver_gender').drugs_related_stop.sum()
drug_gender


# In[78]:


data.groupby('drugs_related_stop').driver_age.describe()


# In[ ]:




