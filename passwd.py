!pip install pyperclip

import random
import string
import pyperclip
import time
#from datetime import date
#from datetime import datetime


print("__________________________________")
print("generador de contraseñas")
print("__________________________________")

#day = date.today()
#print("dia {}".format(day.day))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

chars = lower + upper + num + symbols
temp = random.sample(chars, 25)

nameId = str(input("escriba palabra clave para identificar: "))
passwd = temp

time_list = time.localtime()
time_string = time.strftime("%m/%d/%Y,  %H:%M:%S \n", time_list)
print(time_string)

with open("contraseñas.txt", "a", encoding="utf-8") as file:
    dataId = nameId
    file.write(dataId + "\n \n")

    dataPw = passwd
    file.write(str(time_string) + "".join(dataPw) + "\n \n")
  
pyperclip.copy("".join(dataPw))
print("".join(dataPw))