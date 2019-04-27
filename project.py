# Alexandra Macuga, 2019-04-28
# This is my solution to the Project 2019 for the module Programming and Scripting at GMIT.

# Load modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
file = "iris.csv"
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
dataset = pd.read_csv(file, names=features)

# Show values of each column:
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

