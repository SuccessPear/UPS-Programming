class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder_traversal(root: Node):
    left = False
    right = False
    if(root.left is not None):
        left = postorder_traversal(root.left)
    if(root.right is not None):
        right = postorder_traversal(root.right)
    
    if not left:
        root.left = None
    if not right:
        root.right = None
    if not left and not right and root.val == 0:
        return False
    return True 

def print_tree(root: Node):
    if (root.left is not None):
        print_tree(root.left)
    if (root.right is not None):
        print_tree(root.right)
    print(root.val)
    
def find_subtree(root):
    tmp = root
    postorder_traversal(root)
    print_tree(tmp)

root = Node(1)
node1 = Node(0)
node2 = Node(0)
node3 = Node(0)
node4 = Node(1)
node5 = Node(0)
node6 = Node(1)


root.right = node1
root.right = node4
node1.left = node2
node1.right = node3
node4.left = node5
node4.right = node6

find_subtree(root)
