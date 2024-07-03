class NumberDisplay :
    def __init__(self, v, max) :
        self.__v = v
        self.__max = max

    def tick(self) :
        self.__v = (self.__v + 1) % self.__max

    @property
    def v(self) :
        return self.__v

    def __str__(self) :
        return '{:0>2}'.format(self.__v)

class ClockDisplay :
    def __init__(self, h, m) :
        self.hour = NumberDisplay(h, 24)
        self.min = NumberDisplay(m, 60)

    def tick(self) :
        self.min.tick()
        if(self.min.v == 0) :
            self.hour.tick()

    def __str__(self) :
        return str(self.hour) + ':' + str(self.min)

clock = ClockDisplay(1, 18)
for i in range(1000) :
    clock.tick()
    print(clock)
