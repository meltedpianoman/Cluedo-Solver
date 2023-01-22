from cluedo.notebook import *


class Cluedo:
    class Suggestion:
        def __init__(self, suggestor, character, weapon, room, disprover, card = None):
            self.suggestor = suggestor
            self.character = character
            self.weapon = weapon
            self.room = room
            self.disprover = disprover
            self.card = card

        def card_is_known(self):
            return self.card is not None
    
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
        self.solved = False

    def _find_guilty(self, cards):
        for card in cards:
            innocent = len(self.players)
            for player in self.players:
                if self.notebook.get_player_status(card, player) is PlayerStatus.DoesNotOwn:
                    innocent -= 1
            if innocent == 0:
                for c in cards:
                    if c is card:
                        self.notebook.set_card_status(c, CardStatus.Guilty)
                    else:
                        self.notebook.set_card_status(c, CardStatus.Innocent)
                return True
        return False

    def get_players(self):
        return self.players

    
    def get_notebook(self):
        return self.notebook

    
    def make_note(self, subject, player, status=PlayerStatus.Owns):
        self.notebook.make_note(subject, player, status)

        
    def process_suggestion(self, suggestion):
        if suggestion.card_is_known():
            self.notebook.make_note(suggestion.card, suggestion.disprover)
        else:
            index = self.players.index(suggestion.suggestor)
            while True:
                index = (index + 1) % len(self.players)
                player = self.players[index]
                if player is suggestion.disprover:
                    break
                if player is suggestion.suggestor:
                    break
                self.notebook.make_note(suggestion.character, player, PlayerStatus.DoesNotOwn)
                self.notebook.make_note(suggestion.weapon, player, PlayerStatus.DoesNotOwn)
                self.notebook.make_note(suggestion.room, player, PlayerStatus.DoesNotOwn)

        if self._find_guilty(Characters) and self._find_guilty(Weapons) and self._find_guilty(Rooms):
            self.solved = True

    
    def is_solved(self):
        return self.solved
