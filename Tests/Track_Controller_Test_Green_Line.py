import unittest
#from track_controller import WaysideController
import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)
 
# now we can import the module in the parent
# directory.
from track_controller.track_control_controller import track_control_controller 

class TestTrackController(unittest.TestCase):
    #________________________TOP-RED___________________________
    def test_switch_13_True_occ13_auth12(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("GreenLine Top Red")
        way.set_an_auth(1012, True)
        way.set_an_occ(1013, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(1013), True)
        self.assertEqual(way.get_a_comm_speed(1013), 0b00100000)

    def test_switch_13_False(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("GreenLine Top Red")
        way.set_an_auth(1013, True)
        way.set_an_occ(1001, True)
        way.parse_plc()
        self.assertEqual(way.get_a_light(1001), [True, True])
        self.assertEqual(way.get_a_switch(1013), False)
        self.assertEqual(way.get_a_comm_speed(1001), 0b00100000)
    def test_crossing_19(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Top Red")
            way.set_an_occ(1019, True)
            way.parse_plc()
            self.assertEqual(way.get_a_rail_cross(1019), True)
    def test_crossing_18(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Top Red")
            way.set_an_occ(1018, True)
            way.parse_plc()
            self.assertEqual(way.get_a_rail_cross(1019), True)
    def test_crossing_20(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Top Red")
            way.set_an_occ(1020, True)
            way.parse_plc()
            self.assertEqual(way.get_a_rail_cross(1019), True)
#_______________________MIDDLE-YELLOW__________________________
    def test_switch_29_False(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Middle Yellow")
            way.set_an_auth(1030, True)
            way.set_an_occ(1029, True)
            way.parse_plc()
            self.assertEqual(way.get_a_switch(1029), False)
            self.assertEqual(way.get_a_comm_speed(1029), way.get_a_speed_lim(1029))
    def test_switch_29_True(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Middle Yellow")
            way.set_an_auth(1029, True)
            way.set_an_occ(1150, True)
            way.parse_plc()
            #self.assertEqual(way.get_a_switch(1029), True)
            #self.assertEqual(way.get_a_comm_speed(1150), way.get_a_speed_lim(1150))
#________________________BOTTOM-BLUE___________________________
    def test_switch_77_True(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Bottom Blue")
            way.set_an_auth(1101, True)
            way.set_an_occ(1077, True)
            way.parse_plc()
            self.assertEqual(way.get_a_switch(1077), True)
            self.assertEqual(way.get_a_comm_speed(1077), way.get_a_sug_speed(1077))
    def test_switch_77_False(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Bottom Blue")
            way.set_an_auth(1077, True)
            way.set_an_occ(1076, True)
            way.parse_plc()
            self.assertEqual(way.get_a_switch(1077), False)
            self.assertEqual(way.get_a_comm_speed(1076), way.get_a_sug_speed(1076))
    def test_switch_85_False(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Bottom Blue")
            way.set_an_auth(1086, True)
            way.set_an_occ(1085, True)
            way.parse_plc()
            self.assertEqual(way.get_a_switch(1085), False)
            self.assertEqual(way.get_a_comm_speed(1085), way.get_a_sug_speed(1085))
    def test_switch_85_True(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Bottom Blue")
            way.set_an_auth(1085, True)
            way.set_an_occ(1100, True)
            way.parse_plc()
            self.assertEqual(way.get_a_switch(1085), True)
            self.assertEqual(way.get_a_comm_speed(1100), way.get_a_speed_lim(1100))
    def test_switch_57_False(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Bottom Blue")
            way.set_an_auth(1000, True)
            way.set_an_occ(1057, True)
            way.parse_plc()
            self.assertEqual(way.get_a_switch(1057), False)
            self.assertEqual(way.get_a_comm_speed(1057), way.get_a_speed_lim(1057))
    def test_switch_57_True(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Bottom Blue")
            way.set_an_auth(1058, True)
            way.set_an_occ(1057, True)
            way.parse_plc()
            self.assertEqual(way.get_a_switch(1057), True)
            self.assertEqual(way.get_a_comm_speed(1057), way.get_a_speed_lim(1057))
    def test_switch_63_False(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Bottom Blue")
            way.set_an_auth(1063, True)
            way.set_an_occ(1000, True)
            way.parse_plc()
            self.assertEqual(way.get_a_switch(1063), False)
            self.assertEqual(way.get_a_comm_speed(1000), way.get_a_sug_speed(1000))
    def test_switch_63_True(self):
            controller = track_control_controller()
            way = controller.get_track_control_instance("GreenLine Bottom Blue")
            way.set_an_auth(1063, True)
            way.set_an_occ(1062, True)
            way.parse_plc()
            self.assertEqual(way.get_a_switch(1063), True)
            self.assertEqual(way.get_a_comm_speed(1062), way.get_a_speed_lim(1062))


if __name__ == '__main__':
    unittest.main()