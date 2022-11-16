import numpy as np
import random
class block:
    line_name = "none"
    name = "none"
    length = 0.0
    grade = 0.0
    elevation = 0.0
    speed = 0
    occupancy = 0
    station = "none"
    crossing = 'n'
    crossing_status = 0
    switch = 0
    next_loc = "none"
    switch_forward_loc = "none"
    fault_rail = 0
    fault_cir = 0
    fault_pow = 0
    commanded_speed = 0
    track_heater = 0
    authority = 0
    underground = 'n'
    signal = np.array([0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    
    #default constructor
    def __init__(self,ln, n, g, e, s, st, len, nl, sw,cr,u):
        self.line_name = ln
        self.name = n
        self.grade = g
        self.elevation = e
        self.crossing = cr
        self.speed = s
        self.station = st
        self.length = len
        self.next_loc = nl
        self.switch_forward_loc = sw
        self.underground = u
        
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
    
    def set_occupancy(self):
        self.occupancy = 1
        return self.occupancy
    
    def reset_occupancy(self):
        self.occupancy = 0
        return self.occupancy
    
    def toggle_occupancy(self):
        if self.occupancy == 1:
            self.occupancy = 0
            return self.occupancy
        else:
            self.occupancy = 1
            return self.occupancy
        
    def set_switch(self):
        self.switch = 1
        return self.switch
    
    def reset_switch(self):
        self.switch = 0
        return self.switch
    
    def set_commanded_speed(self, s):
        self.commanded_speed = s
    
    def get_commanded_speed(self):
        return self.commanded_speed
    
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
    
    def get_circuit_failure(self):
        return self.fault_cir
    
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
    
    def get_crossing_status(self):
        return self.crossing_status
    
    def get_switch(self):
        return self.switch
    
    def get_next_loc(self):
        return self.next_loc
    
    def clear_failure(self):
        self.fault_cir = 0
        self.fault_pow = 0
        self.fault_rail = 0
    
    def get_circuit_failure(self):
        return self.fault_cir
    
    def get_pow_failure(self):
        return self.fault_pow
    
    def get_rail_fault(self):
        return self.fault_rail
    
    def get_underground(self):
        return self.underground
    
    def set_track_heater(self):
        self.track_heater = 1
        return self.track_heater
    
    def reset_track_heater(self):
        self.track_heater = 0
        return self.track_heater
    
    def get_track_heater(self):
        return self.track_heater
    
    def set_authority(self):
        self.authority = 1
        
    def get_authority(self):
        return self.authority
    
    def reset_authority(self):
        self.authority = 0
    def get_next_block(self, dir):
        if dir == True :
            if self.switch == 0:
                return self.next_loc
            else:
                return self.switch_forward_loc
        else:
            return self.next_loc