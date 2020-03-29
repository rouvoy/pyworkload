
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

import logging
import random
import time
import yaml
from .distribution import PoissonDistribution, NoDistribution

class Workload:
    """
        Core workload engine that spawns jobs following two given distributions
        for time and number of apps along X iterations.
    """
    def __init__(self, config):
        self.backend = config.backend
        logging.info(f'Preparing the benchmark for {config.times} steps of {config.seconds} seconds...')
        self.dist = config.dist
        self.dist.init(config.mean,config.times)
        logging.debug(f'Generated app distribution for {config.times} steps: {self.dist.values}')
        self.wait = config.wait
        self.wait.init(config.seconds,config.times)
        logging.debug(f'Generated time distribution for {config.times} steps: {self.wait.values}')
        with open(config.input) as file:
            documents = yaml.full_load(file)
            self.apps = documents.items()

    def prepare(self):
        logging.info("Installing dependencies...")
        for image in self.apps:
            self.backend.prepare(image[0])

    def run(self):
        commands = self.backend.commands(self.apps)
        timestamp = 0
        for n in self.dist.range():
            duration = self.wait.value(n)
            time.sleep(duration)
            timestamp += duration
            self.__start(timestamp, self.dist.value(n), commands)
        self.backend.complete()

    def __start(self, timestamp, nb, commands):
        apps = self.__select_apps(nb,commands)
        logging.info(f'T={timestamp}: Spawning {nb} apps: {apps}')
        for app in apps:
            self.backend.start(timestamp, app)

    def __select_apps(self,nb,commands):
        if (nb<=len(commands)):
            return random.sample(commands, nb)
        else:
            apps = []
            for i in range(nb):
                apps += random.sample(commands,1)
            return apps
