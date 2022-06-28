from model.report import Report

REPORT = None

class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value

def search(root: Node, value: int):
    '''returns [Node found, Node parent]'''
    while root != None:
        if root.value == value:
            return root
        root = root.next
    return None

def insert(root: Node, value: int):
    if not root:
        return False

    while root.next is not None:
        if root.next.value == value:
            return False
        root = root.next
    root.next = Node(value)
    return True

def remove(root: Node, value: int):
    if not root:
        return False

    while root.next is not None:
        if root.next.value == value:
            root.next = root.next.next
            return True
        root = root.next
    return False

def printList(root):
    while root != None:
        print(f'{root.value} -> ', end='')
        root = root.next

def test_with_array(array, size):
    REPORT = Report(array_size=size)
    root = Node(array[0])

    for i in array:
        insert(  )