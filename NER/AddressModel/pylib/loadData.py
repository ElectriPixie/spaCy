import csv
import json
import os
import random
import argparse

def add_trailing_slash(path):
    if not path.endswith('/'):
        path += '/'
    return path

SCRIPT_DIR = os.path.dirname(__file__)
DEFAULT_PATH = add_trailing_slash(os.path.dirname(SCRIPT_DIR))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--csv_file', type=str, default='list_of_real_usa_addresses.csv', help='CSV file name')
    parser.add_argument('-d', '--dataDir', type=str, default='data', help='Data directory')
    parser.add_argument('-t', '--trainSize', type=float, default=0.8, help='Training data size (in percentage) eg. 0.8')
    parser.add_argument('-v', '--devSize', type=float, default=0.1, help='Development data size (in percentage) eg. 0.1  also sets testSize')
    parser.add_argument('-s', '--seed', type=int, default=42, help='Random seed for reproducibility')

    args = parser.parse_args()
    if args.dataDir is not None:
        dataDir = args.dataDir
    else:
        dataDir = DEFAULT_PATH+args.dataDir
    csvFile = args.csv_file
    csvPath = add_trailing_slash(dataDir) + csvFile
    trainSize = args.trainSize
    devSize = args.devSize
    seed = args.seed

    with open(csvPath, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        data = []
        for row in reader:
            address = row[0].lower()
            city = row[1].lower()
            state = row[2].lower()
            zipcode = row[3].lower()

            full_address = address + ", " + city + ", " + state + " " + zipcode

            entities = []
            address_idx = 0
            city_idx = address_idx + len(address) + 2
            state_idx = city_idx + len(city) + 2
            zipcode_idx = state_idx + len(state) + 1

            entities.append((address_idx, address_idx + len(address), "ADDRESS"))
            entities.append((city_idx, city_idx + len(city), "CITY"))
            entities.append((state_idx, state_idx + len(state), "STATE"))
            entities.append((zipcode_idx, zipcode_idx + len(zipcode), "ZIPCODE"))

            data.append((full_address, {"entities": entities}))

    random.seed(seed)  # Set seed for reproducibility
    random.shuffle(data)

    total_size = len(data)
    trainSize = int(trainSize * total_size)
    devSize = int(devSize * total_size)

    train_data = data[:trainSize]
    dev_data = data[trainSize:trainSize + devSize]
    test_data = data[trainSize + devSize:]

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