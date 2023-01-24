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

    def __init__(self, players, initial_cards):
        self.NOBODY = "Nobody"
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
        self.myself = self.players[0]
        self.notebook = Notebook(self.ALL_CARDS, self.players)
        self.solved = False
        self.previous_suggestions = []

        for card in self.ALL_CARDS:
            if card in initial_cards:
                self.make_note(card, self.myself, PlayerStatus.Owns)
            else:
                self.make_note(card, self.myself, PlayerStatus.DoesNotOwn)
    
    def _find_guilty(self, cards):
        guilty = None
        innocent = []

        for card in cards:
            if self.notebook.get_card_status(card) is CardStatus.Innocent:
                innocent.append(card)
            players_that_do_not_own = 0
            for player in self.players:
                if self.notebook.get_player_status(card, player) is PlayerStatus.DoesNotOwn:
                    players_that_do_not_own += 1
            if players_that_do_not_own == len(self.players):
                guilty = card
                break

        if len(innocent) == (len(cards) - 1):
            for card in cards:
                if not card in innocent:
                    guilty = card
                    break

        if guilty:
            for card in cards:
                if card is guilty:
                    self.notebook.set_card_status(card, CardStatus.Guilty)
                    for player in self.players:
                        self.notebook.set_player_status(card, player, PlayerStatus.DoesNotOwn)
                else:
                    self.notebook.set_card_status(card, CardStatus.Innocent)
        
        return guilty != None

    
    def _process_previous_suggestions(self):
        for suggestion in self.previous_suggestions:
            if suggestion.card is not None:
                continue

            character_status = self.notebook.get_player_status(
                suggestion.character, suggestion.disprover)
            weapon_status = self.notebook.get_player_status(
                suggestion.weapon, suggestion.disprover)
            room_status = self.notebook.get_player_status(
                suggestion.room, suggestion.disprover)
            if character_status is PlayerStatus.Owns:
                suggestion.card = suggestion.character
            elif weapon_status is PlayerStatus.Owns:
                suggestion.card = suggestion.weapon
            elif room_status is PlayerStatus.Owns:
                suggestion.card = suggestion.room
            elif character_status is PlayerStatus.DoesNotOwn and weapon_status is PlayerStatus.DoesNotOwn:
                suggestion.card = suggestion.room
                self.make_note(suggestion.room, suggestion.disprover)
            elif weapon_status is PlayerStatus.DoesNotOwn and room_status is PlayerStatus.DoesNotOwn:
                suggestion.card = suggestion.character
                self.make_note(suggestion.character, suggestion.disprover)
            elif character_status is PlayerStatus.DoesNotOwn and room_status is PlayerStatus.DoesNotOwn:
                suggestion.card = suggestion.weapon
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
        self.previous_suggestions.append(suggestion)       
        if suggestion.card_is_known():
            self.make_note(suggestion.card, suggestion.disprover)

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

        cards_guilty = 0
        if self._find_guilty(Characters):
            cards_guilty += 1
        if self._find_guilty(Weapons):
            cards_guilty +=1
        if self._find_guilty(Rooms):
            cards_guilty += 1
        if cards_guilty == 3:
            self.solved = True

    def is_solved(self):
        return self.solved
