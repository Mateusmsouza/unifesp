from typing import Callable
from search_algorithms.sequencial_search import test_with_array as sequencial_search_test_with_array
from search_algorithms.binary_search import test_with_array as binary_search_test_with_array
from search_algorithms.binary_tree_search import test_with_array as binary_tree_search_test_with_array
from data_reader import get_array_from_file
import os

DATASET_FILES_TYPES = [
    'sorted',
    'unsorted',
    'reversed_sorted',
    'almost_sorted'
]

DATASET_TEMPLATE_PATHS = [
   './data/{}/data_10.txt',
   './data/{}/data_100.txt',
   './data/{}/data_1000.txt',
   './data/{}/data_10000.txt',
   './data/{}/data_100000.txt',
   './data/{}/data_1000000.txt'
]

def runner(callback: Callable):

    for dataset_file_type in DATASET_FILES_TYPES:
        for dataset_template_path in DATASET_TEMPLATE_PATHS:
            array = get_array_from_file(dataset_template_path.format(dataset_file_type))
            callback(array, len(array), str.upper(dataset_file_type))

if __name__ == '__main__':
    print(f'HI MY PID IS {os.getpid()}')
    #runner(callback=sequencial_search_test_with_array)
    #runner(callback=binary_search_test_with_array)
    #runner(callback=binary_tree_search_test_with_array)