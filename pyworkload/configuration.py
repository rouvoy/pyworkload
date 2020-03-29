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
