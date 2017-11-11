from ADT.tree import BinaryTree
from ADT.stack import Stack
from ADT.queue import Queue

file = open('stored.txt', 'r')
listTree = file.readline().strip().split()
#listTree = ['cat','apple','but','pull','line','food','me','say']

tree = BinaryTree(listTree[0]) #define the root
listTree.remove(listTree[0])



def BuildTree():
    global listTree
    stack = Stack() 
    stack.push(tree)
    current = tree
    for node in listTree:
        if not stack.isEmpty():
            if node<stack.top().getRootVal(): #store in left subtree
                current.insertLeft(node)
                current = current.getLeftChild()
                stack.push(current)
            else:                             #store in right subtree
                while (not stack.isEmpty() and node>stack.top().getRootVal()):                
                    current = stack.pop()
                current.insertRight(node)
                current = current.getRightChild()
                stack.push(current)
            
def level_print(tree):
    Parent_q = Queue() 
    Child_q = Queue() 
    Parent_q.enqueue(tree)
    while not Parent_q.isEmpty():
        while not Parent_q.isEmpty():
            node = Parent_q.dequeue()
            print(node.getRootVal(), end=' ')
            if node.getLeftChild():
                Child_q.enqueue(node.getLeftChild())
            if node.getRightChild():
                Child_q.enqueue(node.getRightChild())
        print()
        while not Child_q.isEmpty():
            Parent_q.enqueue(Child_q.dequeue())
def main():
    BuildTree()
    level_print(tree)
main()    
    