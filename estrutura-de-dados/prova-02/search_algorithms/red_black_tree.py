#from model.report import Report
import time

report = None
ALGO_NAME: str = 'RED_BLACK_TREE_SEARCH'
comparisions_insert = 0
comparisions_search = 0
comparisions_remove = 0

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.color = 'red'
        self.left = None
        self.right = None

def printTree(prefix, node, isLeft):
    if node != None:
        print(prefix, end="")
        print("├──" if isLeft else "└──", end="")
        print(f'{node.value if node else None} - [{node.color if node else None}]')

        printTree( prefix + ("│   " if isLeft else "    "), node.left, True)
        printTree( prefix + ("│   " if isLeft else "    "), node.right, False)

def printTreeInterface(node):
    printTree("", node, False);

def is_black(node: Node):
    return node is None or node.color == 'black'

def is_red(node: Node):
    return node is not None and node.color == 'red'

def black_height(node: Node):
    if not node:
        return 0
    black_height_left, black_height_right = black_height(node.left), black_height(node.right)
    return max(black_height_left, black_height_right) + is_black(node)

def is_red_black_tree(node: Node):
    if not node:
        return True
    if not is_red_black_tree(node.left):
        return False
    if not is_red_black_tree(node.right):
        return False
    if is_red(node) and (not is_black(node.left) or not is_black(node.right)):
        return False
    if black_height(node.left) != black_height(node.right):
        return False

    return True

def change_color(node: Node):
    if node.color == 'red':
        node.color = 'black'
    else:
        node.color = 'red'
    return node

def swap_colors(node: Node):
    node = change_color(node)
    node.left = change_color(node.left)
    node.right = change_color(node.right)
    return node

def right_rotation(node: Node):
    pB = node.left
    node.left = node.right
    pB.right = node
    node = pB
    return node

def left_rotation(node: Node):
    pB = node.right
    node.right = node.left
    pB.left = node
    node = pB
    return node

def balance_left(node: Node, nodeB: Node, nodeC: Node):
    print('balancing left')
    if is_red(nodeC.right):
        swap_colors(nodeC)
    else:
        if(nodeB == node.right):
            print('+--------------+')
            printTreeInterface(node)
            node = left_rotation(node)
            print('+--------------+')
            printTreeInterface(node)
            print('+--------------+')
        #else:
        change_color(node)
        change_color(nodeC)
        node = right_rotation(nodeC)
        print('+-------AQUI-------+')
        printTreeInterface(node)
        print('+--------------+')

    return node

def balance_right(node: Node, nodeB: Node, nodeC: Node):
    if is_red(node.left):
        swap_colors(nodeC)
    else:
        if(nodeB == node.left):
            node = right_rotation(node)
        #else:
        change_color(node)
        change_color(nodeC)
        node = left_rotation(nodeC)

    return node

def balance_node(node: Node, nodeB: Node, nodeC: Node):
    if nodeC is not None and is_red(node) and is_red(nodeB):
        if node == nodeC.left:
            print(f'calling balance left with {node}, {nodeB} and {nodeC}')
            node = balance_left(node, nodeB, nodeC)
        else:
            node = balance_right(node, nodeB, nodeC)
    return node

def recursive_insert(node: Node, nodeB: Node, value: int):

    if not node:
        return Node(value=value)
    elif value < node.value:
        node.left = recursive_insert(node.left, node, value)
        node = balance_node(node, node.left, nodeB)
        return node
    elif value > node.value:
        node.right = recursive_insert(node.right, node, value)
        # print(f'{node.value}')
        # print(f'{nodeB} - {nodeB.value}')
        node = balance_node(node, node.right, nodeB)
        return node
    return node

def insert(root: Node, value: int):
    root = recursive_insert(root, None, value)
    root.color = 'black'
    #print(f'{root.color} - {root.value}')
    return root

def main():
    root = insert(None, 5)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 7)
    #root = insert(root, 6)
    # print(f'{root.value} [{root.color}]')
    # print(f'>>>>{root.right}')
    # print(f'>>>>{root.left.value} [{root.left.color}]')
    # print(f'>>>>>>>>{root.left.left.value} [{root.left.left.color}]')
    # print(f'>>>>>>>>{root.left.right}')
    # print(f'>>>>>>>>>>>>>>>>{root.left.left.left}')
    # print(f'>>>>>>>>>>>>>>>>{root.left.left.right.value} [{root.left.left.right.color}]')
    # print('--------')
    # print(f'>>>>>>>>>>>>>>>>{root.left.left.right.left.left.value}')
    # print(f'>>>>>>>>>>>>>>>>{root.left.left.right.left.right}')
    printTreeInterface(root)

if __name__ == '__main__':
    main()