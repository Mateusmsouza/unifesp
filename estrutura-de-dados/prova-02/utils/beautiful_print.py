def printTree(prefix, node, isLeft):
    if node != None:
        print(prefix, end="")
        print("├──" if isLeft else "└──", end="")
        print(node.value)

        printTree( prefix + ("│   " if isLeft else "    "), node.left, True)
        printTree( prefix + ("│   " if isLeft else "    "), node.right, False)

def printTreeInterface(node):
    printTree("", node, False);