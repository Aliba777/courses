from ADT.tree import BinaryTree
llist = []
def preorder(node):
	if node != None:
		llist.append(node.getRootVal())
	if (node.leftChild != None):
		preorder(node.leftChild)
	if (node.rightChild != None):
		preorder(node.rightChild)

def printer(llist):
	f = open("stored.txt", 'w')
	for k in llist:
		f.write(k + ' ')

tree = BinaryTree('cat')
tree.insertLeft('apple')
tree.insertRight('pull')
tree.getLeftChild().insertRight('but')
tree.getRightChild().insertLeft('line')
tree.getRightChild().insertRight('say')
tree.getRightChild().getLeftChild().insertLeft('food')
tree.getRightChild().getLeftChild().insertRight('me')

preorder(tree)
printer(llist)





