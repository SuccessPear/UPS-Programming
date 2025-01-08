class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def traversal(node: Node, node_list):
    if node is None:
        return
    
    node_list.append(node.left)
    traversal(node.left)
    traversal(node.right)

def assign_node_parent(head:Node, parent_head:Node):
    head.parent = parent_head
    
    if head.left is not None:
        assign_node_parent(head.left, head)
        
    if head.right is not None:
        assign_node_parent(head.right, head)

def is_equal_tree(node1:Node, node2:Node):
    parent1 = node1.parent
    parent2 = node2.parent
    if parent1.val != parent2.val:
        return False
    
    if parent1.val  

def find_largest_common_subtree(head1: Node, head2: Node):
    # find the common node left leaves pairs
    left_list_1 = []
    left_list_2 = []
    traversal(head1, left_list_1)
    traversal(head2, left_list_2)
    
    common_node_pair = []
    for node1 in left_list_1:
        for node2 in left_list_2:
            if node1.data == node2.data:
                common_node_pair.append([node1, node2])
                
    # find the common subtrees
    for [node1, node2] in common_node_pair:
        
    
    # find the largest common tree