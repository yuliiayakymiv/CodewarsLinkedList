# from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    temp = Node(0)
    temp.next = head

    prev = temp
    current = head

    while current is not None and current.next is not None:
        first = current
        second = current.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first
        current = first.next

    return temp.next
