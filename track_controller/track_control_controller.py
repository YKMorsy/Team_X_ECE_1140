from track_controller.track_controller import WaysideController
import threading

class track_control_controller():
    def __init__(self):
        self.track_controller_list = [WaysideController(), WaysideController(), WaysideController(), WaysideController(), WaysideController(), WaysideController()] 

        #red top red 
        auth = {}
        occ = {} 
        stat={}
        sug = {} 
        com = {}
        lim = {}
        for i in range(2000, 2025):
            auth.update({i: False})
            occ.update({i: False})
            stat.update({i: True})
            if(i !=2024):
                sug.update({i: 0b00100000})
                com.update({i: 0b00000000})
                lim.update({i: 0b00100100})
        self.track_controller_list[0].set_authority(auth)
        self.track_controller_list[0].set_switch_positions({2009:False, 2016:False})
        self.track_controller_list[0].set_occupancy(occ)
        self.track_controller_list[0].set_railway_crossings({})
        self.track_controller_list[0].set_light_colors({1:[True,True]})
        self.track_controller_list[0].set_statuses(stat)
        self.track_controller_list[0].set_suggested_speed(sug)
        self.track_controller_list[0].set_commanded_speed(com)
        self.track_controller_list[0].set_speed_limit(lim)
        self.track_controller_list[0].set_PLC("track_controller/blank.txt")

        #Bottom Yellow
        auth = {}
        occ = {} 
        stat={}
        sug = {} 
        com = {}
        lim = {}
        for i in range(2045, 2067):
            auth.update({i: False})
            occ.update({i: False})
            stat.update({i: True})
            if(i !=2045):
                sug.update({i: 0b00100000})
                com.update({i: 0b00000000})
                lim.update({i: 0b00100100})
        self.track_controller_list[2].set_authority(auth)
        self.track_controller_list[2].set_switch_positions({2052:False})
        self.track_controller_list[2].set_occupancy(occ)
        self.track_controller_list[2].set_railway_crossings({2001: False})
        self.track_controller_list[2].set_light_colors({1:[True,True]})
        self.track_controller_list[2].set_statuses(stat)
        self.track_controller_list[2].set_suggested_speed(sug)
        self.track_controller_list[2].set_commanded_speed(com)
        self.track_controller_list[2].set_speed_limit(lim)
        self.track_controller_list[2].set_PLC("track_controller/blank.txt")

        #temp redline middle blue
        auth = {}
        occ = {} 
        stat={}
        sug = {} 
        com = {}
        lim = {}
        for i in range(2023, 2047):
            auth.update({i: False})
            occ.update({i: False})
            stat.update({i: True})
            if(i !=2023 and i!= 2046):
                sug.update({i: 0b00100000})
                com.update({i: 0b00000000})
                lim.update({i: 0b00100100})
        for i in range(2067, 2077):
            auth.update({i: False})
            occ.update({i: False})
            stat.update({i: True})
            sug.update({i: 0b00100000})
            com.update({i: 0b00000000})
            lim.update({i: 0b00100100})
        self.track_controller_list[1].set_authority(auth)
        self.track_controller_list[1].set_switch_positions({2027:False, 2032:False, 2038:False, 2043:False})
        self.track_controller_list[1].set_occupancy(occ)
        self.track_controller_list[1].set_railway_crossings({1:True})
        self.track_controller_list[1].set_light_colors({1:[True,True]})
        self.track_controller_list[1].set_statuses(stat)
        self.track_controller_list[1].set_suggested_speed(sug)
        self.track_controller_list[1].set_commanded_speed(com)
        self.track_controller_list[1].set_speed_limit(lim)
        self.track_controller_list[1].set_PLC("track_controller/blank.txt")

        #temp green line
        auth = {}
        occ = {} 
        stat={}
        sug = {} 
        com = {}
        lim = {}
        for i in range(1001, 1022):
            auth.update({i: False})
            occ.update({i:False})
            stat.update({i:True})
            if(i!= 1021):
                sug.update({i: 0b00100000})
                com.update({i: 0b00000000})
                lim.update({i: 0b00100100})
        self.track_controller_list[3].set_authority(auth)
        self.track_controller_list[3].set_switch_positions({1013:False})
        self.track_controller_list[3].set_occupancy(occ)
        self.track_controller_list[3].set_railway_crossings({1001:False})
        self.track_controller_list[3].set_light_colors({1001:[True,True], 1003:[True,True], 1008:[True,True], 1010:[True,True], 1015:[True,True], 1017:[True,True], 1018:[True,True], 1020:[True,True]})
        self.track_controller_list[3].set_statuses(stat)
        self.track_controller_list[3].set_suggested_speed(sug)
        self.track_controller_list[3].set_commanded_speed(com)
        self.track_controller_list[3].set_speed_limit(lim)
        self.track_controller_list[3].set_PLC("track_controller/GreenLineTop_Red.txt")

        #temp green line
        auth = {}
        occ = {} 
        stat={}
        sug = {} 
        com = {}
        lim = {}
        for i in range(1020, 1037):
            auth.update({i:False})
            occ.update({i:False})
            stat.update({i:True})
            if(i!= 1020 and i!= 1036):
                sug.update({i: 0b00100000})
                com.update({i: 0b00000000})
                lim.update({i: 0b00100100})
        for i in range(1104, 1151):
            auth.update({i:False})
            occ.update({i:False})
            stat.update({i: True})
            if(i!= 1104):
                sug.update({i: 0b00100000})
                com.update({i: 0b00000000})
                lim.update({i: 0b00100100})
        self.track_controller_list[4].set_authority(auth)
        self.track_controller_list[4].set_switch_positions({1029:False})
        self.track_controller_list[4].set_occupancy(occ)
        self.track_controller_list[4].set_railway_crossings({})
        self.track_controller_list[4].set_light_colors({1021:[True,True], 1023:[True,True], 1030:[True,True], 1032:[True,True], 1104:[True,True], 1106:[True,True], 1113:[True,True], 1115:[True,True], 1122:[True,True], 1124:[True,True], 1131:[True,True], 1133:[True,True], 1140:[True,True], 1142:[True,True]})
        self.track_controller_list[4].set_statuses(stat)
        self.track_controller_list[4].set_suggested_speed(sug)
        self.track_controller_list[4].set_commanded_speed(com)
        self.track_controller_list[4].set_speed_limit(lim)
        self.track_controller_list[4].set_PLC("track_controller/GreenLineMiddle_Yellow.txt")

        #temp green line Bottom Blue
        auth = {1000:False}
        occ = {1000:False} 
        stat={1000:False}
        sug = {} 
        com = {}
        lim = {}
        for i in range(1035, 1106):
            auth.update({i:False})
            occ.update({i:False})
            stat.update({i:True})
            if(i!= 1035 and i!= 1105):
                sug.update({i: 0b00100000})
                com.update({i: 0b00000000})
                lim.update({i: 0b00100100})
        self.track_controller_list[5].set_authority(auth)
        self.track_controller_list[5].set_switch_positions({1057:False,  1063:False, 1077:False,1085:False})
        self.track_controller_list[5].set_occupancy(occ)
        self.track_controller_list[5].set_railway_crossings({})
        self.track_controller_list[5].set_light_colors({1038:[True,True], 1040:[True,True], 1047:[True,True], 1049:[True,True], 1056:[True,True], 1058:[True,True], 1064:[True,True], 1066:[True,True],1072:[True,True],1074:[True,True], 1076:[True,True], 1078:[True,True], 1087:[True,True], 1089:[True,True], 1095:[True,True], 1097:[True,True]})
        self.track_controller_list[5].set_statuses(stat)
        self.track_controller_list[5].set_suggested_speed(sug)
        self.track_controller_list[5].set_commanded_speed(com)
        self.track_controller_list[5].set_speed_limit(lim)
        self.track_controller_list[5].set_PLC("track_controller/GreenLineBottom_Blue.txt")

        self.track_controller_list[0].set_wayside_id("RedLine Top Red")
        self.track_controller_list[1].set_wayside_id("RedLine Middle Blue")
        self.track_controller_list[2].set_wayside_id("RedLine Bottom Yellow")
        self.track_controller_list[3].set_wayside_id("GreenLine Top Red")
        self.track_controller_list[4].set_wayside_id("GreenLine Middle Yellow")
        self.track_controller_list[5].set_wayside_id("GreenLine Bottom Blue")

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
     