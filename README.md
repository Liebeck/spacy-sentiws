# spacy-sentiws
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/Liebeck/spacy-sentiws/master/LICENSE.md)
[![Build Status](https://api.travis-ci.org/Liebeck/spacy-sentiws.svg?branch=master)](https://travis-ci.org/Liebeck/spacy-sentiws)

This package uses the [spaCy 2.0 extensions](https://spacy.io/usage/processing-pipelines#extensions) to add [SentiWS](http://wortschatz.uni-leipzig.de/en/download) as German sentiment score directly into your spaCy pipeline.


## Usage
``` python
import spacy
from spacy_sentiws import spaCySentiWS

nlp = spacy.load('de')
sentiws = spaCySentiWS(sentiws_path='data/sentiws/')
nlp.add_pipe(sentiws)
doc = nlp('Die Dummheit der Unterwerfung blüht in hübschen Farben.')

for token in doc:
    print('{}, {}, {}'.format(token.text, token._.sentiws, token.pos_))
```

## Installation
1. Use pip to install spacy-sentiws
``` bash
pip install spacy-sentiws
```
2. Download the SentiWS http://pcai056.informatik.uni-leipzig.de/downloads/etc/SentiWS/SentiWS_v2.0.zip and unzip it.
