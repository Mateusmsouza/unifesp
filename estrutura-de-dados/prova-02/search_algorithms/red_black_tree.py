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
    change_color(node)
    change_color(node.left)
    change_color(node.right)

def right_rotation(node: Node):
    pB = node.left
    node.left = node.right
    pB.right = node
    return pB

def left_rotation(node: Node):
    pB = node.right
    node.right = node.left
    pB.left = node
    return pB

def balance_left(node: Node, nodeB: Node, nodeC: Node):
    print('balancing left')
    if is_red(nodeC.right):
        swap_colors(nodeC)
        return nodeC
    else:
        if(nodeB == node.right):
            #print('+--------------+')
            node = left_rotation(node)
            nodeC.left = node
            #print('+--------------+')
            #printTreeInterface(node)
            #print('+--------------+')
        #else:
        #printTreeInterface(nodeC)
        change_color(node)
        change_color(nodeC)
        #print('+--------------+')
        right_rotation(nodeC)

        return node

def balance_right(node: Node, nodeB: Node, nodeC: Node):
    print('balancing right')
    printTreeInterface(nodeC)
    if is_red(nodeC.left):
        swap_colors(nodeC)
        return nodeC
    else:
        if(nodeB == node.left):
            node = right_rotation(node)
            nodeC.right = node
        #else:
        change_color(node)
        change_color(nodeC)
        left_rotation(nodeC)
        return node

def balance_node(node: Node, nodeB: Node, nodeC: Node):
    if nodeC is not None and is_red(node) and is_red(nodeB):
        if node == nodeC.left:
            node = balance_left(node, nodeB, nodeC)
            return node
        else:
            node = balance_right(node, nodeB, nodeC)
            printTreeInterface(node)
            return node
    return node

def recursive_insert(node: Node, nodeB: Node, value: int):

    if not node:
        return Node(value=value), True
    elif value < node.value:
        print('going to left')
        temp_node, base_case = recursive_insert(node.left, node, value)
        if base_case:
            node.left = temp_node
        else:
            node = temp_node
        node = balance_node(node, node.left, nodeB)
        #printTreeInterface(node.left)
        print(f'returning from left {node} - {hex(id(node))} - {node.value}')
        return node, False
    elif value > node.value:
        print('going to right')
        temp_node, base_case = recursive_insert(node.right, node, value)
        if base_case:
            node.right = temp_node
        else:
            node = temp_node
        node = balance_node(node, node.right, nodeB)
        print(f'returning from right {node} - {hex(id(node))} - {node.value} and son is {node.right} - {hex(id(node.right))} - {node.right.value}')
        #printTreeInterface(node)
        return node, False
    else:
        print(f'returning from else {node} - {hex(id(node))} - {node.value}')
        return node, False

def insert(root: Node, value: int):
    print(f'main {root.value if root else root}')
    print(hex(id(root)))
    root, _ = recursive_insert(root, None, value)
    print(hex(id(root)))
    print(f'main {root.value}')
    root.color = 'black'
    return root

def main():
    # root = Node(value=5)
    # second = Node(value=2)
    # second.color = 'red'
    # root.left = second

    root = insert(None, 5)
    root = insert(root, 2)
    
    root = insert(root, 3)
    root = insert(root, 7)
    print('=============================')
    root = insert(root, 6)
    printTreeInterface(root)

if __name__ == '__main__':
    main()