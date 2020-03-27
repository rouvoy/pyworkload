import docker


class Backend:
    """
        Abstract backend
    """
    def prepare(self, app):
        pass

    def start(self, timer, command):
        pass

    def commands(self, configs):
        commands = []
        for cfg in configs:
            for cmd in cfg[1]:
                commands.append([cfg[0], cmd])
        return commands


class VerboseBackend(Backend):
    """
        Debug backend that prints the tasks
    """
    def prepare(self, app):
        print('Pulling {app}')

    def start(self, timer, command):
        print('{timer}: Running {command}')


class DockerBackend(Backend):
    """
        Backend that runs Docker containers as jobs
    """
    def __init__(self):
        self.docker = docker.from_env()

    def prepare(self, app):
        self.docker.images.pull()

    def start(self, timer, command):
        self.docker.containers.run()
