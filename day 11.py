#!/usr/bin/env python
# coding: utf-8

# In[2]:


class demo:
    def test(self):
        print("test() for the class and method")
        return

abj=demo()    
abj.test()


# In[3]:


def test():
    print("test() for function")
    return
test()


# In[6]:


class demo1:
    def fact(self,n):
        #return the factorial
        fact=1
        while(n!=0):
            fact=fact*n
            n=n-1
        return fact    
        
p1=demo1()        
p1.fact(5)
    


# In[11]:


import numpy as np
np.arange(1,100,9)


# In[12]:


np.arange(1,20,5)


# In[18]:


np.arange(1,2048,564)
np.arange(1,20,5)


# In[21]:


a1=np.array([(1,2,3),(4,5,6)])
print("slicing column :",a1[:,1])


# In[22]:


a1=np.array([(1,2,3),(4,5,6)])
print("slicing column :",a1[:,2])


# In[23]:


a1=np.array([(1,2,3),(4,5,6)])
print("first row :",a1[0])


# In[25]:


a1=np.array([(1,2,3),(4,5,6)])
print("second row :",a1[1])


# In[26]:


a1=np.array([(1,2,3),(4,5,6)])
print(a1)


# In[27]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(A)[2]=5
print(A)


# In[28]:


np.ones((5,5),dtype=np.int64)


# In[29]:


np.zeros((4,2))


# In[30]:


#generate the random numbers from np
a1=np.random.normal(5,0.5,10)
print(a1)


# In[31]:



a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.vstack((a1,a2)))


# In[32]:


a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.hstack((a1,a2)))


# In[33]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
array+10
print(array)


# In[36]:


#Some inheritence
class Person(object):
    #constructor
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
#Derive Class
class Employee(Person):
    def isEmployee(self):
        return True
emp=Person("SHIV")
print(emp.getName(),emp.isEmployee())
emp1=Employee("SHIVA")
print(emp1.getName(),emp1.isEmployee())


# In[35]:


a1=np.random.normal(5,1,10)
print(a1)
print("Minimum value:",np.min(a1))
print("Maximum value:",np.max(a1))
print("Mean value:",np.mean(a1))
print("median value:",np.median(a1))


# In[37]:


c1=np.array([1,2])
c2=np.array([4,5])
np.dot(c1,c2)


# In[41]:


c1=np.array([(1,2),(4,5)])
c2=np.array([(4,3),(2,6)])
np.dot(c1,c2)


# In[1]:


import pandas as pd
dict1={"name":["anil","akhil","dinesh","harsha","ajay","kranth"],
     "email":["anil@gmail.com","akhil@gmail.com","dinesh@gmail.com","harsha@gmail.com","ajay@gmail.com","kranth@gmail.com"],
     "p.no":[2135321525,23601625,36326562536,236262532,6855462322,98754623],
     "address":["dfhfhghfg","gjgfjfgjfg","fgdhhbcbhfghdfh","yityuwrterte","ghdghryjtuitury","wtrqqfwagjty"]}
b=pd.DataFrame(dict1)
print(b)


# In[ ]:




