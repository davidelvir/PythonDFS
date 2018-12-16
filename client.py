import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import threading
import Pyro4
import os
import subprocess as sp
import time

class Client:
    def __init__(self):
        self.server = Pyro4.Proxy('PYRONAME:dfs.server@192.168.0.7')
        self.abort = 0
        self.treedata = sg.TreeData() # nodes (parent,type,mod,name,route)

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
                        if(self.tree[int(tem)][1] == 0):
                            print("¡Debe elegir un archivo!")
                        else:
                            dir = self.tree[int(tem)][4]#se consigue la ruta del archivo
                            content = self.server.fetch(dir)#crear copia del contenido
                            writeBUffer = open(self.tree[int(tem)][3],"w+")#crear copia en en caché
                            writeBUffer.write(content)
                            writeBUffer.close()
                            checktime = os.path.getmtime(self.tree[int(tem)][3])#capturar el tiempo para verificar modificaciones
                            #print(checktime)
                            programName = "notepad.exe"#nombre del editor
                            p = sp.Popen([programName,self.tree[int(tem)][3]])#abrir archivo en el editor
                            #print(p)
                            while p.poll() == None:#mientras el archivo esté abierto esperar
                                pass
                            #print(os.path.getmtime(self.tree[int(tem)][3]))
                            if self.tree[int(tem)][2] == 1:#revisar si la copia no está invalidad
                                print("Su copia no es válida, si hizo cambios no se van a guardar.")
                            else:
                                if checktime != os.path.getmtime(self.tree[int(tem)][3]):#revisar si se modificó el archivo
                                    print("Has salvado!")
                                    readBUffer = open(self.tree[int(tem)][3],"r")
                                    content = readBUffer.read()
                                    readBUffer.close()
                                    self.server.save(int(tem),self.name,self.tree[int(tem)][4],content)#guardar cambio en el servidor
                            os.remove(self.tree[int(tem)][3])#borrar el archivo en caché   
                        
                    if line == '2':
                        tem = input("Ingrese el directorio en el que desea crear un archivo: ")
                        #print(int(tem))
                        if self.tree[int(tem)][1] == 1:
                            print("¡ Debe seleccionar un directorio !")
                        else: 
                            dir = self.tree[int(tem)][4]
                            #print(dir)
                            tem2 = input("Ingrese el nombre del archivo: ")
                            ruta = dir + '/' +tem2
                            #print(ruta)
                            self.server.createFile(int(tem),tem2,ruta)
                        
                    if line == '3':
                        self.printFiles(-1,0)
                    if line == '4':
                        tem = input("Ingrese el directorio en el que desea crear su nuevo directorio: ")
                        if self.tree[int(tem)][1] == 1:
                            print("¡ Debe seleccionar in directorio !")
                        else: 
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

    @Pyro4.expose
    @Pyro4.oneway
    @Pyro4.callback 
    def update(self,index):
        self.tree[index][2] = 1
        print("Se hizo un cambio al archivo: " + self.tree[index][3])

    def printFiles(self,parent,level):
        #print(tree[parent][3])
        for i,filename in enumerate(self.tree):
            if(filename[0] == parent):
                if(filename[1] == 0):
                    print(" "*level+"| "+str(i)+ " Dir: "+filename[3])
                    self.printFiles(i,level+2)
                else:
                    print(" "*level+"| "+str(i)+" File: "+filename[3])

    def makeTree(self,parent):
        # nodes (parent,type,mod,name,route)
        for i,filename in enumerate(self.tree):
            if(filename[0] == parent):
                if(filename[1] == 0):
                    if(parent==-1):
                        self.treedata.Insert("",i,filename[3] ,['Dir']) #Insert(parent_key, key, display_text, values)
                        self.makeTree(i)
                    else:
                        self.treedata.Insert(parent,i,filename[3] ,['Dir']) #Insert(parent_key, key, display_text, values)
                        self.makeTree(i)
                else:
                    self.treedata.Insert(parent,i,filename[3] ,['File']) #Insert(parent_key, key, display_text, values)

                        
    def makeTreeTest(self,parent):
        for i,filename in enumerate(self.tree):
           self.treedata.Insert("",i, filename[3] ,[]) #Insert(parent_key, key, display_text, values)



class DaemonThread(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        self.setDaemon(True)

    def run(self):
        #set host to ip address of client
        with Pyro4.core.Daemon(host="192.168.0.7") as daemon:
            daemon.register(self.client)
            daemon.requestLoop(lambda: not self.client.abort)

client = Client()
daemonthread = DaemonThread(client)
daemonthread.start()
client.start()
client.makeTree(-1)


layout = [[ sg.Text('Archivos') ],
          [ sg.Tree(data=client.treedata, headings=['Tipo'],justification='right',change_submits=True, auto_size_columns=True, num_rows=10, col0_width=25, key='_TREE_', show_expanded=True),
            ],
          [ sg.Button('Read')]]

window = sg.Window('File System').Layout(layout)
print(client.treedata)



while True:     # Event Loop
    event, values = window.Read()
    if event is None:
        break
    if event == 'Update':
        window.FindElement('_TREE_').Update(treedata)
    elif event == 'Read':
        print(event, values)

print('Exit.')




