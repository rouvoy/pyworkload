from .core import Workload
from .backend import DockerBackend
from .configuration import WorkloadCLI

# import argparse

# parser = argparse.ArgumentParser(description='Starts several containers in parallel.')

# parser.add_argument('input', type=str, help='commands file (.yaml)')
# parser.add_argument("-m", "--mean", type=int, default=2,
#                     help="mean number of containers")
# parser.add_argument("-s", "--seconds", type=int, default=30,
#                     help="interval in seconds")
# parser.add_argument("-t", "--times", type=int, default=10,
#                     help="number of times")
# parser.add_argument("--pull", action="store_true", help="Only pulls the images")
# args = parser.parse_args()
cli = WorkloadCLI()
configuration = cli.generate_configuration()

print(f'Loading input file {configuration.input}...')
work = Workload(configuration)

print('Updating all images...')
work.prepare()  # Pulls all required images

if configuration.pull:
    print('Pull completed.')
else:
    print('Starting the workload...')
    work.run()
    print('Workload completed.')
