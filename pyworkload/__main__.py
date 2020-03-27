from .core import Workload
from .backend import DockerBackend

import argparse

parser = argparse.ArgumentParser(description='Starts several containers in parallel.')

parser.add_argument('input', type=str, help='commands file (.yaml)')
parser.add_argument("-m", "--mean", type=int, default=2,
                    help="mean number of containers")
parser.add_argument("-s", "--seconds", type=int, default=30,
                    help="interval in seconds")
parser.add_argument("-t", "--times", type=int, default=10,
                    help="number of times")
args = parser.parse_args()

print(f'Loading input file {args.input}...')
work = Workload(args.input, DockerBackend())

print('Updating all images...')
work.prepare()  # Pulls all required images

print('Starting the workload...')
work.run(args.mean, args.seconds, args.times)

print('Workload completed.')
