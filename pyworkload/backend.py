
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
        
