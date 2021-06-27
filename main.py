import os
import re
import random
from pathlib import Path

def numberCleaner(phrase):
    return re.sub("[^\d\.]", "", phrase)
    
def summation(lst):
    sum = 0
    for i in lst:
        sum += float(i)
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
    for dct in dicts:
        newValueList = []
        sum = summation(list(dct.values())[0])
        for key, values in dct.items():
            for value in values:
                newValueList.append (format ((float(value) / sum), '.4f'))
            dct = { key : newValueList}
        
except Exception:
    raise Exception
    #print("ERROR!!!")