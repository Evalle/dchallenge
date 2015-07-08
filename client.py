from docker import Client
c = Client(base_url='tcp://10.8.0.1:2375')
print c.images()
