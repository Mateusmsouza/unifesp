from model.report import Report
import time

report = None
ALGO_NAME: str = 'SEQUENCIAL_SEARCH'
comparisions_insert = 0
comparisions_search = 0
comparisions_remove = 0

class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value

def search(root: Node, value: int):
    '''returns [Node found, Node parent]'''
    global comparisions_search
    comparisions_search += 1
    while root != None:
        comparisions_search += 1
        if root.value == value:
            return root
        root = root.next
    return None

def insert(root: Node, value: int):
    global comparisions_insert
    comparisions_insert += 1
    if not root:
        return False

    comparisions_insert += 1
    while root.next is not None:
        comparisions_insert += 1
        if root.next.value == value:
            return False
        root = root.next
    root.next = Node(value)
    return True

def remove(root: Node, value: int):
    global comparisions_remove
    comparisions_remove += 1
    if not root:
        return False

    comparisions_remove += 1
    while root.next is not None:
        comparisions_remove += 1
        if root.next.value == value:
            root.next = root.next.next
            return True
        root = root.next
    return False

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