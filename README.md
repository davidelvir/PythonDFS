# PythonDFS
Instalen python 3+ primero !
Pueden editar en vscode o bajar el ide pycharm
Despues abren la carpeta Serpent-master y ejecutan en consola: python setup.py install
Despues abren la carpeta Pyro4-master y ejecutan en consola: python setup.py install
Para usar el DFS:
    1) Pongan el IP de sus computadoras donde diga SuIP que sale por el de ustedes en:
       cliente.py: def __init__(self):
                     self.server = Pyro4.Proxy('PYRONAME:dfs.server@SuIP')
                     self.abort = 0
                   def run(self):
                   #set host to ip address of client
                    with Pyro4.core.Daemon(host="SuIP") as daemon:
                        daemon.register(self.client)
                        daemon.requestLoop(lambda: not self.client.abort)
       server.py: Pyro4.Daemon.serveSimple(
                  {Server: "dfs.server"},
                  host = "SuIp"
                  )
    
    2) Abran una consola y corran: python -m Pyr04.naming --host SuIP
    3) Corran el server solo con python server.py
    4) Corran un cliente solo con python client.py (pueden abrir los clientes que quieran)
    5) Si sos Calvin: No sé si mac tiene notepad, así que buscá la línea 47 donde dice programName = "notepad.exe" y cambiá notepad por el equivalente tuyo
    
Dirección IPv4: 192.168.1.57

