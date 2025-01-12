#!/bin/bash
dataDir="data/"
configDir="config/"
configFile="spacy_config.cfg"
config=$dataDir$configDir$configFile
modelDir="models/"
modelName="address"
modelPath=$modelDir$modelName
mkdir -p $modelPath
python -m spacy train $config --output $modelPath