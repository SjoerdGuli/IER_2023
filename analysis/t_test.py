import pandas as pd
from scipy import stats

# Load your data
file_path = R'C:\Github\research\datasets\updated_dataset.csv'
data = pd.read_csv(file_path)

data['discrepancy'] = data['stap_est'] - data['average_steps_tot']

# Remove rows
clean_data = data.dropna(subset=['stap_est', 'average_steps_tot']).copy()

# Numeric data
clean_data.loc[:, 'stap_est'] = pd.to_numeric(clean_data['stap_est'], errors='coerce')
clean_data.loc[:, 'average_steps_tot'] = pd.to_numeric(clean_data['average_steps_tot'], errors='coerce')

# Drop non-numeric
clean_data = clean_data.dropna(subset=['stap_est', 'average_steps_tot'])

# Paired T-test
t_stat, p_value = stats.ttest_rel(clean_data['stap_est'], clean_data['average_steps_tot'])
print(f"Paired T-test: T-statistic = {t_stat}, P-value = {p_value}")
