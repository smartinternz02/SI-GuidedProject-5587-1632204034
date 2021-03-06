# -*- coding: utf-8 -*-
"""assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eHnyANi5k-j_2G2k_kO5Cc0J2JECeTUl
"""

#Assignment-1
#Dataset Bank

#mount dataset
from google.colab import drive
drive.mount('/content/drive')

#libraries
import pandas as pd
import numpy as np

dataset=pd.read_csv("/content/drive/MyDrive/AI/bank1.csv")
dataset.head(5)

dataset.info()

dataset.isnull().any()

#selected colums for preprocessing
bankdb=pd.DataFrame(dataset,columns=["age","education","marital","loan","previous", "poutcome","deposit"])
bankdb

bankdb["age"].unique()

bankdb["marital"].unique()

bankdb["education"].unique()

bankdb["loan"].unique()

bankdb["previous"].unique()

bankdb["poutcome"].unique()

bankdb["deposit"].unique()

a=bankdb["education"].mode()
a

b=bankdb["poutcome"].mode()
b

#in education and poucome we have unknown values replace with mode since it is categorical
bankdb["education"]=bankdb["education"].replace(to_replace='unknown', value='secondary')
bankdb["education"].unique()

bankdb["poutcome"]=bankdb["poutcome"].replace(to_replace='unknown', value='other')
bankdb["poutcome"].unique()

#label encoding for multiple column
from sklearn.preprocessing import LabelEncoder
label1=['education','marital','loan','poutcome' ]
le=LabelEncoder()
bankdb[label1]=bankdb[label1].apply(le.fit_transform)
bankdb

x=bankdb.iloc[:,0:6].values
y=bankdb.iloc[:,6:7].values
print(x)
print(y)

y.shape

#train split test split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

x_train.shape

y_train.shape

x_test.shape

y_test.shape

x.shape

y.shape