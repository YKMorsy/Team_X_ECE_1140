def switch_if(f, past, fut, other):
    f.write("IF ( ( ( A-"+str(past)+" & F-"+str(past)+" & ! O-"+str(past)+" ) | ( A-"+str(fut)+" & F-"+str(fut)+" & ! O-"+str(fut)+" ) | ( A-"+str(other)+" & F-"+str(other)+" & ! O-"+str(other)+" ) ) & O-"+str(i)+" ) {\n")


with open("track_controller/PLCs/RedLineTop_Red.txt", "w") as f:
    for i in range(2000, 2024):
        past = i-1
        fut = i+1
        if (i == 2001):
            past =  2016
        elif(i == 2009):
            fut = 2000
        elif (i ==2010):
            past = 2000

        if(i == 2016):
            other = 2001
            f.write("IF ( ( ( A-"+str(past)+" & F-"+str(past)+" & ! O-"+str(past)+" ) | ( A-"+str(fut)+" & F-"+str(fut)+" & ! O-"+str(fut)+" ) | ( A-"+str(other)+" & F-"+str(other)+" & ! O-"+str(other)+" ) ) & O-"+str(i)+" ) {\n")
        elif(i == 2000):
            other = 2009
            fut = 2010
            f.write("IF ( ( ( A-"+str(fut)+" & F-"+str(fut)+" & ! O-"+str(fut)+" ) | ( A-"+str(other)+" & F-"+str(other)+" & ! O-"+str(other)+" ) ) & O-"+str(i)+" ) {\n")
        else:
            f.write("IF ( ( ( A-"+str(past)+" & F-"+str(past)+" & ! O-"+str(past)+" ) | ( A-"+str(fut)+" & F-"+str(fut)+" & ! O-"+str(fut)+" ) ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")


    switches = [2000, 2016]
    lower = [2009, 2001]
    higher = [2010, 2015]
    for s in range(len(switches)):
        f.write("IF ( ( O-"+str(lower[s])+" & A-"+str(switches[s])+" ) | ( O-"+str(switches[s])+" & A-"+str(lower[s])+" ) ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( ( O-"+str(higher[s])+" & A-"+str(switches[s])+" ) | ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) ) {\n")
        f.write("S-"+str(switches[s])+" = 1\n")
        f.write("}\n")

    #write lights logic
    light = [2000,2001,2006,2008,2009,2010,2015,2016,2017,2020,2022]
    for l in light:
        f.write("IF ( O-"+str(l)+" ) {\n")
        f.write("L-"+str(l)+" = 11\n")
        f.write("}\n")
        f.write("ELSE {\n")
        f.write("L-"+str(l)+" = 00\n")
        f.write("}\n")


with open("track_controller/PLCs/RedLineMiddle_Blue.txt", "w") as f:
    for i in range(2024, 2046):
        past = i-1
        fut = i+1
        if(i == 2027):
            switch_if(f, past, fut, 2076)
        elif(i == 2033):
            switch_if(f, past, fut, 2072)
        elif(i == 2038):
            switch_if(f, past, fut, 2071)
        elif(i == 2044):
            switch_if(f, past, fut, 2067)
        else:
            f.write("IF ( ( ( A-"+str(past)+" & F-"+str(past)+" & ! O-"+str(past)+" ) | ( A-"+str(fut)+" & F-"+str(fut)+" & ! O-"+str(fut)+" ) ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")

    for i in range(2067, 2077):
        past = i-1
        fut = i+1
        if(i == 2076):
            fut = 2027
        elif(i == 2072):
            past = 2033
        elif(i == 2071):
            fut = 2038
        elif(i == 2067):
            past = 2044
        f.write("IF ( ( ( A-"+str(past)+" & F-"+str(past)+" & ! O-"+str(past)+" ) | ( A-"+str(fut)+" & F-"+str(fut)+" & ! O-"+str(fut)+" ) ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")


    switches = [2027, 2033, 2038, 2044]
    lower = [2028, 2032, 2039, 2043]
    higher = [2076, 2072, 2071, 2067]
    for s in range(len(switches)):
        f.write("IF ( ( O-"+str(lower[s])+" & A-"+str(switches[s])+" ) | ( O-"+str(switches[s])+" & A-"+str(lower[s])+" ) ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( ( O-"+str(higher[s])+" & A-"+str(switches[s])+" ) | ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) ) {\n")
        f.write("S-"+str(switches[s])+" = 1\n")
        f.write("}\n")

    #write lights logic
    light = [2024,2025,2027,2028,2032,2033,2038,2039,2043,2044,2067,2071,2072,2076]
    for l in light:
        f.write("IF ( O-"+str(l)+" ) {\n")
        f.write("L-"+str(l)+" = 11\n")
        f.write("}\n")
        f.write("ELSE {\n")
        f.write("L-"+str(l)+" = 00\n")
        f.write("}\n")

