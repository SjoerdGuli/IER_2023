import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
data = pd.read_csv(os.getcwd() + R"\datasets\updated_dataset.csv", encoding='ISO-8859-1')

# Convert necessary columns to numeric
data['erv_fa'] = pd.to_numeric(data['erv_fa'], errors='coerce')
data['attitu_tot'] = pd.to_numeric(data['attitu_tot'], errors='coerce')

# Scale 'attitude' and 'ErvFA' to a 0-10 scale
data['attitu_tot'] = (data['attitu_tot'] / 7) * 10
data['erv_fa'] = (data['erv_fa'] / 7) * 10

# Calculate the average for each year
average_ErvFA_per_year = data.groupby('year')['erv_fa'].mean()
average_Attitude_per_year = data.groupby('year')['attitu_tot']. mean()

# Combine these averages into a new DataFrame for plotting
averages_per_year = pd.DataFrame({
    'ErvFA': average_ErvFA_per_year,
    'Attitude': average_Attitude_per_year
}).reset_index()

# Plot the data using a bar chart with the specified colors
fig, ax = plt.subplots()
averages_per_year.plot(x='year', kind='bar', ax=ax, color=['#999999', '#555555'], rot=0)
ax.set_xlabel('Year')
ax.set_ylabel('Scores')
plt.legend(title='Metrics', loc='lower right')
plt.show()
