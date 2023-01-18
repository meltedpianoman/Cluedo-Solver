from cluedo.characters import *
from cluedo.weapons import *
from cluedo.rooms import *


class Notebook:
    class PlayerStatus(StrEnum):
        Unknown = auto()
        Owns = auto()
        DoesNotOwn = auto()
    
    def __init__(self, players):
        initial_player_status = {}
        for player in players:
            initial_player_status.update({player: Notebook.PlayerStatus.Unknown})

        self.notes = {}
        self.notes['characters'] = []
        for character in Character:
            self.notes['characters'].append({'name': character, 'innocent': False, 'players': initial_player_status.copy()})
        self.notes['weapons'] = []
        for weapon in Weapon:
            self.notes['weapons'].append({'name': weapon, 'innocent': False, 'players': initial_player_status.copy()})
        self.notes['rooms'] = []
        for room in Room:
            self.notes['rooms'].append({'name': room, 'innocent': False, 'players': initial_player_status.copy()})

    def get_characters(self):
        return self.notes['characters']

    def get_weapons(self):
        return self.notes['weapons']

    def get_rooms(self):
        return self.notes['rooms']

    def make_note(self, subject, player):
        try:
            subject = Character[subject]
        except:
            pass
        if isinstance(subject, Character):
            for character in self.get_characters():
                if character['name'] is subject:
                    character['innocent'] = True
                    for p in character['players']:
                        if p is player:
                            character['players'][p] = Notebook.PlayerStatus.Owns
                        else:
                            character['players'][p] = Notebook.PlayerStatus.DoesNotOwn
                    return

        try:
            subject = Weapon[subject]
        except:
            pass    
        if isinstance(subject, Weapon):
            for weapon in self.get_weapons():
                if weapon['name'] is subject:
                    weapon['innocent'] = True
                    for p in weapon['players']:
                        if p is player:
                            weapon['players'][p] = Notebook.PlayerStatus.Owns
                        else:
                            weapon['players'][p] = Notebook.PlayerStatus.DoesNotOwn
                    return

        try:
            subject = Room[subject]
        except:
            pass    
        if isinstance(subject, Room):
            for room in self.get_rooms():
                if room['name'] is subject:
                    room['innocent'] = True
                    for p in room['players']:
                        if p is player:
                            room['players'][p] = Notebook.PlayerStatus.Owns
                        else:
                            room['players'][p] = Notebook.PlayerStatus.DoesNotOwn
                    return
        
        raise ValueError(f"{subject} is not a valid character, weapon or room")
     