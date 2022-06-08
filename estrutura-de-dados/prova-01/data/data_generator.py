'''this module is responsible for generating several files with random not repeated integer arrays'''
import logging
import sys
import random

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(stream = sys.stdout,
                    format = Log_Format, 
                    level = logging.INFO)


def pre_generate_random_integers(integers_list, numbers_to_generate, max_int):
    generated_numbers = []

    max_range = numbers_to_generate-1
    logging.debug(f'generating {max_range} numbers');
    for i in range(0, max_range):
        generated_numbers.append(random.randint(0, max_int))

    integers_list = integers_list + generated_numbers
    return integers_list[0:numbers_to_generate]

def generate_data(list_size):
    with open(f'unsorted/data_{list_size}.txt', 'w') as file_handler:
        logging.info(f'creating file with {list_size} not repeated integer numbers')
        integers_list = []
        while(len(integers_list) < list_size):
            integers_list = pre_generate_random_integers(integers_list, list_size, max_int=list_size*10)
            integers_list = list(set(integers_list))

        if len(integers_list) != list_size:
            logging.critical(f'generated list has {len(integers_list)} and should have {list_size}')

        logging.debug(f'creating data_{list_size}.txt file')
        first = True
        for integer in integers_list:
            if first:
                file_handler.write(f'{integer}')
                first = False
            else:
                file_handler.write(f' {integer}')

if __name__ == '__main__':
    for number in [10, 100, 1000, 10000, 100000, 1000000]:
        generate_data(number)
