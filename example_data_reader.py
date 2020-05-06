"""This module contains an example of accessing
    the information that is in the file using pandas library.
    For simplicity reasons only an excerpt of the real
    file has been used"""
import pandas as pd


def data_accessor():
    """
    This function reads the information of
    the example csv file and forms it as a
    pandas DataFrame.
    """
    diseases_data = pd.read_csv("example.csv" )
    print(diseases_data.head(5))

    indicators = diseases_data["Indicator"]
    print(indicators)

    places = diseases_data["Place"]
    print(places)

    values = diseases_data["Value"]
    print(values)


if __name__ == "__main__":
    print("Printing the example columns of the information accessed: ")
    data_accessor()
