# Public healthcare, epidemiology and condition research

## About
The main aim of this project is to conduct a research of pubic health and disease\condition rate in United States of America.
This project will be а realization of a web-application, that provides a visualisation of different diseases\conditions rate in United States.
The web application provides the user with an ability to compare two conditions based on the certain indicators using graphs and visualisations.
The web application can be reached on `http://martabilinska.pythonanywhere.com/`.
## Input - Output data
The user will be able to choose indicators available on the web application in the format of dropdown menus.
Then user's input will be analysed and the output is a web page with visualised graphs of user selected data.
If the data user requested in not in the main database, the user will receive the message that he/she has to choose other indicators.
## Project structure (functions, methods, classes)
### Classes
- Tree
###### methods: add_child(key, node); __repr__(); __str__(); search(indicators).
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
- experiment_gender(data, indicator)
- create_plot(data, diseases_lst)
- get_cities(data)
- get_diseases(data)
- get_ethnicities(data)
- get_indicator_disease(data)
- main_experiments()
## Tested cases
There is a function in the in module named `adt_test.py` that checks the Abstract Data Types and how they work.
In the `main.py` which is the main module for implementing the project's code there is functions that execute experiments with the data provided in the file and the main data structure that has been implemented for the project.

## Usage
The URL link of the web application is `http://martabilinska.pythonanywhere.com/`.
This web application will enable users to choose the years and the cities of United States, for which they want to see the visualisation for. The user can also join a couple of diseases in order to compare the rate of disease/conditions.
The user will be able to choose indicators available on the web application in the format of dropdown menus.
Then user's input will be analysed and the output is a web page with visualised graphs of user selected data.
If the data user requested in not in the main database, the user will receive the message that he/she has to choose other indicators.
## Installation
In order to install the program, you can clone the project or download the source code.