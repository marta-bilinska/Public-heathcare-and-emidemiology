"""This module contains an example of reading the file
    to really make sure it contains the needed information.
    For simplicity reasons only an excerpt of the real
    file has been used"""


def file_reader():
    """
    This function reads the information of
    the example csv file to make sure it contains
    the information needed for the research.
    """
    total_diseases = []

    with open("example.csv") as f:

        for line in f:
            record = line.split(",")
            total_diseases.append(record)

    return total_diseases


def show_example():
    """
    This function prints out the insides
    of the file to make sure it contains
    the information needed for the research.
    """
    diseases = file_reader()
    for i in diseases:
        print(i)


if __name__ == "__main__":
    show_example()