import spacy

# Load the model
def add_trailing_slash(path):
    if not path.endswith('/'):
        path += '/'
    return path

modelDir="models"
modelName="address"
modelPath=add_trailing_slash(modelDir)+add_trailing_slash(modelName)+"model-best"
nlp = spacy.load(modelPath)

# Test the model
text = "123 Main Street, Springfield, IL 62701"
doc = nlp(text)

# Print the entities
for ent in doc.ents:
    print(ent.text, ent.label_)