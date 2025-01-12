import csv
import json
import os
import random

def add_trailing_slash(path):
    if not path.endswith('/'):
        path += '/'
    return path

# Define the CSV file and the SpaCy format
csvFile = "list_of_real_usa_addresses.csv"
dataDir = "data"
csvPath = add_trailing_slash(dataDir)+csvFile
TRAIN_DATA = []
TEST_DATA = []

# Read the CSV file
with open(csvPath, "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    data = []
    for row in reader:
        address = row[0].lower()
        city = row[1].lower()
        state = row[2].lower()
        zip_code = row[3].lower()

        # Create the full address
        full_address = address + ", " + city + ", " + state + " " + zip_code

        # Create the SpaCy format
        entities = []
        address_idx = 0
        city_idx = address_idx + len(address) + 2
        state_idx = city_idx + len(city) + 2
        zip_code_idx = state_idx + len(state) + 1

        entities.append((address_idx, address_idx + len(address), "ADDRESS"))
        entities.append((city_idx, city_idx + len(city), "CITY"))
        entities.append((state_idx, state_idx + len(state), "STATE"))
        entities.append((zip_code_idx, zip_code_idx + len(zip_code), "ZIPCODE"))

        data.append((full_address, {"entities": entities}))

# Shuffle the data for randomness
random.seed(42)  # Set seed for reproducibility
random.shuffle(data)

# Split the data into train (80%), dev (10%), and test (10%)
total_size = len(data)
train_size = int(0.8 * total_size)
dev_size = int(0.1 * total_size)

train_data = data[:train_size]
dev_data = data[train_size:train_size + dev_size]
test_data = data[train_size + dev_size:]

# Save the splits to files
os.makedirs(dataDir, exist_ok=True)

with open(os.path.join(dataDir, "spaCyTrain.json"), "w") as f:
    json.dump(train_data, f)

with open(os.path.join(dataDir, "spaCyDev.json"), "w") as f:
    json.dump(dev_data, f)

with open(os.path.join(dataDir, "spaCyTest.json"), "w") as f:
    json.dump(test_data, f)

print("Data splits saved successfully!")
