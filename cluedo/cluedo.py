from cluedo.notebook import *


class Cluedo:
    def __init__(self, players):
        self.CHARACTERS = []
        self.WEAPONS = []
        self.ROOMS = []
        self.ALL_CARDS = []
        for card in Characters:
            self.CHARACTERS.append(card)
            self.ALL_CARDS.append(card)
        for card in Weapons:
            self.WEAPONS.append(card)
            self.ALL_CARDS.append(card)
        for card in Rooms:
            self.ROOMS.append(card)
            self.ALL_CARDS.append(card)
        self.players = players
        self.notebook = Notebook(self.ALL_CARDS, self.players)

    def get_players(self):
        return self.players

    
    def get_notebook(self):
        return self.notebook

    
    def make_note(self, subject, innocent):
        self.notebook.make_note(subject, innocent)

        
    def process_suggestion(self, suggestor, character, weapon, room, disprover, card = None):
        pass

    
    def is_solved(self):
        return False
