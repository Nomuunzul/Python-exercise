#!/usr/bin/env python
# coding: utf-8

# # My First Data Science Project from DataQuest

# ## Helicopter Escapes!
# ### We begin by importing some helper functions

# In[ ]:


from helper import *


# In[ ]:


### Get the Data


# In[ ]:


Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.


# In[10]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
#so here is the URL


# In[11]:


data = data_from_url(url)
#created a variable called data by assigning result passed from the url


# In[ ]:


### Let's print the first three rows


# In[15]:


for row in data[0:4]:
    print(row)


# In[ ]:


### Now lets remove the last column "details" from the data


# In[25]:


index = 0
for row in data:
    data[index] = row[:-1]
    index += 1
print(data[:3])


# In[ ]:


### Now to fetch year from date column


# In[26]:


for row in data:
    row [0] = fetch_year(row[0])
print(data[:3])


# In[ ]:


### To create a list of lists that contains year and number of attempts occured in the corresponding year


# In[34]:


min_year = min(data, key = lambda x: x[0])[0]
max_year = max(data, key = lambda x: x[0])[0]
attempts_per_year = []
for u in range(min_year, max_year+1):
    attempts_per_year.append([u,0])
print(attempts_per_year[:3])


# In[36]:


for row in data:
    for ya in attempts_per_year:
        y = ya[0]
        if row[0] == y:
            ya[1] += 1
print(attempts_per_year)


# In[37]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In which year did the most attempts at breaking out of prison with helicopter occur?
# 1986, 2001, 2007 and 2009

# In[39]:


countries_frequency = df["Country"].value_counts()
print_pretty_table(countries_frequency)


# In[ ]:




