from track_controller import WaysideController


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
        self.track_controller_list[0].set_PLC("track_controller/testPLCfile.txt")

        self.track_controller_list[1].set_authority([(1,True), (2, False), (3, False)])
        self.track_controller_list[1].set_switch_positions([(1,True), (2, True), (3, False)])
        self.track_controller_list[1].set_occupancy([(1,True), (2, True), (4, False)])
        self.track_controller_list[1].set_railway_crossings([(1,True), (2, True), (3, False)])
        self.track_controller_list[1].set_light_colors([(1,True,True), (5, True,True), (3, False,True)])
        self.track_controller_list[1].set_statuses([(1,True), (2, True), (3, True)])
        self.track_controller_list[1].set_PLC("track_controller/testPLCfile.txt")

        self.track_controller_list[0].set_wayside_id(232)
        self.track_controller_list[1].set_wayside_id(572)

    def get_track_control_instance(self, wid):
        for wayside in self.track_controller_list:
            if str(wayside.get_wayside_id()) == wid:
                return wayside

    def get_names_of_controllers(self):
        return [self.track_controller_list[0].get_wayside_id(), self.track_controller_list[1].get_wayside_id()]

