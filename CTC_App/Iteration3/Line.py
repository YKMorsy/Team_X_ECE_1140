import pandas as pd
from CTC_App.Iteration3.Block import Block

class Line:
    # Constructor
    def __init__(self, file_path):

        # Initialize values
        self.block_list = []
        self.throughput = 0
        self.line_color = ''
        self.line_station_list = []
        self.__default_route = []
        self.__section_block_dict = {}

        # Read layout from file
        df_track_layout = pd.read_excel(file_path)

        # Pare data frame into blocks and their information
        self.parseLine(df_track_layout)

        # Create default route depending on line
        self.setRoute()

    # Function to update block list by parsing track layout dataframe
    def parseLine(self, df_track_layout):

        block_section = df_track_layout.loc[:,"Section"]
        unique_block_section = list(set(block_section))
        block_color = df_track_layout.loc[:,"Line"]
        self.line_color = block_color[0]
        block_numbers = df_track_layout.loc[:,"Block Number"]
        block_lengths = df_track_layout.loc[:,"Block Length (m)"]
        block_speed_limits = df_track_layout.loc[:,"Speed Limit (Km/Hr)"]
        block_switches_1 = df_track_layout.loc[:,"Switch 1"]
        block_switches_2 = df_track_layout.loc[:,"Switch 2"]
        block_stations = df_track_layout.loc[:,"Station"]
        self.line_station_list = block_stations.tolist()
        self.line_station_list = [i for i in self.line_station_list if i != -1]

        block_railway_crossing = df_track_layout.loc[:,"Railway Crossing"]

        for i in range(0, len(block_numbers)):
            # Append block objects to block list
            railway_cross = -1
            if block_railway_crossing[i] == 1:
                railway_cross = True
            elif block_railway_crossing[i] == 0:
                railway_cross = False
            self.block_list.append(Block(block_numbers[i], block_lengths[i], block_speed_limits[i], 
            block_switches_1[i], block_switches_2[i], block_stations[i], railway_cross))
            
            # Append section+block to section_block dictionary
            if block_section[i] in self.__section_block_dict:
                self.__section_block_dict[block_section[i]] = self.__section_block_dict[block_section[i]] + [block_numbers[i]]
            else:
                self.__section_block_dict[block_section[i]] = [block_numbers[i]]

    # Function to initialize default route of line depending on line color
    def setRoute(self):
        if self.line_color == 'Blue':
            pass
        elif self.line_color == 'Green':
            # YARD -> K -> L -> M -> N -> O -> P -> Q -> N ->
            # R -> S -> T -> U -> V -> W -> X -> Y -> Z -> F ->
            # E -> D -> C -> B -> A -> D -> E -> F -> G -> H ->
            # I -> YARD
            self.__default_route = self.__section_block_dict['YARD'] + self.__section_block_dict['K'] + self.__section_block_dict['L'] +\
                                    self.__section_block_dict['M'] + self.__section_block_dict['N'] + self.__section_block_dict['O'] +\
                                    self.__section_block_dict['P'] + self.__section_block_dict['Q'] + list(reversed(self.__section_block_dict['N'])) +\
                                    self.__section_block_dict['R'] + self.__section_block_dict['S'] + self.__section_block_dict['T'] +\
                                    self.__section_block_dict['U'] + self.__section_block_dict['V'] + self.__section_block_dict['W'] +\
                                    self.__section_block_dict['X'] + self.__section_block_dict['Y'] + self.__section_block_dict['Z'] +\
                                    list(reversed(self.__section_block_dict['F'])) + list(reversed(self.__section_block_dict['E'])) +\
                                    list(reversed(self.__section_block_dict['D'])) + list(reversed(self.__section_block_dict['C'])) +\
                                    list(reversed(self.__section_block_dict['B'])) + list(reversed(self.__section_block_dict['A'])) +\
                                    self.__section_block_dict['D'] + self.__section_block_dict['E'] + self.__section_block_dict['F'] +\
                                    self.__section_block_dict['G'] + self.__section_block_dict['H'] + self.__section_block_dict['I'] +\
                                    self.__section_block_dict['YARD']

        elif self.line_color == 'Red':
            # YARD -> C -> B -> A -> F -> G -> H12345 -> I -> J12 ->
            # K -> L -> M -> N -> J1 -> I -> H5 -> O -> P -> Q -> H3 ->
            # R -> S -> T -> H1 -> G -> F -> E -> D -> YARD
            self.__default_route = self.__section_block_dict['YARD'] + list(reversed(self.__section_block_dict['C'])) +\
                                    list(reversed(self.__section_block_dict['B'])) + list(reversed(self.__section_block_dict['A'])) +\
                                    self.__section_block_dict['F'] + self.__section_block_dict['G'] + self.__section_block_dict['H1'] +\
                                    self.__section_block_dict['H2'] + self.__section_block_dict['H3'] + self.__section_block_dict['H4'] +\
                                    self.__section_block_dict['H5'] + self.__section_block_dict['I'] + self.__section_block_dict['J1'] +\
                                    self.__section_block_dict['J2'] + self.__section_block_dict['K'] + self.__section_block_dict['L'] +\
                                    self.__section_block_dict['M'] + self.__section_block_dict['N'] + list(reversed(self.__section_block_dict['J1'])) +\
                                    list(reversed(self.__section_block_dict['I'])) + list(reversed(self.__section_block_dict['H5'])) +\
                                    self.__section_block_dict['O'] + self.__section_block_dict['P'] + self.__section_block_dict['Q'] +\
                                    list(reversed(self.__section_block_dict['H3'])) +\
                                    self.__section_block_dict['R'] + self.__section_block_dict['S'] + self.__section_block_dict['T'] +\
                                    list(reversed(self.__section_block_dict['H1'])) +\
                                    list(reversed(self.__section_block_dict['G'])) + list(reversed(self.__section_block_dict['F'])) +\
                                    list(reversed(self.__section_block_dict['E'])) + list(reversed(self.__section_block_dict['E'])) +\
                                    self.__section_block_dict['YARD']
            
    def getRoute(self):
        route = []
        for block in self.__default_route:
            route.append(block)
        return route

    # Called by UI:
    # Function to return list of closed blocks
    def getClosedBlocks(self):
        closed_blocks = []

        for block in self.block_list:
            if block.status == False:
                closed_blocks.append(block.block_number)

        return closed_blocks

    # Function to return list of switch positions ([origin, target])
    def getSwitchState(self):
        switch_state = []

        for block in self.block_list:
            if block.cur_switch_pos != -1:
                switch_state.append([block.block_number, block.cur_switch_pos])
        
        return switch_state

    # Function to return list of blocks and crossing status ([origin, target])
    def getCrossingState(self):
        cross_state = []
        for block in self.block_list:
            if block.block_railway != -1:
                cross_state.append([block.block_number, block.block_railway])
        
        
        return cross_state
        
    # Called by CTC (wayside to CTC)
    
    # Function to update throughput (Track Model to CTC)
    def setThroughput(self, throughput):
        self.throughput = self.throughput + throughput

    # Function to update switch position
    def setSwitchPosition(self, switch_dict):
        for key in switch_dict:
            if self.line_color == "Green":
                cur_key = key - 1000
                self.block_list[cur_key].setSwitchPos(switch_dict[key])
            elif self.line_color == "Red":
                cur_key = key - 2000
                self.block_list[cur_key].setSwitchPos(switch_dict[key])

    # # Function to upate occupancy
    # def setBlockOccupancy(self, block_number, occupancy):
    #     self.block_list[block_number].occupancy = occupancy

    # Function to update block status
    def setBlockStatus(self, status_dict):
        for key in status_dict:
            if self.line_color == "Green":
                cur_key = key - 1000
                self.block_list[cur_key].status = status_dict[key]
            elif self.line_color == "Red":
                cur_key = key - 2000
                self.block_list[cur_key].status = status_dict[key]

    # Function to update railway crossing
    def setRailWayCrossing(self, crossing_dict):
        for key in crossing_dict:
            if self.line_color == "Green":
                cur_key = key - 1000
                self.block_list[cur_key].block_railway = crossing_dict[key]
            elif self.line_color == "Red":
                cur_key = key - 2000
                self.block_list[cur_key].block_railway = crossing_dict[key]




    # Called by wayside (CTC to Wayside):

    def getBlockAuthority(self):
        authority_dict = {}

        for block in self.block_list:
            if self.line_color == "Green":
                cur_block = block.block_number + 1000
            if self.line_color == "Red":
                cur_block = block.block_number + 2000
            authority_dict[cur_block] = block.block_authority

        return authority_dict

    def getBlockSuggestedSpeed(self):
        speed_dict = {}

        for block in self.block_list:
            if self.line_color == "Green":
                cur_block = block.block_number + 1000
            if self.line_color == "Red":
                cur_block = block.block_number + 2000
            speed_dict[cur_block] = block.block_suggested_speed

        return speed_dict


# line_test = Line("Iteration3/Track_Layout_Green.xlsx")
# print(line_test.getBlockSuggestedSpeed())