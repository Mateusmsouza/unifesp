from searchalgorithms.binary_search_tree import *
from utils.beautiful_print_tree import *

values_and_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

NAME = 'ATEUSMACHADODESOUZA'

def exercise_27():

    root = Node(12, 'M')
    fourth_node = None
    count = 0 
    for letter in NAME:
        count+=1
        insert_bst(root=root, value=values_and_letters[letter], letter=letter)
        if count == 3:
            print(f'Eu sou o quarto nó inserido {letter} - {values_and_letters[letter]}')
            fourth_node = values_and_letters[letter]
    print(f'A) tree height is {height(root)}')
    print(f'B) {post_order(root)}')
    print(f'C) o predecessor do quarto nó inserido na árvore é :')
    sucessor(root, root.right)
    fourth_node = search_bst(root, fourth_node)
    print(f'D) o predecessor do quarto nó inserido na árvore é :')
    predecessor(fourth_node, fourth_node.left)

    printTreeInterface(root)
    remove_bst(root, 12)
    print(f'E) {post_order(root)}')
    #printTreeInterface(root)

if __name__ == "__main__":
    exercise_27()
    