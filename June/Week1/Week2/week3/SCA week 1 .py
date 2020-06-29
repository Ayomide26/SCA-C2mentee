#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Guess a number
import random
numofguesses = 0
number= random.randint(1,20)
#while numofguesses < 6:
print("take a guess.")
guess=input()
guess =int(guess)
numofguesses = numofguesses + 1
if guess < number:
        print("NUmber is too Low")
if guess > number:
        print("NUmber is too High")
if guess == number:
        print("You guessed right")
        
    


# In[6]:


import random
characters ='abcdefghijklmnopqrstuvwxyzABDCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*<>?/'
number = input('how many many letters,numbers you want =')
number =int(number)

length = input('How long you want your password? =')
length = int(length)
for p in range(number):
    password = ''
for c in range(length):
    password    = random.choice(characters)
    print(password)


# In[ ]:





# In[ ]:




