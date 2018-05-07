class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


head = Node(1)
head.next = Node(4)
head.next.next = Node(2)


def has_four(head):
    if head.next:
        return has_four(head.next)
    if head.data == 4:
        return True
    else:
        return False


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(4)
    head.next.next = Node(2)
    print(has_four(head))
