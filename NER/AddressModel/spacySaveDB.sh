#!/bin/bash

# Set default values
dataDir="data"
dbDir="spaCy"
trainFile="spaCyTrain.json"
testFile="spaCyTest.json"
devFile="spaCyDev.json"

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -d|--data_dir)
      dataDir="$2"
      shift 2
      ;;
    -db|--db_dir)
      dbDir="$2"
      shift 2
      ;;
    -tf|--train_file)
      trainFile="$2"
      shift 2
      ;;
    -vf|--test_file)
      testFile="$2"
      shift 2
      ;;
    -df|--dev_file)
      devFile="$2"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# Run the Python script with arguments
python3 pylib/spacySaveDB.py \
  -d "$dataDir" \
  -db "$dbDir" \
  -tf "$trainFile" \
  -vf "$testFile" \
  -df "$devFile"