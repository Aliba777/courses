import math

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.p = None
		
count =  1
height = 0			
def createFullTree(node):
	global count 
	global height
	if (count >= height):
		return
	count += 1
	node.l = Node(1)
	node.l.p = node
	node.r = Node(1)
	node.r.p = node
	createFullTree(node.l)
	createFullTree(node.r)
	count -= 1

arr = []
arr2 = []
def readA():
	global arr2
	f = open("data-A.txt", 'r')
	for l in f:
		s = l.strip()
		arr2.append(s)

def readB():
	global arr
	f = open("data-B.txt", 'r')
	
	for l in f:
		s = l.strip()
		arr.append(s)

index = 0
def preorder(node):
	global index
	index += 1
	node.v = arr[index-1]
	if (node.l != None):
		preorder(node.l)
	if (node.r != None):
		preorder(node.r)
arr3 = []
def preorder1(node):
	global arr3
	arr3.append(node.v)
	if (node.l != None):
		preorder1(node.l)
	if (node.r != None):
		preorder1(node.r)

def postorder(node):
	global index
	if (node.l != None):
		postorder(node.l)
	if (node.r != None):
		postorder(node.r)
	index += 1
	node.v = arr2[index-1]

def postorder1(node):
	global arr3
	if (node.l != None):
		postorder1(node.l)
	if (node.r != None):
		postorder1(node.r)
	arr3.append(node.v)

def calc_height_b():
	global height
	f = open("data-B.txt", 'r')
	count = 0
	for l in f:
		count += 1
	
	height = math.log2(count+1)
	f.close()


def calc_height_a():
	global height
	f = open("data-A.txt", 'r')
	count = 0
	for l in f:
		count += 1
	
	height = math.log2(count+1)
	f.close()

def read(node):
	while True:
		play(node)
		if (query("Shall we play again?") == 'N'):
			break
	print("Thanks for teaching me a thing or two")

def play(node):
	while (node.l != None or node.r != None):
		kt = query(node.v)
		if kt == 'Y':
			node = node.l
		elif kt == 'N':
			node = node.r
		elif kt == 'U':
			play(node)
			quit()
	print("My guess is " + node.v + ".")
	t = query("Am I Right?")
	if (t == 'N'):
		learn(node)
	elif t == 'Y':
		print("I knew it all along!!!111")
	else:
		while True:
			choice = input("Is the question " + node.p.v + " where you made a mistake? [Y or N or U] ").upper()
			node1 = Node(1)
			if choice == 'Y':
				if(node.p.l == node):
					node1 = node.p.r
					play(node1)
					quit()
				else:
					node1 = node.p.l
					play(node1)
					quit()
			if (choice == 'N'):
				node1 = node.p.p
				play(node1)
				quit()

			


def learn(node):
	ans = input("I give up. What are you? ")
	animal1 = Node(ans)
	animal2 = node.v
	print("Please type a yes/no question that will distinguish")
	ques = input("Your question: ")
	node.v = ques
	if (query("As a " + ans + ", " + ques)):
		node.l = Node(animal1.v)
		node.r = Node(animal2)
	else:
		node.l = Node(animal2)
		node.r = Node(animal1.v)




def query(s):
	ans = input(s + " [Y or N or U]").upper()
	while(ans != "Y" and ans != "N" and ans != "U"):
		ans = input("Invalid response. Please type Y or N or U").upper()
	return ans

def printer(fname):
	f = open(fname +".txt", 'w')
	for k in arr3:
		f.write(k + "\n")

def main():
	RootNode = Node(1)

	choice = input("Which way dear TA: 'A' or 'B'? ").upper()
	if choice == 'A':
		calc_height_a()
		createFullTree(RootNode)
		readA()
		postorder(RootNode)
		read(RootNode)
		postorder1(RootNode)
		printer("data-A")
	if choice == 'B':
		calc_height_b()
		createFullTree(RootNode)
		readB()
		preorder(RootNode)
		read(RootNode)
		preorder1(RootNode)
		printer("data-B")
main()
