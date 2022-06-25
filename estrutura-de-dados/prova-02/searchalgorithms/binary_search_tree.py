class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def height(root):
    if not root:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


def insert_bst(root, value):
    if not root:
        return Node(value)
    elif value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)
    return root

def sucessor(root, right):
    if right.left:
        found_sucessor = sucessor(root, right.left)
        if found_sucessor:
            right.left = None
    else:
        root.value = right.value
        return True

def predecessor(root, left):
    if left.right:
        found_predecessor =  predecessor(root, left.right)
        if found_predecessor:
            left.right = None
    else:

        root.value = left.value
        return True

def remove_bst(root, value):
    if not root:
        return False
    elif value < root.value:
        remove_bst(root.left, value)
    elif value > root.value:
        remove_bst(root.right, value)
    else:
        temp = root
        if not root.left:
            root = temp.right
        elif not root.right:
            root = temp.left
        else:
            predecessor(root, root.left)


def search_bst(root, value):
    if not root:
        return None
    elif root.value < value:
        return search_bst(root.right, value)
    elif root.value > value:
        return search_bst(root.left, value)
    else:
        return root