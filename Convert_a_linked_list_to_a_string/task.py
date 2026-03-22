"""task 1"""
def stringify(node):
    """
    func stringify
    """
    if node is None:
        return "None"
    result = []
    current = node

    while current is not None:
        result.append(str(current.data))
        current = current.next

    result.append("None")
    return " -> ".join(result)
