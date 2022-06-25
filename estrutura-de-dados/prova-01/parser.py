import re

UNSORTED_DATA = 'Unsorted Data'
SORTED_DATA = 'Sorted Data'
REVERSED_SORTED_DATA = 'Reversed Sorted'
ALMOST_SORTED_DATA = 'Almost Sorted Data'

SIZE_10 = 'array of size 10'
SIZE_100 = 'array of size 100'
SIZE_1000 = 'array of size 1000'
SIZE_10000 = 'array of size 10000'
SIZE_100000 = 'array of size 100000'
SIZE_1000000 = 'array of size 1000000'

QUICK_SORT = "Quick Sort"
MERGE_SORT = "Merge Sort"
HEAP_SORT = "Heap Sort"
INSERTION_SORT = "Insertion Sort"
SELECTION_SORT = "Selection Sort"
BUBBLE_SORT = "Bubble Sort"
STOOGE_SORT = "Stooge Sort"

EXECUTION_TIME = 'execution_time'
CHANGES = 'changes'
COMPARISIONS = 'comparisions'

FORMATED_DATA = {
    UNSORTED_DATA : {
        QUICK_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        MERGE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        HEAP_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        INSERTION_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        SELECTION_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        BUBBLE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        STOOGE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
    },
    SORTED_DATA : {
        QUICK_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        MERGE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        HEAP_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        INSERTION_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        SELECTION_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        BUBBLE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        STOOGE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
    },
    REVERSED_SORTED_DATA : {
        QUICK_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        MERGE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        HEAP_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        INSERTION_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        SELECTION_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        BUBBLE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        STOOGE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
    },
    ALMOST_SORTED_DATA : {
        QUICK_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        MERGE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        HEAP_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        INSERTION_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        SELECTION_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        BUBBLE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
        STOOGE_SORT : {
            EXECUTION_TIME: [],
            CHANGES: [],
            COMPARISIONS: [],
        },
    }
}


def parse_register(register):
    if UNSORTED_DATA in register:
        parse_array_size(register, UNSORTED_DATA)
    elif REVERSED_SORTED_DATA in register:
        parse_array_size(register, REVERSED_SORTED_DATA)
    elif ALMOST_SORTED_DATA in register:
        parse_array_size(register, ALMOST_SORTED_DATA)
    elif SORTED_DATA in register:
        parse_array_size(register, SORTED_DATA)

def parse_array_size(register, tipo):
    if SIZE_10 in register:
        parse_sort(register, tipo, SIZE_10)
    elif SIZE_100 in register:
        parse_sort(register, tipo, SIZE_100)
    elif SIZE_1000 in register:
        parse_sort(register, tipo, SIZE_1000)
    elif SIZE_10000 in register:
        parse_sort(register, tipo, SIZE_10000)
    elif SIZE_100000 in register:
        parse_sort(register, tipo, SIZE_100000)
    elif SIZE_1000000 in register:
        parse_sort(register, tipo, SIZE_1000000)

