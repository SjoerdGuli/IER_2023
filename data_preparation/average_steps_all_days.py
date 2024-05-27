import pandas as pd
import os

# Load the dataset
data = pd.read_csv(os.getcwd() + R"\datasets\IER_Fitbit_Data_2024.csv", encoding='ISO-8859-1')

data = data[~data['year'].isin([2022, 2023])]

# List of columns to average
columns_to_average = [
    'stap_om_1_aantal', 'stap_om_2_aantal', 'stap_om_3_aantal',
    'stap_om_4_aantal', 'stap_om_5_aantal', 'stap_om_6_aantal', 'stap_om_7_aantal'
]

# List of columns to average
columns_to_average2 = [
    'stap_app_1_aantal', 'stap_app_2_aantal', 'stap_app_3_aantal',
    'stap_app_4_aantal', 'stap_app_5_aantal', 'stap_app_6_aantal', 'stap_app_7_aantal'
]

# Calculate the average of these columns for each row
data['average_steps_fitbit'] = data[columns_to_average].mean(axis=1)
data['average_steps_app'] = data[columns_to_average2].mean(axis=1)

columns_to_average3 = [
    'average_steps_fitbit', 'average_steps_app'
]

data['average_steps_tot'] = data[columns_to_average3].mean(axis=1)

# Save the updated data to a new CSV file
data.to_csv(R'datasets\updated_dataset.csv', index=False)
