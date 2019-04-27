# Alexandra Macuga, 2019-04-28
# This is my solution to the Project 2019 for the module Programming and Scripting at GMIT.
# This progam contains my investigations into Iris data set.

# Load modules
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load dataset
file = "iris.csv"
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
dataset = pd.read_csv(file, names=features)

# Compute and show the following values for each feature (column):
# - number of values
# - mean of the values
# - standard deviation
# - minimum of the values
# - lower percentile(25th)
# - median (50th percentile)
# - upper percentile (75th)
# - maximum of the values
print(dataset.describe())

# Create a histograms
dataset.hist()
plt.show()

# Create a scatter plot matrix
scatter_matrix(dataset)
plt.show()
