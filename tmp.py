    for dic in dicts:
        try:
            sum = summation(list(dic.values())[0])
            print(list(dic.values())[0], " --> ", sum)
            for number in list(dic.values())[0]:
                print(dic.key, number)
        except Exception:
            raise Exception
            #print("Minor ERROR!!!")