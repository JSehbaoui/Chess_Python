import datetime

class Clock:

    instances = []

    def __init__(self, time):
        self.starting_time = datetime.datetime.now()
        self.time_now = datetime.datetime.now()
        self.count = None
        self.time = time
        Clock.instances.append(self)

    def getTime(self):
        self.refreshTime()
        return str(self.count)[2:7]

    def refreshTime(self):
        self.time_now = datetime.datetime.now()
        self.count = self.time_now - self.starting_time


# clock = Clock(time = 5)

# time.sleep(4)

# clock.refreshTime()

# print(clock.getTime())

# past = datetime.datetime.now()

# # time.sleep(1)

# now = datetime.datetime.now()

# print(past-now)


