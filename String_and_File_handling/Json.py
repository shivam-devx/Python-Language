import json
print("\n=== JSON FILE HANDLING ===")
# Write JSON file
data = {"name": "Shivam", "age": 20, "course": "BCA"}
with open("data.json", "w") as f:
    json.dump(data, f)

# Read JSON file
with open("data.json", "r") as f:
    loaded = json.load(f)
    print("JSON Loaded:", loaded)

# Convert JSON string to Python dict
text = '{"name": "Flashhy", "age": 18}'
parsed = json.loads(text)
print("JSON String Parsed:", parsed)
