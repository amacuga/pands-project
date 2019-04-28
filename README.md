# Project solution

This repository contains my solutions to the Project 2019 for the module Programming and Scripting at GMIT.
[See here for the instructions](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

## Summary of the Iris data set
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher (1890-1962) in his 1936 paper "The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis". It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. 

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Youngronaldfisher2.JPG/220px-Youngronaldfisher2.JPG "Ronald Fisher in 1913")

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.

![alt text](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png "Iris species")

The dataset contains a set of 150 records under 5 attributes:
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. species:
   * Iris Setosa
   * Iris Versicolour
   * Iris Virginica

The Iris data set is widely used as a beginner's dataset for machine leaning purpose. This dataset is free and is publicly available at the UCI Machine Learning Repository.

## My investigations into the Iris data set

### Dimensions of data set:

![alt text](https://user-images.githubusercontent.com/47215445/56868638-d946b980-69ec-11e9-926d-4bf1048dbb2d.jpg "First ten lines of data set")

![alt text](https://user-images.githubusercontent.com/47215445/56868640-d9df5000-69ec-11e9-8e0f-41c8e3101d1a.jpg "Number or rows and columns")

First, we are going to take a look at a summary of each attribute (feature). In the table below, you can see number of values, mean, standard deviation, minimum, lower percentile(25th), median (50th percentile), upper percentile (75th) and maximum for each attribute.

![alt text](https://user-images.githubusercontent.com/47215445/56868641-d9df5000-69ec-11e9-8b87-fd573ec62ebb.jpg "Statistical summary")

The lowest number in our data set is 0.1 cm and the highest number is 7.9 cm.

![alt text](https://user-images.githubusercontent.com/47215445/56868642-d9df5000-69ec-11e9-9d1d-d95a5dd55d3d.jpg "Variance")

### Histograms:

![alt text](https://user-images.githubusercontent.com/47215445/56849791-1e85c100-68f1-11e9-8615-3ec16c9305f3.jpg "Histograms")

### Scatter plot matrix:

![alt text](https://user-images.githubusercontent.com/47215445/56854379-78a47780-692d-11e9-8e1f-1099178f1a6f.jpg "Scatter plot matrix")

## How to download this repository

1. Go to Github.
2. Click the download button.

## How to run the code

1. Make sure you have Python installed.
2. I would recommend installing the free version of Anaconda, that includes all libraries required to run my script.
3. After you download the repository to your computer, run cmder or similar tool.
4. In cmder, navigate to the downloaded folder.
5. Run "python project.py".

## What each file contains

1. project.py contains my solution to project
2. iris.csv contains iris data set

## References
[UC Irvine Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Iris) I used UC Irvine Machine Learning Repository to write a summary of Iris Data set.

[Wikipedia Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set) I used Wikipedia to write a summary of Iris Data set.

[Wikipedia Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) Source of the image of Ronald Fisher

[Datacamp](https://www.datacamp.com/community/tutorials/machine-learning-in-r) Source of the image of three Iris species

[GitHub](https://gist.github.com/curran/a08a1080b88344b0c8a7) Source of my iris.csv file.

[Machine Learning Mastery](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/) I used Machine Learning Mastery in my solution

[DataScience Made Simple](http://www.datasciencemadesimple.com/variance-function-python-pandas-dataframe-row-column-wise-variance/) I used DataScience Made Simple in my solution

[Kaggle](https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python) I used Kaggle in my solution