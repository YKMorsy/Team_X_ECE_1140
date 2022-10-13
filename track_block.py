import numpy as np
import random
class block:
    line_name = "none"
    name = "none"
    length = 0
    grade = 0
    elevation = 0
    speed = 0
    occupancy = 0
    station = "none"
    crossing = 0
    switch = 0
    next_loc = "none"
    switch_forward_loc = "none"
    fault_rail = 0
    fault_cir = 0
    fault_pow = 0
    signal = np.array([0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    
    #default constructor
    def __init__(self,ln, n, g, e, s, st, len, nl, sw):
        self.line_name = ln
        self.name = n
        self.grade = g
        self.elevation = e
        self.speed = s
        self.station = st
        self.length = len
        self.next_loc = nl
        self.switch_forward_loc = sw
        
    def toggle_fault_rail(self):
        if self.fault_rail == 0:
            self.fault_rail = 1
            return 1
        else:
            self.fault_rail = 0
            return 0
    
    def toggle_fault_circuit(self):
        if self.fault_cir == 0:
            self.fault_cir = 1
            return 1
        else:
            self.fault_cir = 0
            return 0
    
    def toggle_fault_power(self):
        if self.fault_pow == 0:
            self.fault_pow = 1
            return 1
        else:
            self.fault_pow = 0
            return 0
    
    def toggle_occupancy(self):
        if self.occupancy == 0:
            self.occupancy = 1
            return 1
        else:
            self.occupancy = 0
            return 0
    
    def toggle_switch(self):
        if self.switch == 0:
            self.switch = 1
            return 1
        else:
            self.switch = 0
            return 0
    
    def get_length(self):
        return self.length
    
    def get_occupancy(self):
        return self.occupancy
    
    def get_elevation(self):
        return self.elevation
    
    def get_speed(self):
        return self.speed
    
    def get_station_name(self):
        return self.station
    
    def get_switch_forward_loc(self):
        return self.switch_forward_loc
    
    def get_grade(self):
        return self.grade
    
    def get_elevation(self):
        return self.elevation
    
    def get_block_name(self):
        return self.name
    
    def get_line_name(self):
        return self.line_name
    
    def get_crossing(self):
        return self.crossing
    
    def get_switch(self):
        return self.switch
    
    def get_next_loc(self):
        return self.next_loc
    
    def clear_failure(self):
        self.fault_cir = 0
        self.fault_pow = 0
        self.fault_rail = 0