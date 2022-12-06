from CTC_App.Iteration3.Train import Train

class Dispatcher:

    def __init__(self):
        self.trains = []

    # Function to schedule single train
    def scheduleSingle(self, station_list, line, depart_time):
        train_id = len(self.trains) + 1
        self.trains.append(Train(train_id, station_list, line, depart_time))

    def scheduleMultiple(self, filepath):
        pass

    def updateStations(self, idx, station_list):
        self.trains[idx].updateStations(station_list)

    # Function to check if train object needs to be created
    def dispatchTrain(self, cur_time):
        for train in self.trains:
            if(train.depart_time) == cur_time:
                # Create train
                pass

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