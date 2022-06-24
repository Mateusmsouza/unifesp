from searchalgorithms.binary_search_tree import Node, insert
from utils.beautiful_print_tree import printTreeInterface

if __name__ == "__main__":
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    printTreeInterface(r)