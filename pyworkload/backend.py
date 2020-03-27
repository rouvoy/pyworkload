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

    def complete(self):
        pass


class VerboseBackend(Backend):
    """
        Debug backend that prints the tasks
    """
    def prepare(self, app):
        print(f'Pulling image {app}')

    def start(self, timer, command):
        print(f'{timer}: Running container {command}')


class DockerBackend(VerboseBackend):
    """
        Backend that runs Docker containers as jobs
    """
    def __init__(self):
        self.docker = docker.from_env()
        self.images = []
        self.containers = []

    def prepare(self, app):
        super().prepare(app)
        image = self.docker.images.pull(app)
        self.images.append(image)

    def start(self, timer, command):
        super().start(timer,command)
        container = self.docker.containers.run(command[0], command[1], detach=True)
        self.containers.append(container)

    def complete(self):
        super().complete()
        for container in self.containers:
            container.logs()
            container.stop()
        
