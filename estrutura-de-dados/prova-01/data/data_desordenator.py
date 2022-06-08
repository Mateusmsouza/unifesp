'''
this module is responsible for unorder 10% of each ordened array from ./sorted directory and create new data set from this process
'''
import logging
import random
import sys

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(stream = sys.stdout,
                    format = Log_Format, 
                    level = logging.INFO)
RATE_TO_DESORDER = 0.10

def desorder_data(list_size):

    with open(f'sorted/data_{list_size}.txt', 'r') as file_handler:
        logging.info(f'reading file with {list_size} not repeated integer numbers')
        
        line = file_handler.readlines()
        orderd_list = line[0].split(' ')

    logging.debug(f'creating almost sorted list data_{list_size}.txt file')

    swaps = len(orderd_list) * RATE_TO_DESORDER
    swaps_already_made = []

    while(swaps):
        index1 = random.randint(0, len(orderd_list))
        index2 = random.randint(0, len(orderd_list))
        if not f'{index1}:{index2}' in swaps_already_made:
            swaps -= 1
            orderd_list[index1], orderd_list[index2] = orderd_list[index2], orderd_list[index1]
    almost_ordered_list = orderd_list
    with open(f'almost_sorted/data_{list_size}.txt', 'w') as file2_handler:
        first = True
        for integer in almost_ordered_list:
            if first:
                file2_handler.write(f'{integer}')
                first = False
            else:
                file2_handler.write(f' {integer}')

if __name__ == '__main__':
    for number in [10, 100, 1000, 10000, 100000, 1000000]:
        desorder_data(number)
