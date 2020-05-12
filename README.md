# Public healthcare and epidemiology research

## About
The main aim of this project is to conduct a research of pubic health and disease rate in United States of America.
This project will be а realization of a web-application, that provides a visualisation of different disease rate in United States.
## Input - Output data
The user will be able to choose indicators available on the web application in the format of dropdown menus.
Then user's input will be analysed and the output is a web page with visualised graphs of user selected data.
## Project structure (functions, methods, classes)
### Classes
- Tree
###### methods: add_child(key, node); __repr__(); __str__().
- Node
###### methods: get_parent(); add_child(key, node); __str__().
- DiseaseTree
###### methods: add_child(key, node); __repr__(); __str__(); search(disease, city, year, gender, ethnicity).
- ListNode
###### methods: add_child(node); get_parent()
- Disease
###### methods: get_disease(); get_year(); get_indicator()
### Functions (in the main module as for now)
- read_into_data_structure()
- experiment_cities(data, indicator)
- total_value_experiment(data, indicator)
- main()
## Tested cases
There is a function in the in module named `adt_test.py` that checks the Abstract Data Types and how they work.
In the `main.py` which is the main module for implementing the project's code there is functions that execute experiments with the data provided in the file and the main data structure that has been implemented for the project.

## Usage
The URL link will be available on the main github page soon after the launch of the project.
This web application will enable users to choose the years and the cities of United States, for which they want to see the visualisation for. The user can also join a couple of diseases in order to compare the rate of disease spreading.
## Installation
In order to install the program, you can clone the project or download the source code.