from cluedo.cluedo import *
import inquirer


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
            self.notebook = game.get_notebook()
            self.players = players
            self.header = "+----------------+---+"
            for player in self.players:
                self.header += "-"
                self.header += "-" * len(player)
                self.header += "-+"

        
        def _print_header(self):
            print(self.header)

        
        def _print_players(self):
            player_info = ""
            for player in self.players:
                player_info += " " + player + " |"
            print(f"|                |   |{player_info}")

        
        def _print_card(self, card):
            innocent = self.cardStatus[self.notebook.get_card_status(card)]
            player_info = ""
            for player in self.players:
                info = self.playerStatus[self.notebook.get_player_status(card, player)]
                player_info += info.center(len(player) + 2) + "|"
            print(f"| {card:<14} |{innocent}|{player_info}")

        
        def _print_cards(self, cards):
            for card in cards:
                self._print_card(card)

        
        def print(self):
            self._print_header()
            self._print_players()
            self._print_header()
            self._print_cards(Characters)
            self._print_header()
            self._print_cards(Weapons)
            self._print_header()
            self._print_cards(Rooms)
            self._print_header()

    
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
        self.game = Cluedo(self.players)

    
    def _get_initial_cards_for_category(self, cards, category):
        choices = ["Done"] + cards
        while True:
            choice = inquirer.list_input(f"Give your initial {category} cards",
                                         choices=choices)
            choices.remove(choice)
            if choice == "Done":
                break
            self.game.make_note(choice, self.myself, PlayerStatus.Owns)
        for card in choices:
            self.game.make_note(card, self.myself, PlayerStatus.DoesNotOwn)

    
    def get_initial_cards(self):
        self._get_initial_cards_for_category(self.game.CHARACTERS, "character")
        self._get_initial_cards_for_category(self.game.WEAPONS, "weapon")
        self._get_initial_cards_for_category(self.game.ROOMS, "room")
        return

    
    def process_suggestion(self):
        suggestor = inquirer.list_input("Who makes the suggestion?",
                                        choices=self.players)
        character = inquirer.list_input("Character?",
                                        choices=self.game.CHARACTERS)
        weapon = inquirer.list_input("Weapon?", choices=self.game.WEAPONS)
        room = inquirer.list_input("Room?", choices=self.game.ROOMS)
        disprovers = self.players.copy()
        disprovers.append("Nobody")
        disprovers.remove(suggestor)
        disprover = inquirer.list_input("Who disproves the suggestion?",
                                        choices=disprovers)
        if suggestor == self.myself and disprover != "Nobody":
            card = inquirer.list_input(
                f"What card was shown to you by {disprover}?",
                choices=[character, weapon, room])
        else:
            card = None
        self.game.process_suggestion(suggestor, character, weapon, room,
                                     disprover, card)

    
    def finished(self):
        return self.game.is_solved()


def main():
    game = ConsoleGame()
    game.get_player_names()
    game.get_initial_cards()
    game.print_notebook()
    while not game.finished():
        game.process_suggestion()
        game.print_notebook()


if __name__ == "__main__":
    main()
