from setuptools import setup, find_packages

setup(
    name='spacy_iwnlp',
    packages=find_packages(),
    version='0.0.1',
    description='Integration of SentiWS as spaCy extension',
    author='Matthias Liebeck',
    author_email='liebeck@cs.uni-duesseldorf.de',
    url='https://github.com/Liebeck/spacy-sentiws',
    download_url='https://github.com/Liebeck/spacy-sentiws/archive/0.0.1.tar.gz',
    keywords=['IWNLP', 'NLP', 'German', 'sentiment', 'Wiktionary', 'spaCy']
)
