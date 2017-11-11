# implementation by http://interactivepython.org/courselib/static/pythonds/Graphs/Implementation.html
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = { }
        self.condition = False
        self.connectedComponents = set()
        

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected To: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]
        
    def setCondition(self, condition):
        self.condition = condition
    
    def setPred(self, pred_vertex):
        self.predecessor = pred_vertex
    
    def getCondition(self):
        return self.condition
    
    def getPred(self):
        return self.predecessor
        
    def incident_edges(self, v):
        adj = self.connectedTo
        for edge in adj[v].values():
            yield edge
        
    
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.connectedGroups = []

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

