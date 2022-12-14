import threading
import pandas as pd
from track_controller.track_controller import WaysideController

class track_control_controller():
    def __init__(self):
        self.track_controller_list = [WaysideController(), WaysideController(), WaysideController(), WaysideController(), WaysideController(), WaysideController()]
        
        ex_data = pd.read_excel('track_controller/TrackLayout_TrackControl.xlsx', sheet_name = 'Green Line')
        line = ex_data['Line'].values.tolist()
        section = ex_data['Section'].values.tolist()
        input_sec = ex_data['Input'].values.tolist()
        block_num = ex_data['Block Number'].values.tolist()
        speed_lim = ex_data['Speed Limit'].values.tolist()
        is_light = ex_data['Is Light'].values.tolist()
        is_switch = ex_data['Is Switch'].values.tolist()
        
        auth = {}
        occ = {}
        stat ={}
        sug = {}
        com = {}
        lim = {}
        light = {}
        switch = {}

        auth_1 = {}
        occ_1 = {}
        stat_1 ={}
        sug_1 = {}
        com_1 = {}
        lim_1 = {}
        light_1 = {}
        switch_1 = {}

        auth_2 = {}
        occ_2 = {}
        stat_2 ={}
        sug_2 = {}
        com_2 = {}
        lim_2 = {}
        light_2 = {}
        switch_2 = {}
        
        auth_3 = {}
        occ_3 = {}
        stat_3 ={}
        sug_3 = {}
        com_3 = {}
        lim_3 = {}
        light_3 = {}
        switch_3 = {}
        for i in range(len(block_num)) :
            new_block = int(block_num[i]) + 1000
            if section[i] == 1:
                auth = auth_1
                occ = occ_1
                stat = stat_1
                sug = sug_1
                com = com_1
                lim = lim_1
                light = light_1
                switch = switch_1
            elif section[i] == 2:
                auth = auth_2
                occ = occ_2
                stat = stat_2
                sug = sug_2
                com = com_2
                lim = lim_2
                light = light_2
                switch = switch_2
            elif section[i] == 3:
                auth = auth_3
                occ = occ_3
                stat = stat_3
                sug = sug_3
                com = com_3
                lim = lim_3
                light = light_3
                switch = switch_3
            else:
                auth = {}
                occ = {}
                stat ={}
                sug = {}
                com = {}
                lim = {}
                switch = {}
            auth.update({new_block: False})
            occ.update({new_block: False})
            stat.update({new_block: True})
            sug.update({new_block: 0b00100000})
            com.update({new_block: 0b00000000})
            lim.update({new_block: int(float(speed_lim[i]))})
            if is_light[i] == 1:
                light.update({new_block: [True, True]})
            if is_switch[i] == 1:
                switch.update({new_block: False})
            if input_sec[i] == 1:
                auth = auth_1
                occ = occ_1
                stat = stat_1
                sug = sug_1
                com = com_1
                lim = lim_1
                light = light_1
                switch = switch_1
            elif input_sec[i] == 2:
                auth = auth_2
                occ = occ_2
                stat = stat_2
                sug = sug_2
                com = com_2
                lim = lim_2
                light = light_2
                switch = switch_2
            elif input_sec[i] == 3:
                auth = auth_3
                occ = occ_3
                stat = stat_3
                sug = sug_3
                com = com_3
                lim = lim_3
                light = light_3
                switch = switch_3
            else:
                auth = {}
                occ = {}
                stat ={}
                sug = {}
                com = {}
                lim = {}
                light = {}
                switch = {}
            auth.update({new_block: False})
            occ.update({new_block: False})
            stat.update({new_block: True})

        self.track_controller_list[3].set_authority(auth_1)
        self.track_controller_list[3].set_switch_positions(switch_1)
        self.track_controller_list[3].set_occupancy(occ_1)
        self.track_controller_list[3].set_railway_crossings({1019:False})
        self.track_controller_list[3].set_light_colors(light_1)
        self.track_controller_list[3].set_statuses(stat_1)
        self.track_controller_list[3].set_suggested_speed(sug_1)
        self.track_controller_list[3].set_commanded_speed(com_1)
        self.track_controller_list[3].set_speed_limit(lim_1)
        self.track_controller_list[3].set_line_index(1000)
        self.track_controller_list[3].set_PLC("track_controller/PLCs/GreenLineTop_Red.txt")

        self.track_controller_list[4].set_authority(auth_2)
        self.track_controller_list[4].set_switch_positions(switch_2)
        self.track_controller_list[4].set_occupancy(occ_2)
        self.track_controller_list[4].set_railway_crossings({})
        self.track_controller_list[4].set_light_colors(light_2)
        self.track_controller_list[4].set_statuses(stat_2)
        self.track_controller_list[4].set_suggested_speed(sug_2)
        self.track_controller_list[4].set_commanded_speed(com_2)
        self.track_controller_list[4].set_speed_limit(lim_2)
        self.track_controller_list[4].set_line_index(1000)
        self.track_controller_list[4].set_PLC("track_controller/PLCs/GreenLineMiddle_Yellow.txt")

        self.track_controller_list[5].set_authority(auth_3)
        self.track_controller_list[5].set_switch_positions(switch_3)
        self.track_controller_list[5].set_occupancy(occ_3)
        self.track_controller_list[5].set_railway_crossings({})
        self.track_controller_list[5].set_light_colors(light_3)
        self.track_controller_list[5].set_statuses(stat_3)
        self.track_controller_list[5].set_suggested_speed(sug_3)
        self.track_controller_list[5].set_commanded_speed(com_3)
        self.track_controller_list[5].set_speed_limit(lim_3)
        self.track_controller_list[5].set_line_index(1000)
        self.track_controller_list[5].set_PLC("track_controller/PLCs/GreenLineBottom_Blue.txt")

        ex_data = pd.read_excel('track_controller/TrackLayout_TrackControl.xlsx', sheet_name = 'Red Line')
        line = ex_data['Line'].values.tolist()
        section = ex_data['Section'].values.tolist()
        input_sec = ex_data['Input'].values.tolist()
        block_num = ex_data['Block Number'].values.tolist()
        speed_lim = ex_data['Speed Limit'].values.tolist()
        is_light = ex_data['Is Light'].values.tolist()
        is_switch = ex_data['Is Switch'].values.tolist()

        auth = {}
        occ = {}
        stat ={}
        sug = {}
        com = {}
        lim = {}
        light = {}
        switch = {}

        auth_1 = {}
        occ_1 = {}
        stat_1 ={}
        sug_1 = {}
        com_1 = {}
        lim_1 = {}
        light_1 = {}
        switch_1 = {}

        auth_2 = {}
        occ_2 = {}
        stat_2 ={}
        sug_2 = {}
        com_2 = {}
        lim_2 = {}
        light_2 = {}
        switch_2 = {}
        
        auth_3 = {}
        occ_3 = {}
        stat_3 ={}
        sug_3 = {}
        com_3 = {}
        lim_3 = {}
        light_3 = {}
        switch_3 = {}
        for i in range(len(block_num)) :
            new_block = int(block_num[i]) + 2000
            if section[i] == 1:
                auth = auth_1
                occ = occ_1
                stat = stat_1
                sug = sug_1
                com = com_1
                lim = lim_1
                light = light_1
                switch = switch_1
            elif section[i] == 2:
                auth = auth_2
                occ = occ_2
                stat = stat_2
                sug = sug_2
                com = com_2
                lim = lim_2
                light = light_2
                switch = switch_2
            elif section[i] == 3:
                auth = auth_3
                occ = occ_3
                stat = stat_3
                sug = sug_3
                com = com_3
                lim = lim_3
                light = light_3
                switch = switch_3
            else:
                auth = {}
                occ = {}
                stat ={}
                sug = {}
                com = {}
                lim = {}
                switch = {}
            auth.update({new_block: False})
            occ.update({new_block: False})
            stat.update({new_block: True})
            sug.update({new_block: 0b00100000})
            com.update({new_block: 0b00000000})
            lim.update({new_block: int(float(speed_lim[i]))})
            if is_light[i] == 1:
                light.update({new_block: [True, True]})
            if is_switch[i] == 1:
                switch.update({new_block: False})
            if input_sec[i] == 1:
                auth = auth_1
                occ = occ_1
                stat = stat_1
                sug = sug_1
                com = com_1
                lim = lim_1
                light = light_1
                switch = switch_1
            elif input_sec[i] == 2:
                auth = auth_2
                occ = occ_2
                stat = stat_2
                sug = sug_2
                com = com_2
                lim = lim_2
                light = light_2
                switch = switch_2
            elif input_sec[i] == 3:
                auth = auth_3
                occ = occ_3
                stat = stat_3
                sug = sug_3
                com = com_3
                lim = lim_3
                light = light_3
                switch = switch_3
            else:
                auth = {}
                occ = {}
                stat ={}
                sug = {}
                com = {}
                lim = {}
                light = {}
                switch = {}
            auth.update({new_block: False})
            occ.update({new_block: False})
            stat.update({new_block: True})

        self.track_controller_list[0].set_authority(auth_1)
        self.track_controller_list[0].set_switch_positions(switch_1)
        self.track_controller_list[0].set_occupancy(occ_1)
        self.track_controller_list[0].set_railway_crossings({})
        self.track_controller_list[0].set_light_colors(light_1)
        self.track_controller_list[0].set_statuses(stat_1)
        self.track_controller_list[0].set_suggested_speed(sug_1)
        self.track_controller_list[0].set_commanded_speed(com_1)
        self.track_controller_list[0].set_speed_limit(lim_1)
        self.track_controller_list[0].set_line_index(2000)
        self.track_controller_list[0].set_PLC("track_controller/PLCs/RedLineTop_Red.txt")

        self.track_controller_list[1].set_authority(auth_2)
        self.track_controller_list[1].set_switch_positions(switch_2)
        self.track_controller_list[1].set_occupancy(occ_2)
        self.track_controller_list[1].set_railway_crossings({})
        self.track_controller_list[1].set_light_colors(light_2)
        self.track_controller_list[1].set_statuses(stat_2)
        self.track_controller_list[1].set_suggested_speed(sug_2)
        self.track_controller_list[1].set_commanded_speed(com_2)
        self.track_controller_list[1].set_speed_limit(lim_2)
        self.track_controller_list[1].set_line_index(2000)
        self.track_controller_list[1].set_PLC("track_controller/PLCs/RedLineMiddle_Blue.txt")

        self.track_controller_list[2].set_authority(auth_3)
        self.track_controller_list[2].set_switch_positions(switch_3)
        self.track_controller_list[2].set_occupancy(occ_3)
        self.track_controller_list[2].set_railway_crossings({2047: False})
        self.track_controller_list[2].set_light_colors(light_3)
        self.track_controller_list[2].set_statuses(stat_3)
        self.track_controller_list[2].set_suggested_speed(sug_3)
        self.track_controller_list[2].set_commanded_speed(com_3)
        self.track_controller_list[2].set_speed_limit(lim_3)
        self.track_controller_list[2].set_line_index(2000)
        self.track_controller_list[2].set_PLC("track_controller/PLCs/RedLineBottom_Yellow.txt")

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

    def run_all_track_controllers_plc(self):
        t = list()
        for wayside in self.track_controller_list:
            if(not(wayside.get_maintenance_mode())):
                wayside.parse_plc()
                # x =threading.Thread(target=wayside.parse_plc)
                # t.append(x)
                # x.start()
        # for index, thread in enumerate(t):
        #     thread.join()
    def get_all_track_controllers(self):
        return self.track_controller_list
     