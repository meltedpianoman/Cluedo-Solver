from cluedo.cluedo import *
import inquirer

DEBUG=True

class ConsoleGame:

    class NotebookPrinter:

        def __init__(self, game, players):
            self.cardStatus = {
                CardStatus.Unknown: "   ",
                CardStatus.Innocent: " x ",
                CardStatus.Guilty: u"\U0001F480 ",
            }
            self.playerStatus = {
                PlayerStatus.Unknown: " ",
                PlayerStatus.Owns: "x",
                PlayerStatus.DoesNotOwn: "-",
            }
            self.game = game
            self.notebook = self.game.get_notebook()
            self.players = players
            self.header = "+----------------+---+"
            self.max_player_name = len(self.game.NOBODY)
            for player in self.players:
                self.header += "-"
                self.header += "-" * len(player)
                self.header += "-+"
                if len(player) > self.max_player_name:
                    self.max_player_name = len(player)
            self.max_card_name = 0
            for card in self.game.ALL_CARDS:
                if len(card) > self.max_card_name:
                    self.max_card_name = len(card)

        
        def _print_header(self):
            print(self.header)

        
        def _print_players(self):
            player_info = ""
            for player in self.players:
                player_info += " " + player + " |"
            print("|                |   |{}".format(player_info))

        
        def _print_card(self, card):
            innocent = self.cardStatus[self.notebook.get_card_status(card)]
            player_info = ""
            for player in self.players:
                info = self.playerStatus[self.notebook.get_player_status(card, player)]
                player_info += info.center(len(player) + 2) + "|"
            print("| {:<{}} |{}|{}".format(card, self.max_card_name, innocent, player_info))

        
        def _print_cards(self, cards):
            for card in cards:
                self._print_card(card)

        
        def _print_suggestion(self, suggestion):
            print("|{:<{}}|{:<{}}|{:<{}}|{:<{}}|{:<{}}|{:<{}}|".format(
                suggestion.suggestor, self.max_player_name,
                suggestion.character, self.max_card_name,
                suggestion.weapon, self.max_card_name,
                suggestion.room, self.max_card_name,
                suggestion.disprover, self.max_player_name,
                suggestion.card if suggestion.card is not None else "",
                self.max_card_name))


        def _print_suggestion_history(self):
            print("SUGGESTIONS")
            print("|{:<{}}|{:<{}}|{:<{}}|{:<{}}|{:<{}}|{:<{}}|".format(
                "ASK", self.max_player_name,
                "CHARACTER", self.max_card_name,
                "WEAPON", self.max_card_name,
                "ROOM", self.max_card_name,
                "GIVE", self.max_player_name,
                "CARD", self.max_card_name))
            for suggestion in self.game.previous_suggestions:
                self._print_suggestion(suggestion)

        
        def print(self):
            if DEBUG:
                self._print_suggestion_history()
                print("")
            self._print_header()
            self._print_players()
            self._print_header()
            self._print_cards(Characters)
            self._print_header()
            self._print_cards(Weapons)
            self._print_header()
            self._print_cards(Rooms)
            self._print_header()
            print("")

    
    def __init__(self):
        pass

    
    def print_notebook(self):
        printer = ConsoleGame.NotebookPrinter(self.game, self.players)
        printer.print()
        return

    
    def get_player_names(self):
        self.players = []
        self.myself = inquirer.text("What is your name?")
        self.players.append(self.myself)
        while True:
            name = inquirer.text("Next player name?")
            if not name:
                break
            self.players.append(name)

    
    def _get_initial_cards_for_category(self, cards, category):
        selected = []
        choices = ["Done"]
        for card in cards:
            choices.append(card)
        while True:
            choice = inquirer.list_input(f"Give your initial {category} cards",
                                         choices=choices)
            choices.remove(choice)
            if choice == "Done":
                break
            selected.append(choice)

        return selected

    
    def get_initial_cards(self):
        self.initial_cards = []
        self.initial_cards.extend(
            self._get_initial_cards_for_category(Characters, "character"))
        self.initial_cards.extend(
            self._get_initial_cards_for_category(Weapons, "weapon"))
        self.initial_cards.extend(
            self._get_initial_cards_for_category(Rooms, "room"))
        return

    
    def start_game(self):
        self.game = Cluedo(self.players, self.initial_cards)

    
    def process_suggestion(self):
        suggestor = inquirer.list_input("Who makes the suggestion?",
                                        choices=self.players)
        character = inquirer.list_input("Character?",
                                        choices=self.game.CHARACTERS)
        weapon = inquirer.list_input("Weapon?", choices=self.game.WEAPONS)
        room = inquirer.list_input("Room?", choices=self.game.ROOMS)
        disprovers = self.players.copy()
        disprovers.append(self.game.NOBODY)
        disprovers.remove(suggestor)
        disprover = inquirer.list_input("Who disproves the suggestion?",
                                        choices=disprovers)
        if suggestor == self.myself and disprover != self.game.NOBODY:
            card = inquirer.list_input(
                f"What card was shown to you by {disprover}?",
                choices=[character, weapon, room])
        else:
            card = None
        
        suggestion = Cluedo.Suggestion(suggestor, character, weapon, room, disprover, card)
        self.game.process_suggestion(suggestion)

    
    def finished(self):
        return self.game.is_solved()


def main():
    game = ConsoleGame()
    game.get_player_names()
    game.get_initial_cards()
    game.start_game()
    game.print_notebook()
    while not game.finished():
        game.process_suggestion()
        game.print_notebook()


if __name__ == "__main__":
    main()
