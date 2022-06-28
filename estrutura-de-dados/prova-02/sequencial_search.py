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

if __name__ == '__main__':
    root = Node(1)
    insert(root, 32)
    insert(root, 33)
    printList(root)
    remove(root, 32)
    printList(root)