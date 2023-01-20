from cluedo.characters import *
from cluedo.weapons import *
from cluedo.rooms import *

class CardStatus(StrEnum):
    Unknown = auto()
    Guilty = auto()
    Innocent = auto()

class PlayerStatus(StrEnum):
    Unknown = auto()
    Owns = auto()
    DoesNotOwn = auto()

class Notebook:

    class CardInfo:
        def __init__(self, card, players):
            self.card = card
            self.status = CardStatus.Unknown
            self.players = {}
            for player in players:
                self.players.update({player: PlayerStatus.Unknown})

        def get_card_status(self):
            return self.status

        def get_player_status(self, player):
            try:
                return self.players[player]
            except:
                return PlayerStatus.Unknown

        def make_note(self, player):
            self.status = CardStatus.Innocent
            for p in self.players:
                if p is player:
                    self.players[p] = PlayerStatus.Owns
                else:
                    self.players[p] = PlayerStatus.DoesNotOwn
            

    def __init__(self, players):
        self.cards = {}
        for card in Characters:
            self.cards.update({card: Notebook.CardInfo(card, players)})
        for card in Weapons:
            self.cards.update({card: Notebook.CardInfo(card, players)})
        for card in Rooms:
            self.cards.update({card: Notebook.CardInfo(card, players)})

    
    def get_card_status(self, card):
        if card in self.cards:
            return self.cards[card].get_card_status()
        else:
            return CardStatus.Unknown

    
    def get_player_status(self, card, player):
        if card in self.cards:
            return self.cards[card].get_player_status(player)
        else:
            return PlayerStatus.Unknown


    def make_note(self, card, player):
        if card in self.cards:
            self.cards[card].make_note(player)
        else:
            raise ValueError(f"{card} is not a valid character, weapon or room")
