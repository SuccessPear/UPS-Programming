import operator
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
}
def traverse(head, stack):
    if head is None:
        return
    traverse(head.left, stack)
    traverse(head.right, stack)
    
    if head.data not in operators:
        stack.append(head.data)
    else:
        x = stack.pop(-1)
        y = stack.pop(-1)
        stack.append(operators[head.data](int(x), int(y)))

def is_valid_statement():
    head  = Node('-')
    node1 = Node('+')
    node2 = Node('4')
    node3 = Node('0')
    node4 = Node('*')
    node5 = Node('2')
    node6 = Node('4')
    
    head.left = node1
    head.right = node2
    node1.left = node3
    node1.right = node4
    node4.left = node5
    node4.right = node6
    
    stack = []
    traverse(head, stack)
    return stack

print(is_valid_statement())