with open("track_controller/PLCs/RedLineBottom_Yellow.txt", "w") as f:
    for i in range(2046, 2067):
        if(i == 2052):
            other = 2066
            f.write("IF ( ( ( A-"+str(i-1)+" & F-"+str(i-1)+" & ! O-"+str(i-1)+" ) | ( A-"+str(i+1)+" & F-"+str(i+1)+" & ! O-"+str(i+1)+" ) | ( A-"+str(other)+" & F-"+str(other)+" & ! O-"+str(other)+" ) ) & O-"+str(i)+" ) {\n")
        elif(i == 2066):
            other = 2052
            f.write("IF ( ( ( A-"+str(i-1)+" & F-"+str(i-1)+" & ! O-"+str(i-1)+" ) | ( A-"+str(other)+" & F-"+str(other)+" & ! O-"+str(other)+" ) ) & O-"+str(i)+" ) {\n")
        else:
            f.write("IF ( ( ( A-"+str(i-1)+" & F-"+str(i-1)+" & ! O-"+str(i-1)+" ) | ( A-"+str(i+1)+" & F-"+str(i+1)+" & ! O-"+str(i+1)+" ) ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")


    switches = [2052]
    lower = [2053]
    higher = [2066]
    for s in range(len(switches)):
        f.write("IF ( ( O-"+str(lower[s])+" & A-"+str(switches[s])+" ) | ( O-"+str(switches[s])+" & A-"+str(lower[s])+" ) ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( ( O-"+str(higher[s])+" & A-"+str(switches[s])+" ) | ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) ) {\n")
        f.write("S-"+str(switches[s])+" = 1\n")
        f.write("}\n")

    #Railway 47
    f.write("R-2047 = 0\n")
    f.write("IF ( O-2047 | O-2049 | O-2048 | O-2047 | O-2046 | O-2045 ) {\n")
    f.write("R-2047 = 1\n")
    f.write("}\n")

    #write lights logic
    light = [2046,2047,2049,2052,2053,2059,2061,2066]
    for l in light:
        f.write("IF ( O-"+str(l)+" ) {\n")
        f.write("L-"+str(l)+" = 11\n")
        f.write("}\n")
        f.write("ELSE {\n")
        f.write("L-"+str(l)+" = 00\n")
        f.write("}\n")


