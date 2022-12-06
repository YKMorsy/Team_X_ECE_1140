from CTC_App.Iteration3.Train import Train
import pandas as pd
from datetime import datetime

class Dispatcher:

    def __init__(self):
        self.trains = []
        self.train_schedule = []
        self.cur_time = 0

    # Function to schedule single train
    def scheduleSingle(self, station_list, line):
        train_id = len(self.trains) + 1
        self.trains.append(Train(train_id, station_list, line))

    def scheduleMultiple(self, filepath):
        schedule = pd.read_excel(filepath)
        schedule = schedule.loc[:,"Time, Line, and Stations"]
        schedule_time = datetime.timestamp(schedule[0])
        schedule_list = []
        for i in range(1, len(schedule)):
            schedule_list.append(schedule[i])

        self.train_schedule.append([schedule_time, schedule_list])

    def updateStations(self, idx, station_list):
        self.trains[idx].updateStations(station_list)

    # Function to check if train object needs to be created
    def checkDispatch(self, line):
        for train in self.train_schedule.copy():
            if(train[0]) == self.cur_time:
                # Create train
                self.scheduleSingle(train[1], line)
                self.train_schedule.remove(train)

    # Function to update time in dispatcher
    def updateTime(self, cur_time):
        self.cur_time = cur_time

    # Called by CTC (wayside to CTC)
    def setOccupancy(self, occ_dict):
        for key in occ_dict:
            if occ_dict[key] == True:

                if key >= 1000 and key < 2000:
                    line_color = "Green"
                    cur_key = key - 1000
                elif key >= 2000:
                    line_color = "Red"
                    cur_key = key - 2000

                for train in self.trains:
                    # if len(train.route) <= 1:
                    #     self.trains.remove(train)
                    # else:
                    train.setPosition(line_color, cur_key, True)