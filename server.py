import os
import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class Server(object):
    def __init__(self):
        self.clients = [] #client -> (name,callback)
        self.names = []
        self.tree = []  # nodes (parent,type,mod,name,route)
        self.currDir = 'root'
        self.pastDir = ''
        self.dirIndex = 0
        self.pastDirIndex = 0
        self.tree.append((-1, 0, 0, "root",'root'))
        self.fillTree()

    def join(self, name, callback):
        if not name:
            raise ValueError('Nombre inválido')
        if (name in self.names):
            raise ValueError('El nombre ya está en uso')
        self.clients.append((name,callback))
        self.names.append(name)

        print("Se ha unido un nuevo cliente")
    def leave(self, name):
        if name not in self.names:
            print("Este cliente no está registrado")
            return
        for (n,c) in self.clients:
            if(n == name):
                self.names.remove(name)
                self.clients.remove((n,c))
                print("Se ha desconectado un cliente")
                break
        
    def createFile(self,parent,name,dir):
        writeBUffer = open(dir,"w+")
        self.tree.append((parent,1,0,name,dir))
        #writeBUffer.write(content)
        for (n,c) in self.clients:
            c.updateTree()
        writeBUffer.close()

    def mkDir(self,parent,name,dir):
        os.mkdir(dir)#poner 0777 si no funciona
        self.tree.append((parent,0,0,name,dir))
        for (n,c) in self.clients:
            c.updateTree()

    def save(self,parent,name,dir,content):
        writeBUffer = open(dir,"w+")
        self.tree.append((parent,1,0,name,dir))
        writeBUffer.write(content)
        for (n,c) in self.clients:
            c.updateTree()
        writeBUffer.close()
        
    def fillTree(self):
        tem = self.pastDir
        temI = self.pastDirIndex
        for filename in os.listdir(self.currDir):
            if(os.path.isdir(self.currDir+'/'+filename)):
                
                self.pastDir = self.currDir
                
                
                self.currDir = self.currDir+'/'+filename
                node = (self.dirIndex,0,0,filename,self.currDir)
                self.tree.append(node)
                self.pastDirIndex = self.dirIndex
                self.dirIndex = self.tree.index(node)
                
                self.fillTree()
            else:
                node = (self.dirIndex,1,0,filename,self.currDir+'/'+filename)
                self.tree.append(node)
        
        self.dirIndex = temI
        self.currDir = tem
    
    def change(self,index,client,content):
        for (n,c) in self.clients:
            if(n != client):
                #c.change()
                break

    def getTree(self):
        return self.tree
        
    def getNames(self):
        return self.names

    def fetch(self,dir):
        f = open(dir,"r")
        contents = f.read()
        f.close()
        return contents
        

Pyro4.Daemon.serveSimple(
    {Server: "dfs.server"},
    host = "172.16.14.71"
    )
