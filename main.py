import os
import re
import random
from pathlib import Path

def numberCleaner(phrase):
    return re.sub("[^\d\.]", "", phrase)
    
def summation(lst):
    sum = 0
    for i in lst:
        sum += int(i)
    return sum

BaseDir = Path(__file__).resolve().parent
#-----------------------------------------------------------
try:
    with open(os.path.join(BaseDir, "input.txt")) as file:
        lines = file.readlines()

except FileNotFoundError as e:
    print("فایل یافت نشد!")


#-----------------------------------------------------------
else:
    try:
        dicts = []
        for line in lines:
            choosen = map (numberCleaner, line.split(",") )
            dicts.append({ lines.index(line) : list(choosen) })
    except Exception:
        print("ارقام پردازش نشد!")

#-----------------------------------------------------------
try:
    for dic in dicts:
        try:
            sum = summation(list(dic.values())[0])
            print(list(dic.values())[0], " --> ", sum)
        except Exception:
            print("Minor ERROR!!!")
        
except Exception:
    print("ERROR!!!")