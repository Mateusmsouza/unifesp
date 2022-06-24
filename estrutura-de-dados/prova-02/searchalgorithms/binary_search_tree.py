class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if not root:
        return Node(key)

    if root.value == key:
        return root
    elif root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root