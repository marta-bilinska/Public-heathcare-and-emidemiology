"""This module contains main data structures used in the project."""
from data_structures import Node, Tree


class DiseaseTree(Tree):
    """
    Defines a DiseaseTree.
    """

    def __init__(self, root, name='root', children=None):
        """
        str, DynamicArray -> ()
        Initializes a DiseaseRecord tree object.
        """
        super().__init__(root, name, children)

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

    def search(self, indicator, disease, city, gender, ethnicity):
        """
        Searches the data structure for specific records.
        """
        return self.children[indicator].children[disease][city, gender, ethnicity]


class ListNode:
    """
    Defines a node in a tree that contains an list.
    """

    def __init__(self, name, parent=None, children=None):
        """
        self, Tree, DynamicArray -> ()
        Initializes a DiseaseRecord tree object.
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

    def __getitem__(self, item):
        """
        str, str, str -> DiseaseRecord
        Gets the requested item from node's children.
        If not found returns -1.
        """
        records = []
        if item[0]:
            city = item[0]
        else:
            city = 'U.S. Total, U.S. Total'
        if item[1]:
            gender = item[1]
        else:
            gender = 'All'
        if item[2]:
            ethnicity = item[2]
        else:
            ethnicity = 'All'

        for i in self.children:
            if i.city == city and i.gender == gender and i.ethnicity == ethnicity:
                records.append((int(i.year), float(i.value)))
        if not records:
            return -1
        return records


class DiseaseRecord(Node):
    """
    Defines a DiseaseRecord - a leaf in DiseaseTree.
    """

    def __init__(self, parent, city, value, gender, ethnicity, year):
        """
        self, Tree, str, int, str, str, int -> ()
        Initializes a DiseaseRecord node.
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
        """
        self -> str
        Forms a string representation.
        """
        return str(self.value) + " " + str(self.year) + " " \
               + str(self.city) + " " + str(self.gender) + " " + str(self.ethnicity)
