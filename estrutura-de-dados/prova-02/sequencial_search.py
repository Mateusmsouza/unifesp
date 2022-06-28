from model.report import Report
import time

report = None
ALGO_NAME: str = 'SEQUENCIAL_SEARCH'

class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value

def search(root: Node, value: int):
    '''returns [Node found, Node parent]'''
    while root != None:
        if root.value == value:
            return root
        report.comparisions_search += 2
        root = root.next
    return None

def insert(root: Node, value: int):
    report.comparisions_insert += 1
    if not root:
        return False

    while root.next is not None:
        if root.next.value == value:
            return False
        report.comparisions_insert += 2
        root = root.next
    root.next = Node(value)
    return True

def remove(root: Node, value: int):
    report.comparisions_remove += 1
    if not root:
        return False

    while root.next is not None:
        if root.next.value == value:
            root.next = root.next.next
            return True
        root = root.next
    return False

def test_with_array(array, size, scenario):
    global report
    print(f'[{ALGO_NAME}] - initializing tests for array scenario/size: {scenario}/{size}')
    report = Report(array_size=size, algo_name=ALGO_NAME, array_type=scenario)
    root = Node(array[0])

    print(f'[{ALGO_NAME}] - testing insertion')
    for i in array:
        start_time = time.process_time()
        insert(root, i)
        end_time = time.process_time()
        report.time_execution_insert += (end_time - start_time)

    print(f'[{ALGO_NAME}] - testing search')
    for i in array:
        start_time = time.process_time()
        search(root, i)
        end_time = time.process_time()
        report.time_execution_search += (end_time - start_time)

    print(f'[{ALGO_NAME}] - testing remove')
    for i in array:
        start_time = time.process_time()
        remove(root, i)
        end_time = time.process_time()
        report.time_execution_remove += (end_time - start_time)
    report.create_report()