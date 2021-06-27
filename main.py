import os
import re
import random
import math
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
    newDicts = []
    for dct in dicts:
        newValueList = []
        sum = summation(list(dct.values())[0])
        for key, values in dct.items():
            for value in values:
                newValueList.append (format ((float(value) / sum), '.4f'))
        dct = { key : newValueList}
        newDicts.append(dct)
    dicts = newDicts
        
except Exception:
    print("خطا در نرمالسازی!!!")

#-----------------------------------------------------------
try:
    for dct in dicts:
        rndList = []
        while len(rndList)<5:
            random.seed()
            x = random.randint(0,9)
            if x not in rndList:
                rndList.append(x)
        diffList = []
        j = 0
        for rand in rndList:
            values = list(dct.values())[0]
            diff = 0.0
            i = 0
            for num in values:
                diff = float( math.sqrt ( ( float(values[rand]) - float(num) )**2 ) )
                diff = float( format( diff, '.4f') )
                i += 1
                j += 1
                print("----", i, "Diff: ", diff)
            print(j, '----------------------')
                
except Exception:
    raise Exception