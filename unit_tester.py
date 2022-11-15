import unittest
import track_block
import sys
import numpy as np


class unit_tester(unittest.TestCase):
    track_list = np.empty(15,track_block.block)
    block1 = track_block.block("Blue Line","A1",0,0,50,"none",50,"A2","A2")
    block2 = track_block.block("Blue Line","A2",0,0,50,"none",50,"A3","A3")
    block3 = track_block.block("Blue Line","A3",0,0,50,"none",50,"A4","A4")
    block4 = track_block.block("Blue Line","A4",0,0,50,"none",50,"A5","A5")
    block5 = track_block.block("Blue Line","A5",0,0,50,"none",50,"B6","C11")
    block6 = track_block.block("Blue Line","B6",0,0,50,"none",50,"B7","A5")
    block7 = track_block.block("Blue Line","B7",0,0,50,"none",50,"B8","B8")
    block8 = track_block.block("Blue Line","B8",0,0,50,"none",50,"B9","B9")
    block9 = track_block.block("Blue Line","B9",0,0,50,"none",50,"B10","B10")
    block10 = track_block.block("Blue Line","B10",0,0,50,"Station B",50,"none","none")
    block11 = track_block.block("Blue Line","C11",0,0,50,"none",50,"C12","A5")
    block12 = track_block.block("Blue Line","C12",0,0,50,"none",50,"C13","C13")
    block13 = track_block.block("Blue Line","C14",0,0,50,"none",50,"C14","C14")
    block14 = track_block.block("Blue Line","C14",0,0,50,"none",50,"C15","C15")
    block15 = track_block.block("Blue Line","C15",0,0,50,"Station C",50,"none","none")
    track_list[0] = block1
    track_list[1] = block2
    track_list[2] = block3
    track_list[3] = block4
    track_list[4] = block5
    track_list[5] = block6
    track_list[6] = block7
    track_list[7] = block8
    track_list[8] = block9
    track_list[9] = block10
    track_list[10] = block11
    track_list[11] = block12
    track_list[12] = block13
    track_list[13] = block14
    track_list[14] = block15
    
    def test_circuit_fault(self):
        tester = self.track_list[1].toggle_fault_circuit()
        self.assertEqual(tester, 1)
        self.track_list[1].clear_failure()
        tester = self.track_list[1].get_circuit_failure()
        self.assertEqual(tester, 0)
    
    def test_occupancy(self):
        tester = self.track_list[4].toggle_occupancy()
        self.assertEqual(tester , 1)
        tester = self.track_list[4].toggle_occupancy()
        self.assertEqual(tester , 0)
        
    def test_switch(self):
        tester = self.track_list[5].toggle_switch()
        self.assertEqual(tester , 1)
        tester = self.track_list[5].toggle_switch()
        self.assertEqual(tester , 0)

if __name__ == '__main__':
    unittest.main()