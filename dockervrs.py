#!/usr/bin/env python
from docker import Client
cli = Client(base_url='unix://var/run/docker.sock')
print cli.version()
