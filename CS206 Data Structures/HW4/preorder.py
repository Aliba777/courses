class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

def iterativePreorder(root):
    if root is None:
        return

    s = []
    s.append(root)
 
    while(len(s) > 0):
        node = s.pop()
        print (node.key, end = ' ')

        if node.right_child != None:
            s.append(node.right_child)
        if node.left_child != None:
            s.append(node.left_child)
     
root = Node('A')
root.left_child = Node('B')
root.right_child = Node('C')
root.left_child.left_child = Node('D')
root.left_child.left_child.left_child = Node('H')
root.left_child.left_child.right_child = Node('I')
root.left_child.right_child = Node('E')
root.right_child.left_child = Node('F')
root.right_child.right_child = Node('G')
print("Preorder of binary tree is: ")
iterativePreorder(root)

input("Enter any key to continue")