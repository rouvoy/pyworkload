
# Copyright (c) 2020, Romain Rouvoy
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER
# OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import numpy


class Distribution:
    """
        Standard data distribution abstraction
    """
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
    """
        Data distribution following the Poisson distribution
    """
    def __init__(self):
        super().__init__()

    def init(self,mean,length):
        super().init(length)
        self.values = numpy.random.poisson(mean, length)


class NoDistribution(Distribution):
    """
        Data distribution following no specific law (constant values)
    """
    def __init__(self):
        super().__init__()

    def init(self,mean,length):
        super().init(length)
        self.values = [mean] * length
