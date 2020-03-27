import numpy


class Distribution:
    def values(self):
        return []


class PoissonDistribution(Distribution):
    def __init__(self,mean,length):
        self.dist = numpy.random.poisson(mean, length)

    def values(self):
        return self.dist