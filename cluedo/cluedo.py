from cluedo.notebook import *


class Cluedo:

    def __init__(self):
        self.notebook = Notebook()
        self.ALL_CARDS = []
        for character in Character:
            self.ALL_CARDS.append(character)
        for weapon in Weapon:
            self.ALL_CARDS.append(weapon)
        for room in Room:
            self.ALL_CARDS.append(room)

    def get_notebook(self):
        return self.notebook

    def make_note(self, subject, innocent):
        self.notebook.make_note(subject, innocent)
        
    # make_suggestion(self)
