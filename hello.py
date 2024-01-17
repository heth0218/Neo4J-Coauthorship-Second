import json

# Specify the file path
file_path = 'your_file_mining.json'

# Read JSON data from the file
with open(file_path, 'r') as file:
    json_data = file.read()

# Parse JSON data
data = json.loads(json_data)

# Extract top-level keys and put them in a list
top_level_keys = list(data.keys())

# Print the result
print(top_level_keys)
