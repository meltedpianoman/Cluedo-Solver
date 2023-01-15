from cluedo.characters import *
from cluedo.weapons import *
from cluedo.rooms import *


class Notebook:

    def __init__(self):
        self.characters = []
        for character in Character:
            self.characters.append(Notebook.CharacterNote(character))
        self.weapons = []
        for weapon in Weapon:
            self.weapons.append(Notebook.WeaponNote(weapon))
        self.rooms = []
        for room in Room:
            self.rooms.append(Notebook.RoomNote(room))

    class CharacterNote:
        def __init__(self, character):
            self.name = character
            self.innocent = False

        def __str__(self):
            return self.name

        def is_innocent(self):
            return self.innocent;
    
    def get_characters(self):
        return self.characters

    class WeaponNote:
        def __init__(self, weapon):
            self.name = weapon
            self.innocent = False

        def __str__(self):
            return self.name

        def is_innocent(self):
            return self.innocent

    def get_weapons(self):
        return self.weapons

    class RoomNote:
        def __init__(self, room):
            self.name = room
            self.innocent = False

        def __str__(self):
            return self.name

        def is_innocent(self):
            return self.innocent

    def get_rooms(self):
        return self.rooms

    def make_note(self, subject, innocent):
        for character in self.characters:
            if character.name is subject:
                character.innocent = innocent
