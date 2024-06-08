# Please follow the instruction carefully to fully run the script

**NOTE:** Please always run the scripts from the directory where this README file is in. This will make sure that the paths to the csv files with data will be correct.

# Project Dependencies

This project requires the following Python libraries:

## Python Libraries

- **pandas**: A powerful data manipulation library.
- **matplotlib**: A plotting library.
- **numpy**: A library for mathematical functions.
- **seaborn**: A library for making statistical graphics in Python.
- **scikit-learn**: A machine learning library for Python.

## Acces data

To acces the data, please install the data from the fitbit and put the csv file in the datasets directory with the following name:
'IER_Fitbit_Data_2024.csv'. The csv file can be found using the following link:

https://brightspace.tudelft.nl/d2l/le/content/596702/viewContent/3647699/View 

## Installation

To install these packages, use the following command:

```bash
pip install -r requirements.txt
```

## Running Scripts

Here will be the the lines of code that needs to be runned.

### Data preparation

Run the following lines of code for data preparation:

```bash
python .\data_preparation\average_steps_all_days.py
```
This will make sure that the 'IER_Fitbit_Data_2024.csv' is updated to 'updated_dataset.csv', there are three columns added: 
> average_steps_fitbit

> average_steps_app

> average_steps_tot

The average_steps_tot is used in other Python scripts.

### Data analysis

Still from the 'research' directory, run the following scripts to get the data provided in the paper:


Gives a table of all data needed in the table in the report:
```bash
python .\analysys\table_information.py
```


Gives the boxplot for perceived vs actual step counts in different years
```bash
python .\analysys\boxplots_next_eachother.py
```


Gives a bar chart of the perception of phsyical activity and the attitude towards physical activity:
```bash
python .\analysys\barchart_perception_attitude.py
```


Gives a bar chart with a coefficient on how much impact every demographic factor has on the difference in perceived vs actual physical activity:
```bash
python .\analysys\regression.py
```


Gives a clearer line regression for the impact of bmi on perceived vs actual physical activity:
```bash
python .\analysys\bmi_regression.py
```
