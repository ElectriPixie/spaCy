# spaCy
spaCy examples

[NER/AddressModel]
uses https://www.kaggle.com/datasets/ahmedshahriarsakib/list-of-real-usa-addresses/ for a default dataset
added as data/list_of_real_usa_addresses.csv

run ```./sbin/loadData.sh```
to load and parse the data from the csv


run ./sbin/spacySaveDB.sh
to save the data as spacy formats for training and testing with


run ./config/createBaseConfig.sh
to create a base config for spacy


run ./config/createConfig.sh
to create a config from the base config


edit the newly made config so the in the [paths] block edit train="" dev="" test="" to point to the newly created spacy files
to point to the new data/spaCy/train.spacy data/spaCy/dev.spacy and data/spaCy/test.spacy files


run ./sbin/spacyTrainModel.sh 
to train a new model


run ./sbin/spacyAddress.sh 
to test the newly trained model