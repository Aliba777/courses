class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
 
def peek(s):
    if len(s) > 0:
        return s[-1]
    return None


post = []

def postOrderIterative(root):
    if root is None:
        return
 
    s = []
     
    while(True):
         
        while (root):
             if root.right_child != None:
                s.append(root.right_child)
             s.append(root)

             root = root.left_child
         
        root = s.pop()
 
        if (root.right_child != None and
            peek(s) == root.right_child):
            s.pop() 
            s.append(root) 
            root = root.right_child 

        else:
            post.append(root.key) 
            root = None
 
        if (len(s) <= 0):
                break
 
root = Node('A')
root.left_child = Node('B')
root.right_child = Node('C')
root.left_child.left_child = Node('D')
root.left_child.left_child.left_child = Node('H')
root.left_child.left_child.right_child = Node('I')
root.left_child.right_child = Node('E')
root.right_child.left_child = Node('F')
root.right_child.right_child = Node('G')
 
print ("Post Order traversal of binary tree is")
postOrderIterative(root)
print (post)

input("Enter any key to continue")