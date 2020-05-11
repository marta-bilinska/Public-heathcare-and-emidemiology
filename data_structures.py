import array as ar
from arrays import DynamicArray


class Tree:
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = DynamicArray()
        if children is not None:
            for child in children:
                self.add_child(child)

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class DiseaseTree(Tree):
    def __init__(self, name='indicators', children=None):
        super().__init__(name, children)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def search(self, disease, city, gender, ethnicity):
        return self.children[disease].children[city]


class Node:
    def __init__(self, parent=None, children=None):
        self.parent = parent
        self.children = children

    def get_parent(self):
        raise NotImplementedError


class Disease(Node):
    def __init__(self, parent, city, value, gender, ethnicity, year):
        super().__init__(parent, None)
        self.city = city
        self.value = value
        self.gender = gender
        self.ethnicity = ethnicity
        self.year = year

    def get_parent(self):
        return self.parent

    def get_disease(self):
        return self.parent

    def get_year(self):
        return self.year()

    def get_indicator(self):
        return self.parent.parent
