import pandas as pd
from Block import Block

class Line:
    # Constructor
    def __init__(self, file_path):

        # Initialize values
        self.block_list = []
        self.throughput = 0

        # Read layout from file
        df_track_layout = pd.read_excel(file_path)

        # Pare data frame into blocks and their information
        self.parseLine(df_track_layout)

    # Function to update block list by parsing track layout dataframe
    def parseLine(self, df_track_layout):

        block_numbers = df_track_layout.loc[:,"Block Number"]
        block_lengths = df_track_layout.loc[:,"Block Length (m)"]
        block_speed_limits = df_track_layout.loc[:,"Speed Limit (Km/Hr)"]
        block_switches_1 = df_track_layout.loc[:,"Switch 1"]
        block_switches_2 = df_track_layout.loc[:,"Switch 2"]
        block_stations = df_track_layout.loc[:,"Station"]
        block_railway_crossing = df_track_layout.loc[:,"Railway Crossing"]

        for i in range(0, len(block_numbers)):
            self.block_list.append(Block(block_numbers[i], block_lengths[i], block_speed_limits[i], 
            block_switches_1[i], block_switches_2[i], block_stations[i], block_railway_crossing[i]))

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