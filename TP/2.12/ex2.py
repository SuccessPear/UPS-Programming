# Idea: we use the technique Inorder traversal to get a sequence.
# If this is a valid binary search tree then the obtained sequence must be in accendding order
# Return False and break if the next value is smaller than the last value in the list (to safe time)
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def is_valid_BST(root: Node, pre_traversal_list: list):
    # Purpose of check1 and check2 is to stop the recursion as soon as it meets a value
    # that doesn't fit in the accending list, dont need to check further, return False
    
    # Check the left child
    if root.left is not None:
        check1 = is_valid_BST(root.left, pre_traversal_list)
        if check1 == False:
            return False
    
    # if the value of current node is not greater than the last value in pre_traversal_list,
    # return False
    if len(pre_traversal_list) > 0:
        if root.val <= pre_traversal_list[-1]:
            return False
    pre_traversal_list.append(root.val)
    
    # check the right child
    if root.right is not None:
        check2 = is_valid_BST(root.right, pre_traversal_list)
        if check2 == False:
            return False

def check_valid_BST(root: Node):
    if root is None:
        return False
    
    if is_valid_BST(root, []) == False:
        return False
    return True

n1 = Node(4)
n2 = Node(2)
n3 = Node(6)
n4 = Node(1)
n5 = Node(3)
n6 = Node(5)
n7 = Node(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

print(check_valid_BST(n1))