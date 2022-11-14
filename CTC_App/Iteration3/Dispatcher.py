from Train import Train

class Dispatcher:

    def __init__(self):
        self.trains = []

    # Function to schedule single train
    def scheduleSingle(self, station_list, line, depart_time):
        train_id = len(self.trains) + 1
        self.trains.append(Train(train_id, station_list, line, depart_time))

    def scheduleMultiple(self, filepath):
        pass

    # Function to check if train object needs to be created
    def dispatchTrain(self, cur_time):
        for train in self.trains:
            if(train.depart_time) == cur_time:
                # Create train
                pass