from CTC_App.Iteration3.Line import Line

class Train:

    def __init__(self, train_id, station_list, line, train_list, cur_time):

        # Initialize variables
        self.train_id = train_id
        self.station_list = station_list
        self.line = line
        self.current_position = 0
        # Intialize route using arrival stations
        self.route = line.getRoute()
        self.train_list = train_list

        self.cur_time = cur_time
        self.stop_time = cur_time
        self.stop_train = False

        if self.line.line_color == 'Green':
            self.cur_section = 'YARD'
            self.next_section = 'K'
        elif self.line.line_color == 'Red':
            self.cur_section = 'YARD'
            self.next_section = 'CBAFGH1'

        # Set authority and suggested speed of yard and next block
        self.line.block_list[self.route[0]].block_authority = True
        self.line.block_list[self.route[1]].block_authority = True
        self.line.block_list[self.route[0]].block_suggested_speed = self.line.block_list[self.route[0]].block_speed_limit
        # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit

    def updateStations(self, station_list):
        self.station_list = station_list

    def update_time(self, cur_time):
        self.cur_time = cur_time

    def setPosition(self, line_color, block_number, occupancy):
        if (block_number == self.route[1] and self.line.line_color == line_color and occupancy == True):
            
            old_block = self.route[0]
            # Set previous authority to False
            self.line.block_list[self.route[0]].block_authority = False
            
            self.line.block_list[self.route[0]].occupancy = False
            self.line.block_list[self.route[1]].occupancy = True

            # # Set suggested speed of previous block to speed limit
            # self.line.block_list[self.route[0]].block_suggested_speed = self.line.block_list[self.route[0]].block_speed_limit
            next_block_2_station = None
            next_block_2_status = None
            next_block_1_status = None
            next_block_1_station = None
            current_status = None
            current_station = None

            self.route.pop(0)

            two_way_collision_flag = False

            if len(self.route) >= 1:
                self.current_position = self.route[0] # Current position
                current_block = self.line.block_list[self.current_position]

            if self.line.line_color == 'Green':
                # Make sure no collisions happen before entering a two way
                # Get current and next section using current location
                if block_number >= 63 and block_number <= 76:
                    self.cur_section = "KLM"
                    self.next_section = "N"
                elif self.cur_section == "KLM" and block_number >= 77 and block_number <= 85:
                    self.cur_section = "N"
                    self.next_section = "OPQ"
                elif block_number >= 86 and block_number <= 100:
                    self.cur_section = "OPQ"
                    self.next_section = "N"
                elif self.cur_section == "OPQ" and block_number >= 77 and block_number <= 85:
                    self.cur_section = "N"
                    self.next_section = "RSTUVWXYZ"
                elif block_number >= 101 and block_number <= 150:
                    self.cur_section = "RSTUVWXYZ"
                    self.next_section = "FED"
                elif self.cur_section == "RSTUVWXYZ" and block_number >= 13 and block_number <= 29:
                    self.cur_section = "FED"
                    self.next_section = "CBA"
                elif block_number >= 1 and block_number <= 12:
                    self.cur_section = "CBA"
                    self.next_section = "FED"
                elif self.cur_section == "CBA" and block_number >= 13 and block_number <= 16:
                    self.cur_section = "FED"
                    self.next_section = "GHI"
                elif block_number >= 30 and block_number <= 57:
                    self.cur_section = "GHI"
                    self.next_section = "YARD"

                # Check if train is on section OPQ and see if train is coming from N to OPQ
                if self.cur_section == "OPQ":
                    for train in self.train_list:
                        if train.cur_section == "N" and train.next_section == "OPQ":
                            
                            # Check if train is on the last 4 blocks of OPQ
                            if block_number == 96:
                                suggested_speed = 0.75*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 97:
                                suggested_speed = 0.5*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 98:
                                suggested_speed = 0
                            elif block_number == 99:
                                suggested_speed = 0
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                # self.route.insert(0, 98)
                                print("Possible Two Way Collision... Avoiding")
                            else:
                                suggested_speed = current_block.block_speed_limit

                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                            print("Suggested Speed Is " + str(suggested_speed))

                            two_way_collision_flag = True

                            break
                # Check if train is on section KLM and see if train is coming from N to RSTUVWXYZ
                elif self.cur_section == "KLM":
                    for train in self.train_list:
                        if train.cur_section == "N" and train.next_section == "RSTUVWXYZ":
                            
                            # Check if train is on the last 4 blocks of OPQ
                            if block_number == 72:
                                suggested_speed = 0.75*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 73:
                                suggested_speed = 0.5*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 74:
                                suggested_speed = 0
                            elif block_number == 75:
                                suggested_speed = 0
                            elif block_number == 76:
                                suggested_speed = 0
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                # self.route.insert(0, 74)
                                print("Possible Two Way Collision... Avoiding")
                            else:
                                suggested_speed = current_block.block_speed_limit

                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                            print("Suggested Speed Is " + str(suggested_speed))

                            two_way_collision_flag = True

                            break
                # Check if train is on section RSTUVWXYZ and see if train is coming from FED to GHI
                elif self.cur_section == "RSTUVWXYZ":
                    for train in self.train_list:
                        if train.cur_section == "FED" and train.next_section == "GHI":
                            
                            # Check if train is on the last 4 blocks of OPQ
                            if block_number == 145:
                                suggested_speed = 0.75*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 146:
                                suggested_speed = 0.5*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 147:
                                suggested_speed = 0
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                # self.route.insert(0, 148)
                                print("Possible Two Way Collision... Avoiding")
                            else:
                                suggested_speed = current_block.block_speed_limit

                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                            print("Suggested Speed Is " + str(suggested_speed))

                            two_way_collision_flag = True

                            break
                # Check if train is on section CBA and see if train is coming from FED to CBA
                elif self.cur_section == "CBA":
                    for train in self.train_list:
                        if train.cur_section == "FED" and train.next_section == "CBA":
                            
                            # Check if train is on the last 4 blocks of OPQ
                            if block_number == 5:
                                suggested_speed = 0.75*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 4:
                                suggested_speed = 0.5*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 3:
                                suggested_speed = 0
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                # self.route.insert(0, 3)
                                print("Possible Two Way Collision... Avoiding")
                            else:
                                suggested_speed = current_block.block_speed_limit

                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                            print("Suggested Speed Is " + str(suggested_speed))

                            two_way_collision_flag = True

                            break
            
            elif self.line.line_color == 'Red':
                # Make sure no collisions happen before entering a two way
                # Get current and next section using current location
                if self.cur_section == "Yard" and block_number >= 1 and block_number <= 27:
                    self.cur_section = "CBAFGH1"
                    self.next_section = "H2"
                elif self.cur_section == "CBAFGH1" and block_number >= 28 and block_number <= 32:
                    self.cur_section = "H2"
                    self.next_section = "H3"
                elif self.cur_section == "H2" and block_number >= 33 and block_number <= 38:
                    self.cur_section = "H3"
                    self.next_section = "H4"
                elif self.cur_section == "H3" and block_number >= 39 and block_number <= 43:
                    self.cur_section = "H4"
                    self.next_section = "H5IJ1"
                elif self.cur_section == "H4" and block_number >= 44 and block_number <= 52:
                    self.cur_section = "H5IJ1"
                    self.next_section = "J2KLMN"
                elif self.cur_section == "H5IJ1" and block_number >= 53 and block_number <= 66:
                    self.cur_section = "J2KLMN"
                    self.next_section = "H5IJ1"
                elif self.cur_section == "J2KLMN" and block_number >= 44 and block_number <= 52:
                    self.cur_section = "H5IJ1"
                    self.next_section = "OPQ"
                elif self.cur_section == "H5IJ1" and block_number >= 67 and block_number <= 71:
                    self.cur_section = "OPQ"
                    self.next_section = "H3"
                elif self.cur_section == "OPQ" and block_number >= 33 and block_number <= 38:
                    self.cur_section = "H3"
                    self.next_section = "RST"
                elif self.cur_section == "H3" and block_number >= 72 and block_number <= 76:
                    self.cur_section = "RST"
                    self.next_section = "CBAFGH1"
                elif self.cur_section == "RST" and block_number >= 1 and block_number <= 27:
                    self.cur_section = "CBAFGH1"
                    self.next_section = "YARD"

                # # Check if train is on section J2KLMN and see if train is coming from H5IJ1 to J2KLMN
                if self.cur_section == "J2KLMN":
                    for train in self.train_list:
                        if train.cur_section == "H5IJ1" and train.next_section == "J2KLMN":
                            # Check if train is on the last 4 blocks of OPQ
                            if block_number == 62:
                                suggested_speed = 0.75*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 63:
                                suggested_speed = 0.5*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 64:
                                suggested_speed = 0
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                # self.route.insert(0, 64)
                                print("Possible Two Way Collision... Avoiding")
                            else:
                                suggested_speed = current_block.block_speed_limit

                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                            print("Suggested Speed Is " + str(suggested_speed))

                            two_way_collision_flag = True

                            break
                # # Check if train is on section H4 and see if train is coming from H5IJ1 to OPQ
                elif self.cur_section == "H4":
                    for train in self.train_list:
                        if train.cur_section == "H5IJ1" and train.next_section == "OPQ":
                            
                            # Check if train is on the last 4 blocks of OPQ
                            if block_number == 39:
                                suggested_speed = 0.75*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 40:
                                suggested_speed = 0.5*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 41:
                                suggested_speed = 0
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                # self.route.insert(0, 41)
                                print("Possible Two Way Collision... Avoiding")
                            else:
                                suggested_speed = current_block.block_speed_limit

                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                            print("Suggested Speed Is " + str(suggested_speed))

                            two_way_collision_flag = True

                            break
                # # Check if train is on section OPQ and see if train is coming from H3 to H4
                elif self.cur_section == "OPQ":
                    for train in self.train_list:
                        if train.cur_section == "H3" and train.next_section == "H4":
                            
                            # Check if train is on the last 4 blocks of OPQ
                            if block_number == 67:
                                suggested_speed = 0.75*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 68:
                                suggested_speed = 0.5*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 69:
                                suggested_speed = 0
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                # self.route.insert(0, 69)
                                print("Possible Two Way Collision... Avoiding")
                            else:
                                suggested_speed = current_block.block_speed_limit

                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                            print("Suggested Speed Is " + str(suggested_speed))

                            two_way_collision_flag = True

                            break
                # # Check if train is on section H2 and see if train is coming from H3 to RST
                elif self.cur_section == "H2":
                    for train in self.train_list:
                        if train.cur_section == "H3" and train.next_section == "RST":
                            
                            # Check if train is on the last 4 blocks of OPQ
                            if block_number == 28:
                                suggested_speed = 0.75*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 29:
                                suggested_speed = 0.5*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 30:
                                suggested_speed = 0
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                # self.route.insert(0, 30)
                                print("Possible Two Way Collision... Avoiding")
                            else:
                                suggested_speed = current_block.block_speed_limit

                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                            print("Suggested Speed Is " + str(suggested_speed))

                            two_way_collision_flag = True

                            break
                # # Check if train is on section RST and see if train is coming from CBAFGH1 to H2
                elif self.cur_section == "RST":
                    for train in self.train_list:
                        if train.cur_section == "CBAFGH1" and train.next_section == "H2":
                            
                            # Check if train is on the last 4 blocks of OPQ
                            if block_number == 72:
                                suggested_speed = 0.75*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 73:
                                suggested_speed = 0.5*current_block.block_speed_limit
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                print("Possible Two Way Collision... Avoiding")
                            elif block_number == 74:
                                suggested_speed = 0
                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                                # self.route.insert(0, 74)
                                print("Possible Two Way Collision... Avoiding")
                            else:
                                suggested_speed = current_block.block_speed_limit

                                # self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed
                                # self.line.block_list[self.route[1]].block_suggested_speed = self.line.block_list[self.route[1]].block_speed_limit
                            print("Suggested Speed Is " + str(suggested_speed))

                            two_way_collision_flag = True

                            break

            if two_way_collision_flag == False:
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

                        if current_station.isnumeric() == False:
                            suggested_speed = 1
                            # suggested_speed = current_block.block_speed_limit
                            self.station_list.pop(0)
                        else:
                            suggested_speed = 0
                            # suggested_speed = current_block.block_speed_limit
                            if self.stop_train == False:
                                self.stop_time = self.cur_time
                                self.stop_train = True
                            else:
                                if (self.cur_time - self.stop_time) == 30:
                                    self.stop_train == False
                                    self.station_list.pop(0)

                            # self.route.insert(0, old_block)

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


            # Set current authority to True
            if len(self.route) >= 1:
                # print("Block " + str(self.route[0]) + " " + str(suggested_speed))

                if len(self.route) >= 2:
                    if self.line.block_list[self.route[1]].status == False:
                        self.line.block_list[self.route[1]].block_authority = False
                    else:
                        self.line.block_list[self.route[1]].block_authority = True

                    if self.line.block_list[self.route[1]].occupancy == True or self.line.block_list[self.route[1]].status == False:
                        suggested_speed = 0

                self.line.block_list[self.route[0]].block_authority = True

                if ((old_block == 55 or old_block == 56 or old_block == 57 or old_block == 0) and self.line.line_color == 'Green') or ((old_block == 7 or old_block == 8 or old_block == 9 or old_block == 0) and self.line.line_color == 'Red'):
                    # print(self.route[0])
                    suggested_speed = current_block.block_speed_limit
                    self.line.block_list[self.route[0]].block_suggested_speed = current_block.block_speed_limit
                else:
                    self.line.block_list[self.route[0]].block_suggested_speed = suggested_speed


            if suggested_speed == 0:
                # print(old_block)
                self.route.insert(0, old_block)
