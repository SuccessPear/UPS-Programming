class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_tree(root: Node):
    print(root.val)
    if (root.left is not None):
        print_tree(root.left)
    if (root.right is not None):
        print_tree(root.right)
        
def construct_tree(descriptions):
    # element in dictionary will be like this:
    # key: node.val
    # value: node, hasparent
    tree_dictionary = {}
    for [parent, child, isLeft] in descriptions:
        
        if child not in tree_dictionary:
            tree_dictionary[child] = [Node(child), True]
        if parent not in tree_dictionary:
            tree_dictionary[parent] = [Node(parent), False]
        
        tree_dictionary[child][1] = True
        if isLeft:
            tree_dictionary[parent][0].left = tree_dictionary[child][0]
        else:
            tree_dictionary[parent][0].right = tree_dictionary[child][0]
    root = None
    for node in tree_dictionary:
        if tree_dictionary[node][1] == False:
            root = tree_dictionary[node][0]
            break
    
    print_tree(root)
    
descriptions = [[20,15,1], [20,17,0], [50,20,1], [50,80,0], [80,19,1]]
construct_tree(descriptions)
