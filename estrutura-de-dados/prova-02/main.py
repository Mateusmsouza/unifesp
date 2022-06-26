from searchalgorithms.binary_search_tree import *
from searchalgorithms.red_black_tree import insert_rbt, insertRecursive
from model.nodes import RedBlackNode
from utils.beautiful_print_tree import *



def exercise42():

    array = [44, 71, 80, 74, 63, 59, 120, 98, 150]
    root = RedBlackNode(99, 'black')
    for i in array:
        print(f'inserting {i}')
        insert_rbt(root, i)
        print('================')
        printTreeInterface(root)
    print(root)

if __name__ == "__main__":
    exercise42()