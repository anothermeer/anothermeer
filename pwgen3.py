# import
import time
import random
import string
import os
import sys

# greed the user
print('hello, Welcome to Password generator!')

# ask the user his/her name
name = str(input(f"what can i call you?\n"))
print("hi "+name, ", nice to meet you, i am doing some important things for you.")
time.sleep(7)

# ask the user to input the password length
print("hey "+name, ", can you input the length of the password?(8-94)")
length = int(input("length : "))
print("thanks!")
time.sleep(3)

# collect the character
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# make the password
all: int = lower + upper + num + symbols
temp = random.sample(all,length)
password = "".join(temp)

# print the password
print("your random password is :"+password)

# user selection
answer = input("[detector]: program is over, enter any key and press 'enter' to exit: ")