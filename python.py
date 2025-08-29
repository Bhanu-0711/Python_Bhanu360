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
'''a = 10
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
