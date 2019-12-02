#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_excel("C:\\Users\\shubham_kumar\\Desktop\\survey.xls")
df


# In[5]:


#shows the frequency of the perticular data
pd.crosstab(df.Nationality,df.Handedness)


# In[6]:


pd.crosstab(df.Sex,df.Handedness,margins=True)


# In[8]:


pd.crosstab(df.Sex,[df.Handedness,df.Nationality],margins=True)


# In[9]:


#Persentage of data
pd.crosstab(df.Sex,[df.Handedness,df.Nationality],normalize='index')


# In[30]:


#Average of perticular column 
import numpy as np
pd.crosstab([df.Sex],[df.Handedness],values=df.Age,aggfunc=np.average)

