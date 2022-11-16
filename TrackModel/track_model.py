import sys
import TrackModel.station as station
from PyQt5 import QtCore, QtGui, QtWidgets

import TrackModel.track_builder as track_builder


class track_model(object):

    def __init__(self):
        self.Track_Model = QtWidgets.QMainWindow()
        self.ui = track_builder.Ui_Track_Model()
        self.ui.setupUi(self.Track_Model)
        self.stations = station.station()

    def show(self):
        self.Track_Model.show()
    
    def get_red_line_occupancy(self):
        red_line_occupancy = []
        i = 150
        while i < len(self.ui.track_list):
            red_line_occupancy.append(self.ui.track_list[i].get_occupancy())
            i += 1
        return red_line_occupancy
        
    def get_green_line_occupancy(self):
        green_line_occupancy = []
        i = 0
        while i < 150 :
            green_line_occupancy.append(self.ui.track_list[i].get_occupancy())
            i += 1
        return green_line_occupancy
    
    def set_red_line_occupancy(self, loc):
        self.ui.track_list[loc + 149].set_occupancy()
    
    def set_green_line_occupancy(self, loc):
        self.ui.track_list[loc - 1].set_occupancy()
        
    def reset_red_line_occupancy(self, loc):
        self.ui.track_list[loc + 149].reset_occupancy()
    
    def reset_green_line_occupancy(self, loc):
        self.ui.track_list[loc - 1].reset_occupancy()
        
    def set_green_line_switch(self,loc):
        self.ui.track_list[loc - 1].set_switch()
    
    def set_red_line_switch(self,loc):
        self.ui.track_list[loc + 149].set_switch()
    
    def reset_green_line_switch(self,loc):
        self.ui.track_list[loc - 1].reset_switch()
        
    def reset_green_line_switch(self,loc):
        self.ui.track_list[loc + 149].reset_switch()
    
    def set_green_line_commanded_speed(self,loc,sp):
        self.ui.track_list[loc - 1].set_commanded_speed(sp)
        
    def set_red_line_commanded_speed(self,loc,sp):
        self.ui.track_list[loc + 149].set_commanded_speed(sp)
        
    def get_green_line_commanded_speed(self,loc):
        return self.ui.track_list[loc - 1].get_commanded_speed()
    
    def get_red_line_commanded_speed(self,loc):
        return self.ui.track_list[loc + 149].get_commanded_speed()
    
    def get_green_line_above_below_ground(self,loc):
        return self.ui.track_list[loc - 1].get_underground()
    
    def get_red_line_above_below_ground(self, loc):
        return self.ui.track_list[loc + 149].get_underground()
    
    def get_green_line_block_len(self, loc):
        return self.ui.track_list[loc - 1].get_length()
    
    def get_red_line_block_len(self, loc):
        return self.ui.track_list[loc + 149].get_length()
    
    def get_green_line_grade(self, loc):
        return self.ui.track_list[loc - 1].get_grade()
    
    def get_red_line_grade(self, loc):
        return self.ui.track_list[loc + 149].get_grade()
    
    def get_passengers(self,cap):
        return self.stations.get_passengers(cap)
    
    def get_throughput(self):
        return self.stations.get_throughput()
    
    def get_red_line_circuit_status(self):
        i = 150
        red_line_circuit = []
        while i < len(self.ui.track_list):
            red_line_circuit.append(self.ui.track_list[i].get_circuit_failure())
            i += 1
        return red_line_circuit
    
    def get_red_line_rail_status(self):
        i = 150
        red_line_rail = []
        while i < len(self.ui.track_list):
            red_line_rail.append(self.ui.track_list[i].get_rail_failure())
            i += 1
        return red_line_rail
    
    def get_red_line_power_status(self):
        i = 150
        red_line_power = []
        while i < len(self.ui.track_list):
            red_line_power.append(self.ui.track_list[i].get_pow_failure())
            i += 1
        return red_line_power
    
    def get_green_line_circuit_status(self):
        i = 0
        red_line_circuit = []
        while i < 150:
            red_line_circuit.append(self.ui.track_list[i].get_circuit_failure())
            i += 1
        return red_line_circuit
    
    def get_green_line_rail_status(self):
        i = 0
        red_line_rail = []
        while i < 150:
            red_line_rail.append(self.ui.track_list[i].get_rail_failure())
            i += 1
        return red_line_rail
    
    def get_green_line_power_status(self):
        i = 0
        red_line_power = []
        while i < 150:
            red_line_power.append(self.ui.track_list[i].get_pow_failure())
            i += 1
        return red_line_power
    
    def clear_failures(self):
        self.ui.clear_failure()
    
    def set_green_line_authority(self,loc):
        self.ui.track_list[loc -1].set_authority()
        
    def reset_green_line_authority(self, loc):
        self.ui.track_list[loc - 1].reset_authority()
        
    def get_green_line_authority(self, loc):
        return self.ui.track_list[loc -1].get_authority()
    
    def set_red_line_authority(self,loc):
        self.ui.track_list[loc + 149].set_authority()
        
    def reset_red_line_authority(self, loc):
        self.ui.track_list[loc + 149].reset_authority()
        
    def get_red_line_authority(self, loc):
        return self.ui.track_list[loc + 149].get_authority()

    def get_occupancy_0(self):
        out = {}
        out.update({2000 : self.ui.track_list[226].get_occupancy()})
        i = 150
        j = 2001
        
        while i < 174:
            out.update({j : self.ui.track_list[i].get_occupancy()})
            i += 1
            j += 1
        return out

    def get_occupancy_1(self):
        out = {}
        
        i = 172
        j = 2023
        
        while i < 196:
            out.update({j : self.ui.track_list[i].get_occupancy()})
            i += 1
            j += 1
        i = 216
        j = 2067
        
        while i < 226:
            out.update({j : self.ui.track_list[i].get_occupancy()})
            i += 1
            j += 1
        return out
    def get_occupancy_2(self):
        out = {}
        
        i = 194
        j = 2045
        
        while i < 216:
            out.update({j : self.ui.track_list[i].get_occupancy()})
            i += 1
            j += 1
        return out

    def get_occupancy_3(self):
        out = {}
        
        i = 0
        j = 1001
        
        while i < 24:
            out.update({j : self.ui.track_list[i].get_occupancy()})
            i += 1
            j += 1
        return out

    def get_occupancy_4(self):
        out = {}
        
        i = 19
        j = 1020
        
        while i < 36:
            out.update({j : self.ui.track_list[i].get_occupancy()})
            i += 1
            j += 1
        
        i = 103
        j = 1104
        while i < 150:
            out.update({j : self.ui.track_list[i].get_occupancy()})
            i += 1
            j += 1
            
        return out
    def get_occupancy_5(self):
        out = {}
        
        i = 34
        j = 1000
        out.update({j : self.ui.track_list[227].get_occupancy()})
        j = 1035
        while i < 105:
            out.update({j : self.ui.track_list[i].get_occupancy()})
            i += 1
            j += 1
        return out

    def get_fault_0(self):
        out = {}
        out.update({2000 : self.ui.track_list[226].controller_fault_status()})
        i = 150
        j = 2001
        
        while i < 174:
            out.update({j : self.ui.track_list[i].controller_fault_status()})
            i += 1
            j += 1
        return out

    def get_fault_1(self):
        out = {}
        
        i = 172
        j = 2023
        
        while i < 196:
            out.update({j : self.ui.track_list[i].controller_fault_status()})
            i += 1
            j += 1
        i = 216
        j = 2067
        
        while i < 226:
            out.update({j : self.ui.track_list[i].controller_fault_status()})
            i += 1
            j += 1
        return out

    def get_fault_2(self):
        out = {}
        
        i = 194
        j = 2045
        
        while i < 216:
            out.update({j : self.ui.track_list[i].controller_fault_status()})
            i += 1
            j += 1
        return out

    def get_fault_3(self):
        out = {}
        
        i = 0
        j = 1001
        
        while i < 24:
            out.update({j : self.ui.track_list[i].controller_fault_status()})
            i += 1
            j += 1
        return out

    def get_fault_4(self):
        out = {}
        
        i = 19
        j = 1020
        
        while i < 36:
            out.update({j : self.ui.track_list[i].controller_fault_status()})
            i += 1
            j += 1
        
        i = 103
        j = 1104
        while i < 150:
            out.update({j : self.ui.track_list[i].controller_fault_status()})
            i += 1
            j += 1
            
        return out

    def get_fault_5(self):
        out = {}
        
        i = 34
        j = 1000
        out.update({j : self.ui.track_list[227].controller_fault_status()})
        j = 1035
        while i < 105:
            out.update({j : self.ui.track_list[i].controller_fault_status()})
            i += 1
            j += 1
        return out

    def set_total_authority(self, auth_dic):
        i = 1

    def set_switch_position(self,sw_dic):
        i = 1

    def set_commanded_speed(self,com_dic):
        i = 1

    def set_lights(self, lights_dic):
        i = 1

    def set_crossings(self, cr_dic):
        i = 1
    
        
    # sys.exit(app.exec_())

   