import sys
import threading
import Pyro4
import os
import subprocess as sp
import time

class Client:
    def __init__(self):
        self.server = Pyro4.Proxy('PYRONAME:dfs.server@192.168.0.43')
        self.abort = 0
        #self.openFiles = {}
    

    def start(self):
        names = self.server.getNames()
        if names:
            print('Los siguientes clientes se encuentran conectados al servidor: %s' % (', '.join(names)))
        self.name = input('Elija un nombre para su cliente: ').strip()
        self.server.join(self.name,self)
        self.tree = self.server.getTree()
        print("¡ Bienvenido al sistema de archivos DDJC !")
        print("")
        self.printFiles(-1,0)
        try:
            try:
                while not self.abort:
                    print("-----Menu Principal------")
                    print("1. Leer archivo")
                    print("2. Crear archivo")
                    print("3. Ver directorio")
                    print("4. Crear directorio")
                    print("5. Salir")
                    line = input("Ingrese el número de la opción que desea: ")
                    if line == '1':
                        tem = input("Ingrese el número del archivo que quiere ver: ")
                        #print("wtf"+tem)
                        dir = self.tree[int(tem)][4]
                        content = self.server.fetch(dir)
                        writeBUffer = open(self.tree[int(tem)][3],"w+")
                        writeBUffer.write(content)
                        writeBUffer.close()
                        programName = "notepad.exe"
                        p = sp.Popen([programName, dir])
                        #print(p)
                        while p.poll() == None:
                            pass
                        os.remove(self.tree[int(tem)][3])   
                        
                    if line == '2':
                        tem = input("Ingrese el directorio en el que desea crear un archivo: ")
                        #print(int(tem))
                        dir = self.tree[int(tem)][4]
                        print(dir)
                        tem2 = input("Ingrese el nombre del archivo: ")
                        ruta = dir + '/' +tem2
                        print(ruta)
                        self.server.createFile(int(tem),tem2,ruta,"hola")
                        
                    if line == '3':
                        self.printFiles(-1,0)
                    if line == '4':
                        tem = input("Ingrese el directorio en el que desea crear su nuevo directorio: ")
                        dir = self.tree[int(tem)][4]
                        tem2 = input("Ingrese el nombre del directorio: ")
                        ruta = dir + '/' +tem2
                        self.server.mkDir(int(tem),tem2,ruta)
                    if line == '5':
                        
                        break
                    time.sleep(0.5)
                   
            except EOFError:
                pass
        finally:
            self.server.leave(self.name)
            self.abort = 1
            self._pyroDaemon.shutdown()

    @Pyro4.expose
    @Pyro4.oneway
    @Pyro4.callback    
    def updateTree(self):
        print("La estructura de directorios ha sido modificada !")
        print("Se actualizará su árbol")
        #print("Cargando sistema de nuevo")
        #while refresh != 'R' or refresh !='r':
        #    refresh = input("No puede continuar si no da refresh")
        self.tree = self.server.getTree()
        self.printFiles(-1,0)
        
    def printFiles(self,parent,level):
        #print(tree[parent][3])
        for i,filename in enumerate(self.tree):
            if(filename[0] == parent):
                if(filename[1] == 0):
                    print(" "*level+"| "+str(i)+ " Dir: "+filename[3])
                    self.printFiles(i,level+2)
                else:
                    print(" "*level+"| "+str(i)+" File: "+filename[3])

class DaemonThread(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        self.setDaemon(True)

    def run(self):
        #set host to ip address of client
        with Pyro4.core.Daemon(host="192.168.0.43") as daemon:
            daemon.register(self.client)
            daemon.requestLoop(lambda: not self.client.abort)

client = Client()
daemonthread = DaemonThread(client)
daemonthread.start()
client.start()
print('Exit.')




