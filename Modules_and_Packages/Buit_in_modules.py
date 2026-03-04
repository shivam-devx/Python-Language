
import math 
# provides mathematical funtions like square root, power, trigonometry, constant(pi, e)
# Example:

print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))
print("Value of pi:", math.pi)
print("Cosine of 0:", math.cos(0))

import random 

# used for generating random numbers, choices, and shuffling
# Example:

print("Random integer (1-10):", random.randint(1, 10))
print("Random float (0-1):", random.random())
print("Random choice:", random.choice(["apple", "banana", "Cherry"]))

items = [1, 2, 3, 4, 5]
random.shuffle(items)
print("Shuffled list:", items)

import datetime

# used for working with dates and times
# Example:

now = datetime.datetime.now()
print("Current DateTime:", now)

d = datetime.date(2026, 3, 4)
print("Custom Date:", d)

print("Formatted Date:", now.strftime("%d-%m-%Y %H:%M:%S"))

import os 
print("Current Working Directory:", os.getcwd())

os.mkdir("test_folder")
print("Folder created.")

print("Files:", os.listdir())
os.rmdir("test_folder")
print("Folder removed")


import sys

print("Python Version:", sys.version)
print("Platform:", sys.platform)
print("Command Line Arguments:", sys.argv)

# math -> advanced math functions
# random -> random numvers and choices 
# datetime -> dates and times
# os -> operating system interation
# sys -> system parameters

import json

# purpose -> work with json data(APIs, configs)
# Function:
# dump(obj,file) -> write json
# load(file) -> read json
# dumps(obj) -> convert to json string
# loads(str) -> convert string to dict

# Example:
data = {"name":"Shivam","age":20}
text = json.dumps(data)
print("JSON String:", text)
parsed = json.loads(text)
print("Parsed:", parsed["name"])

import csv

# Purpose: work with tabular data
# function:
# writer() -> write rows
# reader() -> read rows
# DictReader() -> read as dictionary

# Example:
with open("data.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age"])
    writer.writerow(["Shivam",20])

with open("data.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)