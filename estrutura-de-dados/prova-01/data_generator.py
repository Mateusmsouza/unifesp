import logging
import sys
import json
import random

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(stream = sys.stdout,
                    format = Log_Format, 
                    level = logging.INFO)


def pre_generate_random_integers(integers_list, numbers_to_generate, max_int):
    generated_numbers = []
    for i in range(0, numbers_to_generate-1):
        generated_numbers.append(random.randint(0, max_int))

    return integers_list + generated_numbers


def generate_data(list_size):
    with open(f'data_{list_size}.txt', 'w') as file_handler:
        logging.info(f'creating file with {list_size} not repeated integer numbers')
        integers_list = []
        while(len(integers_list) < list_size):
            integers_list = pre_generate_random_integers(integers_list, list_size, max_int=list_size*10)
            integers_list = list(set(integers_list))

        json.dump(integers_list, file_handler)



if __name__ == '__main__':
    for number in [10, 100, 1000, 10000, 100000, 1000000]:
        generate_data(number)
