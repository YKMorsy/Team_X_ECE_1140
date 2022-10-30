import pandas as pd

class CTC:
    def __init__(self):
        self.__track_dictionary  =	{
                                    "track_id_external": [], 
                                    "track_throughput": [], 
                                    "track_block_linked_list": [], 
                                    "track_block_fault_status": [], 
                                    "track_block_maintenance_status": [], 
                                    "track_block_length": [], 
                                    "track_block_speed_limit": [], 
                                    "track_block_suggested_speed": [], 
                                    "track_block_switches": [],
                                    "track_block_crossing": [],
                                    "track_block_stations": [], 
                                    "track_block_occupancy": [], 
                                    "track_block_authority": [] 
                                    }

        self.__train_dictionary = {}
        self.__manula_mode_flag = False

    def add_track(self, file_path):
        # load track layout
        df_track_layout = pd.read_excel(file_path)

        # set track id and update track id counter
        line_num = df_track_layout.loc[:,"Line"]
        self.__track_dictionary["track_id_external"].append(line_num[0])

        # set throughput of track to 0
        self.__track_dictionary["track_throughput"].append(0)

        # set switches from df
        all_blocks = df_track_layout.loc[:,"Block Number"]
        switches_1 = df_track_layout.loc[:,"Switch 1"]
        switches_2 = df_track_layout.loc[:,"Switch 2"]
        block_switches = []
        for i in range(0, len(all_blocks)):
            if switches_1[i] == 0:
                block_switches.append(None)
            else:
                block_switches.append([switches_1[i], switches_2[i]])
        self.__track_dictionary["track_block_switches"].append(block_switches)

        # set block length, speed limit, suggested speed, fault status, maintenance status, occupancy, crossing, station, authority in dictionary
        block_length = df_track_layout.loc[:,"Block Length (m)"]
        block_speed_limit = df_track_layout.loc[:,"Speed Limit (Km/Hr)"]
        block_crossing = df_track_layout.loc[:,"Railway Crossing"]
        block_station = df_track_layout.loc[:,"Station"]
        block_length_dict = {}
        block_speed_limit_dict = {}
        block_suggest_speed_dict = {}
        block_fault_status_dict = {}
        block_maintenance_status_dict = {}
        block_occpuancy_dict = {}
        block_authority_dict = {}
        block_crossing_dict = {}
        block_station_dict = {}
        for i in range(0, len(all_blocks)):
            block_length_dict[all_blocks[i]] = block_length[i]
            block_speed_limit_dict[all_blocks[i]] = block_speed_limit[i]
            block_suggest_speed_dict[all_blocks[i]] = block_speed_limit[i]
            block_fault_status_dict[all_blocks[i]] = False
            block_maintenance_status_dict[all_blocks[i]] = False
            block_occpuancy_dict[all_blocks[i]] = False
            block_authority_dict[all_blocks[i]] = True
            if block_crossing[i] == 0:
                block_crossing_dict[all_blocks[i]] = None
            else:
                block_crossing_dict[all_blocks[i]] = False
            if block_station[i] == 0:
                block_station_dict[all_blocks[i]] = None
            else:
                block_station_dict[all_blocks[i]] = block_station[i]

        # set track block "linked list" and authority based on switches
        block_linked = {}
        end_block = df_track_layout.loc[:,"End"]
        for i in range(0, len(all_blocks)):
            if switches_1[i] == 0:
                if end_block[i] == 1:
                    block_linked[all_blocks[i]] = None
                else:
                    block_linked[all_blocks[i]] = all_blocks[i+1]
            else:
                block_linked[all_blocks[i]] = switches_1[i]
                block_authority_dict[switches_2[i]] = False
                
        self.__track_dictionary["track_block_linked_list"].append(block_linked)
            
        self.__track_dictionary["track_block_length"].append(block_length_dict)
        self.__track_dictionary["track_block_speed_limit"].append(block_speed_limit_dict)
        self.__track_dictionary["track_block_suggested_speed"].append(block_suggest_speed_dict)
        self.__track_dictionary["track_block_fault_status"].append(block_fault_status_dict)
        self.__track_dictionary["track_block_maintenance_status"].append(block_maintenance_status_dict)
        self.__track_dictionary["track_block_occupancy"].append(block_occpuancy_dict)
        self.__track_dictionary["track_block_authority"].append(block_authority_dict)
        self.__track_dictionary["track_block_crossing"].append(block_crossing_dict)
        self.__track_dictionary["track_block_stations"].append(block_station_dict)

    # input is list of tuples -> [(x0,y0),(x1,y1),...,(xn,yn)] -> [(1001, 0), (1002, 1),...]
    def set_fault_status(self, block_bool):
        # get fault status list from dictionary
        fault_status_list = self.__track_dictionary["track_block_fault_status"]
        authority_list = self.__track_dictionary["track_block_authority"]
        for i in range(0, len(block_bool)):
            curr_block = block_bool[i]
            line_num = int((curr_block[0]-(curr_block[0]%1000))/1000) # translate line num (2000 + xyz -> 2)
            block_num = int(curr_block[0] - (line_num*1000))
            block_status = curr_block[1]

            # get line and block index
            line_index = self.__track_dictionary["track_id_external"].index(line_num)
            # update status using indices
            fault_status_list[line_index][block_num] = block_status
            # update authority
            if block_status == True:
                authority_list[line_index][block_num] = False
        
        # update fault status and authority list in dictionary
        self.__track_dictionary["track_block_fault_status"] = fault_status_list
        self.__track_dictionary["track_block_authority"] = authority_list

    def set_switch_position(self, block_bool):
        # get switch state list from dictionary
        block_switches_list = self.__track_dictionary["track_block_switches"]
        track_linked_list = self.__track_dictionary["track_block_linked_list"]
        authority_list = self.__track_dictionary["track_block_authority"]
        for i in range(0, len(block_bool)):
            curr_block = block_bool[i]
            line_num = int((curr_block[0]-(curr_block[0]%1000))/1000) # translate line num (2000 + xyz -> 2)
            block_num = int(curr_block[0] - (line_num*1000))
            switch_state = curr_block[1]

            # get line and block index
            line_index = self.__track_dictionary["track_id_external"].index(line_num)

            # get block switches
            block_switches = block_switches_list[line_index][block_num-1]

            if switch_state == True:
                track_linked_list[line_index][block_num] = max(block_switches[1], block_switches[0])
                authority_list[line_index][min(block_switches[1], block_switches[0])] = False
                authority_list[line_index][max(block_switches[1], block_switches[0])] = True
            else:
                track_linked_list[line_index][block_num] = min(block_switches[1], block_switches[0])
                authority_list[line_index][max(block_switches[1], block_switches[0])] = False
                authority_list[line_index][min(block_switches[1], block_switches[0])] = True

        # update linked list and authority list in dictionary
        self.__track_dictionary["track_block_linked_list"] = track_linked_list
        self.__track_dictionary["track_block_authority"] = authority_list

    # output is list of tuples -> [(x0,y0),(x1,y1),...,(xn,yn)] -> [(1001, 0), (1002, 1),...]
    def get_authority(self):
        track_id = self.__track_dictionary["track_id_external"]
        authority_list = self.__track_dictionary["track_block_authority"]
        authority_tuple_list = []
        # Loop through lines
        for i in range(0,len(authority_list)):
            line_num = track_id[i]
            authority_dict = authority_list[i]
            # Loop through authority of 
            for key in authority_dict:
                authority_tuple_list.append((((line_num*1000) + key), authority_dict[key]))

        return authority_tuple_list




ctc_test = CTC()
ctc_test.add_track("Iteration3/Track_Layout_Blue.xlsx")
# ctc_test.set_fault_status([(1003, True)])
ctc_test.set_switch_position([(1005, True)])
authority_tuple_list = ctc_test.get_authority()
print(authority_tuple_list)
