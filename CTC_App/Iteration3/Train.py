import pandas as pd
from Line import Line

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
            self.route.pop(0)
            self.current_position = self.route[0]
            current_block = self.line.block_list[self.current_position]
            current_station = current_block.block_station
            current_status = current_block.status
            suggested_speed = current_block.block_speed_limit

            next_block_number_1 = self.route[1]
            next_block_1 = self.line.block_list[next_block_number_1]
            next_block_1_station = next_block_1.block_station
            next_block_1_status = next_block_1.status

            next_block_number_2 = self.route[2]
            next_block_2 = self.line.block_list[next_block_number_2]
            next_block_2_station = next_block_2.block_station
            next_block_2_status = next_block_2.status

            next_station = self.station_list[0]
            
            upcoming_block = next_block_number_1
            upcoming_block_authority = True

            # Check if next 2 blocks have destinations stations
            # If blocks have destiantion stations, slowly decrement suggested speed until 0
            if ((next_block_2_station == next_station) and (next_block_2_status == True)):
                suggested_speed = 0.75*suggested_speed
            elif ((next_block_1_station == next_station) and (next_block_1_status == True)):
                suggested_speed = 0.5*suggested_speed
            elif (current_station == next_station and (current_status == True)):
                suggested_speed = 0*suggested_speed

                # Wait then increase speed and remove station from list
                ####### WAIT 
                suggested_speed = current_block.block_speed_limit
                self.station_list.pop(0)


            elif (current_status == True):
                suggested_speed = suggested_speed

            # # Check if next 2 blocks have fault
            # # If blocks have fault, decrement speed and set authority to 0
            # if (next_block_2_status == False):
            #     suggested_speed = 0.5*suggested_speed
            # elif (next_block_1_status == False):
            #     suggested_speed = 0*suggested_speed
            #     upcoming_block_authority = False
