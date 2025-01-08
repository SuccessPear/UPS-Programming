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

def find_middle(llist):
    head1 = llist.head
    head2 = llist.head
    
    if head2.next is None:
        return head2
    head2 = head2.next
    if head2.next is None:
        return head2
    head2 = head2.next
    length = 2
    
    while (head2):
        head1 = head1.next
        if head2.next is not None:
            head2 = head2.next
            head2 = head2.next
            length += 2
        else:
            head2 = head2.next
            length += 1
    if length % 2 == 0:
        return head1.next
    return head1
    
def main():
    llist = LinkedList()
    llist.append(8)
    llist.append(2)
    llist.append(4)
    llist.append(9)
    llist.append(5)
    llist.append(3)
    llist.append(10)
    llist.append(7)
    llist.append(3)
    
    node = find_middle(llist)
    print(node.val)
    
main()