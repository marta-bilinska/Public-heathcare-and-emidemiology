"""This module contains all of the abstract data types that
will be used in this project."""


class Tree:
    """
    Defines a tree data structure.
    """

    def __init__(self, root, name='root', children=None):
        """
        str, DynamicArray -> ()
        Initializes a tree object.
        """
        self.name = name
        self.root = root
        self.children = dict()
        if children is not None:
            for child in children:
                self.add_child(str(child), child)

    def add_child(self, key, node):
        """
        self, Node -> ()
        Adds a child to a tree.
        """
        assert isinstance(node, Node)
        self.children[key] = node
        self.root.add_child(key, node)

    def __repr__(self):
        """
        self -> str
        Forms a representation of the object.
        """
        raise NotImplementedError

    def __str__(self):
        """
        self -> str
        Forms a string representation of the object.
        """
        raise NotImplementedError


class Node:
    """
    Defines a node in a tree.
    """

    def __init__(self, name, parent=None):
        """
        self, Tree, DynamicArray -> ()
        Initializes a Disease tree object.
        """
        self.parent = parent
        self.children = dict()
        self.name = name

    def get_parent(self):
        """
        self -> Tree
        Gets the parent of the node.
        """
        return self.parent

    def add_child(self, key, node):
        """
        self, Node -> ()
        Adds a child to a tree.
        """
        self.children[key] = node

    def __str__(self):
        """
        Forms a string representation of a node.
        """
        children = ''
        for i in self.children:
            children += str(self.children[i]) + ', '
        children = children[:-2]
        return "( " + str(self.name) + " -> [" + children + "] )"
