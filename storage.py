import json

# Step 1: Save initial data to a JSON file
initial_data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'hobbies': ['reading', 'traveling', 'coding']
}

with open('data1.json', 'w') as file:
    json.dump(initial_data, file, indent=4)

print("Initial dictionary saved to data1.json")

# Step 2: Load the existing data from the JSON file
with open('data1.json', 'r') as file:
    data = json.load(file)

print("Existing data loaded from data.json")
print(data)

# Step 3: Add a nested dictionary to the existing dictionary
new_nested_data = {
    'job3': {
        'title': 'Engineer',
        'department': 'Development',
        'skills': ['Python', 'C++', 'Machine Learning']
    }
}

data.update(new_nested_data)

# Step 4: Save the updated dictionary back to the JSON file
with open('data1.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Updated dictionary with nested dictionary saved to data.json")
