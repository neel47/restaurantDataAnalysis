
# coding: utf-8

# In[10]:




import seaborn as sb
import pandas as pd
import numpy as np
import math 


df=pd.read_csv('Restaurant.csv')

df.replace({ 'sex': {'Male':0 , 'Female':1} ,
            'smoker' : {'No': 0 , 'Yes': 1},
            'time' : {'Lunch': 0 , 'Dinner': 1},
            'day': {'Sun':7 , 'Sat':6, 'Fri':5, 'Thur':4},
            'food': {'poutine':1 , 'pizza':2, 'burger':3, 'shawarma':4,'bagel':5 , 'tacos':6, 'nachos':7, 'butter tarts':8,
                     'burritos':9 }
            } ,inplace=True)

X = df[['sex','smoker','size','day','time']]
Y = df[['tip']]

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test , y_train , y_test = train_test_split(X,Y,test_size=0.25,random_state=26)

model = LinearRegression()
model.fit(X_train, y_train)

predictions=model.predict(X_test)

#sex=Male,smoker=Yes,Table size=2,day=Sunday,time=dinner
myvals = np.array([0,1,2,7,1]).reshape(1,-1)
p=model.predict(myvals)
print("Predicted tip amount : ",math.ceil(p*100)/100)




