import string
from random import *

pw = ""
pw_len = int(input("How long will your password be?"))
 
for i in range(pw_len):
    pw += choice(string.printable)

print(pw)