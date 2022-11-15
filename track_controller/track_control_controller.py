from track_controller.track_controller import WaysideController
import threading

class track_control_controller():
    def __init__(self):
        self.track_controller_list = [WaysideController(), WaysideController(), WaysideController(), WaysideController(), WaysideController(), WaysideController()] 

        #toy data
        self.track_controller_list[0].set_authority([(1,True), (2, False), (3, False)])
        self.track_controller_list[0].set_switch_positions([(1,True), (2, True), (3, False)])
        self.track_controller_list[0].set_occupancy([(1,True), (2, True), (3, False)])
        self.track_controller_list[0].set_railway_crossings([(1,True), (2, True), (3, False)])
        self.track_controller_list[0].set_light_colors([(1,True,True), (5, True,True), (3, False,True)])
        self.track_controller_list[0].set_statuses([(1,True), (2, True), (3, True)])
        self.track_controller_list[0].set_suggested_speed([(1,0b00011010), (2, 0b00100111), (3, 0b00010101)])
        self.track_controller_list[0].set_commanded_speed([(1,0b000000000), (2, 0b00000000), (3, 0b00000000)])
        self.track_controller_list[0].set_speed_limit([(1,0b000000000), (2, 0b00000000), (3, 0b00000000)])
        self.track_controller_list[0].set_PLC("track_controller/testPLCfile.txt")

        self.track_controller_list[1].set_authority([(1,True), (2, False), (3, False), (4, False), (5, False)])
        self.track_controller_list[1].set_switch_positions([(1,True)])
        self.track_controller_list[1].set_occupancy([(1,True), (2, False), (3, False), (4, False), (5, False)])
        self.track_controller_list[1].set_railway_crossings([(1,True)])
        self.track_controller_list[1].set_light_colors([(1,True,True)])
        self.track_controller_list[1].set_statuses([(1,True), (2, False), (3, False), (4, False), (5, False)])
        self.track_controller_list[1].set_suggested_speed([(1,0b00011010), (2, 0b00100111), (3, 0b00010101),(4, 0b00010101), (5, 0b00010101)])
        self.track_controller_list[1].set_commanded_speed([(1,0b00000000), (2, 0b00000000), (3, 0b00000000), (4, 0b00010101), (5, 0b00010101)])
        self.track_controller_list[1].set_speed_limit([(1,0b000100000), (2, 0b00000100), (3, 0b00100000),(4, 0b00000101), (5, 0b100000001)])
        self.track_controller_list[1].set_PLC("track_controller/testPLCfile.txt")

        #temp redline
        auth = []
        occ = [] 
        stat=[]
        sug = [] 
        com = []
        lim = []
        for i in range(1023, 1047):
            auth.append((i, False))
            occ.append((i, False))
            stat.append((i, True))
            if(i !=1023 and i!= 1046):
                sug.append((i, 0b00100000))
                com.append((i, 0b00000000))
                lim.append((i, 0b00100010))
        for i in range(1067, 1077):
            auth.append((i, False))
            occ.append((i, False))
            stat.append((i, True))
            sug.append((i, 0b00100000))
            com.append((i, 0b00000000))
            lim.append((i, 0b00100010))
        self.track_controller_list[2].set_authority(auth)
        self.track_controller_list[2].set_switch_positions([(1027,False), (1032,False), (1038,False), (1043,False)])
        self.track_controller_list[2].set_occupancy(occ)
        self.track_controller_list[2].set_railway_crossings([(1,True)])
        self.track_controller_list[2].set_light_colors([(1,True,True)])
        self.track_controller_list[2].set_statuses(stat)
        self.track_controller_list[2].set_suggested_speed(sug)
        self.track_controller_list[2].set_commanded_speed(com)
        self.track_controller_list[2].set_speed_limit(lim)
        self.track_controller_list[2].set_PLC("track_controller/RedLine_Middle_blue_PLC.txt")

        #temp green line
        auth = []
        occ = [] 
        stat=[]
        sug = [] 
        com = []
        lim = []
        for i in range(1001, 1021):
            auth.append((i, False))
            occ.append((i, False))
            stat.append((i, True))
            if(i!= 1021):
                sug.append((i, 0b00100000))
                com.append((i, 0b00000000))
                lim.append((i, 0b00100010))
        self.track_controller_list[3].set_authority(auth)
        self.track_controller_list[3].set_switch_positions([(1013,False)])
        self.track_controller_list[3].set_occupancy(occ)
        self.track_controller_list[3].set_railway_crossings([(1001,False)])
        self.track_controller_list[3].set_light_colors([(1001,True,True), (1003,True,True), (1008,True,True), (1010,True,True), (1015,True,True), (1017,True,True), (1018,True,True), (1020,True,True)])
        self.track_controller_list[3].set_statuses(stat)
        self.track_controller_list[3].set_suggested_speed(sug)
        self.track_controller_list[3].set_commanded_speed(com)
        self.track_controller_list[3].set_speed_limit(lim)
        self.track_controller_list[3].set_PLC("track_controller/GreenLineTop_Red.txt")


        #temp green line
        auth = []
        occ = [] 
        stat=[]
        sug = [] 
        com = []
        lim = []
        for i in range(1020, 1037):
            auth.append((i, False))
            occ.append((i, False))
            stat.append((i, True))
            if(i!= 1020 or i!= 1036):
                sug.append((i, 0b00100000))
                com.append((i, 0b00000000))
                lim.append((i, 0b00100010))
        for i in range(1104, 1150):
            auth.append((i, False))
            occ.append((i, False))
            stat.append((i, True))
            if(i!= 1104):
                sug.append((i, 0b00100000))
                com.append((i, 0b00000000))
                lim.append((i, 0b00100010))
        self.track_controller_list[4].set_authority(auth)
        self.track_controller_list[4].set_switch_positions([(1029,False)])
        self.track_controller_list[4].set_occupancy(occ)
        self.track_controller_list[4].set_railway_crossings([])
        self.track_controller_list[4].set_light_colors([(1021,True,True), (1023,True,True), (1030,True,True), (1032,True,True), (1104,True,True), (1106,True,True), (1113,True,True), (1115,True,True), (1122,True,True), (1124,True,True), (1131,True,True), (1133,True,True), (1140,True,True), (1142,True,True)])
        self.track_controller_list[4].set_statuses(stat)
        self.track_controller_list[4].set_suggested_speed(sug)
        self.track_controller_list[4].set_commanded_speed(com)
        self.track_controller_list[4].set_speed_limit(lim)
        self.track_controller_list[4].set_PLC("track_controller/GreenLineTop_Red.txt")

        #temp green line
        auth = []
        occ = [] 
        stat=[]
        sug = [] 
        com = []
        lim = []
        for i in range(1020, 1037):
            auth.append((i, False))
            occ.append((i, False))
            stat.append((i, True))
            if(i!= 1020 or i!= 1036):
                sug.append((i, 0b00100000))
                com.append((i, 0b00000000))
                lim.append((i, 0b00100010))
        for i in range(1104, 1151):
            auth.append((i, False))
            occ.append((i, False))
            stat.append((i, True))
            if(i!= 1104):
                sug.append((i, 0b00100000))
                com.append((i, 0b00000000))
                lim.append((i, 0b00100010))
        self.track_controller_list[4].set_authority(auth)
        self.track_controller_list[4].set_switch_positions([(1029,False)])
        self.track_controller_list[4].set_occupancy(occ)
        self.track_controller_list[4].set_railway_crossings([])
        self.track_controller_list[4].set_light_colors([(1021,True,True), (1023,True,True), (1030,True,True), (1032,True,True), (1104,True,True), (1106,True,True), (1113,True,True), (1115,True,True), (1122,True,True), (1124,True,True), (1131,True,True), (1133,True,True), (1140,True,True), (1142,True,True)])
        self.track_controller_list[4].set_statuses(stat)
        self.track_controller_list[4].set_suggested_speed(sug)
        self.track_controller_list[4].set_commanded_speed(com)
        self.track_controller_list[4].set_speed_limit(lim)
        self.track_controller_list[4].set_PLC("track_controller/GreenLineMiddle_Yellow.txt")

        #temp green line Bottom Blue
        auth = [(0, False)]
        occ = [(0, False)] 
        stat=[]
        sug = [] 
        com = []
        lim = []
        for i in range(35, 1105):
            auth.append((i, False))
            occ.append((i, False))
            stat.append((i, True))
            if(i!= 1035 or i!= 1105):
                sug.append((i, 0b00100000))
                com.append((i, 0b00000000))
                lim.append((i, 0b00100010))
        self.track_controller_list[5].set_authority(auth)
        self.track_controller_list[5].set_switch_positions([(1057,False), (1063,False), (1077,False), (1085,False)])
        self.track_controller_list[5].set_occupancy(occ)
        self.track_controller_list[5].set_railway_crossings([])
        self.track_controller_list[5].set_light_colors([(1038,True,True), (1040,True,True), (1047,True,True), (1049,True,True), (1056,True,True), (1058,True,True), (1064,True,True), (1066,True,True), (1072,True,True), (1074,True,True), (1076,True,True), (1078,True,True), (1087,True,True), (1089,True,True), (1095,True,True), (1097,True,True)])
        self.track_controller_list[5].set_statuses(stat)
        self.track_controller_list[5].set_suggested_speed(sug)
        self.track_controller_list[5].set_commanded_speed(com)
        self.track_controller_list[5].set_speed_limit(lim)
        self.track_controller_list[5].set_PLC("track_controller/GreenLineMiddle_Yellow.txt")

        self.track_controller_list[0].set_wayside_id("RedLine A")
        self.track_controller_list[1].set_wayside_id("RedLine B")
        self.track_controller_list[2].set_wayside_id("RedLine Blue")
        self.track_controller_list[3].set_wayside_id("GreenLine Red")
        self.track_controller_list[4].set_wayside_id("GreenLine Yellow")
        self.track_controller_list[5].set_wayside_id("GreenLine Blue")

    def get_track_control_instance(self, wid):
        for wayside in self.track_controller_list:
            if str(wayside.get_wayside_id()) == wid:
                return wayside

    def get_names_of_controllers(self):
        names= []
        for track in self.track_controller_list:
            names.append(track.get_wayside_id())
        return names

    def add_new_wayside_controller(self, wayside):
        self.track_controller_list.append(wayside)

    def Run_All_Track_Controllers_PLC(self):
        t = list()
        for wayside in self.track_controller_list:
            if(not(wayside.get_maintenance_mode())):
                #wayside.ParsePLC()
                x =threading.Thread(target=wayside.ParsePLC)
                t.append(x)
                x.start()
        for index, thread in enumerate(t):
            thread.join()
    def get_all_track_controllers(self):
        return self.track_controller_list
     