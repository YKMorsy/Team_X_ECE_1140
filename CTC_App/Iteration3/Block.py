# Block class containing information about block

class Block:
    # Constructor
    def __init__(self, block_number, block_length, block_speed_limit, block_switch_1, block_switch_2, block_station, block_railway):
        # Default attributes
        self.occupancy = 0
        self.status = True

        # Defined attributes
        self.block_number = block_number
        self.blocK_length = block_length
        self.block_speed_limit = block_speed_limit
        self.block_railway = block_railway

        self.block_authority = False
        self.block_suggested_speed = self.block_speed_limit

        # Switch info - Used also to link blocks even if they do not have switches
        self.cur_switch_pos = block_switch_1
        self.block_switch_1 = block_switch_1
        self.block_switch_2 = block_switch_2

        # Station info
        self.block_station = block_station

    # Function to set switch position
    def setSwitchPos(self, pos_bool):
        if pos_bool == True:
            self.cur_switch_pos = max(self.block_switch_1, self.block_switch_2)
        else:
            self.cur_switch_pos = min(self.block_switch_1, self.block_switch_2)


