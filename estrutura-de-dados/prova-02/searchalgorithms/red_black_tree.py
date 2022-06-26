from model.nodes import RedBlackNode

def is_black(node):
    return node is not None and node.color == 'black'

def is_red(node):
    return node is not None and node.color == 'red'

def invert_color(node):
    if not node:
        return

    if node.color == 'red':
        node.color = 'black'
    elif node.color == 'black':
        node.color = 'red'

def change_colors(node):
    invert_color(node)
    invert_color(node.left)
    invert_color(node.right)

def right_rotation(pA):
    pB = pA.left
    pA.left = pB.right
    pB.right = pA
    pA = pB


def left_rotation(pA):
    pB = pA.right
    pA.right = pB.left
    pB.left = pA
    pA = pB

def balance_left(pA, pB, pC):
    if is_red(pC.right):
        change_colors(pC)
    else:
        if pB == pA.right:
            left_rotation(pA)
        change_colors(pA)
        change_colors(pC)
        right_rotation(pC)

def balance_right(pA, pB, pC):
    if is_red(pC.left):
        change_colors(pC)
    else:
        if (pB == pA.left):
            right_rotation(pA)
        change_colors(pA)
        change_colors(pC)
        left_rotation(pC)

def balance_node(pA, pB, pC):
    if pC and is_red(pA) and is_red(pB):
        if pA == pC.left:
            balance_left(pA, pB, pC)
        else:
            balance_right(pA, pB, pC)

def black_height(node):
    if not node:
        return 0
    
    left_height = black_height(node.left)
    right_height = black_height(node.right)

    return max(left_height, right_height) + 1 if is_black(node) else 0

def red_black_tree(node):
    if not node:
        return True

    if not red_black_tree(node.left):
        return False

    if not red_black_tree(node.right):
        return False

    if is_red(node) and not is_black(node.left) or not is_black(node.right):
        return False
    
    if black_height(node.left) != black_height(node.right):
        return False    
    return True

def insertRecursive(pA, pC, value):
    if not pA:
        return RedBlackNode(value, 'red')
    elif value < pA.value:
        pA.left = insertRecursive(pA.left, pA, value)
        balance_node(pA, pA.left, pC)
        return pA.left
    elif value > pA.value:
        pA.right = insertRecursive(pA.right, pA, value)
        balance_node(pA, pA.right, pC)
        return pA.right

def insert_rbt(pRaiz, value):
    pRaiz = insertRecursive(pRaiz, None, value)
    pRaiz.color = 'black'
    return pRaiz
