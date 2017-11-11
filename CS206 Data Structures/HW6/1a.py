from ADT.VertGraph import Vertex, Graph
from ADT.Stack import Stack

tree = Graph()
def DFS(graph, start, visited):
    print(start)
    start.setCondition(True)
    visited.append(start.id)

    for next in start.getConnections():
        if (not next.getCondition()):
            tree.addEdge(start.id, next.id)
            DFS(graph, next, visited)

visited = []
V = Graph()
def print_tree(n, start):
    for i in range(n):
        print (" ", end = ' ')
    print(start.id)
    for next in start.getConnections():
        print_tree(n+5, next)
'''
#Graph from the lecture

V.addEdge('V0','V1')
V.addEdge('V0','V2')
V.addEdge('V1','V3')
V.addEdge('V1','V4')
V.addEdge('V2','V5')
V.addEdge('V2','V6')
V.addEdge('V3','V7')
V.addEdge('V4','V7')
V.addEdge('V5','V7')
V.addEdge('V6','V7')

V.addEdge('V1','V0')
V.addEdge('V2','V0')
V.addEdge('V1','V3')
V.addEdge('V4','V1')
V.addEdge('V5','V2')
V.addEdge('V6','V2')
V.addEdge('V7','V3')
V.addEdge('V7','V4')
V.addEdge('V7','V5')
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


startV = V.getVertex('V1')
DFS(V, startV, visited)
start = tree.getVertex('V1')
print_tree(3, start)
# for i in visited: 
#     print(i.)
print (visited)
# for v in tree:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))

# print(V.getVertex('V0').getConnections())


