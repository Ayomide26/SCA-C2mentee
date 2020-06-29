#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#password genrate
import random
characters ='abcdefghijklmnopqrstuvwxyzABDCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*<>?/'
number = input('how many many letters,numbers you want =')
number =int(number)

length = input('How long you want your password? =')
length = int(length)
for p in range(number):
    while length < 6:
        print('Please use a length of password greater than 6')
    break
password = ''
for c in range(length):
    password    = random.choice(characters)
    print(password)


# In[ ]:




