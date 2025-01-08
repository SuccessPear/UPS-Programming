class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None
node_list = []
def create_BBT(head, left, right):
    if head.data - left > 1:
        left_node = Node(int((head.data + left)/2))
        node_list.append(left_node)
        head.left = left_node
        create_BBT(left_node, left, head.data)
    if right - head.data > 1:
        right_node = Node(int((head.data + right)/2))
        node_list.append(right_node)
        head.right = right_node
        create_BBT(right_node, head.data, right)

def traverse_tree(head, count):
    if head is None:
        return
    count[0] += 1
    traverse_tree(head.left, count)
    traverse_tree(head.right, count)

def create_BBT_tree_1_to_n(n):
    head = Node(int(n/2))
    node_list.append(head)
    create_BBT(head, 0, n+1)
    count = [0]
    traverse_tree(head, count)
    for i in node_list:
        print(i.data)
    print(len(node_list))
    
create_BBT_tree_1_to_n(20)