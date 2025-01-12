import spacy
import json
import os
from pathlib import Path
from spacy.tokens import DocBin
import warnings

def add_trailing_slash(path):
    if not path.endswith('/'):
        path += '/'
    return path

dataDir="data"
dbDir="spaCy"
model="address"
trainFile="spaCyTrain.json"
devFile="spaCyDev.json"
testFile="spaCyTest.json"

def process_data(data):
    DATA = []
    for text, annot in data:
        DATA.append([text, {"entities": annot["entities"]}])
    return DATA

def saveDB(lang: str, DATA, output_path: Path):
    nlp = spacy.blank(lang)
    db = DocBin()
    for text, annot in DATA:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                print(msg)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk(output_path)

train_data = []
with open(add_trailing_slash(dataDir)+trainFile, "r") as f:
    train_data = json.load(f)
TRAIN_DATA = process_data(train_data)

test_data = []
with open(add_trailing_slash(dataDir)+testFile, "r") as f:
    test_data = json.load(f)
TEST_DATA = process_data(test_data)

dev_data = []
with open(add_trailing_slash(dataDir)+devFile, "r") as f:
    dev_data = json.load(f)
DEV_DATA = process_data(dev_data)



# Save the data
os.makedirs(add_trailing_slash(dataDir)+add_trailing_slash(dbDir), exist_ok=True)

saveDB("en", TRAIN_DATA, add_trailing_slash(dataDir)+add_trailing_slash(dbDir)+"train.spacy")
saveDB("en", TEST_DATA, add_trailing_slash(dataDir)+add_trailing_slash(dbDir)+"test.spacy")
saveDB("en", TEST_DATA, add_trailing_slash(dataDir)+add_trailing_slash(dbDir)+"dev.spacy")