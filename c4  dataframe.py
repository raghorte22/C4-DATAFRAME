#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd #USE FOR DATAFRAMES


# In[7]:


stats = pd.read_csv(r"C:\Users\Achal Raghorte\OneDrive\Desktop\Data Science with AI\17th,18th\17th,18th\DataFrame_ Pandas\data1.csv")


# In[8]:


stats


# In[9]:


stats.head()


# In[10]:


stats.tail()


# In[11]:


stats.columns


# In[12]:


stats.info()


# In[13]:


stats


# In[14]:


len(stats)


# In[15]:


len(stats.columns)


# In[16]:


stats.head(2)


# In[17]:


stats.tail(3)


# In[18]:


stats.describe()


# In[19]:


stats.describe().transpose()


# In[20]:


stats.describe().transpose() #rows into columns


# In[21]:


stats.head()


# In[22]:


stats.columns=('a','b','c','d','e')
stats.head()


# In[23]:


stats.columns=(
'CountryName' ,'CountryCode',	'BirthRate',	'InternetUsers',	'IncomeGroup')


# In[24]:


stats.head()


# ###### subsetting a dataframes in pandas
# 
# #1. Rows
# #2. Columns
# #3. combine the two

# In[25]:


stats[2:3]


# In[26]:


stats[21:26]


# In[27]:


stats[:]


# In[28]:


stats[:10]


# In[29]:


stats.head(10)


# In[30]:


stats[::-1]


# In[31]:


stats


# In[32]:


stats[::20]


# In[33]:


stats.columns


# In[34]:


stats.head()


# In[35]:


stats['CountryName'].head()


# In[36]:


stats['CountryName'].head()


# In[37]:


stats[['CountryName','BirthRate']].head()


# In[38]:


stats.head()


# In[39]:


stats['CountryCode'].head()


# In[40]:


stats['BirthRate']


# ###### combine two

# In[41]:


stats[4:8][['CountryName','BirthRate']]


# In[42]:


stats[['CountryName','BirthRate']][4:8]


# In[43]:


df1=stats[['CountryName','BirthRate']]


# In[44]:


df1


# In[45]:


df2=stats[4:8]


# In[46]:


df2


# In[47]:


df3=stats[4:10]


# In[48]:


df3


# In[49]:


stats.head()


# In[50]:


#Mathmetical operation = 
stats.InternetUsers * stats.BirthRate


# ###### Add columns

# In[51]:


stats['Mycalc']=stats.InternetUsers * stats.BirthRate


# In[52]:


stats.head()


# In[53]:


stats.drop('Mycalc',axis=1)


# In[54]:


stats=stats.drop('Mycalc',axis=1)


# In[55]:


stats.head()


# In[56]:


stats.columns[3]


# In[57]:


stats.columns[2]


# In[58]:


stats.InternetUsers<2


# In[59]:


stats.InternetUsers<2


# In[60]:


Filter=stats.InternetUsers<2


# In[61]:


Filter


# In[62]:


stats[3:7]


# In[63]:


stats[30:40]


# In[64]:


stats[Filter]


# In[65]:


Filter2 = stats.BirthRate>40


# In[66]:


Filter2


# In[67]:


stats[Filter2]


# In[68]:


stats[Filter2]


# In[72]:


stats[stats.BirthRate >40]


# In[73]:


stats[stats.BirthRate<40]


# In[78]:


stats[stats.IncomeGroup=='Low income']


# In[80]:


stats[stats.IncomeGroup=='High income']


# In[87]:


stats[(stats.BirthRate > 20) & (stats.InternetUsers < 80)]


# In[90]:


stats[(stats.BirthRate<50)&(stats.InternetUsers<80)]


# In[91]:


stats.head()


# ###### How to get the unique categories

# In[92]:


stats.IncomeGroup.unique()


# #### Introduction to seaborn # seaborn is very powerfull visualizatio(STATISTIC VISULAIZATION) pkg in python
# 

# In[94]:


import matplotlib.pyplot as plt #visulization 
import seaborn as sns #distribution visulization

 
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 8,4

#import warnings
#warnings.filterwarnings('ignore')


# In[95]:


stats.head()


# ###### Distribution

# In[98]:


vis1=sns.distplot(stats["InternetUsers"])


# In[99]:


vis2=sns.distplot(stats["BirthRate"])


# In[100]:


vis1=sns.distplot(stats["InternetUsers"],bins=10)


# ###### Box Plot

# In[104]:


vis3=sns.boxplot(data=stats,x='IncomeGroup', y='BirthRate')


# ###### visualizing with seaborn

# In[105]:


vis4=sns.lmplot(data=stats,x='InternetUsers',y='BirthRate',fit_reg=False)


# In[108]:


vis5=sns.lmplot(data=stats,x='InternetUsers',y='BirthRate')


# In[109]:


vis5 = sns.lmplot(data = stats,x = 'InternetUsers', y = 'BirthRate',
                  fit_reg = False,hue = 'IncomeGroup') #hue - parameter for color


# In[ ]:




