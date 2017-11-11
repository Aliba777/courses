from ADT.VertGraph import Vertex
from ADT.VertGraph import Graph
from ADT.Stack import Stack

tree = Graph()
def DFS(start, s):
    print(start)
    s.add(start)
    start.setCondition(True)

    for next in start.getConnections():
        if (not next.getCondition()):
            DFS(next, s)

def ConnectedComponents(V):              
    for vert in V.vertList.values():
        if (not vert.getCondition()):
            s = set()        
            DFS(vert,s)
            V.connectedGroups.append(s)
##Sample graph
V = Graph()
V.addEdge('V0','V1')
V.addEdge('V1','V0')    #V0--V1--V2--V3
V.addEdge('V1','V2')    #         |
V.addEdge('V2','V3')    #         V4
V.addEdge('V3','V2')    #
V.addEdge('V2','V1')    #V5---V6
V.addEdge('V2','V4')
V.addEdge('V4','V2')
V.addEdge('V5','V6')
V.addEdge('V6','V5')
                    
ConnectedComponents(V)                
group_ind = 1

for i in V.connectedGroups:
    print(group_ind,end=': ')
    for vert in i:
        print(vert, end =', ')
    print()
    group_ind+=1    




   



