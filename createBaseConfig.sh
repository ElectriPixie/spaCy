#!/bin/bash

dataDir="data/"
configDir="config/"
baseConfigFile="spacy_base_config.cfg"
baseConfig=$dataDir$configDir$baseConfigFile
python3 -m spacy init config $baseConfig --lang en --pipeline ner --force