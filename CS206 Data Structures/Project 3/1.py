arr = []
class WUG:
	def __init__(self, directed = False):
		self._outgoing = {}
		self.edges = {}

	def vertexCount(self):
		return len(self._outgoing)

	def getVertices(self):
		vertices = [] # {key: value}
		for key in self._outgoing:
 			vertices.append(key)
		return vertices

	def edgeCount(self):
		total = sum(len(self._outgoing[v].neighbors()) for v in self._outgoing)
		return total // 2

	def weight(self, u, v):
		#print(self._outgoing)
		return self.edges[(u,v)].element()

	def degree(self, v):
		adj = self._outgoing
		return len(adj[v].neighbors())

	def getNeighbors(self, u):
		neighborss = []
		for key in self._outgoing[u].neighbors():
			neighborss.append(key)
		return neighborss

	def addVertex(self, x):
		vertex = Vertex(x)
		self._outgoing[vertex.element()] = vertex

	def isVertex(self, u):
		return True if self._outgoing.get(u, False) else False
	
	def isEdge(self, u, v):
		return True if self.edges.get((u,v), False) else False

	def addEdge(self, u, v, x):
		e = Edge(Vertex(u), Vertex(v), x)
		self._outgoing[u].neighbors().append(v)
		self._outgoing[v].neighbors().append(u)
		self.edges[(u,v)] = self.edges[(v,u)] = e

		return "Edge Added"

	def removeEdge(self, u, v):
		del self.edges[(u,v)]
		del self.edges[(v,u)]
		self._outgoing[u].neighbors().remove(v)
		self._outgoing[v].neighbors().remove(u)
		return "Edge Removed"
		#{obj.element() : }
	def removeVertex(self, u):
		neighbors = self._outgoing[u].neighbors()[:]
		for v in neighbors:
			self._outgoing[u].neighbors().remove(v)
			self._outgoing[v].neighbors().remove(u)
			del self.edges[(u,v)]
			del self.edges[(v,u)]
		del self._outgoing[u]
		return "Vertex Removed"
			
class Vertex:
	__slots__ = '_element', '_neighbors'

	def __init__(self, x):
		self._element = x
		self._neighbors = []

	def element(self):
		return self._element
	def neighbors(self):
		return self._neighbors

	def __hash__(self):
		return hash(id(self))

class Edge:
	__slots__ = '_origin', '_destination', '_element'

	def __init__(self, u, v, x):
		self._origin = u
		self._destination = v
		self._element = x
	def endpoints(self):
		return (self._origin, self._destination)
	def element(self):
		return self._element
	def __hash__(self):
		return hash( (self._origin, self._destination))
	def __str__(self):
		return ("%s + %s + %s" % (self._origin, self._destination, self._element))

g = WUG()
# ver0 = Vertex('0')
# ver1 = Vertex('1')
# ver2 = Vertex('2')
# ver3 = Vertex('3')
# ver4 = Vertex('4')
# ver5 = Vertex('5')
# ver6 = Vertex('6')
g.addVertex('0')
g.addVertex('1')
g.addVertex('2')
g.addVertex('3')
g.addVertex('4')
g.addVertex('5')
g.addVertex('6')
g.addEdge('0', '1', 28)
g.addEdge('0', '5', 10)
g.addEdge("1", '2', 16)
g.addEdge('1', '6', 14)
g.addEdge('2', '3', 12)
g.addEdge('3', '4', 22)
g.addEdge('3', '6', 18)
g.addEdge('4', '6', 24)
g.addEdge('4', '5', 25)

print(g.vertexCount()) #1
print(g.edgeCount()) #2
print(g.getVertices()) #3
print(g.removeVertex('6')) #4
print(g.isVertex('6')) #5
print(g.isVertex('3')) #6
print(g.degree('3')) #7
print(g.getNeighbors('3')) #8
print(g.getVertices())
print(g.addEdge('0', '4', 25)) #9
print(g.removeEdge('0', '1')) #10
print(g.isEdge('0', '1'))
print(g.weight('0', '4'))
print(g.edgeCount())