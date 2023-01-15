from cluedo.characters import *
from cluedo.weapons import *
from cluedo.rooms import *


class Notebook:

    def __init__(self):
        self.notes = {}
        self.notes['characters'] = []
        for character in Character:
            self.notes['characters'].append({'name': character, 'innocent': False})
        self.notes['weapons'] = []
        for weapon in Weapon:
            self.notes['weapons'].append({'name': weapon, 'innocent': False})
        self.notes['rooms'] = []
        for room in Room:
            self.notes['rooms'].append({'name': room, 'innocent': False})

    def get_characters(self):
        return self.notes['characters']

    def get_weapons(self):
        return self.notes['weapons']

    def get_rooms(self):
        return self.notes['rooms']

    def make_note(self, subject, innocent):
        for character in self.get_characters():
            if character['name'] is subject:
                character['innocent'] = innocent
                break
