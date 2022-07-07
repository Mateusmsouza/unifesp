from model.report import Report
import time

report = None
ALGO_NAME: str = 'BINARY_TREE_SEARCH'
comparisions_insert = 0
comparisions_search = 0
comparisions_remove = 0


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    
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
    if node is None:
        comparisions_insert -= 2
        return Node(value)
    elif value < node.value:
        comparisions_insert -= 1
        node.left = insert(node.left, value)
        return node
    elif value > node.value:
        node.right = insert(node.right, value)
        return node
    else:
        # value is already in the tree
        return node

def sucessor(node: Node, sub_node: Node):
    global comparisions_remove
    comparisions_remove += 1
    if sub_node.left is not None:
        return sucessor(node, sub_node.left)
    else:
        return sub_node


def remove(node: Node, value: int):
    global comparisions_remove
    comparisions_remove += 3
    if not node:
        comparisions_remove -= 2
        return None
    elif value < node.value:
        comparisions_remove -= 1
        node.left = remove(node.left, value)
        return node
    elif value > node.value:
        node.right = remove(node.right, value)
        return node
    else:
        comparisions_remove += 2
        if node.left == None:
            comparisions_remove -= 1
            return node.right
        elif node.right == None:
            return node.left
        else:
            return sucessor(node, node.right)

def test_with_array(array, size, scenario):
    global report
    global comparisions_insert
    global comparisions_search
    global comparisions_remove


    print(f'[{ALGO_NAME}] - initializing tests for array scenario/size: {scenario}/{size}')
    report = Report(array_size=size, algo_name=ALGO_NAME, array_type=scenario)
    root = Node(array[0])

    print(f'[{ALGO_NAME}] - testing insertion')
    for i in array:
        start_time = time.process_time()
        insert(root, i)
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
