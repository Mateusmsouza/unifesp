'''this module is responsible for reversing the sorted arrays from ./sorted directory and create new data set from this process
'''
import logging
import sys
import random

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(stream = sys.stdout,
                    format = Log_Format, 
                    level = logging.INFO)

def reverse_data(list_size):
    with open(f'sorted/data_{list_size}.txt', 'r') as file_handler:
        logging.info(f'reading file with {list_size} not repeated integer numbers')
        
        line = file_handler.readlines()
        orderd_list = line[0].split(' ')
        reversed_list = orderd_list[::-1]

        logging.debug(f'creating reversed list data_{list_size}.txt file')

        with open(f'reversed_sorted/data_{list_size}.txt', 'w') as file2_handler:
            first = True
            for integer in reversed_list:
                if first:
                    file2_handler.write(f'{integer}')
                    first = False
                else:
                    file2_handler.write(f' {integer}')

if __name__ == '__main__':
    for number in [10, 100, 1000, 10000, 100000, 1000000]:
        reverse_data(number)
