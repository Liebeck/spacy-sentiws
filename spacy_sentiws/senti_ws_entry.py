class SentiWSEntry(object):
    def __init__(self, form, pos):
        self.form = form
        self.pos = pos

    def __str__(self):
        return '{}|{}'.format(self.form, self.pos)

    def __hash__(self):
        return hash((self.form, self.pos))

    def __eq__(self, other):
        return (self.form, self.pos) == (other.form, other.pos)

    def __ne__(self, other):
        return not (self == other)
