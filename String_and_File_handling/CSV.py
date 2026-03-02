import csv
print("\n=== CSV FILE HANDLING ===")

# Write CSV file
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Shivam", 20])
    writer.writerow(["Flashhy", 18])

# Read CSV file
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("CSV Row:", row)

# Read CSV as dictionary
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("CSV Dict:", row)

