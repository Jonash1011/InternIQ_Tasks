import string
import random
length=int(input("Enter length:"))
chars=string.ascii_letters
chars+=string.digits
chars+=string.punctuation
password=''.join([random.choice(chars) for i in range (length)])
print("Your random password:",password)