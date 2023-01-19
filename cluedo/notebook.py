from cluedo.characters import *
from cluedo.weapons import *
from cluedo.rooms import *


class Notebook:

    class CardStatus(StrEnum):
        Unknown = auto()
        Guilty = auto()
        Innocent = auto()
    
    class PlayerStatus(StrEnum):
        Unknown = auto()
        Owns = auto()
        DoesNotOwn = auto()

    def __init__(self, players):
        initial_player_status = {}
        for player in players:
            initial_player_status.update(
                {player: Notebook.PlayerStatus.Unknown})

        self.notes = {}
        self.notes['characters'] = []
        for character in Character:
            self.notes['characters'].append({
                'name': character,
                'innocent': False,
                'status': Notebook.CardStatus.Unknown,
                'players': initial_player_status.copy()
            })
        self.notes['weapons'] = []
        for weapon in Weapon:
            self.notes['weapons'].append({
                'name': weapon,
                'innocent': False,
                'status': Notebook.CardStatus.Unknown,
                'players': initial_player_status.copy()
            })
        self.notes['rooms'] = []
        for room in Room:
            self.notes['rooms'].append({
                'name': room,
                'innocent': False,
                'status': Notebook.CardStatus.Unknown,
                'players': initial_player_status.copy()
            })

    def get_characters(self):
        return self.notes['characters']

    def get_weapons(self):
        return self.notes['weapons']

    def get_rooms(self):
        return self.notes['rooms']

    def get_card_status(self, card):
        try:
            card = Character[card]
        except:
            pass
        if isinstance(card, Character):
            for character in self.get_characters():
                if character['name'] is card:
                    return character['status']

        try:
            card = Weapon[card]
        except:
            pass
        if isinstance(card, Weapon):
            for weapon in self.get_weapons():
                if weapon['name'] is card:
                    return weapon['status']

        try:
            card = Room[card]
        except:
            pass
        if isinstance(card, Room):
            for room in self.get_rooms():
                if room['name'] is card:
                    return room['status']

        return Notebook.CardStatus.Unknown

    
    def get_player_status(self, card, player):
        try:
            card = Character[card]
        except:
            pass
        if isinstance(card, Character):
            for character in self.get_characters():
                if character['name'] is card:
                    try:
                        return character['players'][player]
                    except:
                        return Notebook.PlayerStatus.Unknown

        try:
            card = Weapon[card]
        except:
            pass
        if isinstance(card, Weapon):
            for weapon in self.get_weapons():
                if weapon['name'] is card:
                    try:
                        return weapon['players'][player]
                    except:
                        return Notebook.PlayerStatus.Unknown

        try:
            card = Room[card]
        except:
            pass
        if isinstance(card, Room):
            for room in self.get_rooms():
                if room['name'] is card:
                    try:
                        return room['players'][player]
                    except:
                        return Notebook.PlayerStatus.Unknown

        return Notebook.PlayerStatus.Unknown

    def make_note(self, card, player):
        try:
            card = Character[card]
        except:
            pass
        if isinstance(card, Character):
            for character in self.get_characters():
                if character['name'] is card:
                    character['innocent'] = True
                    character['status'] = Notebook.CardStatus.Innocent
                    for p in character['players']:
                        if p is player:
                            character['players'][p] = Notebook.PlayerStatus.Owns
                        else:
                            character['players'][p] = Notebook.PlayerStatus.DoesNotOwn
                    return

        try:
            card = Weapon[card]
        except:
            pass
        if isinstance(card, Weapon):
            for weapon in self.get_weapons():
                if weapon['name'] is card:
                    weapon['innocent'] = True
                    weapon['status'] = Notebook.CardStatus.Innocent
                    for p in weapon['players']:
                        if p is player:
                            weapon['players'][p] = Notebook.PlayerStatus.Owns
                        else:
                            weapon['players'][p] = Notebook.PlayerStatus.DoesNotOwn
                    return

        try:
            card = Room[card]
        except:
            pass
        if isinstance(card, Room):
            for room in self.get_rooms():
                if room['name'] is card:
                    room['innocent'] = True
                    room['status'] = Notebook.CardStatus.Innocent
                    for p in room['players']:
                        if p is player:
                            room['players'][p] = Notebook.PlayerStatus.Owns
                        else:
                            room['players'][p] = Notebook.PlayerStatus.DoesNotOwn
                    return

        raise ValueError(f"{card} is not a valid character, weapon or room")
