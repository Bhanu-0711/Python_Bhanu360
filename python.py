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

#swaping two variables 
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