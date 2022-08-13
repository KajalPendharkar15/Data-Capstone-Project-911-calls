#!/usr/bin/env python
# coding: utf-8

# # Data Capstone project 911 calls

# In[1]:


import numpy as np
import pandas as pd 


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv(r"C:\Users\Kajal\Downloads\911-Emergency-calls-data\911.csv")
df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.isna()


# In[7]:


# top 5 zip) for 911  calls 

df['zip'].value_counts().head()


# In[8]:


# top 5 townships(twp) for 911  calls 
df['twp'].value_counts().head()


# In[9]:


# how many unique title codes are there
len(df['title'].unique())


# In[10]:


df['title'].nunique()


# In[11]:


# Creatig new features

### In this title columns there are "Reasons/Departments" specified before the title code. These are  EMS, Fire,  and Traffic . Use apply() with a custom lambda expression to crwate a new column calles "Reason"   that contains this string value.

### For example, if the title column value is EMS: BACk PAINS/INJURY, the  Reason column value woulb be EMS 
x = df['title'].iloc[0]


# In[12]:


x.split(':')[0]


# In[13]:


df['Reason']=df['title'].apply(lambda title: title.split(':')[0])


# In[14]:


df['Reason']


# In[15]:


# What is the most commomn reason foa  a911 call based  off of this new column?
df['Reason'].value_counts()


# In[16]:


# Now use SEABORN to use countplot for 911 calls  by Reason
sns.countplot(x='Reason', data=df, palette= 'viridis')


# In[17]:


#what is the data type of teh object in the time stamp column 
type(df['timeStamp'].iloc[0])


# In[18]:


# Use pd.datetime top cobnvert the column from strings to Datetime objects
df['timeStamp']= pd.to_datetime(df['timeStamp'])


# In[19]:


type(df['timeStamp'].iloc[0])


# In[20]:


#The timeStamp colums are actually DateTime objects, use .apply() to create 3 new columns  calles Hour, Month and Day of the week. You will create  these columns  based  off of the  timeStamp column,
time  = df['timeStamp'].iloc[0]
time.hour


# In[21]:


time.month


# In[22]:


time.year


# In[23]:


time.dayofweek


# In[24]:


df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)


# In[25]:


df['Hour']


# In[26]:


df['month'] = df['timeStamp'].apply(lambda time: time.month)


# In[27]:


df['month']


# In[28]:


df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[29]:


df['Day of Week'] 


# In[30]:


df.head()


# In[31]:


# The dayofweek is an integer 0-6. Use the .map() with the dictionary to map the actual string names to the day of week
dmap ={0 : 'Mon', 1 : 'Tue', 2 : 'Wed', 3 : 'Thu', 4 : 'Fri', 5 : 'Sat', 6 :'Sun'}


# In[32]:


df['Day of Week'] = df['Day of Week'].map(dmap)
df['Day of Week']


# In[33]:


df.head()


# In[37]:


# Now use Seaborn to create a countplot of the Day of Week column  with teh hue based off  of the Reason Column 
sns.countplot(x= 'Day of Week', data=df, hue='Reason', palette='viridis')
# to relocate the legend 
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[39]:


#group by month
bymonth  = df.groupby('month').count()


# In[42]:


bymonth.head()


# In[44]:


#create a simple plot off of the data frame indiacting the count of calls per months
bymonth['lat'].plot()


# In[46]:


sns.countplot(x= 'month', data=df, palette='viridis')
# to relocate the legend 
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[48]:


# use seaborn lmplot()  to create a linear fit on the number of calls  per month
sns.lmplot(x='month', y='twp', data=bymonth.reset_index())


# In[52]:


#ceate a new column calles 'Date' that contains the  date from the timeStamp column. 
t =  df['timeStamp'].iloc[0]
t


# In[54]:


df['Date']=df['timeStamp'].apply(lambda t:t.date())
df['Date']


# In[55]:


t.date()


# In[56]:


# groupby this date column with count() aggregate  and create  a plot  of counts of 911  calls.
df.groupby('Date').count().head()


# In[61]:


df.groupby('Date').count()['lat'].plot()


# In[58]:


# create a seperate plots with  each plot representing a Reason for  the 911 calls 


# In[68]:


# Traffic was the reason fo 911 calls
df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[69]:


# Fire was the reason fo 911 calls
df[df['Reason']=='Fire'].groupby('Date').count()['lat'].plot()
plt.title('Fire')
plt.tight_layout()


# In[70]:


# EMS was the reason fo 911 calls
df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
plt.tight_layout()


# In[76]:


# create a heatmaps with seaborn and our data restructure the dataframe so that the columns become an hours and the index becomes the Day of Week
dayHour=df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()


# In[77]:


dayHour


# In[79]:


# create a Heatmap using a new DataFrame 
sns.heatmap(dayHour, cmap='viridis')


# In[81]:


#create a cluster map using the data frame 
sns.clustermap(dayHour)


# In[84]:


#repeat the same plots and operations, for tha data frame that shows month as a column
daymonth=df.groupby(by=['Day of Week','month']).count()['Reason'].unstack()
daymonth.head()


# In[89]:


plt.figure(figsize=(12,6))
sns.heatmap(daymonth, cmap='coolwarm')


# In[ ]:




