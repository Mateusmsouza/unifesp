class Node:
    def __init__(self, value, letter = ''):
        self.left = None
        self.right = None
        self.value = value
        self.letter = letter

def height(root):
    if not root:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


def insert_bst(root, value, letter = ''):
    if not root:
        return Node(value, letter)
    elif value < root.value:
        root.left = insert_bst(root.left, value, letter)
    elif value > root.value:
        root.right = insert_bst(root.right, value, letter)
    return root

def sucessor(root, right):
    if right.left:
        found_sucessor = sucessor(root, right.left)
        if found_sucessor:
            right.left = None
    else:
        root.value = right.value
        root.letter = right.letter
        print(root.letter)
        return True

def predecessor(root, left):
    if left.right:
        found_predecessor =  predecessor(root, left.right)
        if found_predecessor:
            left.right = None
    else:

        root.value = left.value
        root.letter = left.letter
        print(left.letter)
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