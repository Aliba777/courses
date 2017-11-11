from ADT.VertGraph import Vertex, Graph
from ADT.Queue import Queue

tree = Graph()

def BFS(start):
  queue = Queue()
  queue.enqueue(start)
  start.setCondition(True)
  while (not queue.isEmpty()):
      currentVert = queue.dequeue()
      print(currentVert, 'is adding to the tree')
      for next in currentVert.getConnections():
        if (not next.getCondition()):
            next.setCondition(True)
            tree.addEdge(currentVert.id, next.id)
            queue.enqueue(next)
###=================
V = Graph()
'''
##Graph from the lecture for example

V.addEdge('V0','V2')
V.addEdge('V2','V0')

V.addEdge('V0','V1')
V.addEdge('V1','V0')

V.addEdge('V1','V3')
V.addEdge('V3','V1')

V.addEdge('V1','V4')
V.addEdge('V4','V1')

V.addEdge('V2','V5')
V.addEdge('V5','V2')

V.addEdge('V2','V6')
V.addEdge('V6','V2')

V.addEdge('V3','V7')
V.addEdge('V7','V3')

V.addEdge('V4','V7')
V.addEdge('V7','V4')

V.addEdge('V6','V7')
V.addEdge('V7','V6')

'''
#Sample graph

V.addEdge('V0','V1')    #V0---V1---V2
V.addEdge('V1','V0')    #|     |    |
V.addEdge('V1','V2')    #V7---V9---V3
V.addEdge('V2','V1')    #|     |    |
V.addEdge('V2','V3')    #V6---V5---V4
V.addEdge('V3','V2')
V.addEdge('V3','V4')
V.addEdge('V4','V3')
V.addEdge('V5','V4')
V.addEdge('V4','V5')
V.addEdge('V6','V5')
V.addEdge('V5','V6')
V.addEdge('V6','V7')
V.addEdge('V7','V6')
V.addEdge('V7','V0')
V.addEdge('V0','V7')
V.addEdge('V1','V9')
V.addEdge('V9','V1')
V.addEdge('V9','V5')
V.addEdge('V5','V9')
V.addEdge('V9','V7')
V.addEdge('V7','V9')
V.addEdge('V9','V3')
V.addEdge('V3','V9')




###==========================

startV = V.getVertex('V3')
BFS(startV)
start = tree.getVertex('V3')
def print_tree(n, start):
    for i in range(n):
        print (" ", end = ' ')
    print(start.id)
    for next in start.getConnections():
        print_tree(n+5, next)
print_tree(3, start)