#!/bin/bash

SCRIPT_DIR=$(dirname $(readlink -f $BASH_SOURCE[0]))
DEFAULT_PATH=$(dirname $SCRIPT_DIR)

# Set default values
dataDir="${DEFAULT_PATH}/data/"
configDir="config/"
configFile="spacy_config.cfg"
modelDir="${DEFAULT_PATH}/models/"

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -d|--dataDir)
      dataDir="$2"
      shift 2
      ;;
    -cd|--configDir)
      configDir="$2"
      shift 2
      ;;
    -cf|--configFile)
      configFile="$2"
      shift 2
      ;;
    -md|--modelDir)
      modelDir="$2"
      shift 2
      ;;
    -h|--help)
      echo "Usage: $0 [-d|--dataDir] [-cd|--configDir] [-cf|--configFile] [-mn|--modelName]"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
done

# Set variables
config=$dataDir$configDir$configFile

# Create directories and train the model
mkdir -p $modelDir
python3 -m spacy train $config --output $modelDir