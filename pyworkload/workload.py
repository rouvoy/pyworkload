import docker
import logging
import numpy as np
import random
import time
import yaml


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
            # self.docker.images.pull(image[0])

    def run(self, parallelism, interval, steps):
        commands = self.backend.commands(self.configs)
        logging.info('Starting the benchmark for ' + str(steps) + ' steps of ' + str(interval) + ' seconds')
        dist = np.random.poisson(parallelism, steps)
        timer = 0
        for n in dist:
            time.sleep(interval)
            timer += interval
            self.__start(n, timer, commands)

    def __start(self, n, timer, commands):
        apps = random.sample(commands, min(n, len(commands)))
        for app in apps:
            self.backend.start(timer, app)


class Backend:
    """
        Sample backend that prints the tasks
    """
    def prepare(self, app):
        pass

    def start(self, timer, command):
        pass

    def commands(configs):
        commands = []
        for cfg in configs:
            for cmd in cfg[1]:
                commands.append([cfg[0], cmd])
        return commands


class VerboseBackend(Backend):
    """
        Sample backend that prints the tasks
    """
    def prepare(self, app):
        print 'Pulling ' + app

    def start(self, timer, command):
        print str(timer) + ': Running ' + str(command)


class DockerBackend(Backend):
    """
        Sample backend that runs Docker containers as jobs
    """
    def __init__(self):
        self.docker = docker.from_env()

    def prepare(self, app):
        pass
        # docker.images.pull()

    def start(self, timer, command):
        pass
        # docker.containers.run()


work = Workload(r'bench.yaml', VerboseBackend())
work.prepare()  # Pulls all required images
work.run(4, 2, 10)  # Spawn 4 new containers every 2 seconds 10 times
