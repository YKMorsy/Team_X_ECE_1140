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
    
    def get_widget(self):
        return self.Track_Model
    
    def get_commanded_speed_dict(self):
        out = {}
        i = 0
        out.update({"YARDR" : self.ui.track_list[226].get_commanded_speed()})
        out.update({"YARDG" : self.ui.track_list[227].get_commanded_speed()})
        while i < 150:
            store_block_num = str(i + 1)
            new_key = store_block_num + "G"
            out.update({new_key : self.ui.track_list[i].get_commanded_speed()})
            i += 1
        i = 150
        j = 1
        while i < 226 :
            new_key = str(j) + "R"
            out.update({new_key : self.ui.track_list[i].get_commanded_speed()})
            i += 1
            j += 1
        return out 
    def get_authority_dict(self):
        out = {}
        i = 0
        out.update({"YARDR" : self.ui.track_list[226].get_authority()})
        out.update({"YARDG" : self.ui.track_list[227].get_authority()})
        while i < 150:
            store_block_num = str(i + 1)
            new_key = store_block_num + "G"
            out.update({new_key : self.ui.track_list[i].get_authority()})
            i += 1
        i = 150
        j = 1
        while i < 226 :
            new_key = str(j) + "R"
            out.update({new_key : self.ui.track_list[i].get_authority()})
            i += 1
            j += 1
        return out
    
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

    def clear_block_failure(self,block_number):
        self.ui.track_list[block_number].clear_failure()

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
        for key in auth_dic:
            temp = key
            if temp == 1000:
                if auth_dic[key] == True:
                    self.ui.track_list[227].set_authority()
                else:
                    self.ui.track_list[227].reset_authority()
            if temp == 2000:
                if auth_dic[key] == True:
                    self.ui.track_list[226].set_authority()
                else:
                    self.ui.track_list[226].reset_authority()
            if temp > 2000:
                temp -= 2000
                if auth_dic[key] == True:
                    self.ui.track_list[149 + temp].set_authority()
                else:
                    self.ui.track_list[149 + temp].reset_authority()
            if (temp > 1000) and (temp < 2000):
                temp -= 1000
                if auth_dic[key] == True:
                    self.ui.track_list[temp - 1].set_authority()
                else:
                    self.ui.track_list[temp - 1].reset_authority()

        # print(self.ui.track_list[62].get_authority())
        # self.train_model.set_authority(self.get_authority_dict())            

    def set_switch_position(self,sw_dic):
        for key in sw_dic:
            temp = key
            if temp == 1000:
                if sw_dic[key] == True:
                    self.ui.track_list[227].set_switch()
                else:
                    self.ui.track_list[227].reset_switch()
            if temp == 2000:
                if sw_dic[key] == True:
                    self.ui.track_list[226].set_switch()
                else:
                    self.ui.track_list[226].reset_switch()
            if temp > 2000:
                temp -= 2000
                if sw_dic[key] == True:
                    self.ui.track_list[149 + temp].set_switch()
                else:
                    self.ui.track_list[149 + temp].reset_switch()
            if (temp > 1000) and (temp < 2000):
                temp -= 1000
                if sw_dic[key] == True:
                    self.ui.track_list[temp - 1].set_switch()
                else:
                    self.ui.track_list[temp - 1].reset_switch()

    def set_commanded_speed(self,com_dic):
        for key in com_dic:
            temp = key
            if temp == 1000:
                self.ui.track_list[227].set_commanded_speed(com_dic[key])
            
            if temp == 2000:
                    self.ui.track_list[226].set_commanded_speed(com_dic[key])
            if temp > 2000:
                temp -= 2000
                self.ui.track_list[149 + temp].set_commanded_speed(com_dic[key])
            if (temp > 1000) and (temp < 2000):
                temp -= 1000
                self.ui.track_list[temp - 1].set_commanded_speed(com_dic[key])



    def set_lights(self, lights_dic):
        for key in lights_dic:
            temp = key
            if temp == 1000:
                if lights_dic[key] == True:
                    self.ui.track_list[227].lights = 1
                else:
                    self.ui.track_list[227].lights = 0
            if temp == 2000:
                if lights_dic[key] == True:
                    self.ui.track_list[226].lights = 1
                else:
                    self.ui.track_list[226].lights = 0
            if temp > 2000:
                temp -= 2000
                if lights_dic[key] == True:
                    self.ui.track_list[149 + temp].lights = 1
                else:
                    self.ui.track_list[149 + temp].lights = 0
            if temp > 1000 and temp < 2000:
                temp -= 1000
                if lights_dic[key] == True:
                    self.ui.track_list[temp - 1].lights = 1
                else:
                    self.ui.track_list[temp - 1].lights = 0

    def set_crossings(self, cr_dic):
        for key in cr_dic:
            temp = key
            if temp == 1019 :
                if cr_dic[key] == True:
                    self.ui.track_list[18].crossing_status = 1
                else:
                    self.ui.track_list[18].crossing_status = 0
            if temp == 2047 :
                if cr_dic[key] == True:
                    self.ui.track_list[196].crossing_status = 1
                else:
                    self.ui.track_list[196].crossing_status = 0
                
    
    def set_train_status(self, train):
        line = train.line_name
        if line.upper() == "GREEN":
            mr_block = train.most_recent_block
            if mr_block == "YARD":
                block_number = 228
            else:
                block_number = int(train.most_recent_block)
            if train.current_distance_in_block >=  32 and train.current_distance_in_block <= (self.get_green_line_block_len(block_number)) : 
                store_curr = self.ui.track_list[block_number - 1].name
                curr_block = store_curr[1:]
                train.event_distance_in_block = self.get_green_line_block_len(block_number) 
                mr1_block = train.block_list[0]
                if mr1_block == "YARD":
                    last_block = 228
                else:
                    last_block = int(train.block_list[0])
                self.reset_green_line_occupancy(last_block)
                if mr_block == "YARD":
                    train.commanded_speed = self.get_green_line_commanded_speed(228 )
                else:
                    train.commanded_speed = self.get_green_line_commanded_speed(int(curr_block) )
                list1 = [] 
                list1.append(train.most_recent_block)
                train.block_list = list1
                return 0
            else:
                train.current_distance_in_block -= train.event_distance_in_block
                train.event_distance_in_block = 32
                if mr_block == "YARD":
                    block_number = 228
                else:
                    block_number = int(train.most_recent_block)
                next_block = self.ui.track_list[block_number - 1].get_next_block_green(train,self.ui.track_list)
                if next_block.upper() == "YARD":
                    self.ui.track_list[55].reset_occupancy()
                    self.ui.track_list[56].reset_occupancy()
                    self.ui.track_list[227].reset_occupancy()
                    return -1
                curr_block = next_block[1:]
                train.block_list.append(curr_block)
                train.most_recent_block = curr_block
                new_block = int(curr_block)
                train.commanded_speed = self.get_green_line_commanded_speed(new_block )
                if train.direction:
                    train.current_grade = self.get_green_line_grade(new_block)
                else: 
                    train.current_grade = 0 - self.get_green_line_grade(new_block)
                self.ui.track_list[new_block - 1].set_occupancy()
                train.commanded_authority = "True" if self.get_green_line_authority(new_block) else "False"
                train.beacon_data = self.ui.track_list[new_block -1].get_beacon()


                return 0
                
        else:
            mr_block = train.most_recent_block
            if mr_block == "YARD":
                block_number = 77
            else:
                block_number = int(train.most_recent_block)
            if train.current_distance_in_block >=  32 and train.current_distance_in_block < self.get_red_line_block_len(block_number) : 
                store_curr = self.ui.track_list[block_number + 149].name
                curr_block = store_curr[1:]
                train.event_distance_in_block = self.get_red_line_block_len(block_number)
                mr1_block = train.block_list[0]
                if mr1_block == "YARD":
                    last_block = 77
                else:
                    last_block = int(train.block_list[0])
                if mr_block == "YARD":
                    train.commanded_speed = self.get_red_line_commanded_speed(77 )
                else:
                    train.commanded_speed = self.get_red_line_commanded_speed(last_block )

                self.reset_red_line_occupancy(last_block)
                list1 = [] 
                list1.append(train.most_recent_block)
                train.block_list = list1
                return 0
            else:
                train.current_distance_in_block -= train.event_distance_in_block
                train.event_distance_in_block = 32

                if mr_block == "YARD":
                    block_number = 77 
                else:
                    block_number = int(train.most_recent_block)
                next_block = self.ui.track_list[block_number + 149].get_next_block_red(train,self.ui.track_list)
                if next_block.upper() == "YARD":
                    self.ui.track_list[157].reset_occupancy()
                    self.ui.track_list[158].reset_occupancy()
                    return -1
                curr_block = next_block[1:]
                train.most_recent_block = curr_block
                train.block_list.append(curr_block)
                new_block = int(curr_block)
                if train.direction:
                    train.current_grade = self.get_red_line_grade(new_block)
                else: 
                    train.current_grade = 0 - self.get_red_line_grade(new_block)
                self.ui.track_list[new_block + 149 ].set_occupancy()
                train.commanded_authority = "True" if self.get_red_line_authority(new_block) else "False"
                train.beacon_data = self.ui.track_list[new_block + 149].get_beacon()
                return 0

    def get_speed(self, train):
        line = train.line_name
        if line.upper() == "GREEN":
            mr_block = train.most_recent_block
            if mr_block == "YARD":
                block_number = 228
            else:
                block_number = int(train.most_recent_block)
            mr1_block = train.block_list[0]
            if mr1_block == "YARD":
                bl_number = 228
            else:
                bl_number = int(train.block_list[0])
            if self.get_green_line_commanded_speed(block_number) > 0 and self.get_green_line_commanded_speed(block_number) < 2:
                train.commanded_speed = self.get_green_line_commanded_speed(block_number)
            elif self.get_green_line_commanded_speed(block_number) < self.get_green_line_commanded_speed(bl_number):
                train.commanded_speed = self.get_green_line_commanded_speed(bl_number)
            elif block_number == 101 or block_number == 77 or block_number == 55: 
                train.commanded_speed = 40
            else:
                train.commanded_speed = self.get_green_line_commanded_speed(block_number)
            #print(self.get_green_line_commanded_speed(block_number))
        else:
            mr_block = train.most_recent_block
            if mr_block == "YARD":
                block_number = 77
            else:
                block_number = int(train.most_recent_block)
            mr1_block = train.block_list[0]
            if mr1_block == "YARD":
                bl_number = 77
            else:
                bl_number = int(train.block_list[0])
            if self.get_red_line_commanded_speed(block_number) > 0 and self.get_red_line_commanded_speed(block_number) < 2:
                train.commanded_speed = self.get_red_line_commanded_speed(block_number)
            elif self.get_red_line_commanded_speed(block_number) < self.get_red_line_commanded_speed(bl_number):
                train.commanded_speed = self.get_red_line_commanded_speed(bl_number)
            else:
                train.commanded_speed = self.get_red_line_commanded_speed(block_number)
  
    # sys.exit(app.exec_())

   