from model.report import Report
import time

report = None
ALGO_NAME: str = 'INTERVAL_TREE_SEARCH'
comparisions_insert = 0
comparisions_search = 0
comparisions_remove = 0

class Interval:

    def __init__(self, low, high) -> None:
        self.low = low
        self.high = high

class Node:

    def __init__(self, interval: Interval) -> None:
        self.interval = interval
        self.max = interval.high
        self.left = None
        self.right = None

    def get_low(self):
        return self.interval.low

def insert(root: Node, interval: Interval):
    global comparisions_insert
    comparisions_insert += 2
    if not root:
        comparisions_insert -= 1
        return Node(interval)

    if interval.low >= root.get_low():
        root.right = insert(root.right, interval)
    else:
        root.left = insert(root.left, interval)

    comparisions_insert += 1
    if root.max  < interval.high:
        root.max = interval.high

    return root

def overlaps(interval_a: Interval, interval_b: Interval):
    global comparisions_search
    comparisions_search += 2
    return (interval_a.low <= interval_b.high) and (interval_b.low <= interval_a.high)

def find_overlap(root: Node, interval: Interval):
    global comparisions_search

    comparisions_search += 1
    if not root:
        return

    comparisions_search += 1
    if overlaps(root.interval, interval):
        return root.interval
    
    comparisions_search += 2
    if root.left and root.left.max >= interval.low:
        return find_overlap(root.left, interval)
    return find_overlap(root.right, interval)

def min_low_interval(root):
    global comparisions_remove
    while root.left:
        comparisions_remove += 1
        root = root.left

    comparisions_remove += 1
    return root

def delete(root: Node, interval: Interval):
    global comparisions_remove

    comparisions_remove += 1
    if not root:
        return None

    comparisions_remove += 2
    if interval.low < root.get_low():
        comparisions_remove -= 1
        root.left = delete(root.left, interval)
    elif interval.low > root.get_low():
        root.right = delete(root.right, interval)
    else:
        comparisions_remove += 1
        if interval.high == root.interval.high:
            # actually delete
            comparisions_remove += 2
            if root.left == None:
                comparisions_remove -=1
                return root.right
            elif root.right == None:
                return root.left
            min_interal = min_low_interval(root.right);
            root.interval = min_interal.interval
            root.right = delete(root.right, min_interal.interval);
        else:
            root.right = delete(root.right, interval)
    
    comparisions_remove += 1
    root.max=max(root.interval.high, 0 if not root.left else root.left.max, 0 if not root.right else root.right.max)
    return root

def test_with_array(array, size, scenario):
    global report
    global comparisions_insert
    global comparisions_search
    global comparisions_remove


    print(f'[{ALGO_NAME}] - initializing tests for array scenario/size: {scenario}/{size}')
    report = Report(array_size=size, algo_name=ALGO_NAME, array_type=scenario)
    root = None

    print(f'[{ALGO_NAME}] - testing insertion')
    for i in range(0, len(array)):
        if i + 2 <= len(array)-1:
            interval = Interval(array[i], array[i+2])
            start_time = time.process_time()
            insert(root, interval)
            end_time = time.process_time()
            report.time_execution_insert.append(end_time - start_time)
            report.comparisions_insert.append(comparisions_insert)
    comparisions_insert = 0
    report.consolidate_insertion()

    print(f'[{ALGO_NAME}] - testing search')
    for i in range(0, len(array)):
        if i + 2 <= len(array)-1:
            interval = Interval(array[i], array[i+2])
            start_time = time.process_time()
            find_overlap(root, interval)
            end_time = time.process_time()
            report.time_execution_search.append(end_time - start_time)
            report.comparisions_search.append(comparisions_search)
    comparisions_search = 0
    report.consolidate_search()

    print(f'[{ALGO_NAME}] - testing remove')
    for i in range(0, len(array)):
        if i + 2 <= len(array)-1:
            interval = Interval(array[i], array[i+2])
            start_time = time.process_time()
            delete(root, interval)
            end_time = time.process_time()
            report.time_execution_remove.append(end_time - start_time)
            report.comparisions_remove.append(comparisions_remove)
    comparisions_remove = 0
    report.consolidate_remove()
    report.create_report()