with open("track_controller/PLCs/GreenLineTop_Red.txt", "w") as f:
    switches = [1013]
    lower = [1001]
    higher = [1012]

    #command speed -- occupancy and authority
    for i in range(1001, 1013):
        past = i-1
        if (i == 1001):
            past  = 1013
        f.write("IF ( ( A-"+str(past)+" & ! O-"+str(past)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")
    for i in range(1013, 1021):
        f.write("IF ( ( ( A-"+str(i-1)+" & ! O-"+str(i-1)+" ) | ( A-"+str(i+1)+" & ! O-"+str(i+1)+" ) ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")

    #command speed -- faults
    #fault on E/D
    f.write("IF (")
    for i in range(1013, 1022):
        f.write(" ! F-"+str(i)+" ")
        if(i != 1021):
            f.write("|")
    f.write(") {\n")
    for i in range(1013, 1021):
        f.write("C-"+str(i)+" = 0\n")
    for i in range(1001, 1007):
        f.write("C-"+str(i)+" = 0\n")
    f.write("}\n")
    #fault on A/B/C
    f.write("IF (")
    for i in range(1001, 1013):
        f.write(" ! F-"+str(i)+" ")
        if(i != 1012):
            f.write("|")
    f.write(") {\n")
    for i in range(1001, 1017):
        f.write("C-"+str(i)+" = 0\n")
    f.write("}\n")
    

    #switches 
    for s in range(len(switches)):        
        f.write("IF ( O-"+str(lower[s])+" & A-"+str(switches[s])+" ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) {\n")
        f.write("S-"+str(switches[s])+" = 1\n")
        f.write("}\n")

    #write lights and rail way crossing logic
    #Railway
    f.write("R-1019 = 0\n")
    f.write("IF ( O-1020 | O-1021 | O-1019 | O-1018 | O-1017 | O-1016 ) {\n")
    f.write("R-1019 = 1\n")
    f.write("}\n")

    #Lights
    stations = [1002, 1009, 1012, 1013, 1016 ,1019] #TODO: Fix Logic Probably
    for l in stations:
        f.write("IF ( O-"+str(l-1)+" & A-"+str(l)+" ) {\n")
        f.write("L-"+str(l-1)+" = 11\n")
        f.write("L-"+str(l+1)+" = 00\n")
        f.write("}\n")
        f.write("IF ( O-"+str(l+1)+" & A-"+str(l)+" ) {\n")
        f.write("L-"+str(l+1)+" = 11\n")
        f.write("L-"+str(l-1)+" = 00\n")
        f.write("}\n")
    sw = [1001, 1012, 1013]


    #Authority
    #for i in range(1001, 1021):
     #   f.write("IF ( ! F-"+str(i)+" ) {\n")
    #    f.write("A-"+str(i)+" = 0\n")
    #    f.write("}\n")

with open("track_controller/PLCs/GreenLineMiddle_Yellow.txt", "w") as f:
    for i in range(1030, 1036):
        f.write("IF ( ( A-"+str(i+1)+" & ! O-"+str(i+1)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")
    for i in range(1105, 1151):
        fut = i+1
        if(i == 1150):
            fut = 1029
        f.write("IF ( ( A-"+str(fut)+" & ! O-"+str(fut)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")
    for i in range(1021, 1030):
        f.write("IF ( ( ( A-"+str(i-1)+" & ! O-"+str(i-1)+" ) | ( A-"+str(i+1)+" & ! O-"+str(i+1)+" ) ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")
    switches = [1029]
    lower = [1030]
    higher = [1150]
    for s in range(len(switches)):
        f.write("IF ( O-"+str(switches[s])+" & A-"+str(lower[s])+" ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( O-"+str(higher[s])+" & A-"+str(switches[s])+" ) {\n")
        f.write("S-"+str(switches[s])+" = 1\n")
        f.write("}\n")

    #write lights and rail way crossing logic
    #Lights
    stations = [1022, 1031, 1105 ,1114, 1123, 1132, 1141]
    for l in stations:
        f.write("IF ( O-"+str(l-1)+" & A-"+str(l)+" ) {\n")
        f.write("L-"+str(l-1)+" = 11\n")
        f.write("L-"+str(l+1)+" = 00\n")
        f.write("}\n")
        f.write("IF ( O-"+str(l+1)+" & A-"+str(l)+" ) {\n")
        f.write("L-"+str(l+1)+" = 11\n")
        f.write("L-"+str(l-1)+" = 00\n")
        f.write("}\n")

    #Authority
    #for i in range(1021, 1036):
    ##    f.write("IF ( ! F-"+str(i)+" ) {\n")
    #    f.write("A-"+str(i)+" = 0\n")
    #    f.write("}\n")
    #for i in range(1105, 1151):
    #    f.write("IF ( ! F-"+str(i)+" ) {\n")
    #    f.write("A-"+str(i)+" = 0\n")
    #    f.write("}\n")

with open("track_controller/PLCs/GreenLineBottom_Blue.txt", "w") as f:
    switches = [1057, 1063, 1077, 1085]
    lower = [1000, 1000, 1076, 1086]
    higher = [1058, 1062, 1101, 1100]

    f.write("IF ( ( A-"+str(1063)+" & ! O-"+str(1063)+" ) & O-"+str(1000)+" ) {\n")
    f.write("C-"+str(1000)+" = D-"+str(1000)+"\n")
    f.write("}\n")
    f.write("ELSE\n")
    f.write("{\n")
    f.write("C-"+str(1000)+" = 0\n")
    f.write("}\n")

    for i in range(1036, 1077):
        f.write("IF ( ( A-"+str(i+1)+" & ! O-"+str(i+1)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")
    for i in range(1086, 1105):
        fut = i+1
        if(i==1100):
            fut = 1085
        f.write("IF ( ( A-"+str(fut)+" & ! O-"+str(fut)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")
    for i in range(1077, 1086):
        past = i-1
        if(i == 1077):
            past = 1101
        f.write("IF ( ( ( A-"+str(past)+" & ! O-"+str(past)+" ) | ( A-"+str(i+1)+" & ! O-"+str(i+1)+" ) ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")
    #switches
    for s in range(len(switches)):
        if(s == 2):
            f.write("IF ( O-"+str(lower[s])+" & A-"+str(switches[s])+" ) {\n")
            f.write("S-"+str(switches[s])+" = 0\n")
            f.write("}\n")
            f.write("IF ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) {\n")
            f.write("S-"+str(switches[s])+" = 1\n")
            f.write("}\n")
        elif(s==3):
            f.write("IF ( O-"+str(switches[s])+" & A-"+str(lower[s])+" ) {\n")
            f.write("S-"+str(switches[s])+" = 0\n")
            f.write("}\n")
            f.write("IF ( O-"+str(higher[s])+" & A-"+str(switches[s])+" ) {\n")
            f.write("S-"+str(switches[s])+" = 1\n")
            f.write("}\n")
        elif(s==0):
            f.write("IF ( O-"+str(switches[s])+" & A-"+str(lower[s])+" ) {\n")
            f.write("S-"+str(switches[s])+" = 0\n")
            f.write("}\n")
            f.write("IF ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) {\n")
            f.write("S-"+str(switches[s])+" = 1\n")
            f.write("}\n")
        elif(s==1):
            f.write("IF ( O-"+str(lower[s])+" & A-"+str(switches[s])+" ) {\n")
            f.write("S-"+str(switches[s])+" = 0\n")
            f.write("}\n")
            f.write("IF ( O-"+str(higher[s])+" & A-"+str(switches[s])+" ) {\n")
            f.write("S-"+str(switches[s])+" = 1\n")
            f.write("}\n")
        else:
            f.write("IF ( ( O-"+str(lower[s])+" & A-"+str(switches[s])+" ) | ( O-"+str(switches[s])+" & A-"+str(lower[s])+" ) ) {\n")
            f.write("S-"+str(switches[s])+" = 0\n")
            f.write("}\n")
            f.write("IF ( ( O-"+str(higher[s])+" & A-"+str(switches[s])+" ) | ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) ) {\n")
            f.write("S-"+str(switches[s])+" = 1\n")
            f.write("}\n")
    #write lights and rail way crossing logic
    #Lights
    stations = [1039, 1048, 1057, 1065, 1073, 1077, 1088, 1096]
    for l in stations:
        f.write("IF ( O-"+str(l-1)+" & A-"+str(l)+" ) {\n")
        f.write("L-"+str(l-1)+" = 11\n")
        f.write("L-"+str(l+1)+" = 00\n")
        f.write("}\n")
        f.write("IF ( O-"+str(l+1)+" & A-"+str(l)+" ) {\n")
        f.write("L-"+str(l+1)+" = 11\n")
        f.write("L-"+str(l-1)+" = 00\n")
        f.write("}\n")

    #Authority
    #for i in range(1036, 1104):
    #    f.write("IF ( ! F-"+str(i)+" ) {\n")
    #    f.write("A-"+str(i)+" = 0\n")
    #    f.write("}\n")