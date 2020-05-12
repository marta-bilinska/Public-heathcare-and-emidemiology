"""This module contains a function that tests ADTs."""
from data_structures import Tree, Node


def adt_check():
    """
    () -> ()
    Tests the ADTs that are used in the realisation.
    """
    node = Node('root')
    tree = Tree(node)
    node1 = Node(1, node)
    tree.add_child('one', node1)
    tree.add_child('two', Node(2, node))
    tree.add_child('three',  Node(3, node))
    node1.add_child('four', Node(4, node))
    node1.add_child('five', Node(5, node))
    node1.add_child('six', Node(6, node))

    print(node)
    for i in tree.children:
        print(tree.children[i], str(i))


if __name__ == "__main__":
    adt_check()
