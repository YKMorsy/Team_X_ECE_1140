import pandas as pd
from Line import Line

class Train:

    def __init__(self, train_id, station_list, line):

        # Initialize variables
        self.train_id = train_id
        self.station_list = station_list
        self.line = line

        # Intialize route using arrival stations
        self.route = []
    
    def generateRoute(self, line):
        
        pass