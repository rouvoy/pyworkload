from .core import Workload
from .backend import VerboseBackend

work = Workload(r'bench.yaml', VerboseBackend())
work.prepare()  # Pulls all required images
work.run(4, 2, 10)  # Spawn 4 new containers every 2 seconds 10 times
