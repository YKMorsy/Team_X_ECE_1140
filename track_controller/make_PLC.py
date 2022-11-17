

with open("track_controller/RedLineBottom_yellow.txt", "w") as f:
    for i in range(2046, 2067):
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
        f.write("S-"+str(switches[s])+" = 1\n")
        f.write("IF ( O-"+str(switches[s])+" & A-"+str(lower[s])+" & ! A-"+str(higher[s])+" ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( O-"+str(switches[s])+" & ! A-"+str(lower[s])+" & A-"+str(higher[s])+" ) {\n")
        f.write("S-"+str(switches[s])+" = 1\n")
        f.write("}\n")
        f.write("IF ( O-"+str(lower[s])+" & A-"+str(switches[s])+" ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( O-"+str(higher[s])+" & A-"+str(switches[s])+" ) {\n")
        f.write("S-"+str(switches[s])+" = 1\n")
        f.write("}\n")
    #write lights and rail way crossing logic

with open("track_controller/GreenLineTop_Red.txt", "w") as f:
    for i in range(1001, 1013):
        past = i-1
        if(i==1001):
            past = 1013
        f.write("IF ( ( A-"+str(past)+" & F-"+str(past)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("C-"+str(past)+" = D-"+str(past)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")
    for i in range(1013, 1021):
        f.write("IF ( ( A-"+str(i+1)+" & ! O-"+str(i+1)+" ) & O-"+str(i)+" ) {\n")
        if(i != 1020):
            f.write("C-"+str(i+1)+" = D-"+str(i+1)+"\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        if(i != 1020):
            f.write("C-"+str(i+1)+" = 0\n")
        f.write("}\n")
        f.write("IF ( ( A-"+str(i-1)+" & ! O-"+str(i-1)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i-1)+" = D-"+str(i-1)+"\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("C-"+str(i-1)+" = 0\n")
        f.write("}\n")
    switches = [1013]
    lower = [1001]
    higher = [1012]
    for s in range(len(switches)):
        #f.write("S-"+str(switches[s])+" = 1\n")
        f.write("IF ( O-"+str(lower[s])+" ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( O-"+str(higher[s])+" | ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) ) {\n")
        f.write("S-"+str(switches[s])+" = 1\n")
        f.write("}\n")

    #write lights and rail way crossing logic
    #Railway
    f.write("R-1 = 0\n")
    f.write("IF ( ( O-1018 & A-1019 ) | ( O-1017 & A-1018 ) ) {\n")
    f.write("R-1001 = 1\n")
    f.write("}\n")
    f.write("IF ( O-1020 & A-1019 ) {\n")
    f.write("R-1001 = 1\n")
    f.write("}\n")

    #Lights
    stations = [1002, 1009, 1016 ,1019]
    for l in stations:
        f.write("IF ( O-"+str(l-1)+" & A-"+str(l)+" ) {\n")
        f.write("L-"+str(l-1)+" = 11\n")
        f.write("L-"+str(l+1)+" = 00\n")
        f.write("}\n")
        f.write("IF ( O-"+str(l+1)+" & A-"+str(l)+" ) {\n")
        f.write("L-"+str(l+1)+" = 11\n")
        f.write("L-"+str(l-1)+" = 00\n")
        f.write("}\n")
    for i in range(1001, 1021):
        f.write("IF ( ! F-"+str(l)+" ) {\n")
        f.write("A-"+str(l+1)+" = 0\n")
        f.write("}\n")

    #Authority
    #for i in range(1001, 1021):
     #   f.write("IF ( ! F-"+str(i)+" ) {\n")
    #    f.write("A-"+str(i)+" = 0\n")
    #    f.write("}\n")

with open("track_controller/GreenLineMiddle_Yellow.txt", "w") as f:
    for i in range(1029, 1036):
        f.write("IF ( ( A-"+str(i+1)+" & F-"+str(i+1)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        if(i != 1035):
            f.write("C-"+str(i)+" = D-"+str(i+1)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        if(i != 1035):
            f.write("C-"+str(i+1)+" = 0\n")
        f.write("}\n")
    for i in range(1105, 1151):
        fut = i+1
        if(i == 1150):
            fut=1029
        f.write("IF ( ( A-"+str(fut)+" & F-"+str(fut)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("C-"+str(fut)+" = D-"+str(fut)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("}\n")
    for i in range(1021, 1029):
        f.write("IF ( ( A-"+str(i-1)+" & F-"+str(i-1)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        if(i!=1021):
            f.write("C-"+str(i-1)+" = D-"+str(i-1)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        if(i!=1021):
            f.write("C-"+str(i-1)+" = 0\n")
        f.write("}\n")
        f.write("IF ( ( A-"+str(i+1)+" & F-"+str(i+1)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("C-"+str(i+1)+" = D-"+str(i+1)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("C-"+str(i+1)+" = 0\n")
        f.write("}\n")
    switches = [1029]
    lower = [1030]
    higher = [1150]
    for s in range(len(switches)):
        #f.write("S-"+str(switches[s])+" = 1\n")
        f.write("IF ( O-"+str(lower[s])+" | ( O-"+str(switches[s])+" & A-"+str(lower[s])+" ) ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( O-"+str(higher[s])+" | ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) ) {\n")
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

with open("track_controller/GreenLineBottom_Blue.txt", "w") as f:
    switches = [1057, 1063, 1077, 1085]
    lower = [1000, 1000, 1076, 1086]
    higher = [1058, 1062, 1101, 1100]

    for i in range(1036, 1077):
        f.write("IF ( ( A-"+str(i+1)+" & F-"+str(i+1)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("C-"+str(i+1)+" = D-"+str(i+1)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("C-"+str(i+1)+" = 0\n")
        f.write("}\n")
    for i in range(1086, 1105):
        fut = i+1
        if(i==1100):
            fut = 1085
        f.write("IF ( ( A-"+str(fut)+" & F-"+str(fut)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        if(i!=1104):
            f.write("C-"+str(fut)+" = D-"+str(fut)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        if(i!=1104):
            f.write("C-"+str(fut)+" = 0\n")
        f.write("}\n")
    for i in range(1077, 1086):
        past = i-1
        if(i == 1077):
            past = 1101
        f.write("IF ( ( A-"+str(past)+" & F-"+str(past)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("C-"+str(past)+" = D-"+str(past)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("C-"+str(past)+" = 0\n")
        f.write("}\n")
        f.write("IF ( ( A-"+str(i+1)+" & F-"+str(i+1)+" ) & O-"+str(i)+" ) {\n")
        f.write("C-"+str(i)+" = D-"+str(i)+"\n")
        f.write("C-"+str(i+1)+" = D-"+str(i+1)+"\n")
        f.write("}\n")
        f.write("ELSE\n")
        f.write("{\n")
        f.write("C-"+str(i)+" = 0\n")
        f.write("C-"+str(i+1)+" = 0\n")
        f.write("}\n")
    #switches
    for s in range(len(switches)):
        #f.write("S-"+str(switches[s])+" = 1\n")
        f.write("IF ( O-"+str(lower[s])+" | ( O-"+str(switches[s])+" & A-"+str(lower[s])+" ) ) {\n")
        f.write("S-"+str(switches[s])+" = 0\n")
        f.write("}\n")
        f.write("IF ( O-"+str(higher[s])+" | ( O-"+str(switches[s])+" & A-"+str(higher[s])+" ) ) {\n")
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