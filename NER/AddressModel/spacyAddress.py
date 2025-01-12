import spacy
import argparse

# Load the model
def add_trailing_slash(path):
    if not path.endswith('/'):
        path += '/'
    return path

def parse_args():
    parser = argparse.ArgumentParser(description='Load and test a spaCy model')
    parser.add_argument('-md', '--modelDir', default='models', help='Directory containing the model')
    parser.add_argument('-mn', '--modelName', default='address', help='Name of the model')
    parser.add_argument('-t', '--text', default='123 Main Street, Springfield, IL 62701', help='Text to test the model')
    return parser.parse_args()

def main():
    args = parse_args()
    modelDir = args.modelDir
    modelName = args.modelName
    text = args.text

    modelPath = add_trailing_slash(modelDir) + add_trailing_slash(modelName) + "model-best"
    nlp = spacy.load(modelPath)

    doc = nlp(text)

    # Print the entities
    for ent in doc.ents:
        print(ent.text, ent.label_)

if __name__ == "__main__":
    main()