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
    #for figure in mainList:
    #    print(figure.get(0))
except Exception:
    raise Exception

#-----------------------------------------------------------
try:
    with open("output.txt", "w") as file:
        try:
            for figure in mainList:
                file.write("**********************************************\n")
                file.write("**\t\t\t\t    Row: " + str( list( figure.keys() )[0]) + '    \t\t\t\t**\n')
                file.write("**********************************************\n")
                valueList = []
                dicts = figure.get(list(figure.keys())[0])
                
                try:
                    tDiff = 0.0
                    mValues = dicts.get('mValues')
                    rValues = dicts.get('rValues')
                    j = 0
                    for mval in mValues:
                        file.write("markaz: "+ mval+ " -----------\n")
                        i = 0
                        diff = 0.0
                        for rval in rValues:
                            diff = float( math.sqrt ( ( float(mval) - float(rval) )**2 ) )
                            diff = float( format( diff, '.4f') )
                            i += 1
                            j += 1
                            tDiff += diff
                            tDiff = float( format( tDiff, '.4f') )
                            file.write("----%s Diff: %s \n" % (str(rval), str(diff)))
                        
                except Exception:
                    raise Exception


        except Exception:
            raise Exception   
except Exception:
    raise Exception

#-----------------------------------------------------------
       
    