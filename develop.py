import spacy
from spacy_sentiws import spaCySentiWS

print("Running the local development script for this example")

nlp = spacy.load('de_core_news_sm')
nlp.add_pipe('sentiws', config={'sentiws_path': 'data/sentiws/'})
doc = nlp('Die Dummheit der Unterwerfung blüht in hübschen Farben.')

for token in doc:
    print('{}, {}, {}'.format(token.text, token._.sentiws, token.pos_))
