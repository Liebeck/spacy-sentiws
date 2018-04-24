import unittest
import spacy
from spacy_sentiws import spaCySentiWS


class SentiWSWrapperTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.nlp = spacy.load('de')
        sentiws = spaCySentiWS(sentiws_path='data/sentiws/')
        self.nlp.add_pipe(sentiws)

    def test_example1(self):
        doc = self.nlp('Die Dummheit der Unterwerfung blüht in hübschen Farben.')
        assert doc[0]._.sentiws is None
        assert doc[1]._.sentiws == -0.4877
        assert doc[2]._.sentiws is None
        assert doc[3]._.sentiws == -0.3279
        assert doc[4]._.sentiws == 0.2028
        assert doc[5]._.sentiws is None
        assert doc[6]._.sentiws == 0.4629
        assert doc[7]._.sentiws is None
        assert doc[8]._.sentiws is None
