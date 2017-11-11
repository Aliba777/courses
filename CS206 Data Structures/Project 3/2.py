arr = []
parent = dict()
rank = dict()

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
		neighbors = []
		for key in self._outgoing[u].neighbors():
			neighbors.append(key)
		return neighbors

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

	def removeEdge(self, u, v):
		del self.edges[(u,v)]
		del self.edges[(v,u)]
		#{obj.element() : }
	def removeVertex(self, u):
		neighbors = self._outgoing[u].neighbors()[:]
		for v in neighbors:
			self._outgoing[u].neighbors().remove(v)
			self._outgoing[v].neighbors().remove(u)
			del self.edges[(u,v)]
			del self.edges[(v,u)]
		del self._outgoing[u]


def makeSet(g, vertice):
        parent[vertice] = vertice
        rank[vertice] = 0

def find(g, vertice):
        if parent[vertice]!= vertice:
                parent[vertice] = find(g,parent[vertice])
        return parent[vertice]

def union(g,vertice1, vertice2):
	root1 = find(g,vertice1)
	root2 = find(g,vertice2)
	if root1!=root2:
		if rank[root1] > rank[root2]:
			parent[root2] = root1
		else:
			parent[root1] = root2
		if rank[root1] == rank[root2]: rank[root2] += 1

def minSpanTree(g):
        for vertice in g._outgoing:
                makeSet(g,vertice)
        minimum_spanning_tree = set()
        ribs = []
        for (u, v) in g.edges:
                ribs.append((g.edges[(u, v)].element(), (u, v)))
        ribs.sort(key = lambda x: x[0])
	   #print (ribs)
		#print edges
        for edge in ribs:
                weight, (vertice1, vertice2) = edge
                if find(g,vertice1) != find(g,vertice2):
                        union(g,vertice1, vertice2)
                        minimum_spanning_tree.add(edge)
	    #print (minimum_spanning_tree
        return sorted(minimum_spanning_tree)

			
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
ver0 = Vertex('0')
ver1 = Vertex('1')
ver2 = Vertex('2')
ver3 = Vertex('3')
ver4 = Vertex('4')
ver5 = Vertex('5')
ver6 = Vertex('6')
g.addVertex(ver0)
g.addVertex(ver1)
g.addVertex(ver2)
g.addVertex(ver3)
g.addVertex(ver4)
g.addVertex(ver5)
g.addVertex(ver6)
g.addEdge(ver0, ver1, 28)
g.addEdge(ver0, ver5, 10)
g.addEdge(ver1, ver2, 16)
g.addEdge(ver1, ver6, 14)
g.addEdge(ver2, ver3, 12)
g.addEdge(ver3, ver4, 22)
g.addEdge(ver3, ver6, 18)
g.addEdge(ver4, ver6, 24)
g.addEdge(ver4, ver5, 25)

print (minSpanTree(g))
print("________________________________________")
print()
print("Have a good day, TA!")
print("See you in the final exam!")
print("Wish you all the best!")
print("It took us a lot ! :C ")
print("Maybe one day")
print("Or two! ")
print("________________________________________")