def parse_sort(register, tipo, tamanho):
    values = re.findall(r'\d+', register)

    if QUICK_SORT in register:
        FORMATED_DATA[tipo][QUICK_SORT][EXECUTION_TIME].append(f'{values[4]}.{values[5]}')
        FORMATED_DATA[tipo][QUICK_SORT][CHANGES].append(f'{values[2]}')
        FORMATED_DATA[tipo][QUICK_SORT][COMPARISIONS].append(f'{values[1]}')

    elif MERGE_SORT in register:
        FORMATED_DATA[tipo][MERGE_SORT][EXECUTION_TIME].append(f'{values[4]}.{values[5]}')
        FORMATED_DATA[tipo][MERGE_SORT][CHANGES].append(f'{values[2]}')
        FORMATED_DATA[tipo][MERGE_SORT][COMPARISIONS].append(f'{values[1]}')

    elif HEAP_SORT in register:
        FORMATED_DATA[tipo][HEAP_SORT][EXECUTION_TIME].append(f'{values[4]}.{values[5]}')
        FORMATED_DATA[tipo][HEAP_SORT][CHANGES].append(f'{values[2]}')
        FORMATED_DATA[tipo][HEAP_SORT][COMPARISIONS].append(f'{values[1]}')

    elif INSERTION_SORT in register:
        FORMATED_DATA[tipo][INSERTION_SORT][EXECUTION_TIME].append(f'{values[4]}.{values[5]}')
        FORMATED_DATA[tipo][INSERTION_SORT][CHANGES] .append(f'{values[2]}')
        FORMATED_DATA[tipo][INSERTION_SORT][COMPARISIONS] .append(f'{values[1]}')
    
    elif SELECTION_SORT in register:
        FORMATED_DATA[tipo][SELECTION_SORT][EXECUTION_TIME].append(f'{values[4]}.{values[5]}')
        FORMATED_DATA[tipo][SELECTION_SORT][CHANGES] .append(f'{values[2]}')
        FORMATED_DATA[tipo][SELECTION_SORT][COMPARISIONS] .append(f'{values[1]}')

    elif BUBBLE_SORT in register:
        FORMATED_DATA[tipo][BUBBLE_SORT][EXECUTION_TIME].append(f'{values[4]}.{values[5]}')
        FORMATED_DATA[tipo][BUBBLE_SORT][CHANGES] .append(f'{values[2]}')
        FORMATED_DATA[tipo][BUBBLE_SORT][COMPARISIONS] .append(f'{values[1]}')
    
    elif STOOGE_SORT in register:
        FORMATED_DATA[tipo][STOOGE_SORT][EXECUTION_TIME].append(f'{values[4]}.{values[5]}')
        FORMATED_DATA[tipo][STOOGE_SORT][CHANGES] .append(f'{values[2]}')
        FORMATED_DATA[tipo][STOOGE_SORT][COMPARISIONS] .append(f'{values[1]}')


def formated_print():
    
    show_changes('Conjunto não ordenado', UNSORTED_DATA)
    show_changes('Conjunto ordenado', SORTED_DATA)
    show_changes('Conjunto reversamente ordenado', REVERSED_SORTED_DATA)
    show_changes('Conjunto quase ordenado', ALMOST_SORTED_DATA)

def show_execuction_time(conjunto, data_type):
    print(f'### {conjunto} - Tempo de Execução')
    print('quick_sort_time = ', end='')
    print(FORMATED_DATA[data_type][QUICK_SORT][EXECUTION_TIME], sep=', ')
    print('merge_sort_time = ', end='')
    print(FORMATED_DATA[data_type][MERGE_SORT][EXECUTION_TIME], sep=', ')
    print('heap_sort_time = ', end='')
    print(FORMATED_DATA[data_type][HEAP_SORT][EXECUTION_TIME], sep=', ')
    print('insertion_sort_time = ', end='')
    print(FORMATED_DATA[data_type][INSERTION_SORT][EXECUTION_TIME], sep=', ')
    print('selection_sort_time = ', end='')
    print(FORMATED_DATA[data_type][SELECTION_SORT][EXECUTION_TIME], sep=', ')
    print('bubble_sort_time = ', end='')
    print(FORMATED_DATA[data_type][BUBBLE_SORT][EXECUTION_TIME], sep=', ')
    print('stooge_sort_time = ', end='')
    print(FORMATED_DATA[data_type][STOOGE_SORT][EXECUTION_TIME], sep=', ')

    print(f'plt.plot(array_size, quick_sort_time, label="{QUICK_SORT}")')
    print(f'plt.plot(array_size, merge_sort_time, label="{MERGE_SORT}")')
    print(f'plt.plot(array_size, heap_sort_time, label="{HEAP_SORT}")')
    print(f'plt.plot(array_size, insertion_sort_time, label="{INSERTION_SORT}")')
    print(f'plt.plot(array_size, selection_sort_time, label="{SELECTION_SORT}")')
    print(f'plt.plot(array_size, bubble_sort_time, label="{BUBBLE_SORT}")')
    print(f'plt.plot(array_size, stooge_sort_time, label="{STOOGE_SORT}")')
    print('==================================================================')

