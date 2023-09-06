#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[5]:


#Data loading  stage ( we import the data )
df=pd.read_csv('titanic_data.csv') 


# In[6]:


#Satge 2- Data exploration and data cleaning 
df.head()


# In[6]:


df.describe() # have a aggregation over the numerical data 
    


# In[9]:


df.isnull().sum() #this shows that we have missed rows in AGe and Cabin*/


# In[13]:


#Sunderstand the Age columen uisng histogram

#import seaborn as sns
#import matplotlib.pyplot as plt

# Create a figure and axes
#fig, ax = plt.subplots()

# Create the histogram
#sns.histplot(df['Age'].dropna(), kde=False, bins=30, ax=ax)

# Show the plot
#plt.show()

Ax=df['Age'].hist(bins=15, density=True, stacked = True, color = 'red', alpha =0.6) 


# In[14]:


#We will fill up the missine values uisng some strategy 
# In this we will undertsand the average number in AGe  of people accoriding to there Pclass 
df.groupby('Pclass').mean()

#The average Age for the Age is 38 for pclass 1


# In[7]:


# Handling missing values - Feature engineering 
#so now we write our function to fill up our empty  gap using the Age column and thr Pclass 

def get_Age(cols):
    Age=cols[0]
    Pclass=cols[1]
    
    if pd.isnull(Age):
            if Pclass ==1:
                return 38
            elif Pclass==2:
                return 29
            else:
                return 25
    else:
         return Age
        
df['Age']= df[['Age','Pclass']].apply(get_Age,axis =1)


# In[28]:


df.isnull().sum()  # confirming our funtcion really worked  


# In[31]:


sns.countplot(x = 'Survived', hue = 'Sex', data = df)  # 0 means not surved and 1 means surved 


# In[ ]:





# In[32]:


sns.countplot(x = 'Survived', hue = 'Pclass', data = df) #


# In[33]:


df['Fare'].hist()


# In[8]:


#Stage four - This is the stage we perform our feature engineering on our dataset by doing some data type convemtion 
# deleting uncessary columns 
#Lets Perform Data Convention s. letes converrt categoricall varibales to numerical valyes using Get_dummie
#method in 
sex= pd.get_dummies(df['Sex'],drop_first = True)
embarked = pd.get_dummies(df['Embarked'],drop_first = True)

df= pd.concat([df,sex,embarked],axis =1 )


# In[9]:


df.head(3)


# In[ ]:


# drop columns 
df.drop(['Name','Sex','Ticket','Fare','Embarked'],axis =1 ,inplace = True )


# In[57]:


df


# In[44]:


df.drop(['Cabin'], axis =1, inplace = True )


# In[65]:


#Spliting your datset into things we know and thhings we are trying to predict
#Lets get our independent varibales and dependeent vairbal e
y = df['Survived'] # dependeant varible eg Survived because we r trying predict survived and not surviveed 

x = df.drop('Survived', axis = 1)# independenet eg Age, male,


# In[66]:


print(y)


# In[70]:


x


# In[68]:


# Lets import a function that will help us split our dataset into training set and test set  test. 
from sklearn.model_selection import train_test_split

x_train,x_test, y_train,Y_test = train_test_split(x,y, test_size = 0.3, random_state = 0)
# this code above will split the dataset into 70:30 


# In[69]:


x_train # will be used on the training stage of the model


# In[72]:


y_train  # will be used for the model training 


# In[75]:


#Fiting the logistic regression into the dataset
from sklearn.linear_model import LogisticRegression

smartfriend =LogisticRegression(max_iter = 1000) # max_iter means the number of times it will try to find patterns 
smartfriend.fit(x_train,y_train)


# In[77]:


y_predict = smartfriend.predict(x_test) 


# In[78]:


y_predict 


# In[84]:


# Evaluate the model
from sklearn.metrics import classification_report,accuracy_score, confusion_matrix
print(classification_report(Y_test, y_predict))
    
print(accuracy_score(Y_test,y_predict))
print(confusion_matrix(Y_test, y_predict)) 


# In[92]:


y_predict_labels = ['Survived' if prediction==1 else 'Not Survived' for prediction in y_predict]


# In[96]:


y_predict_labels = ['Survived' if prediction==1 else 'Not Survived' for prediction in y_predict]


print(y_predict_lables)



# In[ ]:




