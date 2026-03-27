class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    temp_first = Node(0)
    temp_second = Node(0)

    first_tail = temp_first
    second_tail = temp_second

    current = head
    index = 0

    while current is not None:
        if index % 2 == 0:
            first_tail.next = current
            first_tail = first_tail.next
        else:
            second_tail.next = current
            second_tail = second_tail.next

        current = current.next
        index += 1

    first_tail.next = None
    second_tail.next = None

    return Context(temp_first.next, temp_second.next)
