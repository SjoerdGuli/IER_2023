import pandas as pd
import os

# Load the dataset
data = pd.read_csv(os.getcwd() + R"\datasets\updated_dataset.csv", encoding='ISO-8859-1')

# Ensure that 'bmi' and 'year' are the correct data types
data['bmi'] = pd.to_numeric(data['bmi'], errors='coerce')
data['year'] = pd.to_numeric(data['year'], errors='coerce')
data['average_steps_tot'] = pd.to_numeric(data['average_steps_tot'], errors='coerce')
data['stap_est'] = pd.to_numeric(data['stap_est'], errors='coerce')
data['erv_fa'] = pd.to_numeric(data['erv_fa'], errors='coerce')
data['attitu_tot'] = pd.to_numeric(data['attitu_tot'], errors='coerce')

# Scale attitude anf ErvFA to 0-10 scale
data['attitu_tot'] = (data['attitu_tot'] / 7) * 10
data['erv_fa'] = (data['erv_fa'] / 7) * 10

# Calculate the average for each year
average_bmi_per_year = data.groupby('year')['bmi'].mean()
average_steps_tot_per_year = data.groupby('year')['average_steps_tot'].mean()
average_eststeps_per_year = data.groupby('year')['stap_est'].mean()
average_ErvFA_per_year = data.groupby('year')['erv_fa'].mean()
average_Attitude_per_year = data.groupby('year')['attitu_tot'].mean()

# Calculate the percentage of people with a BMI of more than 25.0 for each year
def calculate_percentage(group):
    total_count = len(group)
    count_over_25 = len(group[group['bmi'] >= 25.0])
    print(f"Total count over 25: {count_over_25}")
    if total_count > 0:
        return (count_over_25 / total_count) * 100
    else:
        return 0

percentage_bmi_over_25_per_year = data.groupby('year').apply(calculate_percentage)

# Print the results
print(f"Average BMI per Year: \n{average_bmi_per_year}")
print(f"\nAverage Estimated Steps per Year: \n{average_eststeps_per_year}")
print(f"\nAverage steps a day per Year: \n{average_steps_tot_per_year}")
print(f"\nPercentage of people with a BMI over 25.0 per Year: \n{percentage_bmi_over_25_per_year}")
print(f"\nAverage ErvFA per Year: \n{average_ErvFA_per_year}")
print(f"\nAverage Attitude per Year: \n{average_Attitude_per_year}")