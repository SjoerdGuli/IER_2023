import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Load the data
data = pd.read_csv(os.getcwd() + R"\datasets\updated_dataset.csv")

# Difference between estimated and actual steps
data['StepDifference'] = data['stap_est'] - data['average_steps_tot']

data = pd.get_dummies(data, columns=['gender', 'living'], drop_first=True)
data = data.dropna(subset=['bmi', 'stap_est', 'StepDifference', 'gender_Male', 'living_Moved_out'])

# Plot
plt.figure(figsize=(10, 6))
sns.regplot(x='bmi', y='StepDifference', data=data, scatter_kws={'alpha':0.5, "color":"black"}, line_kws={"color":"black"})
plt.xlabel('BMI')
plt.ylabel('Step Difference')
plt.ylim(-5000, 6000)
plt.show()