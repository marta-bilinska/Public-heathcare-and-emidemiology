"""This module contains a main function for doing experiments with the data.
!!! Notice that for this program to be faster, the file that is used in it
is an excerpt from the whole file.
"""
import random
import matplotlib.pyplot as plt
import numpy
import pandas as pd
from data_structures import Node
from disease_tree import DiseaseTree, ListNode, DiseaseRecord


def read_into_data_structure():
    """
    () -> DiseaseTree
    This function reads the information of
    the example csv file, forms it as a
    pandas DataFrame and conducts experiments of the data.
    """
    diseases_dataframe = pd.read_csv("BCHI-dataset.csv")
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
            continue
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
        for j in disease.children:
            cities += str(j.city) + "; "
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
        for j in disease.children:
            value += float(j.value)
    return value


def experiment_gender(data, indicator):
    """
    DiseaseTree, str -> str
    Does experiments with gender values of all diseases
    linked to indicator.
    """
    disease_node = data.children[indicator]
    value_male = 0
    value_female = 0
    for i in disease_node.children:
        disease = disease_node.children[i]
        for j in disease.children:
            if j.gender == 'Male':
                value_male += 1
            elif j.gender == 'Female':
                value_female += 1
    return value_male, value_female


def main_experiments():
    """
    () -> ()
    Main function that conducts experiments.
    """
    disease_data = read_into_data_structure()
    city_experiment = experiment_cities(disease_data, 'Behavioral Health/Substance Abuse')
    print(city_experiment)

    value_experiment = total_value_experiment(disease_data, 'Behavioral Health/Substance Abuse')
    string_value = str(round(value_experiment, 2))
    print("The total value of the cities is: ", string_value, "Per 100 000 of population")

    male_cases, female_cases = experiment_gender(disease_data, 'Cancer')
    male_cases, female_cases = str(male_cases), str(female_cases)
    print("Female to male cases are: ", female_cases, "/", male_cases)


def get_indicator_disease(data):
    """
    DiseaseTree -> set()
    Gets a set of tuples of diseases and indicators.
    """
    disease_tuple_set = set()
    for i in data.children:
        for j in data.children[i].children:
            disease_tuple_set.add((i, j))
    return disease_tuple_set


def get_diseases(data):
    """
    DiseaseTree -> list
    Gets a list of all diseases.
    """
    disease_set = set()
    for i in data.children:
        for j in data.children[i].children:
            disease_set.add(j)
    return sorted(list(disease_set))


def get_cities(data):
    """
    DiseaseTree -> list
    Gets a list of all cities.
    """
    cities = set()
    for indicator in data.children:
        diseasenode = data.children[indicator]
        for j in diseasenode.children:
            disease = diseasenode.children[j]
            for i in disease.children:
                cities.add(i.city)
    return sorted(list(cities))


def get_ethnicities(data):
    """
    DiseaseTree -> list
    Gets a list of all ethnicities.
    """
    ethnicities = set()
    for indicator in data.children:
        disease_node = data.children[indicator]
        for k in disease_node.children:
            disease = disease_node.children[k]
            for i in disease.children:
                ethnicity = i.ethnicity
                ethnicities.add(ethnicity)
    return sorted(list(ethnicities))


def create_plot(data, diseases_lst):
    """
    DiseaseTree, list -> str
    Creates a plot of the two diseases
    and saves it.
    """
    colors = ['#7bc5c9', '#7ec479']
    index_number = 0
    has_data = False
    for i in diseases_lst:
        index_number += 1
        records_ = data.search(i[0], i[1], i[2], i[3], i[4])
        if records_ == -1:
            continue
        df_new = pd.DataFrame(records_, columns=['Year', 'Disease' + str(index_number)])
        has_data = True
        plt.plot('Year', 'Disease' + str(index_number), data=df_new, marker='',
                 color=colors[index_number - 1], linewidth=4)

    if not has_data:
        return None

    random.seed()
    number = str(random.randint(1, 1000000000))
    name = 'static/plot' + number + '.png'
    plt.savefig(name)
    plt.close()
    return name


if __name__ == "__main__":
    # main_experiments()
    pass
