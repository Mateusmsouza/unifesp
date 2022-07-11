from model.report import Report
import time

report = None
ALGO_NAME: str = 'AVL_TREE_SEARCH'
comparisions_insert = 0
comparisions_search = 0
comparisions_remove = 0

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def height(node: Node):
    global comparisions_insert
    comparisions_insert += 1
    if not node:
        return -1
    return max(height(node.left), height(node.right)) + 1

def balance_factor(node: Node):
    global comparisions_insert
    comparisions_insert += 1
    if not node:
        return 0
    return height(node.left) - height(node.right)

def is_avl_tree(node: Node):
    if not node:
        return True

    if not is_avl_tree(node.left):
        return False

    if not is_avl_tree(node.right):
        return True
    node_balance_factor = balance_factor()

    if node_balance_factor > 1 or node_balance_factor < -1:
        return False
    return True

def left_left_rotation(node: Node):
    left = node.left
    node.left = left.right
    left.right = node
    node = left
    return node

def right_right_rotation(node: Node):
    right = node.right
    node.right = right.left
    right.left = node
    node = right
    return node

def left_right_rotation(node: Node):
    pB = node.left
    pC = pB.right
    pB.right = pC.left
    pC.left = pB
    node.left = pC.right
    pC.right = node
    node = pC
    return node

def right_left_rotation(node: Node):
    pB = node.right
    pC = pB.left
    pB.left = pC.right
    pC.right = pB
    node.right = pC.left
    pC.left = node
    node = pC
    return node

def balance_left(node: Node):
    global comparisions_insert
    comparisions_insert += 2
    node_balance_factor = balance_factor(node.left)
    if node_balance_factor > 0:
        comparisions_insert -= 1
        node = left_left_rotation(node)
        return node
    elif node_balance_factor < 0:
        node = left_right_rotation(node)
        return node
    return node

def balance_right(node: Node):
    global comparisions_insert
    comparisions_insert += 2
    node_balance_factor = balance_factor(node.right)
    if node_balance_factor < 0:
        comparisions_insert -= 1
        node = right_right_rotation(node)
        return node
    elif node_balance_factor > 0:
        node = right_left_rotation(node)
        return node
    return node

def balance_node(node: Node):
    global comparisions_insert
    comparisions_insert += 2
    
    node_balance_factor = balance_factor(node)
    if node_balance_factor > 1:
        comparisions_insert -= 1
        return balance_left(node)
    elif node_balance_factor < -1:
        return balance_right(node)
    return node
    
def search(node: Node, value: int):
    global comparisions_search

    comparisions_search += 3
    if not node:
        comparisions_search -= 2
        return None
    elif value < node.value:
        comparisions_search -= 1
        return search(node.left, value)
    elif value > node.value:
        return search(node.right, value)
    else:
        return node

def insert(node: Node, value: int):
    global comparisions_insert
    comparisions_insert += 3
    if not node:
        comparisions_insert -= 2
        return Node(value)
    elif value < node.value:
        comparisions_insert -= 1
        node.left = insert(node.left, value)
        node = balance_node(node)
        return node
    elif value > node.value:
        node.right = insert(node.right, value)
        node = balance_node(node)
        return node
    else:
        return node
        

def sucessor(node: Node, sub_node: Node):
    global comparisions_remove
    comparisions_remove += 1
    if sub_node.left:
        node, delete_left = sucessor(node, sub_node.left)
        if delete_left:
            sub_node.left = None
        return node, False
    else:
        node.value = sub_node.value
        return node, True

def remove(node: Node, value: int):
    global comparisions_remove
    
    comparisions_remove += 3
    if not node:
        comparisions_remove -= 2
        return node
    elif value < node.value:
        comparisions_remove -= 1
        return remove(node.left, value)
    elif value > node.value:
        return remove(node.right, value)
    else:
        comparisions_remove += 2
        if not node.left:
            comparisions_remove -= 1
            node = node.right
        elif not node.right:
            node = node.left
        else:
            node, _ = sucessor(node, node.right)
        return node

def test_with_array(array, size, scenario):
    global report
    global comparisions_insert
    global comparisions_search
    global comparisions_remove


    print(f'[{ALGO_NAME}] - initializing tests for array scenario/size: {scenario}/{size}')
    report = Report(array_size=size, algo_name=ALGO_NAME, array_type=scenario)
    root = None

    print(f'[{ALGO_NAME}] - testing insertion')
    for i in array:
        start_time = time.process_time()
        root = insert(root, i)
        end_time = time.process_time()
        report.time_execution_insert.append(end_time - start_time)
        report.comparisions_insert.append(comparisions_insert)
    comparisions_insert = 0
    report.consolidate_insertion()

    print(f'[{ALGO_NAME}] - testing search')
    for i in array:
        start_time = time.process_time()
        search(root, i)
        end_time = time.process_time()
        report.time_execution_search.append(end_time - start_time)
        report.comparisions_search.append(comparisions_search)
    comparisions_search = 0
    report.consolidate_search()

    print(f'[{ALGO_NAME}] - testing remove')
    for i in array:
        start_time = time.process_time()
        remove(root, i)
        end_time = time.process_time()
        report.time_execution_remove.append(end_time - start_time)
        report.comparisions_remove.append(comparisions_remove)
    comparisions_remove = 0

    report.consolidate_remove()
    report.create_report()