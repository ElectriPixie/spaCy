#!/bin/bash
SCRIPT_DIR=$(dirname $(readlink -f $BASH_SOURCE[0]))
DEFAULT_PATH=$(dirname $SCRIPT_DIR)

dataDir="${DEFAULT_PATH}/data/"
configDir="config/"
baseConfigFile="spacy_base_config.cfg"
configFile="spacy_config.cfg"
baseConfig=$dataDir$configDir$baseConfigFile
config=$dataDir$configDir$configFile

python3 -m spacy init fill-config $baseConfig $config || {
  echo "Error initializing SpaCy configuration file"
  exit 1
}