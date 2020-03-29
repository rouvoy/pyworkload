Python Workload Generator Repository
========================

Installation
----------
::
    % pip install -r requirements.txt


Execution
----------
Runs a new workload from applications listed in ``example.yaml`` with the following configuration: spawn 3 apps on average along 4 cycles separated by exactly 2 seconds::
    python3.7 -m pyworkload example.yaml -m 3 -s 2 -t 4

Only install the dependencies required to run the workload specified in ``example.yaml``::
    python3.7 -m pyworkload example.yaml --pull

For more details run, ``python3.7 -m pyworkload --help``::
    usage: __main__.py [-h] [-m MEAN] [-s SECONDS] [-t TIMES] [--pull] input

    Starts several containers in parallel.

    positional arguments:
    input                 commands file (.yaml)

    optional arguments:
    -h, --help            show this help message and exit
    -m MEAN, --mean MEAN  mean number of containers
    -s SECONDS, --seconds SECONDS
                            interval in seconds
    -t TIMES, --times TIMES
                            number of times
    --pull                Only pulls the images