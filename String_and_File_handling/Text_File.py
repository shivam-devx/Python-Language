# Write to file 
with open("sample.txt", "w") as file:
    file.write("HEllo Shivam, Welcome to file handling program")

# Append to file
with open("sample.txt", "w") as file:
    file.write("\nCreate some program and enjoy the code")

# Read file 
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nText File Content:\n", content)
