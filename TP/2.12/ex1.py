class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkSymmetricTree(root1: Node, root2: Node):
    # Purpose of 2 check variables is to break the recursion as soon as possible
    check1 = True
    check2 = True
    # If value of the 2 root is not equal then return False
    if root1.val != root2.val:
        return False
    
    # If the left of root1 and right of root2, one is None and one is not the return False
    if (root1.left is None and root2.right is not None) or (root1.left is not None and root2.right is None):
        return False
    # Same for right of root 1 and left of root2
    if (root1.right is None and root2.left is not None) or (root1.right is not None and root2.left is None):
        return False

    if root1.left is not None and root2.right is not None:
        check1 = checkSymmetricTree(root1.left, root2.right)
    if root1.right is not None and root2.left is not None:
        check2 = checkSymmetricTree(root1.right, root2.left)
    
    return check1 and check2
        
def symmetric_tree(root):
    if root.left is None:
        # if this tree contain only the root and no children then return True
        if root.right is None:
            return True
        else:
            return False
    if root.right is None:
        return False
    
    return checkSymmetricTree(root.left, root.right)

n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(3)
n5 = Node(4)
n6 = Node(4)
n7 = Node(3)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

print(symmetric_tree(n1))