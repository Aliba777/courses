class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,item):
        self.key = item
    
    def getRootVal(self):
        return self.key

class Tree:
    def  __init__(self, item):
        self.item = item
        self.children = []
        
    def addChild(self, childObj):
        self.children.append(childObj)
    
    def getChildrenList(self):
        return self.children
    
        
         