"""This module contains a main function for doing experiments with the data."""

import pandas as pd
from data_structures import DiseaseTree, Node, ListNode, Disease


def data_accessor():
    """
    This function reads the information of
    the example csv file, forms it as a
    pandas DataFrame and conducts experiments of the data.
    """
    diseases_dataframe = pd.read_csv("example.csv")
    rows = diseases_dataframe.shape[0]
    diseases_tree = DiseaseTree()

    for i in range(rows):
        diseases_data = diseases_dataframe.iloc[i]
        indicator = str(diseases_data.values[0])
        disease = str(diseases_data.values[1])
        year = int(diseases_data.values[2])
        place = str(diseases_data.values[6])
        sex = str(diseases_data.values[3])
        value = float(diseases_data.values[5])
        ethnicity = str(diseases_data.values[4])

        if indicator not in diseases_tree.children:
            diseases_tree.add_child(indicator, Node('indicator', diseases_tree))
        indicator_node = diseases_tree.children[indicator]
        if disease not in indicator_node.children:
            indicator_node.add_child(disease, ListNode('disease', indicator_node))
        disease_node = indicator_node.children[disease]
        record = Disease(disease_node, place, value, sex, ethnicity, year)
        disease_node.add_child(record)
        print(record)
        print("Successfully moved data to the data structure.")


if __name__ == "__main__":
    data_accessor()

