from track_controller.track_controller import WaysideController


class track_control_controller():
    def __init__(self):
        self.track_controller_list = [WaysideController(), WaysideController()] 

        #toy data
        self.track_controller_list[0].set_authority([(1,True), (2, False), (3, False)])
        self.track_controller_list[0].set_switch_positions([(1,True), (2, True), (3, False)])
        self.track_controller_list[0].set_occupancy([(1,True), (2, True), (4, False)])
        self.track_controller_list[0].set_railway_crossings([(1,True), (2, True), (3, False)])
        self.track_controller_list[0].set_light_colors([(1,True,True), (5, True,True), (3, False,True)])
        self.track_controller_list[0].set_statuses([(1,True), (2, True), (3, True)])
        self.track_controller_list[0].set_suggested_speed([(1,0b00011010), (2, 0b00100111), (3, 0b00010101)])
        self.track_controller_list[0].set_commanded_speed([(1,0b000000000), (2, 0b00000000), (3, 0b00000000)])
        self.track_controller_list[0].set_speed_limit([(1,0b000000000), (2, 0b00000000), (3, 0b00000000)])
        self.track_controller_list[0].set_PLC("track_controller/testPLCfile.txt")

        self.track_controller_list[1].set_authority([(1,True), (2, False), (3, False), (4, False), (5, False)])
        self.track_controller_list[1].set_switch_positions([(1,True)])
        self.track_controller_list[1].set_occupancy([(1,True), (2, False), (3, False), (4, False), (5, False)])
        self.track_controller_list[1].set_railway_crossings([(1,True)])
        self.track_controller_list[1].set_light_colors([(1,True,True)])
        self.track_controller_list[1].set_statuses([(1,True), (2, False), (3, False), (4, False), (5, False)])
        self.track_controller_list[1].set_suggested_speed([(1,0b00011010), (2, 0b00100111), (3, 0b00010101),(4, 0b00010101), (5, 0b00010101)])
        self.track_controller_list[1].set_commanded_speed([(1,0b00000000), (2, 0b00000000), (3, 0b00000000), (4, 0b00010101), (5, 0b00010101)])
        self.track_controller_list[1].set_speed_limit([(1,0b000100000), (2, 0b00000100), (3, 0b00100000),(4, 0b00000101), (5, 0b100000001)])
        self.track_controller_list[1].set_PLC("track_controller/testPLCfile.txt")

        self.track_controller_list[0].set_wayside_id("RedLine A")
        self.track_controller_list[1].set_wayside_id(572)

    def get_track_control_instance(self, wid):
        for wayside in self.track_controller_list:
            if str(wayside.get_wayside_id()) == wid:
                return wayside

    def get_names_of_controllers(self):
        return [self.track_controller_list[0].get_wayside_id(), self.track_controller_list[1].get_wayside_id()]

    def add_new_wayside_controller(self, wayside):
        self.track_controller_list.append(wayside)

    def Run_All_Track_Controllers_PLC(self):
        for wayside in self.track_controller_list:
            if(not(wayside.get_maintenance_mode())):
                wayside.ParsePLC()
                print("run")
    def get_all_track_controllers(self):
        return self.track_controller_list
     