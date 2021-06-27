          
    diff = 0.0
    i = 0
    for num in values:
        diff = float( math.sqrt ( ( float(values[rand]) - float(num) )**2 ) )
        diff = float( format( diff, '.4f') )
        i += 1
        j += 1
        print("----", i, "Diff: ", diff)
    print(j, '----------------------')