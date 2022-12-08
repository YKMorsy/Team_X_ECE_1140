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
            # print("Error " + changes) ### COMMENTED BY YASSER... WILL UNCOMMENT
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
    def set_occupancy(self, occ):
        self.occupancy = occ
    def set_switch_positions(self, sw):
        self.switch_positions = sw
    def set_railway_crossings(self, rc):
        self.railway_crossings = rc
    def set_light_colors(self, lc):
        self.light_colors = lc
    def set_statuses(self, st):
        self.statuses = st
        for key, val in st.items():
            if(val == False):
                self.authority[key] = False
        self.temp_statuses = st.copy()
    def set_suggested_speed(self, ss):
        self.suggested_speed = ss
    def set_commanded_speed(self, cs):
        self.commanded_speed = cs
    def set_speed_limit(self, sl):
        self.speed_limit = sl
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
                self.PLC_info.change_PLC_file("track_controller/blank.txt")
                self.PLC_info2.change_PLC_file("track_controller/blank.txt")
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
    def get_occupancy(self):
        return self.occupancy
    def get_switch_positions(self):
        return self.switch_positions
    def get_railway_crossings(self):
        return self.railway_crossings
    def get_light_colors(self):
        return self.light_colors
    def get_statuses(self):
        return self.statuses
    def get_suggested_speed(self):
        return self.suggested_speed
    def get_PLC (self):
        return self.PLC_info.get_PLC_file()
    def get_commanded_speed (self):
        return self.commanded_speed
    def get_speed_limit (self):
        return self.speed_limit
    def get_maintenance_mode (self):
        return self.maintencMode
    def get_line_index(self):
        return self.line_index