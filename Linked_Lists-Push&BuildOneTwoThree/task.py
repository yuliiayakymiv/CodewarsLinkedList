"""
func
"""
class Node:
    """node"""
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """
    Створює новий вузол з даними data і робить його головою списку
    """
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """
    Створює список 1 -> 2 -> 3 -> None
    """
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)

    return head
