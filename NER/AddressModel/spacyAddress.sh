#!/bin/bash

# Set default values
modelDir="models"
text="123 Main Street, Springfield, IL 62701"
help="False"

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -md|--modelDir)
      modelDir="$2"
      shift 2
      ;;
    -t|--text)
      text="$2"
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
python3 pylib/spacyAddress.py \
  -md "$modelDir" \
  -t "$text" \
  $([ "$help" = "True" ] && echo "-h")