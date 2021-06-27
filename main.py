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

def generateRL():
    rndList = []
    random.seed()
    while len(rndList)<5:
        x = random.randint(0,9)
        if x not in rndList:
            rndList.append(x)
    return rndList

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
mainList = []
try:
    for dct in dicts:
        mMarks = generateRL()
        values = list(dct.values())[0]

        rValues = []
        for i in range(0, len(values)):
            if not (i in mMarks):
                rValues.append(values[i])
        #print(rValues)
        
        mValues = []
        for i in range(0, len(values)):
            if i in mMarks:
                mValues.append(values[i])
        #print(mValues)
        print()
        dct = { list(dct.keys())[0] : {
                                        'rValues' : rValues,
                                        'mValues' : mValues,    }
                                        
                }
        mainList.append(dct)
    print(mainList)  
except Exception:
    raise Exception

#-----------------------------------------------------------
"""           
    diff = 0.0
    i = 0
    for num in values:
        diff = float( math.sqrt ( ( float(values[rand]) - float(num) )**2 ) )
        diff = float( format( diff, '.4f') )
        i += 1
        j += 1
        print("----", i, "Diff: ", diff)
    print(j, '----------------------') """