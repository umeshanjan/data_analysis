# -*- coding: utf-8 -*-
"""DAP.ipynp

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yyeOk2tGv1hJX8LevXwrWvSLGEXbtC1w
"""

!pip install numpy
matrix1 = np.array([[1, 2],
           [3, 4]])

matrix2 = np.array([[5, 6],
           [7, 8]])

result = np.add(matrix1, matrix2)
if result.any():
    print("Result of Matrix Addition:")
    for row in result:
        print(row)



import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

zeros_arr=np.zeros((3,3))
print(zeros_arr.astype(int))

ones_arr=np.ones((2,2))
print(ones_arr.astype(int))

arange_arr=np.arange(10)
print(arange_arr)

reshaped_arr=arr.reshape(5,1)
print(reshaped_arr)

sliced_arr=arr[2:4]
print(sliced_arr)

a1=np.array([1,2,3,4,5])
a2=np.array([6,7,8,9,10])
c=np.vstack(a1+a2)
print(c)
d=np.stack(a1+a2)
print(d)

arr=np.array([1,2,3,4])
arr1=np.split(arr,2)
print(arr1)

a=np.array([[1,2,3,4],[5,6,7,8]])
b=a.T
print(b)

a=np.array(([1,2],[3,4]))
print(a)
b=np.array(([5,6],[7,8]))
print(b)
c=np.dot(a,b)
print(c)

d=np.linalg.eig(c)
print(d)

a=np.array(([1,2,3],[4,5,6]))
b=np.array(([5,6,7],[9,8,4]))
c=np.sum(a+b)
print(c)

c=np.sum(a,axis=0)
d=np.sum(a,axis=1)
print(c)
print(d)

a=np.array([1,2,3,4,5])
b=np.mean(a)
c=np.median(a)
d=np.var(a)
e=np.std(a)
print(b)
print(c)
print(d)
print(e)

import numpy as np

arr1=np.array([1,2,3,4,5])
a=arr1+3
print(a)
arr2=np.array([6,7,8,9,10])

result=arr1+arr2

print(result)

import numpy as np
data=np.loadtxt("/content/date.txt.txt",dtype=int)
d=np.savetxt("/content/date.txt",data)
print(d)
print(data)

import matplotlib.pyplot as plt
a=np.array([1,2,3,4,5,6,7,8,9])
plt.plot(a)

import pandas as pd
a=["umesh","aakhil","prasad","farhan","lovaraj","umar","purna"]
r=pd.Series(a,index=[34,56,78,90,23,45,67])
print(r)

df=pd.read_csv("/content/insurance.csv",sep=" ")
print(df)



dff=pd.read_csv("/content/insurance.csv",sep=" ")
print(dff)

df=pd.read_csv("/content/aiii.txt.txt",sep=" ")
print(df)

df=pd.read_excel("/content/salesworkload.xlsx",sheet_name=0)
print(df)
print(df.loc[1])
print(df.loc[2:5])

dff.head(5)
dff.tail(5)
dff.shape

df=pd.read_csv("/content/insurance.csv",sep=" ")
print(df)
df.head(5)



from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
a=pd.read_csv("/insurance.csv")
print(a)
a.shape
b=a.head(10)
c=a.tail(10)
d=pd.concat([b,c],axis=0)
d.to_csv("umesh.csv")
print(d.groupby(['age'])['bmi'].count())

import numpy as np
import matplotlib.pyplot as plt
runs = np.array([100,50,91,78,89,25,34,19,9,10])
w=np.array([1,0,2,0,3,7,8,9,7,5])
plt.plot(runs,w,color='orange')
plt.title('IndvsAus_score')
plt.show

import numpy as np
import matplotlib.pyplot as plt
tigar=np.linspace(-2*np.pi,2*np.pi,50)
print(tigar)
plt.scatter(tigar,np.sin(tigar) ,color='pink')
plt.title("sin(x)")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

overs=np.arange(5,50,5)
overs_a=np.arange(5,30,5)
plt.subplot(2,1,2)
runs_i=np.array([25,51,84,131,160,189,220,250,267])
runs_a=np.array([15,41,94,110,151])
wickets=np.array([12,32,96])

plt.plot(overs,runs_i,color='blue',label='India')
plt.plot(overs_a,runs_a,color='yellow',label='Aus')

import matplotlib.pyplot as plt

a=[230,560,780,127,128]
b=[200,160,270,127,400]
years=[1,2,3,4]

profit_a=[(a[i]-a[i-1]) for i in range(1,len(a))]
profit_b=[(b[i]-b[i-1]) for i in range(1,len(b))]
plt.subplot(2,1,2)
plt.plot(years,profit_a,color='hotpink',linewidth='3',label='CompanyA',marker='>',ms='15',mec='k')
plt.subplot(2,1,1)
plt.plot(years,profit_b,color='black',linestyle='dotted',label='CompanyB',marker='H')

a=np.array([25,60,5,10])
labe=["AIML","Python","Pandas","Numpy"]
plt.pie(a,labels=labe)
plt.show()

a=np.array([25,60,5,10])
labe=["AIML","Python","Pandas","Numpy"]
explo=[0.2,0,0,0]
plt.pie(a,labels=labe,explode=explo,startangle=180,textprops={'fontsize':34})
plt.show()