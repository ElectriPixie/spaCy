#!/bin/bash

# Set default values
csvFile="list_of_real_usa_addresses.csv"
dataDir="data"
trainSize="0.8"
devSize="0.1"
seed="42"
help="False"

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -c|--csv_file)
      csvFile="$2"
      shift 2
      ;;
    -d|--data_dir)
      dataDir="$2"
      shift 2
      ;;
    -t|--train_size)
      trainSize="$2"
      shift 2
      ;;
    -v|--dev_size)
      devSize="$2"
      shift 2
      ;;
    -s|--seed)
      seed="$2"
      shift 2
      ;;
    -h|--help)
      help="True"
      shift
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# Run the Python script with arguments
python3 pylib/loadData.py \
  -c "$csvFile" \
  -d "$dataDir" \
  -t "$trainSize" \
  -v "$devSize" \
  -s "$seed" \
  $([ "$help" = "True" ] && echo "-h")