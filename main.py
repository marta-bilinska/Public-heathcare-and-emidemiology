"""This module contains a main function for doing experiments with the data."""

import pandas as pd
from data_structures import DiseaseTree, Node


def data_accessor():
    """
    This function reads the information of
    the example csv file and forms it as a
    pandas DataFrame.
    """
    diseases_data = pd.read_csv("example.csv")
    rows = diseases_data.shape[0]
    diseases_tree = DiseaseTree()

    for i in range(rows):
        diseases_data = diseases_data.iloc[i]
        indicator = str(diseases_data.values[0])
        disease = str(diseases_data.values[1])
        year = int(diseases_data.values[2])
        place = str(diseases_data.values[6])
        sex = str(diseases_data.values[3])
        value = float(diseases_data.values[5])
        ethnicity = str(diseases_data.values[4])

        if not indicator in diseases_tree.root.children:
            diseases_tree.add_child(Node())



    # diseases_data = diseases_data.iloc[0]




if __name__ == "__main__":
    data_accessor()
    # print(int(year), place, sex, value, ethnicity)