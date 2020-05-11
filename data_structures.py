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


class DiseaseTree(Tree):
    """
    Defines a DiseaseTree.
    """

    def __init__(self, name='root', children=None):
        """
        str, DynamicArray -> ()
        Initializes a Disease tree object.
        """
        super().__init__(name, children)

    def __repr__(self):
        """
        self -> str
        Forms a representation of the object.
        """
        return self.name

    def __str__(self):
        """
        self -> str
        Forms a string representation of the object.
        """
        return self.name

    def search(self, disease, city, year, gender, ethnicity):
        """
        Searches the data structure for specific records.
        """
        return self.children[disease].children[city][year, gender, ethnicity]


class Node:
    """
    Defines a node in a tree.
    """

    def __init__(self, name, parent=None, children=None):
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
        # assert isinstance(node, Node)
        self.children[key] = node


class ListNode:
    """
    Defines a node in a tree that contains an list.
    """

    def __init__(self, name, parent=None, children=None):
        """
        self, Tree, DynamicArray -> ()
        Initializes a Disease tree object.
        """
        self.parent = parent
        self.children = list()
        self.name = name
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, child):
        """
        self, Node -> ()
        Adds a child to a tree.
        """
        assert isinstance(child, Node)
        self.children.append(child)


class Disease(Node):
    """
    Defines a Disease - a leaf in DiseaseTree.
    """

    def __init__(self, parent, city, value, gender, ethnicity, year):
        """
        self, Tree, str, int, str, str, int -> ()
        Initializes a Disease node.
        """
        super().__init__(parent, None)
        self.city = city
        self.value = value
        self.gender = gender
        self.ethnicity = ethnicity
        self.year = year

    def get_disease(self):
        """
        self -> str
        Gets the disease name of the node.
        """
        return self.parent

    def get_year(self):
        """
        self -> int
        Gets the year of the disease record.
        """
        return self.year()

    def get_indicator(self):
        """
        self -> str
        Gets the indicator of the disease record.
        """
        return self.parent.parent

    def __str__(self):
        return str(self.value) + " " + str(self.year) + " "\
               + str(self.city) + " " + str(self.gender) + " " + str(self.ethnicity)
