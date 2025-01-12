#!/bin/bash

dataDir="../data/"
configDir="config/"
baseConfigFile="spacy_base_config.cfg"
configFile="spacy_config.cfg"
baseConfig=$dataDir$configDir$baseConfigFile
config=$dataDir$configDir$configFile

python3 -m spacy init fill-config $baseConfig $config || {
  echo "Error initializing SpaCy configuration file"
  exit 1
}