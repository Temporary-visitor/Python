#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Here we imported our csv filed data.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

google_play_store = pd.read_csv ('googleplaystore.csv' )
print(google_play_store.head(2), google_play_store.tail(2))

# using methods "head()" and "tail()", we showed only top 2 rows and bottom 2 rows.

print('\n' , google_play_store.columns)

# just showed how data is divided into groups.


# In[7]:


google_play_store.sort_values('Rating', ascending =False)

# Sorted out data according to rating


# In[8]:


business_category = google_play_store.loc[google_play_store['Category'] == 'BUSINESS']
business_category

# here filtered data of app regarding Business, opening new frame.


# In[9]:


print(google_play_store['Category'].value_counts(dropna =False))
# Counted number of apps in each category, in descending form.


# In[10]:


google_play_store[google_play_store['Reviews']==max(google_play_store.Reviews)]
# most viewed and displayed apps


# In[11]:


google_play_store[google_play_store['Reviews']==min(google_play_store.Reviews)]
# least viewed and displayed apps


# In[12]:


google_play_store[google_play_store['Reviews']==min(google_play_store.Reviews)]
# least viewed and displayed apps


# In[13]:


google_play_store.isnull().sum()

#It appears that the value of the rating is a little empty. We're gonna have to fill it.


# In[14]:


from sklearn.impute import SimpleImputer
im=SimpleImputer(missing_values='NaN', strategy='mean')
google_play_store.iloc[:,2:3]=im.fit_transform(google_play_store.iloc[:,2:3])

#so,We've done adding implants to the empty spaces by taking the mean.

google_play_store.isnull().sum()


# In[15]:


google_play_store.head()


# In[16]:


print(google_play_store['Category'].value_counts(dropna =False))


# In[19]:


import seaborn as sns
plt.style.use('ggplot')

sns.barplot(x=google_play_store['Category'].value_counts().index,  y=google_play_store['Category'].value_counts().values)
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Category Count Operation")
plt.xticks(rotation=90)
plt.show()
#It seems that the most family and game categories are traded.


# In[20]:


google_play_store.sort_values('Rating', ascending =False)

# Sorted out data according to rating


# In[21]:


business_category = google_play_store.loc[google_play_store['Category'] == 'BUSINESS']
business_category

# here filtered data of app regarding Business, opening new frame.


# In[22]:


print(google_play_store['Category'].value_counts(dropna =False))
# Counted number of apps in each category, in descending form.


# In[23]:


google_play_store[google_play_store['Reviews']==max(google_play_store.Reviews)]
# most viewed and displayed apps


# In[24]:


google_play_store[google_play_store['Reviews']==min(google_play_store.Reviews)]
# least viewed and displayed apps


# In[25]:


google_play_store.isnull().sum()

#It appears that the value of the rating is a little empty. We're gonna have to fill it.


# In[28]:


from sklearn.impute import SimpleImputer
im=SimpleImputer(missing_values='NaN', strategy='mean')
google_play_store.iloc[:,2:3]=im.fit_transform(google_play_store.iloc[:,2:3])

#so,We've done adding implants to the empty spaces by taking the mean.


# In[29]:


google_play_store.head()


# In[30]:


print(google_play_store['Category'].value_counts(dropna =False))


# In[31]:


import seaborn as sns
plt.style.use('ggplot')

sns.barplot(x=google_play_store['Category'].value_counts().index,  y=google_play_store['Category'].value_counts().values)
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Category Count Operation")
plt.xticks(rotation=90)
plt.show()
#It seems that the most family and game categories are traded.


# In[32]:


# using the variable ax for single a Axes
fig, ax = plt.subplots()

ax.scatter(x = google_play_store.groupby('Category')['Rating'].mean()[1:].index, y = google_play_store.groupby('Category')['Rating'].mean()[1:].values)
plt.ylabel('Category', fontsize=20)
plt.xlabel('Rating', fontsize=12)
plt.xticks(rotation=90)
plt.show()


# In[ ]:




