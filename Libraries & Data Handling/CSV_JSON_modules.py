# CSV Module (comma separated values)
# -> Used for tabular data(like Excel sheets)
# -> Each row = record, each column = field
# -> Python has a built-in csv module


# Example: writing CSV

import csv 
data = [ 
    ["Name", "Age", "Course"],
    ["Shivam",20,"BCA"],
    ["Flashy", 19, "BCA"]       
]

with open("students.csv", "w", newline="") as file:
    writer= csv.writer(file)
    writer.writerows(data)
    
print("\n")

# Example: Reading CSV

import csv 
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
        
# jSON MODULE (javascript object notation)

# -> used for hierarchical data (like dictionaries)
# -> very common in API and web apps
# -> python has a built in json module

# Example to writing json 

print("\n")
import json 

student = {
    "name": "shivam", 
    "age": 20, 
    "course": "BCA", 
    "skills": ["Python","cpp", "c", "java"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
    
# now Example to reading a json file 

print("\n")
import json 
with open("student.json ","r") as file:
    data = json.load(file)
print(data)
print("Name:", data["name"])