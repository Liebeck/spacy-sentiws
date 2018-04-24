from spacy.tokens import Token
from spacy_sentiws.senti_ws_wrapper import SentiWSWrapper


class spaCySentiWS(object):
    def __init__(self, sentiws_path):
        self.sentiws = SentiWSWrapper(sentiws_path=sentiws_path)
        Token.set_extension('sentiws', getter=self.get_sentiment, force=True)

    def __call__(self, doc):
        for token in doc:
            token._.sentiws = self.get_sentiment(token)
        return doc

    def get_sentiment(self, token):
        return self.sentiws.determine(token.text, pos_universal_google=token.pos_)
