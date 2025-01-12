import spacy

# Load the model
model_path = ""
nlp = spacy.load(model_path)

# Test the model
text = ""
doc = nlp(text)

# Print the entities
for ent in doc.ents:
    print(ent.text, ent.label_)