
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

import argparse
from .backend import DockerBackend
from .distribution import NoDistribution, PoissonDistribution

class WorkloadCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Starts several containers in parallel.')
        self.parser.add_argument('input', type=str, help='commands file (.yaml)')
        self.parser.add_argument("-m", "--mean", type=int, default=2,
                    help="mean number of containers")
        self.parser.add_argument("-s", "--seconds", type=int, default=30,
                    help="interval in seconds")
        self.parser.add_argument("-t", "--times", type=int, default=10,
                    help="number of times")
        self.parser.add_argument("--pull", action="store_true", help="Only pulls the images")

    def generate_configuration(self):
        args = self.parser.parse_args()
        config = WorkloadConfiguration()
        config.input = args.input
        config.mean = args.mean
        config.seconds = args.seconds
        config.times = args.times
        config.pull = args.pull
        return config


class WorkloadConfiguration:
    def __init__(self):
        self.backend = DockerBackend()
        self.dist = PoissonDistribution()
        self.wait = NoDistribution()
