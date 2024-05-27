import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

# Load the dataset
data = pd.read_csv(os.getcwd() + "/datasets/updated_dataset.csv", encoding='ISO-8859-1')
data_long = pd.melt(data, id_vars=['year'], value_vars=['stap_est', 'average_steps_tot'],
                    var_name='Type', value_name='Steps')

# Create a boxplot
plt.figure(figsize=(12, 6))
boxplot = sns.boxplot(x='year', y='Steps', hue='Type', data=data_long, palette=['#999999', '#555555'],
                      width=0.8, dodge=0.3)

plt.xlabel('Year')
plt.ylabel('Number of Steps')

handles, labels = boxplot.get_legend_handles_labels()
handles = [handles[1], handles[0]]
labels = ['Actual Steps (Dark)', 'Estimated Steps (light)']
plt.legend(handles=handles, title='Type', labels=labels, loc='upper center')

plt.show()
