#!/bin/bash

# Set default values
dataDir="data"
dbDir="spaCy"
trainFile="spaCyTrain.json"
testFile="spaCyTest.json"
devFile="spaCyDev.json"
help="False"

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -d|--data_dir)
      dataDir="$2"
      shift 2
      ;;
    -db|--dbDir)
      dbDir="$2"
      shift 2
      ;;
    -tf|--trainFile)
      trainFile="$2"
      shift 2
      ;;
    -vf|--testFile)
      testFile="$2"
      shift 2
      ;;
    -df|--devFile)
      devFile="$2"
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
python3 pylib/spacySaveDB.py \
  -d "$dataDir" \
  -db "$dbDir" \
  -tf "$trainFile" \
  -vf "$testFile" \
  -df "$devFile" \
  $([ "$help" = "True" ] && echo "-h")