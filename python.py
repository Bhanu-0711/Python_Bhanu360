#Casing 
'''
camelCase = 'Bhanu'
Pasclecase = 'Pratap'
snake_case = 'Singh' 
'''

# Many To Multiple Variable
'''x,y,z=1,2,3
print(id(x))
print(id(y))
print(id(z))'''

# One To Multiple
'''x=y=z=7
print(id(x))
print(id(y))
print(id(z))'''

# Unpacking
'''a=['apple','banana','cherry']
x,y,z=a
print(x)
print(y)
print(z)'''

# Global Variable 
'''global x # using keyword to declare globally
y='WOW'  # declaring globally in the code'''

# Numeric Data Type
'''
a = 10
b = 10.0
c = True
d = 2+3j
print(type(a))
print(type(b)) 
print(type(c))
print(type(d))  '''  

#single line commenting
'''multi line commenting'''  

# Using len function
'''a='hello world' 
print(len(a))''' 
    
#Replace string
'''a="Hello World"
print(a.replace("H","J"))'''

#Split string
'''a="Hello World"
print(a.split(","))'''

#Using Format instrings
'''age=36
txt=f"My name is John, I am {age}"
print(txt)'''

#Boolean 
'''a=(5>2)
print(a)'''

'''print(bool(-1))'''

#Function returning a boolean value
'''def myfunc():
    return True

if myfunc():
    print("YES!")
else:
    print("NO!")'''
    
#Sequence Datatype
#LIST
'''list=['abcd', 786 ,2.23 , 'john' , 70.2]
tinylist= [23, 'cutie']
print (list)
print(type(list))
print(list[2:])
print(list + tinylist)'''

#TUPLE (same as list except the brackets)
'''tuple=('abcd', 786 ,2.23 , 'john' , 70.2)
print(tuple *2)'''

#Range(start ,stop , step)
'''for i in range(1,5,2):
    print(i)'''
    
#match statement
'''day =10
match day:
    case 5:
        print("Monday")
    case 6:
        print("Tuesday")
    case 7:
        print("Wednesday")
    case 4:
        print("Thursday")
    case _:
        print("Invalid day")'''

#using multiple cases in match and also use conditions inside case
'''day=5
match day:
    case 1|2|3|4|5 if day==5:
        print("Weekday")
    case _:
        print("Invalid Day")'''
        
        
#while loop
'''i=1
while i<6:
    print(i)
    i+=1'''

#square of a no.    
'''a=int(input('Enter a no.'))
print(a**2)'''

#sum of two nos.
'''a=int(input('Enter no. 1'))
b=int(input('Enter no. 2'))
print(a+b)'''

#swapping two variables 
#1
'''a=int(input('enter no. 1'))
b=int(input('enter no. 2'))
a=a+b
b=a-b
a=a-b
print('Nos. are swapped')'''

#2
'''import math
a=int(input('enter no. 1'))
b=int(input('enter no. 2'))
swap(a,b)'''

##Guessing Number Game 
'''import math
import random
x=int(input('Enter the range:- '))
y=str(x//2)
print('You will get only '+y+' chances') 
a=random.randint(1,x)
for i in range(1,(x//2)+1):
    b=int(input('Enter the no. you guess:- '))
    if (a==b):
        print('You guessed it right')
        print(f'The no. was {a}')
        flag=1
        break
    else:
        print('You guessed wrong')
        flag=0
        pass
if(flag==1):
    pass
else:
    print(f'The no. was {a}')'''

#check no is even or odd
'''a=int(input('enter a no'))
if(a%2==0):
    print(f'{a} is Even')
else:
    print(f'{a} is Odd')'''
    
#converting celcius to fahrenheit
'''a=int(input('enter temp in celcius'))
b=int(input('enter temp in fahrenheit'))
print('temp in fahrenheit is',(9/5*a)+32)
print('temp in celcius is',(b-32)*(5/9))'''

#type of a variable
'''a=int(input('enter no'))
b=bool(input())
print(type(a),type(b))'''

#simple interest
'''p=int(input('enter principle'))
r=float(input('enter rate of interest'))
t=int(input('enter time'))
print('The simple interest is ',(p*r*t)/100)'''

#reverse of a string
'''a=input('enter a string:-  ')
print(a[::-1])'''


#using break in while
'''i=0
while i<6:
    print(i)
    if i==3:
        break
    i+=1'''

#using continue in while
'''i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)'''
    
#list in python
'''fruits=['Apple','Cherry','Banana']
for i in fruits:
    print(i)'''
    
#string iteration
'''for i in "Apple":
    print(i)'''
    
# break in list
'''fruits=['Apple','Banana','Cherry']
for i in fruits:
    print(i)
    if i=='Banana':
        break'''

# continue in list
'''fruits=['Apple','Banana','Cherry']
for i in fruits:
    if i=='Banana':
        continue        
    print(i)'''
    
# Range with start,end,step value
'''for i in range(1,10,2):
    print(i)'''
    
# using else after for 
'''for i in range(10):
    print(i)
else:
    print('Finally')'''
    
# using else after while
'''i=0
while (i<6):
    print(i)
    i+=1
else:
    print('Iteration completed')'''
    
# nested loop
'''a=['A','B','C']
fruits=['Banana','Apple','Cherry']
for x in a:
    for y in fruits:
        print(x,y)'''
        
# pass statement
'''for i in range(5):
    pass'''
    

## LIST 
# 1 list allows duplicate values
# 2 list is ordered and changable
'''list1=["red","blue","green","red",1,3,10.34]
print(list1)'''
# list constructor function
'''list2=list(("red","blue","green","red",1,3,10.34))
print(list2)'''
# indexing
'''list1=["red","blue","green","red",1,3,10.34]
print(list[1])'''
# negative indexing
'''list1=["red","blue","green","red",1,3,10.34]
print(list[-1])'''
# range of indexing
'''list1=["red","blue","green","red",1,3,10.34]
print(list[2:4])'''
# negative range
'''list1=["red","blue","green","red",1,3,10.34]
print(list[-4:-1])'''
# check if item present
'''list1=["red","blue","green","red",1,3,10.34]
if "green" in list1:
    print("YES")'''
# change list item
'''list1=["red","blue","green","red",1,3,10.34]
list1="pink"
print(list1)'''
# changing range of items
'''list1=["red","blue","green","red",1,3,10.34]
list1[1:3]=['red']*2
print(list1)'''
# using insert function
'''list1=["red","blue","green","red",1,3,10.34]
list1.insert(2,'hello')
print(list1)'''
# using append function
'''list1=["red","blue","green","red",1,3,10.34]
list1.append('world')
print(list1)'''
# using remove function
'''list1=["red","blue","green","red",1,3,10.34]
list1.remove('world')
print(list1)'''
# extending a list
'''list1=["red","blue","green","red",1,3,10.34]
list2=['rothan','bhanu','ayushi']
list1.extend(list2)
print(list1)'''
# using pop function
'''list1=["red","blue","green","red",1,3,10.34]
list1.pop(3) # entering the index to delete
print(list1)'''
