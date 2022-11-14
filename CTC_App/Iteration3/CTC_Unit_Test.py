import unittest
from Iteration3.CTC_old import CTC

class Test_CTC(unittest.TestCase):
    def test_add_track(self):
        ctc_test = CTC()
        ctc_test.add_track("Iteration3/Track_Layout_Blue.xlsx")
        self.assertEqual(ctc_test.get_authority(), [(1001, True), (1002, True), (1003, True), (1004, True), (1005, True), (1006, True), 
                                                    (1007, True), (1008, True), (1009, True), (1010, True), (1011, False), (1012, True), 
                                                    (1013, True), (1014, True), (1015, True)])

    def test_set_fault_status(self):
        ctc_test = CTC()
        ctc_test.add_track("Iteration3/Track_Layout_Blue.xlsx")
        ctc_test.set_fault_status([(1003, True)])
        self.assertEqual(ctc_test.get_authority(), [(1001, True), (1002, True), (1003, False), (1004, True), (1005, True), (1006, True), 
                                                    (1007, True), (1008, True), (1009, True), (1010, True), (1011, False), (1012, True), 
                                                    (1013, True), (1014, True), (1015, True)])

    def test_set_switch_position(self):
        ctc_test = CTC()
        ctc_test.add_track("Iteration3/Track_Layout_Blue.xlsx")
        ctc_test.set_switch_position([(1005, True)])
        self.assertEqual(ctc_test.get_authority(), [(1001, True), (1002, True), (1003, True), (1004, True), (1005, True), (1006, False), 
                                                    (1007, True), (1008, True), (1009, True), (1010, True), (1011, True), (1012, True), 
                                                    (1013, True), (1014, True), (1015, True)])

if __name__ == '__main__':
    unittest.main()