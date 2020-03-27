import logging
import random
import time
import yaml
from .distribution import PoissonDistribution

class Workload:
    """
        Core workload engine that spawns jobs following a Poisson distribution
        along X iterations.
    """
    def __init__(self, apps, backend):
        self.backend = backend
        with open(apps) as file:
            documents = yaml.full_load(file)
            self.configs = documents.items()

    def prepare(self):
        logging.info("Pulling all required images from DockerHub")
        for image in self.configs:
            self.backend.prepare(image[0])

    def run(self, parallelism, interval, steps):
        commands = self.backend.commands(self.configs)
        logging.info('Starting the benchmark for ' + str(steps) + ' steps of ' + str(interval) + ' seconds')
        dist = PoissonDistribution(parallelism,steps)
        timer = 0
        for n in dist.values():
            time.sleep(interval)
            timer += interval
            self.__start(n, timer, commands)

    def __start(self, n, timer, commands):
        apps = random.sample(commands, min(n, len(commands)))
        for app in apps:
            self.backend.start(timer, app)
