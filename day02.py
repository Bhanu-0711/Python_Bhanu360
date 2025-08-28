##Guessing Number Game 
import math
import random
x=int(input('Enter the range:- '))
y=str (x//2)
print('You will get only '+y+' chances') 
for i in range(1,(x//2)+1):
    a=random.randint(1,10)
    b=int(input('Enter the no. you guess:- '))
    if (a==b):
        print('You guessed it right')
        break
    else:
        print('You guessed wrong')
        pass