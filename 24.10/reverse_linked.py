class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

def reverse_linkedlist(node: Node):
    previous = None
    while (node):
        next = node.next
        node.next = previous
        previous = node
        node = next
    return previous

def print_list(node):
    while(node):
        print(node.val)
        node = node.next        
def main():
    llist = LinkedList()
    llist.append(8)
    llist.append(9)
    llist.append(2)
    llist.append(4)
    llist.append(5)
    llist.append(3)
    llist.append(10)
    llist.append(7)
    
    node = reverse_linkedlist(llist.head)
    print_list(node)
    
main()