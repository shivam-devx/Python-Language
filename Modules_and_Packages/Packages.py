""" 
    package -> purpose -> common opertions
    
    Numpy -> numerical computing -> arrays, matrics, math functions
    pandas -> data analysis -> dataframes, csv/excel handlling, filtering
    matplotlib -> visualization -> line plots, bar charts, scatter plots
    seaborn -> advanced visualization -> heatmaps, statistical plots
    requests -> http requests -> Get/Post apis,headers, json response
    flask -> web development -> build apis, lightweight web apps
    django -> web development -> full stack framework, ORM, authentication
    sqlaichemy -> database ORM -> connect to dbs, query building \
    opencv -> computer vision -> image processing, face detection
    scikit-learn -> machine learning -> classification, regression, clustring
    tensorflow/pytorch -> deep learning -> neural network, gpu training
    beatifulsoup -> web scaping -> parse html, extract data
    pytest -> testing -> unit tests, fixtures, assertions
    os/ sys -> System utilities -> file handling, environment, runtime info
    json / csv -> data formats -> read/write structured/ tabular data 
"""

# numpy Example:

import numpy as np
arr = np.array([1, 2, 3])
print("Mean:", np.mean(arr))
print("Square roots:", np.sqrt(arr))

# Pandas Example:

import pandas as pd
data = {"Name":["Shivam","Flashhy"], "Age":[20,18]}
df = pd.DataFrame(data)
print(df)
print(df[df["Age"] > 18])

# Requests Example:

import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())

# matplotlib Example:

import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,25,30]
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.show()