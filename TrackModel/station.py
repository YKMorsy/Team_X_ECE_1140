import random

class station(object):
    def __init__(self):
        self.throughput = 0
        self.passengers = 0
    
    def get_passengers(self, cap):
        rand = random.randint(1,15)
        self.passengers += rand
        self.throughput += rand
        
        ret = 0
        while self.passengers > 0 and cap > 0:
            ret += 1
            self.passengers -= 1
            cap -= 1
        return ret
    
    def get_throughput(self):
        temp = self.throughput
        self.throughput = 0
        return temp