from cluedo.notebook import *


class Cluedo:
    def __init__(self, players):
        self.players = players
        self.notebook = Notebook(self.players)
        self.ALL_CARDS = []
        for character in Characters:
            self.ALL_CARDS.append(character)
        for weapon in Weapons:
            self.ALL_CARDS.append(weapon)
        for room in Rooms:
            self.ALL_CARDS.append(room)

    def get_players(self):
        return self.players

    def get_notebook(self):
        return self.notebook

    def make_note(self, subject, innocent):
        self.notebook.make_note(subject, innocent)
        
    # make_suggestion(self)
