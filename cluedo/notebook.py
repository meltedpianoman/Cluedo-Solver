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

        
        def set_card_status(self, status):
            self.status = status

        
        def make_note(self, player, status=PlayerStatus.Owns):
            self.players[player] = status
                

    def __init__(self, cards, players):
        self.cards = {}
        for card in cards:
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


    def set_card_status(self, card, status):
        if card in self.cards:
            self.cards[card].set_card_status(status)
        else:
            raise ValueError(f"{card} is not a valid character, weapon or room")

    
    def set_player_status(self, card, player, status=PlayerStatus.Owns):
        if status is PlayerStatus.Unknown:
            raise ValueError(f"{status} is not a valid player status")
        if card in self.cards:
            self.cards[card].make_note(player, status)
        else:
            raise ValueError(f"{card} is not a valid character, weapon or room")
