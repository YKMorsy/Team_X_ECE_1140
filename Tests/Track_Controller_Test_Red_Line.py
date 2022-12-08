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
        self.assertEqual(way.get_a_comm_speed(2016), 0b00100000)

    def test_switch_16_True_occ16_auth15(self):
        controller = track_control_controller()
        way = controller.get_track_control_instance("RedLine Top Red")
        way.set_an_auth(2015, True)
        way.set_an_occ(2016, True)
        way.parse_plc()
        self.assertEqual(way.get_a_switch(2016), True)
        self.assertEqual(way.get_a_comm_speed(2016), 0b00100000)
#________________________MIDDLE-BLUE___________________________
#_______________________BOTTOM-YELLOW__________________________

if __name__ == '__main__':
    unittest.main()