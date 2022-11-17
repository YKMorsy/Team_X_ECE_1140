import pandas as pd
from CTC_App.Iteration3.Line import Line

class Train:

    def __init__(self, train_id, station_list, line, depart_time):

        # Initialize variables
        self.train_id = train_id
        self.station_list = station_list
        self.line = line
        self.current_position = 0
        self.depart_time = depart_time

        # Intialize route using arrival stations
        self.route = line.getRoute()

    def updateStations(self, station_list):
        self.station_list = station_list

    def setPosition(self, line_color, block_number, occupancy):
        if (block_number == self.route[1] and self.line.line_color == line_color and occupancy == True):

            # Set previous authority to False
            self.line.block_list[self.route[0]].block_authority = False

            # # Set suggested speed of previous block to speed limit
            # self.line.block_list[self.route[0]].block_suggested_speed = self.line.block_list[self.route[0]].block_speed_limit

            self.route.pop(0)
            if len(self.route) >= 1:
                self.current_position = self.route[0] # Current position
                current_block = self.line.block_list[self.current_position]
                current_station = current_block.block_station
                current_status = current_block.status
                suggested_speed = current_block.block_speed_limit

            if len(self.route) >= 2:
                next_block_number_1 = self.route[1]
                next_block_1 = self.line.block_list[next_block_number_1]
                next_block_1_station = next_block_1.block_station
                next_block_1_status = next_block_1.status

            if len(self.route) >= 3:
                next_block_number_2 = self.route[2]
                next_block_2 = self.line.block_list[next_block_number_2]
                next_block_2_station = next_block_2.block_station
                next_block_2_status = next_block_2.status

            if len(self.station_list) > 0:
                next_station = self.station_list[0]


                # Check if next 2 blocks have destinations stations
                # If blocks have destiantion stations, slowly decrement suggested speed until 0
                if ((next_block_2_station == next_station) and (next_block_2_status == True)):
                    suggested_speed = 0.75*suggested_speed
                elif ((next_block_1_station == next_station) and (next_block_1_status == True)):
                    suggested_speed = 0.5*suggested_speed
                elif (current_station == next_station and (current_status == True)):
                    suggested_speed = 1

                    # suggested_speed = current_block.block_speed_limit
                    self.station_list.pop(0)


                elif (current_status == True):
                    suggested_speed = suggested_speed

            # Check if next block is a switch
            if len(self.route) >= 2:
                block_switch_1 = self.line.block_list[self.route[1]].block_switch_1
                block_switch_2 = self.line.block_list[self.route[1]].block_switch_2
                if self.route[1] == block_switch_1:
                    self.line.block_list[block_switch_2].block_authority = False
                elif self.route[1] == block_switch_2:
                    self.line.block_list[block_switch_1].block_authority = False

            # Set next next authority to True
            # if len(self.route) >= 3:
                # self.line.block_list[self.route[2]].block_authority = True

            # Set next authority to True
            if len(self.route) >= 2:
                self.line.block_list[self.route[1]].block_authority = True
                self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit


            # Set current authority to True
            # Set next authority to True
            if len(self.route) >= 1:
                self.line.block_list[self.route[0]].block_authority = True
                self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed

            # Set suggested speed
            self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed

            # print("sugg speed on current block " + str(self.route[0]) + " is " + str(self.line.block_list[self.route[0]].block_suggested_speed))
            # print("sugg speed on next block " + str(self.route[1]) + " is " + str(self.line.block_list[self.route[1]].block_suggested_speed))
            # print("Authority on current block " + str(self.route[0]) + " is " + str(self.line.block_list[self.route[0]].block_authority))
            # print("Authority on next block " + str(self.route[1]) + " is " + str(self.line.block_list[self.route[1]].block_authority))
            
