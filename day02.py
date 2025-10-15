##Guessing Number Game 
import math
import random
x=int(input('Enter the range:- '))
print(f'You will get only {x//2} chances') 
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
    print(f'The no. was {a}')

