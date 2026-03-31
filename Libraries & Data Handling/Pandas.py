# INTRODUCTION to Pandas

# -> pandas is built on top of numpy
# -> it provides two main data structure 
# >>series -> one-dimensional 
# >>DataFrame -> two-dimensional 

# With pandas you can 
# load data from csv, excel, json, sql ets 
# clean and tranform data(droping missing values, rename columns)
# Analyze data (mean , sum , group by )
# Visualize data (integrates with matplotlib and seaborn)

# Example of creating a dataframe

import pandas as pd 
data = {
    "Name": ["shivani", "shivam", "flashy"],
    "Age": [20, 21, 19],
    "Course": ["BCA","BBA", "B-Tech" ]
}

df = pd.DataFrame(data)

print("Dataframe:\n",df)
print("\n Average Age:", df["Age"].mean())


# Now Example of reading csv file 
df = df.dropna()

df.rename(columns={ "Name": "StudentName"}, inplace = True)

# Now this example to creating small data and read and write rename 

# suppose have csv file with data
import pandas as pd
import matplotlib.pyplot as plt 

# Load data

df = pd.read_csv("students.csv")

# show first rows
print(df.head())

# Calculate average marks per subject
print("\nAverage Marks:\n",  df[["Math","Science","English"]].mean())

# Add new column: Total Marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis = 1)

# Add another column: Average Marks
df["Average"] = df["Total"] / 3


# now visualization 
# Bar chart: Total marks per student
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Total"], color="skyblue")
plt.title("Total Marks per Student")
plt.xlabel("Student")
plt.ylabel("Total Marks")
plt.show()

# Histogram: Distribution of Average Marks
plt.figure(figsize=(8,5))
plt.hist(df["Average"], bins=5, color="orange", edgecolor="black")
plt.title("Distribution of Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.show()

# Line chart: Subject-wise averages
subject_avg = df[["Math","Science","English"]].mean()
subject_avg.plot(kind="line", marker="o", color="green", title="Subject-wise Average Marks")
plt.ylabel("Marks")
plt.show()