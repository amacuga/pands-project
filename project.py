# Alexandra Macuga, 2019-04-28
# This is my solution to the Project 2019 for the module Programming and Scripting at GMIT.
# This progam contains my investigations into Iris data set, you can find the references in README file.

# Load modules
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load dataset
file = "iris.csv"
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
dataset = pd.read_csv(file, names=features)

# Print first 10 lines of the dataset
print(dataset.head(10))

# Print the number of rows and columns
print(dataset.shape)

# For each column, calculate the following values:
# - number of values
# - mean
# - standard deviation
# - minimum
# - lower percentile(25th)
# - median (50th percentile)
# - upper percentile (75th)
# - maximum
describe = dataset.describe()

# Round the results to two decimal places
describe = round(describe, 2)

# Print the results
print(describe)

# Calculate the variance of each column
df = pd.DataFrame(dataset)
df = df.var()

# Round the variance to two decimal places
df = round(df, 2)

# Print the variance
print('Variance: ' '\n' + str(df))

# Create a histogram
dataset.hist()
plt.show()

# Create a scatter plot matrix
scatter_matrix(dataset)
plt.show()