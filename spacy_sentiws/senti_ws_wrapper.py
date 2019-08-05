from spacy_sentiws.senti_ws_entry import SentiWSEntry
import io


class SentiWSWrapper(object):
    def __init__(self, sentiws_path='data/sentiws'):
        self.load_files(sentiws_path)

    def map_pos(self, pos_universal_google):
        if pos_universal_google == 'VERB':
            return 'VVINF'
        elif pos_universal_google == 'ADJ':
            return 'ADJX'
        elif pos_universal_google == 'NOUN':
            return 'NN'
        elif pos_universal_google == 'ADV':
            return 'ADV'
        else:
            return None

    def contains(self, word, pos_universal_google):
        key = SentiWSEntry(word, self.map_pos(pos_universal_google))
        return (key in self.entries)

    def determine(self, word, pos_universal_google, lemmas=None):
        pos = self.map_pos(pos_universal_google)
        key = SentiWSEntry(word, pos)
        if key in self.entries:
            return self.entries[key]
        key = SentiWSEntry(word.lower(), pos)
        if key in self.entries:
            return self.entries[key]
        if lemmas is not None:
            for lemma in lemmas:
                key = SentiWSEntry(lemma, pos)
                if key in self.entries:
                    return self.entries[key]
        if pos == 'NN':
            key = SentiWSEntry(word[:1].upper() + word[1:], 'NN')
            if key in self.entries:
                return self.entries[key]
        return None

    def load_files(self, directory):
        self.entries = {}
        self.entries.update(self.load_file(directory + '/SentiWS_v2.0_Positive.txt'))
        self.entries.update(self.load_file(directory + '/SentiWS_v2.0_Negative.txt'))

    def process_line(self, line):
        entries = {}
        elements = line.split("\t")
        first_entry = elements[0].split("|")
        pos = first_entry[1]
        score = float(elements[1])
        forms = []
        forms.append(first_entry[0])
        if len(elements) > 2:
            for form in elements[2].split(","):
                forms.append(form)
        for form in forms:
            entries[SentiWSEntry(form, pos)] = score
        return entries

    def load_file(self, path):
        entries = {}
        with io.open(path, encoding='utf-8') as file:
            content = file.readlines()
            content = [x.strip() for x in content]
            for line in content:
                entries.update(self.process_line(line))
        return entries
