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
    def test_switch_16_False_occ16_auth1(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Top Red")
        way.set_an_auth(2001, True)
        way.set_an_occ(2016, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2016), False)
        self.assertEqual(way.get_a_comm_speed(2016), way.get_a_comm_speed(2016))

    def test_switch_16_True_occ16_auth15(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Top Red")
        way.set_an_auth(2015, True)
        way.set_an_occ(2016, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2016), True)
        self.assertEqual(way.get_a_comm_speed(2016), way.get_a_comm_speed(2016))

    def test_switch_9_False_from_yard(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Top Red")
        way.set_an_auth(2009, True)
        way.set_an_occ(2000, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2000), False)
        self.assertEqual(way.get_a_comm_speed(2000), way.get_a_comm_speed(2000))

    def test_switch_9_False_to_yard(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Top Red")
        way.set_an_auth(2000, True)
        way.set_an_occ(2009, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2000), False)
        self.assertEqual(way.get_a_comm_speed(2009), way.get_a_comm_speed(2009))

    def test_switch_9_True_to_10(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Top Red")
        way.set_an_auth(2010, True)
        way.set_an_occ(2009, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2000), False)
        self.assertEqual(way.get_a_comm_speed(2009), way.get_a_comm_speed(2009))
    def test_switch_9_False_from_10(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Top Red")
        way.set_an_auth(2009, True)
        way.set_an_occ(2010, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2000), False)
        self.assertEqual(way.get_a_comm_speed(2010), way.get_a_comm_speed(2010))
    def test_light(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Top Red")
        way.set_an_auth(2016, True)
        way.set_an_occ(2017, True)
        way.parse_plc()
        self.assertEqual(way.get_a_light(2017), [True, True])

#________________________MIDDLE-BLUE___________________________
    def test_switch_27_False_1(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Middle Blue")
        way.set_an_auth(2028, True)
        way.set_an_occ(2027, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2027), False)
        self.assertEqual(way.get_a_comm_speed(2027), way.get_a_comm_speed(2027))

    def test_switch_27_False_2(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Middle Blue")
        way.set_an_auth(2027, True)
        way.set_an_occ(2028, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2027), False)
        self.assertEqual(way.get_a_comm_speed(2028), way.get_a_comm_speed(2028))
    def test_switch_27_True_1(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Middle Blue")
        way.set_an_auth(2076, True)
        way.set_an_occ(2027, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2027), True)
        self.assertEqual(way.get_a_comm_speed(2027), way.get_a_comm_speed(2027))

    def test_switch_27_True_2(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Middle Blue")
        way.set_an_auth(2027, True)
        way.set_an_occ(2076, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2027), True)
        self.assertEqual(way.get_a_comm_speed(2076), way.get_a_comm_speed(2076))
#_______________________BOTTOM-YELLOW__________________________
    def test_switch_52_False_1(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Bottom Yellow")
        way.set_an_auth(2053, True)
        way.set_an_occ(2052, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2052), False)
        self.assertEqual(way.get_a_comm_speed(2052), way.get_a_comm_speed(2052))

    def test_switch_52_False_2(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Bottom Yellow")
        way.set_an_auth(2052, True)
        way.set_an_occ(2053, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2052), False)
        self.assertEqual(way.get_a_comm_speed(2053), way.get_a_comm_speed(2053))

    def test_switch_52_True_1(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Bottom Yellow")
        way.set_an_auth(2066, True)
        way.set_an_occ(2052, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2052), True)
        self.assertEqual(way.get_a_comm_speed(2052), way.get_a_comm_speed(2052))

    def test_switch_52_True_2(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Bottom Yellow")
        way.set_an_auth(2052, True)
        way.set_an_occ(2066, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2052), True)
        self.assertEqual(way.get_a_comm_speed(2066), way.get_a_comm_speed(2066))

if __name__ == '__main__':
    unittest.main()