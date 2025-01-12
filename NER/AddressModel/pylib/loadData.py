import csv
import json
import os
import random
import argparse

def add_trailing_slash(path):
    if not path.endswith('/'):
        path += '/'
    return path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csv_file', type=str, default='list_of_real_usa_addresses.csv', help='CSV file name')
    parser.add_argument('-d', '--data_dir', type=str, default='data', help='Data directory')
    parser.add_argument('-t', '--train_size', type=float, default=0.8, help='Training data size (in percentage)')
    parser.add_argument('-v', '--dev_size', type=float, default=0.1, help='Development data size (in percentage)')
    parser.add_argument('-s', '--seed', type=int, default=42, help='Random seed for reproducibility')

    args = parser.parse_args()

    csvFile = args.csv_file
    dataDir = args.data_dir
    csvPath = add_trailing_slash(dataDir) + csvFile
    train_size = args.train_size
    dev_size = args.dev_size
    seed = args.seed

    with open(csvPath, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        data = []
        for row in reader:
            address = row[0].lower()
            city = row[1].lower()
            state = row[2].lower()
            zip_code = row[3].lower()

            full_address = address + ", " + city + ", " + state + " " + zip_code

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

    random.seed(seed)  # Set seed for reproducibility
    random.shuffle(data)

    total_size = len(data)
    train_size = int(train_size * total_size)
    dev_size = int(dev_size * total_size)
    test_size = total_size - train_size - dev_size

    train_data = data[:train_size]
    dev_data = data[train_size:train_size + dev_size]
    test_data = data[train_size + dev_size:]

    os.makedirs(dataDir, exist_ok=True)

    with open(os.path.join(dataDir, "spaCyTrain.json"), "w") as f:
        json.dump(train_data, f)

    with open(os.path.join(dataDir, "spaCyDev.json"), "w") as f:
        json.dump(dev_data, f)

    with open(os.path.join(dataDir, "spaCyTest.json"), "w") as f:
        json.dump(test_data, f)

    print("Data splits saved successfully!")

if __name__ == "__main__":
    main()