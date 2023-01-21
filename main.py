from cluedo.cluedo import *
import inquirer

class ConsoleGame:
    class NotebookPrinter:
        def __init__(self, game, players):
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
            innocent = "X" if self.notebook.get_card_status(card) is CardStatus.Innocent else " "
            player_info = ""
            for player in self.players:
                status = self.notebook.get_player_status(card, player)
                info = "x" if status is PlayerStatus.Owns else "-" if status is PlayerStatus.DoesNotOwn else " "
                player_info += info.center(len(player) + 2) + "|"
            print(f"| {card:<14} | {innocent} |{player_info}")

        
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

    
    def get_initial_cards(self):
        choices = ["Done"] + self.game.ALL_CARDS
        while True:
            choice = inquirer.list_input("Give your initial cards", choices=choices)
            if choice == "Done":
                break
            self.game.make_note(choice, self.myself)
            choices.remove(choice)
     

def main():
    game = ConsoleGame()
    game.get_player_names()
    game.get_initial_cards()
    game.print_notebook()


if __name__ == "__main__":
    main()
