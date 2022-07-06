from model.report import Report
import time

report = None
ALGO_NAME: str = 'BINARY_SEARCH'
comparisions_insert = 0
comparisions_search = 0
comparisions_remove = 0

def insert(array, data):
    global comparisions_insert
    comparisions_insert += 1
    if not array:
        return [data]
    
    for i in range(len(array)):
        comparisions_insert += 2
        if array[i] > data:
            comparisions_insert -= 1
            print(f'inserting {data} at {i}')
            array.insert(i, data)
            return
        elif array[i] == data:
            return

def remove(array, data):
    global comparisions_insert

    for i in range(len(array)):
        comparisions_insert += 1
        if array[i] == data:
            array.pop(i)
            return

def binary_search(array, left, right, data):
    global comparisions_insert

    mid = (left + right) // 2
    comparisions_insert += 3
    if left > right:
        comparisions_insert -= 2
        return
    elif data > array[mid]:
        comparisions_insert -= 1
        return binary_search(array, mid+1, right, data)
    elif data < array[mid]:
        return binary_search(array, left, mid-1, data)
    else:
        return mid

def search(array, data):
    return binary_search(array, 0, len(array)-1, data)


        

def test_with_array(array, size, scenario):
    global report
    global comparisions_insert
    global comparisions_search
    global comparisions_remove


    print(f'[{ALGO_NAME}] - initializing tests for array scenario/size: {scenario}/{size}')
    report = Report(array_size=size, algo_name=ALGO_NAME, array_type=scenario)
    root = insert([], array[0])

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
