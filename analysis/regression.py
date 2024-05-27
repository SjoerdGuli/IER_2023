import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

# Load the data
data = pd.read_csv(os.getcwd() + R"\datasets\updated_dataset.csv")

# Calculate the difference between estimated and actual steps
data['StepDifference'] = data['stap_est'] - data['average_steps_tot']

# Create dummy variables for gender and living situation
data = pd.get_dummies(data, columns=['gender', 'living'], drop_first=True)

# Drop rows with NaN values
data = data.dropna(subset=['bmi', 'stap_est', 'StepDifference', 'gender_Male', 'living_Moved_out'])

# Define variables
X = data[['bmi', 'gender_Male', 'living_Moved_out']]
y = data['StepDifference']

# Normalize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Create and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

print(model.coef_)

# Plot the coefficients
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
ax = coefficients.plot(kind='bar', color='#555555')
plt.ylabel('Coefficient Value')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.show()
