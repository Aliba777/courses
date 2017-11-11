class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

def priority(ch):
  if(ch == '('):
    return(0);
  
  if(ch == '+' or ch == '-'):
    return(1);
  
  if(ch == '*' or ch == '/' or ch == '%'):
    return(2);
 
  return(3);

def operations(a, b, ch):
	error = "Division by zero\n"	
	if ch == '+':
		return a + b
	elif ch == '-':
		return a - b
	elif ch == '*':
		return a * b
	elif ch == '/':
		if (b != 0):
			return a // b
		else:
			return error
def isSign(a):
	if a in ['+','-','*','/']:
		return True

def toPostfix(infix):
	operators = Stack()
	infix_list = []
	tmp = ''
	for i in infix:
		if (i in '1234567890'):
			tmp += i
		elif (i in '+-*/()'):
			if tmp != '':
				infix_list.append(tmp)
			infix_list.append(i)
			tmp = ''
	infix_list.append(tmp)
	postfix_list = []  

	for i in infix_list:
		if i.isdigit():
			postfix_list.append(i)
		elif i == '(':
			operators.push(i)
		elif i == ')':
			if not operators.isEmpty():
				top = operators.pop()
				while top != '(':
					postfix_list.append(top)
					top = operators.pop()
		elif isSign(i):
			while (not operators.isEmpty() \
					and priority(operators.peek())>=priority(i)):
				postfix_list.append(operators.pop())
			operators.push(i)

	while not operators.isEmpty():
		postfix_list.append(operators.pop())
	return postfix_list

infix = input("Please, enter a fully parenthesized infix form: ")
def postfix_evaluation(postfix):
	operand = Stack()
	for i in postfix:
		if i.isdigit():
			operand.push(int(i))
		elif isSign(i):
			int2 = operand.pop()
			int1 = operand.pop()
			operand.push(operations(int1, int2, i))
	return operand.peek()

print("The result is:", postfix_evaluation(toPostfix(infix)))

input("\nPress any key to exit.\n")