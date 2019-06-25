#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=15
if(x<=15):
    print("the number is less than 15")


# In[ ]:


x=10
if(x<10):
    print("ok")
else:
    print("....")


# In[ ]:


a=10
b=20
if(a<b):
    print("b is grater")
else:
    print("a is grater")


# In[ ]:


a=10
b=20
if(a==b):
    print(a**2)
else:
    print(a*b)


# In[ ]:


x=0
if(x>0):
    print("x is a positive number")
elif(x<0):
    print("x is a negative number")
elif(x==0):
    print("x = 0")


# In[33]:


a=1
while(a<=10):
    print(a);
    a=a+1


# In[35]:


a=-22
while(a>=-45):
    print(a);
    a=a-1


# In[37]:


x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
sum=0;
while(x!=y):
    if(x%2==0):
        sum=sum+x;
    x=x+1;
print(sum);


# In[46]:


x=int(input("enter the value"))
sum=0
while(x!=0):
    r=x%10;
    if(r%2==0):
        sum=sum+r;
    x=x//10;
print(sum)


# In[47]:


x=int(input("enter the number"))
while(x!=0):
    r=x%10;
    if(r==1):
        print("one")
    elif(r==2):
        print("two")
    elif(r==3):
        print("three")
    elif(r==4):
        print("four")
    elif(r==5):
        print("five")
        x=x//6


# In[49]:


x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
z=int(input("enter the value of z"))
digit=0
c=0
while(y<=z):
    j=y;
    while(j!=0):
        digit=j%10;
        if(digit==x):
            c=c+1;
        j=j//10;
    y=y+1;
print(c);      


# In[51]:


def printnaturalnumbers(n):
  count=1;
  while(count<=n):
    print(count,end=" ");
    count=count+1;
  print()
  return


printnaturalnumbers(15);


# In[52]:


def fact(n):
    fact=1;
    while(n!=0):
        fact=fact*n;
        n=n-1;
    return fact    
    
print(fact(5))


# In[ ]:


def countOfPalindrome(n1,n2):
    cnt=0
    
    while(n1!=n2):
        sum=0
        buffer=n1
        while(n1!=0):
            r=n1%10
            sum=(sum*10)+r
            n1=n1//10
        if(buffer==sum):
            cnt=cnt+1
        n1=buffer
        n1=n1+1
    return cnt;
print(countOfPalindrome(10,30));
print(countOfPalindrome(1,10000000));

    


# In[2]:


def printeven(n):
    count=0;
    sum=0;
    while(count!=n):
        if(count%2==0):
            sum=sum+count;
        count=count+1;
    return sum;
 
print(printeven(20))    


# In[5]:


def factlist(n):
    i=1;
    while(i!=n):
      if(n%i==0):
        print(i);
      i=i+1;
    return i;
factlist(30);


# In[6]:


list=[1,2,3,4,5];
print(list);
print(list[3])
      


# In[10]:


list1=[1,2,3,4,5,6,7]
for x in list1:
    print(x)
    
print();
print(list[4]);
print(list[3:6]);
print(list[0:4]);


# In[17]:


list=[1,2,3,4,5,6,7,8,9]
for x in list:
    print(x)
    
print(list[8:1:-1]);
print(list[::3]);
print(list[::2]);    
    


# In[34]:


list1=["pranay","ashish","vamshi",1]
#for x in list:
list1[2]=6;
print(list1);
del list1[1];
print(list1);


# In[38]:


list2=[1,2,3,4,4,4,5,6,7,9]
print(list2.count(4))
list2.append(8)
print(list2)


# In[39]:



#List example with particular index
list1=[1,2,3,4,5,6,7]
for x in list1:
    print(x,end=" ")
    
print();
print(list1[4]);
print(list1[3:6]);
print(list1[0:7]);
print(list1[0:5]);


# In[40]:


list1=[1,2,3,4,5,6,7,8,9,10]
for x in list1:
    print(x,end=" ")

print();
print(list1[1:-1]);
print(list1[2:-2]);
print(list1[::2]);
print(list1[::3]);


# In[44]:



list1=["shiva","pranay","ashish"]
print(list1);
list1[2]=15;
print(list1);
list1[1]=12;
print(list1);
del list1[0]
print(list1)
list2=[1,2,3];
print(list2);
print(list1+list2);


# In[46]:



#Adding a number to list
list1=[9,8,7,6,5,4,3,2,1]
print(list1);
list1[3]="abcd";
list1[4]="hi";
del list1[2];
list1.append(124);
print(list1);


# In[49]:



list1=["python","programming",1,5,"gitam"]
print(list1)
n=list1.index("python");
print(n)
list1.index(1)
print(len(list1))
list1.insert(2,"hi")
list1.append("bye")
print(list1)
list1.pop(4)
print(len(list1))
list1.insert(4,"hello")
print(list1)


# In[50]:


list1=["python","programming",1,5,"gitam"]
print(list1)
n=list1.index("python");
print(n)
list1.index(1)
print(len(list1))
list1.insert(2,"hi")
list1.append("bye")
print(list1)
list1.pop(4)
print(len(list1))
list1.insert(4,"hello")
print(list1)
list1.reverse()
print(list1)


# In[52]:


#linear search
def linearsearch(a,key):
    flag=0;
    for i in range(len(a)):
        if a[i]==key:
            flag=1;
            break
    if(flag!=0):
        print("Target is Found")
    else:
        print("target is not found")

