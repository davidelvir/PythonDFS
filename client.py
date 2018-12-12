import sys
import threading
import Pyro4

server = Pyro4.Proxy('PYRONAME:dfs.server@172.16.14.71')

print(server.getTree())