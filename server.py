import os
import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class Server(object):
    def __init__(self):
        self.tree = []  # nodes (parent,type,mod,name)
        self.client = []
        self.currDir = 'root'
        self.pastDir = ''
        self.dirIndex = 0
        self.pastDirIndex = 0
        self.tree.append((-1, 0, 0, "root"))
        self.fillTree()

    def fillTree(self):
        tem = self.pastDir
        temI = self.pastDirIndex
        for filename in os.listdir(self.currDir):
            if(os.path.isdir(self.currDir+'/'+filename)):
                
                self.pastDir = self.currDir
                node = (self.dirIndex,0,0,filename)
                self.tree.append(node)
                self.currDir = self.currDir+'/'+filename
                self.pastDirIndex = self.dirIndex
                self.dirIndex = self.tree.index(node)
                
                self.fillTree()
            else:
                node = (self.dirIndex,1,0,filename)
                self.tree.append(node)
        
        self.dirIndex = temI
        self.currDir = tem
    
    def getTree(self):
        return self.tree
Pyro4.Daemon.serveSimple(
    {Server: "dfs.server"},
    host = "172.16.14.71"
    )
