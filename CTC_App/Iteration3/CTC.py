import pandas as pd

class CTC:
    def __init__(self):
        self.__track_dictionary  =	{
                                    "track_id": [], #
                                    "track_throughput": [], #
                                    "track_block_linked_list": [], #
                                    "track_block_fault_status": [], #
                                    "track_block_maintenance_status": [], #
                                    "track_block_length": [], #
                                    "track_block_speed_limit": [], #
                                    "track_block_suggested_speed": [], #
                                    "track_block_switches": [], #
                                    "track_block_crossing": [], #
                                    "track_block_stations": [], #
                                    "track_block_occupancy": [], #
                                    "track_block_authority": [] #
                                    }

        self.__train_dictionary = {}
        self.__manula_mode_flag = False
        self.__rack_id_counter = 0

    def add_track(self, file_path):
        # load track layout
        df_track_layout = pd.read_excel(file_path)

        # set track id and update track id counter
        self.__track_dictionary["track_id"].append(self.__rack_id_counter)
        self.__rack_id_counter += 1

        # set throughput of track to 0
        self.__track_dictionary["track_throughput"].append(0)

        # set switches from df
        all_blocks = df_track_layout.loc[:,"Block Number"]
        switches_1 = df_track_layout.loc[:,"Switch 1"]
        switches_2 = df_track_layout.loc[:,"Switch 2"]
        block_switches = []
        for i in range(0, len(all_blocks)):
            if switches_1[i] == 0:
                block_switches.append(0)
            else:
                block_switches.append([switches_1[i], switches_2[i]])
        self.__track_dictionary["track_block_switches"].append(block_switches)

        # set track block "linked list" based on switches
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
        self.__track_dictionary["track_block_linked_list"].append(block_linked)

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
            block_fault_status_dict[all_blocks[i]] = 0
            block_maintenance_status_dict[all_blocks[i]] = 0
            block_occpuancy_dict[all_blocks[i]] = 0
            block_authority_dict[all_blocks[i]] = 1
            if block_crossing[i] == 0:
                block_crossing_dict[all_blocks[i]] = None
            else:
                block_crossing_dict[all_blocks[i]] = 0
            if block_station[i] == 0:
                block_station_dict[all_blocks[i]] = None
            else:
                block_station_dict[all_blocks[i]] = block_station[i]
            
        self.__track_dictionary["track_block_length"].append(block_length_dict)
        self.__track_dictionary["track_block_speed_limit"].append(block_speed_limit_dict)
        self.__track_dictionary["track_block_suggested_speed"].append(block_suggest_speed_dict)
        self.__track_dictionary["track_block_fault_status"].append(block_fault_status_dict)
        self.__track_dictionary["track_block_maintenance_status"].append(block_maintenance_status_dict)
        self.__track_dictionary["track_block_occupancy"].append(block_occpuancy_dict)
        self.__track_dictionary["track_block_authority"].append(block_authority_dict)
        self.__track_dictionary["track_block_crossing"].append(block_crossing_dict)
        self.__track_dictionary["track_block_stations"].append(block_station_dict)

    

ctc_test = CTC()
CTC.add_track(ctc_test, "Iteration3/Track_Layout_Blue.xlsx")


        
        



        



    


