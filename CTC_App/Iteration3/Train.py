import pandas as pd
from Line import Line

class Train:

    def __init__(self, train_id, station_list):

        # Initialize variables
        self.train_id = train_id
        self.station_list = station_list

        # Intialize route using arrival stations
        self.route = []
    