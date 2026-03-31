# libraries is ready made code collections
# they save time add advanced features and make your projects recruiter friendly
# for data handling the most important one are 
# numpy -> numerical data, arrays, matrics
# pandas -> tabular data like excel and csv file and cleaning analysis
# matplotlib / seaborn -> visualization  like charts graphs
# csv / json modules -> reading / writing structured files
# Stepwise data handling workflow 

# 1 Load data

import pandas as pd 

df = pd.read_csv("students.csv")
print(df.head())

# 2. Clean data

df = df.dropna() # drop missing values
df.rename(columns={"Name":"studentName"}, inplace=True)

# 3. Analyze data

print("Average Age:", df["Age"].mean())
print("Course Counts:\n", df["Course"].value_counts())

# 4.Visualize Data

import matplotlib.pyplot as plt

df["Age"].plot(kind="hist", bins= 5, title = "Age Distribution")
plt.show()