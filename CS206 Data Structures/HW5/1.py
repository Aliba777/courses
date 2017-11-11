from ADT.stack import Stack
from ADT.tree import BinaryTree
    
def isSign(value): 
    if value in ['+','-','*','/']:
        return True
    return False

# isFloat function
# http://stackoverflow.com/questions/2356925/how-to-check-whether-string-might-be-type-cast-to-float-in-python
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
     
def expression_to_list(expression):
    exp_l = []
    tmp = ''
    for i in expression:
        if (i in '1234567890') or (i=='.'):
            tmp += i
        elif isSign(i) or (i in '()'):
            if tmp != '':
                exp_l.append(tmp)
            exp_l.append(i)
            tmp = ''
    return exp_l

def BuildTree(expression_l):
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current = tree
    
    for i in expression_l:
        if i == '(':
            current.insertLeft('')
            left = current.getLeftChild()
            stack.push(current)
            current = left
        elif i.isdigit() or isFloat(i):
            current.setRootVal(i)
            current = stack.pop()
        elif isSign(i):
            current.setRootVal(i)
            current.insertRight('')
            stack.push(current)
            current = current.getRightChild()
        elif i == ')':
            current = stack.pop()
        else:
            raise ValueError            
    return tree

        
def postorder(node):
    if node:
        postorder(node.getLeftChild())
        postorder(node.getRightChild())
        post_l.append(node.getRootVal())
        
def op_result(a,b,op):
    if op == '+':
        return float(a) + float(b)
    elif op == '-':
        return float(a) - float(b)
    elif op == '*':
        return float(a) * float(b)
    elif op == '/':
        if float(b) == 0:
            return "Division by zero"
        return float(a) / float(b)       
    
def evaluation(post_l):
    expr = Stack()
    for i in post_l:
        if i.isdigit() or isFloat(i):
            expr.push(i)
        elif isSign(i):
            b=expr.pop()
            a=expr.pop()
            expr.push(op_result(a,b,i))
    print ('The result is:', expr.top())
    return expr.top()
                
def main(expression):
    exp = expression_to_list(expression)

    tree = BuildTree(exp)
    global post_l
    post_l = []
    postorder(tree)
    evaluation(post_l)

while True:
    expression = input('Print an expression: ')
    main(expression)