def show_comparisions(conjunto, data_type):
    print(f'### {conjunto} - Comparações')
    print('array_size = [10, 100, 1000, 10000, 100000]')
    print('quick_sort_comparisions = ', end='')
    print(FORMATED_DATA[data_type][QUICK_SORT][COMPARISIONS], sep=', ')
    print('merge_sort_comparisions = ', end='')
    print(FORMATED_DATA[data_type][MERGE_SORT][COMPARISIONS], sep=', ')
    print('heap_sort_comparisions = ', end='')
    print(FORMATED_DATA[data_type][HEAP_SORT][COMPARISIONS], sep=', ')
    print('insertion_sort_comparisions = ', end='')
    print(FORMATED_DATA[data_type][INSERTION_SORT][COMPARISIONS], sep=', ')
    print('selection_sort_comparisions = ', end='')
    print(FORMATED_DATA[data_type][SELECTION_SORT][COMPARISIONS], sep=', ')
    print('bubble_sort_comparisions = ', end='')
    print(FORMATED_DATA[data_type][BUBBLE_SORT][COMPARISIONS], sep=', ')
    print('stooge_sort_comparisions = ', end='')
    print(FORMATED_DATA[data_type][STOOGE_SORT][COMPARISIONS], sep=', ')

    print(f'plt.plot(array_size, quick_sort_comparisions, label="{QUICK_SORT}")')
    print(f'plt.plot(array_size, merge_sort_comparisions, label="{MERGE_SORT}")')
    print(f'plt.plot(array_size, heap_sort_comparisions, label="{HEAP_SORT}")')
    print(f'plt.plot(array_size, insertion_sort_comparisions, label="{INSERTION_SORT}")')
    print(f'plt.plot(array_size, selection_sort_comparisions, label="{SELECTION_SORT}")')
    print(f'plt.plot(array_size, bubble_sort_comparisions, label="{BUBBLE_SORT}")')
    print(f'plt.plot(array_size, stooge_sort_comparisions, label="{STOOGE_SORT}")')
    print('plt.xticks(array_size)')
    print('==================================================================')

def show_changes(conjunto, data_type):
    print(f'### {conjunto} - Movimentações')
    print('array_size = [10, 100, 1000, 10000, 100000]')
    print('quick_sort_changes = ', end='')
    print(FORMATED_DATA[data_type][QUICK_SORT][COMPARISIONS], sep=', ')
    print('merge_sort_changes = ', end='')
    print(FORMATED_DATA[data_type][MERGE_SORT][COMPARISIONS], sep=', ')
    print('heap_sort_changes = ', end='')
    print(FORMATED_DATA[data_type][HEAP_SORT][COMPARISIONS], sep=', ')
    print('insertion_sort_changes = ', end='')
    print(FORMATED_DATA[data_type][INSERTION_SORT][COMPARISIONS], sep=', ')
    print('selection_sort_changes = ', end='')
    print(FORMATED_DATA[data_type][SELECTION_SORT][COMPARISIONS], sep=', ')
    print('bubble_sort_changes = ', end='')
    print(FORMATED_DATA[data_type][BUBBLE_SORT][COMPARISIONS], sep=', ')
    print('stooge_sort_changes = ', end='')
    print(FORMATED_DATA[data_type][STOOGE_SORT][COMPARISIONS], sep=', ')

    print(f'plt.plot(array_size, quick_sort_changes, label="{QUICK_SORT}")')
    print(f'plt.plot(array_size, merge_sort_changes, label="{MERGE_SORT}")')
    print(f'plt.plot(array_size, heap_sort_changes, label="{HEAP_SORT}")')
    print(f'plt.plot(array_size, insertion_sort_changes, label="{INSERTION_SORT}")')
    print(f'plt.plot(array_size, selection_sort_changes, label="{SELECTION_SORT}")')
    print(f'plt.plot(array_size, bubble_sort_changes, label="{BUBBLE_SORT}")')
    print(f'plt.plot(array_size, stooge_sort_changes, label="{STOOGE_SORT}")')
    print('plt.xticks(array_size)')
    print('==================================================================')

with open('dataset.txt', 'r') as dataset:
    while(True):
        register = ''
        line = dataset.readline()
        if not line:
            break
        if '----' in line and not register:
            while(True):
                line = dataset.readline()
                if '----' in line:
                    break
                register += ' ' + line.rstrip()        
        parse_register(register)
        register = ''

    formated_print()