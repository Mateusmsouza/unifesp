def printTree(prefix, node, isLeft):
    if node != None:
        print(prefix, end="")
        print("├──" if isLeft else "└──", end="")
        print(f'{node.color}-{node.value}')

        printTree( prefix + ("│   " if isLeft else "    "), node.left, True)
        printTree( prefix + ("│   " if isLeft else "    "), node.right, False)

def printTreeInterface(node):
    printTree("", node, False);

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(f'{root.letter}', end=', ')