#!/usr/bin/env python
# Simple check script
from docker import Client
cli = Client(base_url='unix://var/run/docker.sock')
print cli.version()
