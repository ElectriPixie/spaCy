#!/bin/bash
SCRIPT_DIR=$(dirname $(readlink -f $BASH_SOURCE[0]))
DEFAULT_PATH=$(dirname $SCRIPT_DIR)

dataDir="${DEFAULT_PATH}/data/"
configDir="config/"
baseConfigFile="spacy_base_config.cfg"
baseConfig=$dataDir$configDir$baseConfigFile
python3 -m spacy init config $baseConfig --lang en --pipeline ner --force