class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr):
    """
    func
    """
    if list_repr == "None":
        return None

    parts = list_repr.split(" -> ")
    values = parts[:-1]

    head = None

    for value in reversed(values):
        head = Node(int(value), head)

    return head
