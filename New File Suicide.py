#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


s= pd.read_excel('master_excel.xlsx')


# In[4]:


s.isnull().sum()


# In[5]:


us=s[s['country']=='United States'].copy()


# In[5]:


us


# In[6]:


us.isnull().sum()


# In[36]:


avg_s_us= us.groupby('year')['suicides/100k pop'].mean()
avg_s_world= s.groupby('year')['suicides/100k pop'].mean()


# In[42]:


fig = plt.figure(figsize=(15,5))
plt.plot(avg_s_us, color='r')
plt.plot(avg_s_world)
plt.xlabel('Year')
plt.ylabel('Avg Suicides/100k Population')
plt.title('Avg Suicides/100k pop- US vs World' , fontsize=18)
plt.show()             # To remove extra texts from graph


# In[10]:


age_wise_pivot=pd.pivot_table(us, index=['year'], columns=['age'], values=['suicides_no'])
age_wise_pivot


# In[11]:


age_wise_pivot.plot.bar(stacked=True, figsize=(20,10))
plt.legend(title='Age')
plt.xlabel(' ')
plt.title('Avg Suicides occured by Age Group', fontsize=18)
plt.show()


# In[49]:


avg_s_agegroup=us.groupby('age')['suicides_no'].sum()
ages=us['age'].unique()


# In[50]:


ages


# In[63]:


fig = plt.figure(figsize=(15,6))
plt.bar(ages, avg_s_agegroup, color='purple')
plt.title('Age Group vs Suicides', fontsize=18)
plt.ylabel('Total suicides')
plt.show()


# In[12]:


gender_wise_pivot= pd.pivot_table(us, index=['year'], columns=['sex'], values=['suicides_no'])
gender_wise_pivot


# In[40]:


fig = plt.figure(figsize=(15,5))
gender_wise_pivot.plot()
plt.xlabel(' ')
plt.title('Male vs Female- Avg Suicides in the US', fontsize=18)
plt.show()


# In[14]:


gender_wise_pivot.plot.bar(stacked=True, figsize=(20,8))
plt.show()


# In[15]:


s_values=us.groupby('sex').suicides_no.sum()


# In[16]:


s_values


# In[17]:


colours=['green', 'yellow']
plt.pie(s_values, labels=['Women', 'Men'], colors= colours , autopct='%1.1f%%', radius= 1.5, shadow= True)
plt.show()


# In[41]:


fig = plt.figure(figsize=(15,5))
plt.plot(us['year'], us['gdp_per_capita ($)'], color='g')
plt.ylabel('GDP per capita $')
plt.title('GDP per capita in the US', fontsize=18)
plt.show()


# In[19]:


import seaborn as sns


# In[20]:


us_avg_gdp= us.groupby('year')['gdp_per_capita ($)'].mean()
us_avg_suicides=us.groupby('year')['suicides/100k pop'].mean()


# In[61]:


fig = plt.figure(figsize=(20,5))
sns.regplot(us_avg_gdp, us_avg_suicides, data=us, color='maroon')
plt.title('Correlation btw GDP/Capita and Suicides/100k Population', fontsize=18)


# In[ ]:




