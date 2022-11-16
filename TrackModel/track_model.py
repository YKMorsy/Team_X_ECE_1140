import sys
import TrackModel.station as station
from PyQt5 import QtCore, QtGui, QtWidgets

import TrackModel.track_builder as track_builder


class track_model(object):
    app = QtWidgets.QApplication(sys.argv)
    Track_Model = QtWidgets.QMainWindow()
    ui = track_builder.Ui_Track_Model()
    ui.setupUi(Track_Model)
    Track_Model.show()
    stations = station.station()
    def get_occupancy_0(self):
        red_line_occupancy = {}
        i = 150
        j = 1000
        while i < :
            red_line_occupancy.append(self.ui.track_list[i].get_occupancy())
            i += 1
        return red_line_occupancy
    
    def get_occupancy_1(self):
        i = 150
        
    def get_occupancy_2(self):
        i = 150
        
    def get_occupancy_3(self):
        i = 150
        
    def get_occupancy_4(self):
        i = 150 
        
    def get_occupancy_5(self):
        green_line_occupancy = []
        i = 0
        while i < 150 :
            green_line_occupancy.append(self.ui.track_list[i].get_occupancy())
            i += 1
        return green_line_occupancy
    
    def get_fault_0(self):
        1 = 150
    
    def get_fault_1(self):
        i = 150
        
    def get_fault_2(self):
        i = 150
        
    def get_fault_3(self):
        i = 150
        
    def get_fault_4(self):
        i = 150
        
    def get_fault_5(self):
        i = 150
        
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
    
    def set_train_status(self, train):
        if train.line_name == "GREEN":
            if train.current_distance_in_block >=  32 and train.current_distance_in_block < self.get_green_line_block_len(train.most_recent_block) : 
                train.block_list.append(self.ui.track_list[train.most_recent_block].get_next_block())
                train.event_distance_in_block = self.get_green_line_block_len(train.most_recent_block)
                last_block = train.block_list[0]
                self.reset_green_line_occupancy(last_block)
                list1 = [] 
                list1.append(train.most_recent_block)
                train.block_list = list1
            else:
                
                
                train.event_distance_in_block = 32
                if train.direction:
                    train.current_grade = self.get_green_line_grade(train.most_recent_block)
                else: 
                    train.current_grade = 0 - self.get_green_line_grade(train.most_recent_block)
                train.commanded_authority = self.get_green_line_authority(train.most_recent_block)
                train.commanded_speed = self.get_green_line_commanded_speed(train.most_recent_block)
                train.beacon_info = self.get_green_line_above_below_ground(train.most_recent_block)
                
        else:
            if train.current_distance_in_block >=  32 and train.current_distance_in_block < self.get_red_line_block_len(train.most_recent_block) : 
                list1 = [] 
                list1.append(train.most_recent_block)
                last_block = train.block_list[0]
                self.reset_red_line_occupancy(last_block)
                train.block_list.append(self.ui.track_list[train.most_recent_block].get_next_block())
                
                train.block_list = list1
                train.event_distance_in_block = self.get_red_line_block_len(train.most_recent_block)
            else:
                
                train.event_distance_in_block = 32
                if train.direction:
                    train.current_grade = self.get_red_line_grade(train.most_recent_block)
                else:
                    train.current_grade = 0 - self.get_red_line_grade(train.most_recent_block)
                train.commanded_authority = self.get_red_line_authority(train.most_recent_block)
                train.commanded_speed = self.get_red_line_commanded_speed(train.most_recent_block)
                train.beacon_info = self.get_red_line_above_below_ground(train.most_recent_block)
                
            
            
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
        
    
    sys.exit(app.exec_())

   