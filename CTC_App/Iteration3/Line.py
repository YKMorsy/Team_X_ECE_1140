import pandas as pd
from Block import Block

class Line:
    # Constructor
    def __init__(self, file_path):

        # Initialize values
        self.block_authorities = []
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
            self.block_list.append(Block(block_numbers[i], block_lengths[i], block_speed_limits[i], 
            block_switches_1[i], block_switches_2[i], block_stations[i], block_railway_crossing[i]))
            self.block_authorities.append(1)
            
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
            pass

    def getRoute(self):
        return self.__default_route

    # Function to update throughput
    def setThroughput(self, throughput):
        self.throughput = throughput

    # Function to update switch position
    def setSwitchPosition(self, block_number, pos_bool):
        self.block_list[block_number].setSwitchPos(pos_bool)

    # Function to upate occupancy
    def setBlockOccupancy(self, block_number, occupancy):
        self.block_list[block_number].occupancy = occupancy

    # Function to update block status
    def setBlockStatus(self, block_number, status):
        self.block_list[block_number].status = status

    # Function to update railway crossing
    def setRailWayCrossing(self, block_number, status):
        self.block_list[block_number].block_railway = status

# line_test = Line("Iteration3/Track_Layout_Green.xlsx")
# print(line_test.getRoute())