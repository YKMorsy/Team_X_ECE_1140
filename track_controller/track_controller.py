from track_controller.PLC_Parser import PLC_Parser

class WaysideController ():
    def __init__(self):
        self.wayside_id = 0
        self.PLC_info = PLC_Parser()
        self.PLC_info2 = PLC_Parser()
        self.authority = {}
        self.occupancy = {}
        self.switch_positions = {}
        self.railway_crossings = {}
        self.light_colors = {}
        self.statuses = {}
        self.temp_statuses = {}
        self.suggested_speed = {} #0b00010100 #20 in binary
        self.commanded_speed = {}#0b00010100 #20 in binary
        self.speed_limit = {}#0b00010100 #20 in binary
        self.maintencMode = False
        self.line_index = 0

    def parse_plc(self):
        changes = self.PLC_info.parse_PLC(self.switch_positions, self.occupancy, self.authority,self.suggested_speed, self.statuses, self.speed_limit)
        changes2 = self.PLC_info2.parse_PLC(self.switch_positions, self.occupancy, self.authority,self.suggested_speed, self.statuses, self.speed_limit)
        any_changes = (set(changes) - set(changes2))
        if(len(any_changes)!=0):
            print("difference in plc parsing")
            return
        if isinstance(changes, str):
            print("Error " + changes)
            return False
        for change in changes:
            (typeS, bl, val) = change
            if typeS == "S":
                self.make_changes(change, self.switch_positions)
            elif typeS == "A":
                self.make_changes(change, self.authority)
            elif typeS == "R":
                self.make_changes(change, self.railway_crossings)
            elif typeS == "L":
                self.make_light_changes(change, self.light_colors)
            elif typeS == "F":
                #self.make_changes(change, self.statuses)
                return False
            elif typeS == "C":
                self.make_speed_change(change, self.commanded_speed)

    def make_changes(self, change, table):
        (typeS, bl, val) = change
        table[int(bl)] = val == "True"
    
    def make_speed_change(self, change, table):
        (typeS, bl, val) = change
        table[int(bl)] = int(val)

    def make_light_changes(self, change, table):
        t= len(table)
        (typeS, bl, val) = change
        if(val[0]=='1'):
            val1 = True
        else:
            val1 = False
        if(val[0]=='1'):
            val2 = True
        else:
            val2 = False
        table[int(bl)] = [val1, val2]

    #----setters----
    def set_wayside_id(self, wid):
        self.wayside_id = wid
    def set_authority(self, auth):
        self.authority = auth
    def set_an_auth(self, key, val):
        self.authority[key] = val
    def set_occupancy(self, occ):
        self.occupancy = occ
    def set_an_occ(self, key, val):
        self.occupancy[key] = val
    def set_switch_positions(self, sw):
        self.switch_positions = sw
    def set_a_switch(self, key, val):
        self.switch_positions[key] = val
    def set_railway_crossings(self, rc):
        self.railway_crossings = rc
    def set_a_railway_cross(self, key, val):
        self.railway_crossings[key] = val
    def set_light_colors(self, lc):
        self.light_colors = lc
    def set_a_light(self, key, val):
        self.light_colors[key] = val
    def set_statuses(self, st):
        self.statuses = st
        for key, val in st.items():
            if(val == False):
                self.authority[key] = False
        self.temp_statuses = st.copy()
    def set_a_stat(self, key, val):
        self.statuses[key] = val
    def set_suggested_speed(self, ss):
        self.suggested_speed = ss
    def set_a_sug_speed(self, key, val):
        self.suggested_speed[key] = val
    def set_commanded_speed(self, cs):
        self.commanded_speed = cs
    def set_a_command_speed(self, key, val):
        self.commanded_speed[key] = val
    def set_speed_limit(self, sl):
        self.speed_limit = sl
    def set_a_speed_lim(self, key, val):
        self.speed_limit[key] = val
    def set_maintenance_mode(self,m):
        self.maintencMode = m
        if(m):
            self.temp_statuses = self.statuses.copy()
            for i in self.statuses.keys():
                self.statuses[i] = False
        else:
            self.statuses = self.temp_statuses.copy()
    def set_PLC (self, plc):
        testPLC = PLC_Parser()
        testPLC.change_PLC_file(plc)
        issue = testPLC.parse_PLC(self.switch_positions, self.occupancy, self.authority,self.suggested_speed, self.statuses, self.speed_limit)
        if(isinstance(issue, str)):
            if(self.PLC_info.get_PLC_file() ==""):
                self.PLC_info.change_PLC_file("track_controller/PLCs/blank.txt")
                self.PLC_info2.change_PLC_file("track_controller/PLCs/blank.txt")
            return issue
        self.PLC_info.change_PLC_file(plc)
        self.PLC_info2.change_PLC_file(plc)
        return True
    def set_line_index(self, lineIn):
        self.line_index = lineIn

    #----getters----
    def get_wayside_id(self):
        return self.wayside_id
    def get_authority(self):
        return self.authority
    def get_an_auth(self, key):
        return self.authority[key]
    def get_occupancy(self):
        return self.occupancy
    def get_an_occ(self, key):
        return self.occupancy[key]
    def get_switch_positions(self):
        return self.switch_positions
    def get_a_switch(self, key):
        return self.switch_positions[key]
    def get_railway_crossings(self):
        return self.railway_crossings
    def get_a_rail_cross(self, key):
        return self.railway_crossings[key]
    def get_light_colors(self):
        return self.light_colors
    def get_a_light(self, key):
        return self.light_colors[key]
    def get_statuses(self):
        return self.statuses
    def get_a_stat(self, key):
        return self.statuses[key]
    def get_suggested_speed(self):
        return self.suggested_speed
    def get_a_sug_speed(self, key):
        return self.suggested_speed[key]
    def get_PLC (self):
        return self.PLC_info.get_PLC_file()
    def get_commanded_speed (self):
        return self.commanded_speed
    def get_a_comm_speed(self, key):
        return self.commanded_speed[key]
    def get_speed_limit (self):
        return self.speed_limit
    def get_an_speed_lim(self, key):
        return self.speed_limit[key]
    def get_maintenance_mode (self):
        return self.maintencMode
    def get_line_index(self):
        return self.line_index