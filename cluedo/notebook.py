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

    def __init__(self, players):
        initial_player_status = {}
        for player in players:
            initial_player_status.update({player: PlayerStatus.Unknown})

        self.notes = {}
        self.notes['characters'] = []
        for character in Characters:
            self.notes['characters'].append({
                'name': character,
                'status': CardStatus.Unknown,
                'players': initial_player_status.copy()
            })
        self.notes['weapons'] = []
        for weapon in Weapons:
            self.notes['weapons'].append({
                'name': weapon,
                'status': CardStatus.Unknown,
                'players': initial_player_status.copy()
            })
        self.notes['rooms'] = []
        for room in Rooms:
            self.notes['rooms'].append({
                'name': room,
                'status': CardStatus.Unknown,
                'players': initial_player_status.copy()
            })

    
    def get_card_status(self, card):
        try:
            card = Characters[card]
        except:
            pass
        if isinstance(card, Characters):
            for character in self.notes['characters']:
                if character['name'] is card:
                    return character['status']

        try:
            card = Weapons[card]
        except:
            pass
        if isinstance(card, Weapons):
            for weapon in self.notes['weapons']:
                if weapon['name'] is card:
                    return weapon['status']

        try:
            card = Rooms[card]
        except:
            pass
        if isinstance(card, Rooms):
            for room in self.notes['rooms']:
                if room['name'] is card:
                    return room['status']

        return CardStatus.Unknown

    
    def get_player_status(self, card, player):
        try:
            card = Characters[card]
        except:
            pass
        if isinstance(card, Characters):
            for character in self.notes['characters']:
                if character['name'] is card:
                    try:
                        return character['players'][player]
                    except:
                        return PlayerStatus.Unknown

        try:
            card = Weapons[card]
        except:
            pass
        if isinstance(card, Weapons):
            for weapon in self.notes['weapons']:
                if weapon['name'] is card:
                    try:
                        return weapon['players'][player]
                    except:
                        return PlayerStatus.Unknown

        try:
            card = Rooms[card]
        except:
            pass
        if isinstance(card, Rooms):
            for room in self.notes['rooms']:
                if room['name'] is card:
                    try:
                        return room['players'][player]
                    except:
                        return PlayerStatus.Unknown

        return PlayerStatus.Unknown

    def make_note(self, card, player):
        try:
            card = Characters[card]
        except:
            pass
        if isinstance(card, Characters):
            for character in self.notes['characters']:
                if character['name'] is card:
                    character['status'] = CardStatus.Innocent
                    for p in character['players']:
                        if p is player:
                            character['players'][p] = PlayerStatus.Owns
                        else:
                            character['players'][p] = PlayerStatus.DoesNotOwn
                    return

        try:
            card = Weapons[card]
        except:
            pass
        if isinstance(card, Weapons):
            for weapon in self.notes['weapons']:
                if weapon['name'] is card:
                    weapon['status'] = CardStatus.Innocent
                    for p in weapon['players']:
                        if p is player:
                            weapon['players'][p] = PlayerStatus.Owns
                        else:
                            weapon['players'][p] = PlayerStatus.DoesNotOwn
                    return

        try:
            card = Rooms[card]
        except:
            pass
        if isinstance(card, Rooms):
            for room in self.notes['rooms']:
                if room['name'] is card:
                    room['status'] = CardStatus.Innocent
                    for p in room['players']:
                        if p is player:
                            room['players'][p] = PlayerStatus.Owns
                        else:
                            room['players'][p] = PlayerStatus.DoesNotOwn
                    return

        raise ValueError(f"{card} is not a valid character, weapon or room")
