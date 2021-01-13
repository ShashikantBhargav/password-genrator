import random

lower = "abcdefghijklmnopqrstvuwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"
number = "123456789"
symbols = "[]{}()*;/,_-"

all = lower+upper+number+symbols

length=16
password= "".join(random.sample(all,length))
print(password)
