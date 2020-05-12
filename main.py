"""This module contains a main function for doing experiments with the data.
!!! Notice that for this program to be faster, the file that is used in it
is an excerpt from the whole file.
"""
import numpy
import pandas as pd
from data_structures import Node
from disease_tree import DiseaseTree, ListNode, DiseaseRecord


def read_into_data_structure():
    """
    This function reads the information of
    the example csv file, forms it as a
    pandas DataFrame and conducts experiments of the data.
    """
    diseases_dataframe = pd.read_csv("example.csv")
    rows = diseases_dataframe.shape[0]
    node = Node('root')
    diseases_tree = DiseaseTree(node)

    for i in range(rows):
        diseases_data = diseases_dataframe.iloc[i]
        indicator = str(diseases_data.values[0])
        disease = str(diseases_data.values[1])
        year = int(diseases_data.values[2])
        place = str(diseases_data.values[6])
        sex = str(diseases_data.values[3])
        value = diseases_data.values[5]
        if numpy.isnan(value):
            value = float(0)
        else:
            value = float(value)
        ethnicity = str(diseases_data.values[4])
        if indicator not in diseases_tree.children:
            diseases_tree.add_child(indicator, Node('indicator', diseases_tree))
        indicator_node = diseases_tree.children[indicator]
        if disease not in indicator_node.children:
            indicator_node.add_child(disease, ListNode('disease', indicator_node))
        disease_node = indicator_node.children[disease]
        record = DiseaseRecord(disease_node, place, value, sex, ethnicity, year)
        disease_node.add_child(record)

    print("* Successfully moved data to the data structure. *")
    return diseases_tree


def experiment_cities(data, indicator):
    """
    DiseaseTree, str -> str
    Does experiments with city names.
    """
    disease_node = data.children[indicator]
    cities = "First couple of cities: "
    for i in disease_node.children:
        disease = disease_node.children[i]
        for i in disease.children:
            cities += str(i.city) + "; "
    return cities


def total_value_experiment(data, indicator):
    """
    DiseaseTree, str -> str
    Does experiments with values of all diseases.
    """
    disease_node = data.children[indicator]
    value = 0
    for i in disease_node.children:
        disease = disease_node.children[i]
        for i in disease.children:
            value += float(i.value)
    return value


def main():
    """
    Main function that conducts experiments.
    """
    disease_data = read_into_data_structure()
    city_experiment = experiment_cities(disease_data, 'Behavioral Health/Substance Abuse')
    print(city_experiment)
    value_experiment = total_value_experiment(disease_data, 'Behavioral Health/Substance Abuse')
    string_value = str(round(value_experiment, 2))
    print("The total value of the cities is: ", string_value, "Per 100 000 of population")


if __name__ == "__main__":
    main()



