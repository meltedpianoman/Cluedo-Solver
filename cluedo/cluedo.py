from cluedo.notebook import *


class Cluedo:

    class Suggestion:

        def __init__(self,
                     suggestor,
                     character,
                     weapon,
                     room,
                     disprover,
                     card=None):
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
        self.previous_suggestions = []

    def _find_guilty(self, cards):
        for card in cards:
            innocent = len(self.players)
            for player in self.players:
                if self.notebook.get_player_status(
                        card, player) is PlayerStatus.DoesNotOwn:
                    innocent -= 1
            if innocent == 0:
                for c in cards:
                    if c is card:
                        self.notebook.set_card_status(c, CardStatus.Guilty)
                    else:
                        self.notebook.set_card_status(c, CardStatus.Innocent)
                return True
        return False

    def _process_previous_suggestions(self):
        for suggestion in self.previous_suggestions:
            character_status = self.notebook.get_player_status(
                suggestion.character, suggestion.disprover)
            weapon_status = self.notebook.get_player_status(
                suggestion.weapon, suggestion.disprover)
            room_status = self.notebook.get_player_status(
                suggestion.room, suggestion.disprover)
            if character_status is PlayerStatus.DoesNotOwn and weapon_status is PlayerStatus.DoesNotOwn:
                self.make_note(suggestion.room, suggestion.disprover)
            elif weapon_status is PlayerStatus.DoesNotOwn and room_status is PlayerStatus.DoesNotOwn:
                self.make_note(suggestion.character, suggestion.disprover)
            elif character_status is PlayerStatus.DoesNotOwn and room_status is PlayerStatus.DoesNotOwn:
                self.make_note(suggestion.weapon, suggestion.disprover)

    def get_players(self):
        return self.players

    def get_notebook(self):
        return self.notebook

    def make_note(self, card, player, status=PlayerStatus.Owns):
        self.notebook.set_player_status(card, player, status)
        if status is PlayerStatus.Owns:
            self.notebook.set_card_status(card, CardStatus.Innocent)
            for p in self.players:
                if p is not player:
                    self.notebook.set_player_status(card, p,
                                                    PlayerStatus.DoesNotOwn)

    def process_suggestion(self, suggestion):
        if suggestion.card_is_known():
            self.make_note(suggestion.card, suggestion.disprover)
        else:
            self.previous_suggestions.append(suggestion)
            index = self.players.index(suggestion.suggestor)
            while True:
                index = (index + 1) % len(self.players)
                player = self.players[index]
                if player is suggestion.disprover:
                    break
                if player is suggestion.suggestor:
                    break
                self.make_note(suggestion.character, player,
                               PlayerStatus.DoesNotOwn)
                self.make_note(suggestion.weapon, player,
                               PlayerStatus.DoesNotOwn)
                self.make_note(suggestion.room, player,
                               PlayerStatus.DoesNotOwn)

        self._process_previous_suggestions()

        if self._find_guilty(Characters) and self._find_guilty(
                Weapons) and self._find_guilty(Rooms):
            self.solved = True

    def is_solved(self):
        return self.solved
