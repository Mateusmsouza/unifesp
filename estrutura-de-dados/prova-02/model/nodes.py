class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class RedBlackNode:

    def __init__(self, value, color):
        self.left = None
        self.right = None
        self.value = value
        self.color = color