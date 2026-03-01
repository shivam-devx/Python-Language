# DICTIONARIES

# key value pairs, unordered, mutable and defined with curly braces {key: value}
# keys must be unique and immutable (string, number, tuple)
# values ca be anything and useful for mapping relationships

# Examples:

student = {"name": "Shivam", "age": 20}
print(student["name"])   # Shivam

student["course"] = "BCA"
print(student)

del student["age"]
print(student)

for key, value in student.items():
    print(key, ":", value)

marks = {"math": 90, "science": 85}
print(marks.get("math"))       # 90
print(marks.get("english", 0)) # 0 (default value)