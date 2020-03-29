import numpy


class Distribution:
    def __init__(self):
        self.size = 0
        self.values = None

    def init(self,length):
        self.size = length
        self.values = [None] * self.size

    def range(self):
        return range(self.size)

    def value(self,n):
        return self.values[n]


class PoissonDistribution(Distribution):
    def __init__(self):
        super().__init__()

    def init(self,mean,length):
        super().init(length)
        self.values = numpy.random.poisson(mean, length)


class NoDistribution(Distribution):
    def __init__(self):
        super().__init__()

    def init(self,mean,length):
        super().init(length)
        self.values = [mean] * length