a=[1,4,2,8,54,78,34,56,32]
key=int(input("Enter The Number to search"))
linearsearch(a,key)


# In[55]:


#Duplicate linear search
def linearsearchdup(a,key):
    flag=0;
    for i in range(len(a)):
        if a[i]==key:
            flag=flag+1;
            
    print(flag)        
    if(flag!=0):
        print("Target is Found")
    else:
        print("target is not found")

a=[145,576,423,76,432,7,875,543]
key=int(input("Enter The Number to search"));
linearsearchdup(a,key)


# In[58]:


def linearexample(a,key):
    for i in range(len(a)):
        if a[i]==key:
            print(i,end=" ")

a=[1,2,3,4,5,6,7,8]
linearexample(a,5)



# In[68]:


def linearexample2(a,item):
    for i in range(len(a)):
        if(a[i]==item):
            j=0
            while(j!=i):
                print("$",end='   ')
                j+=1
            print(' ')
a=[1,2,9,3,4,5,6,7,8,2]
linearexample(a,4)


# In[ ]:


def linearexample(a):
    for i in range(len(a)):
        if(a[i]%3==0 and a[i]%5==0):
            print()


# In[69]:


def linear1(a):
    sum=0;
    for i in range(len(a)):
        if(a[i]%3==0 and a[i]%5==0):
            sum=sum+a[i]
    print(sum)
a=[15,12,2,9,18,36,45]
linear1(a)


# In[70]:


def linear2(a):
    for i in range(len(a)):
        if i==0 or i==(len(a)-1):
            print(a[i],end=" ")
        else:
                print(a[i-1]*a[i+1],end=" ")
    print(a[i])
    
    
    
a=[1,2,3,4,5]    
linear2(a)


# In[71]:



def linear3(a):
    for i in range(len(a)):
        if i==0 or i==(len(a)-1):
            print(a[i],end=" ")
        elif(a[i-1]%2==0 and a[i+1]%2==0):
            print(a[i],end=" ")
        else:print(end=" ")
            
a=[1,6,9,4,16,19,22]    
linear3(a)


# In[3]:


def binarysearch(a,lindex,rindex,key):
    while lindex<=rindex:
        mindex=lindex+(rindex-lindex)//2
        if a[mindex]==key:
            return mindex
        if a[mindex]>key:
            rindex=mindex-1
        else :
            lindex=mindex+1
    return -1;
a=[1,4,8,9,75,82,94,112]
key=int(input("Enter The Element To search"))
res=binarysearch(a,0,7,key)
if res!=-1:
    print("It is Found")
else:
    print("It is Not found")


# In[5]:


def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                
for i in range(len(a)):
    print(a[i],end="  ")
    
list1=[19,1,25,6,18,3]
bubblesort(list1)


# In[6]:


#creating a string
str = "application"
print(str)

str1 = 'application'
print(str1)

str2="""application test
        working
        completed
        list
        strings
        python"""
print(str2)


# In[9]:


str="application"
print(str)
print("str[0]=",str[0])
print("str[1]=",str[1])
print("str[-3]=",str[-3])
print("str[-2]=",str[-2])
print("str[2]=",str[2])
print("str[2:-2]=",str[2:-2])
print("str[3:5]=",str[3:5])
print("str[0:5:2]=",str[0:5:2])


# In[1]:


#function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
     
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
  

s=input("Enter The Character")

ans = isPalindrome(s) 
  
if ans == True: 
    print("Yes") 
else: 
    print("No")


# In[2]:


#count of upper case letters
def countupperletters(str):
    cnt=0
    for i in range (len(str)):
        if(str[i]<="A" or str[i]>="Z"):
            cnt=cnt+1;
        else:
            i=i+1;
    return cnt

print(countupperletters("HJKHJH")) 


# In[3]:


def countchars(str):
    return len(str)
s=str("enter a string")
countchars(s)


# In[4]:


def countdigit(n):
    return len(n)

countdigit("231456987")


# In[5]:


#Count of upper case letters
def countOfUpperCaseChars(str):
    cnt=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=65 and ord(str[i])<=90:
            cnt=cnt+1;
         
        
    return cnt;


print(countOfUpperCaseChars('HIknashdghgUIHUIib'))
print(countOfUpperCaseChars('LYTUD'))


# In[6]:


def printdigits(str):
    return print(str)


str="Applications"
printdigits(str)


# In[7]:


str='H'
str1='i'
str1.islower()


# In[15]:


str='H'
str1='i'
str1.islower()


# In[16]:


str='H'
str1='i'
str1.islower()


# In[ ]:





# In[17]:


str='H'
str1='i'
str1.islower()


# In[18]:


str='H'
str1='i'
str1.islower()


# In[19]:


str='H'
str1='i'
str1.islower()


# In[20]:


def printdigits(str):
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            print(lst[x],end="")
    return;        
          
print(printdigits("Miketesting 124123"))   


# In[26]:


def sumofdigits(str):
    sum=0
    lst = list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord (lst[x])<=57:
            sum = sum + ord(lst[x])-48;
            
    return sum
sumofdigits("shiva4321")


# In[29]:


def evensumdigits(str):
    sum=0
    lst=list(str)
    for x in range(len(str)):
        if ord(str[x])>=48 and ord(lst[x])<=57:
            if ((ord(lst[x])-48)%2==0):
                sum=sum+ord(lst[x])-48
                
    return sum
print(evensumdigits("shiva9876"))
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




