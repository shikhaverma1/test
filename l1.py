# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 22:21:30 2018

@author: HP
"""
#%%
import pandas as pd
import numpy as np
import statistics as stats
#%%
a=10
b=5
#%%
ab = np.add(a,b)
#%%
ab1 = np.subtract(a,b)
#%%
s = [12,24,44,6,67,7]    
#%%
ab11=np.divide(a,b)
#%%
smax=np.max(s)
#%%
smin=np.min(s)
#%%
smean=np.mean(s)
#%%
smedean=np.median(s)
#%%
abc = [1,2,3,2,2,2,2]
#%%
ab11= stats.mode(abc)
#%%
abc11 = np.mod(a,b)
#%%
adf = [[1,3,4,4],[3,5,5,6]]
#%%
a_dic={"a":"aa","b":"bb","c":"cc"}

#%%
m=np.mat([[2,4],[2,3]])
amat=np.mat('4 3; 2 1')
#%%
arr_adf=np.array(adf)      
#%%
arr1=np.array([[1,3,6,7],[8,9,7,4]])

#%%
arrme=np.mean(1)
arrshape=np.shape(arr1)
#%%
d={'col1':[1,2],'col2':[3,4]}
df=pd.DataFrame(data=d)

df2=pd.DataFrame(np.random.randint(low=0, high=10, size=(5,5)),
       columns=['a','b','c','d','c'])

df3=pd.DataFrame(np.random.randint(low=0,high=7,size=(3,3)),
                 columns=['1','2','3'])

absdf=pd.abs(df3)



#%%
df4=pd.DataFrame(np.random.randint(low=0,high=10,size=(6,6)),
                 columns=['a','b','c','d','e','f'])
                 
#%%
s=pd.Series([-1,1.2,3,4.5])
s.abs()
t=pd.Series([pd.Timedelta('1 days')])
t.abs()
se=pd.Series([2,7,5,3])
se.add_prefix('xo_')        #for series the row lable is prefix and same as for suffixed

#%%
df5=pd.DataFrame({
        'a':[1,3,3,5,5],
        'b':[-4,5,6,8,1],
        'c':[5,7,2,9,0,]})
df5
df5.abs()
df6=pd.DataFrame({
        'a':[1,3,np.nan],
        'b':[3,6,7],
        'd':[1,5,3]})
add56=df5.add(df6 ,fill_value=0)
#%%
abc = [1,2,3,4,5,6,7]
dftd = pd.SeriesI(abc)
#%%
df5.add_prefix('item_')    #For dataframe the colume lable is prefix and same as for suffixed

df6.agg(['sum','min'])    #use for performing one or more opration on row

df6.agg("sum", axis="columns") #use 4 performing one operation on column

df6.agg({'a':['sum','min'], 'b':['max','min'],'d':['sum','max'] }) #diff operation per columns

#%%
'''dfxx = pd.DataFrame([[1, 2, 3],
                    [4, 5, 6],
                   [7, 8, 9],
                    [np.nan, np.nan, np.nan]],
                columns=['A', 'B', 'C'])          this work on column,it is wrong
dfxx.agg(['sum','min'])'''
#%%
s1=pd.Series([True,True])
df7=pd.DataFrame({
        'a':[True,True],
        'b':[True,False]})
df7.all()
s1.all()
df7.any()
s1.any()

