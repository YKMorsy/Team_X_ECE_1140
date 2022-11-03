import unittest
from track_controller import WaysideController

class TestTrackController(unittest.TestCase):

    #note these tests represent a track that looks like:
    # -<    the left is block one the top one is block 3 and the bottom is block 2
    #when trhe switch is down it is 0, up is 1

    def test_SwitchIsFalseWhenComingFromLowerTrack(self):
        way = WaysideController()
        way.set_authority([(1,True), (2, False), (3, False)])
        way.set_switch_positions([(1,True)])
        way.set_occupancy([(1,False), (2, True), (3, False)])
        way.set_railway_crossings([(1,False)])
        way.set_light_colors([(1,True,True)])
        way.set_statuses([(1,True), (2, True), (3, True)])
        way.set_suggested_speed([(1,0b00011010), (2, 0b00100111), (3, 0b00010101)])
        way.set_commanded_speed([(1,0b000001000), (2, 0b01000000), (3, 0b00001000)])
        way.set_speed_limit([(1,0b000100000), (2, 0b00010000), (3, 0b00010000)])
        way.set_PLC("TestingPLC.txt")

        way.ParsePLC()
        self.assertEqual(way.get_switch_positions(), [(1,False)])

    def test_SwitchIsTrueWhenComingFromLeftTrack(self):
        way = WaysideController()
        way.set_authority([(1,False), (2, False), (3, True)])
        way.set_switch_positions([(1,False)])
        way.set_occupancy([(1,True), (2, False), (3, False)])
        way.set_railway_crossings([(1,False)])
        way.set_light_colors([(1,True,True)])
        way.set_statuses([(1,True), (2, True), (3, True)])
        way.set_suggested_speed([(1,0b00011010), (2, 0b00100111), (3, 0b00010101)])
        way.set_commanded_speed([(1,0b000001000), (2, 0b01000000), (3, 0b00001000)])
        way.set_speed_limit([(1,0b000100000), (2, 0b00010000), (3, 0b00010000)])
        way.set_PLC("TestingPLC.txt")

        way.ParsePLC()
        self.assertEqual(way.get_switch_positions(), [(1,True)])
        
    def test_commandSpeedIsZeroWhenAuthorityAheadIsFalse (self):
        way = WaysideController()
        way.set_authority([(1,False), (2, False), (3, False)])
        way.set_switch_positions([(1,True)])
        way.set_occupancy([(1,False), (2, True), (3, False)])
        way.set_railway_crossings([(1,False)])
        way.set_light_colors([(1,True,True)])
        way.set_statuses([(1,True), (2, True), (3, True)])
        way.set_suggested_speed([(1,0b00011010), (2, 0b00100111), (3, 0b00010101)])
        way.set_commanded_speed([(1,0b000001000), (2, 0b01000000), (3, 0b00001000)])
        way.set_speed_limit([(1,0b000100000), (2, 0b00010000), (3, 0b00010000)])
        way.set_PLC("TestingPLC.txt")

        way.ParsePLC()
        self.assertEqual(way.get_commanded_speed(), [(1,0b000001000), (2, 0b0), (3, 0b00001000)])


if __name__ == '__main__':
    unittest.main()