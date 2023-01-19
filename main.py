from cluedo.cluedo import *
import inquirer

class ConsoleGame:
    def print_notebook(self):
        notebook = self.game.get_notebook()
        header = "+----------------+---+"
        for player in self.players:
            header += "-"
            header += "-" * len(player)
            header += "-+"
        print(header)
        player_info = ""
        for player in self.players:
            player_info += " " + player + " |"
        print(f"|                |   |{player_info}")
        print(header)
        for card in Characters:
            innocent = "X" if notebook.get_card_status(card) is CardStatus.Innocent else " "
            player_info = ""
            for player in self.players:
                status = notebook.get_player_status(card, player)
                info = "x" if status is PlayerStatus.Owns else "-" if status is PlayerStatus.DoesNotOwn else " "
                player_info += info.center(len(player) + 2) + "|"
            print(f"| {card:<14} | {innocent} |{player_info}")
        print(header)
        for card in Weapons:
            innocent = "X" if notebook.get_card_status(card) is CardStatus.Innocent else " "
            player_info = ""
            for player in self.players:
                status = notebook.get_player_status(card, player)
                info = "x" if status is PlayerStatus.Owns else "-" if status is PlayerStatus.DoesNotOwn else " "
                player_info += info.center(len(player) + 2) + "|"
            print(f"| {card:<14} | {innocent} |{player_info}")
        print(header)
        for card in Rooms:
            innocent = "X" if notebook.get_card_status(card) is CardStatus.Innocent else " "
            player_info = ""
            for player in self.players:
                status = notebook.get_player_status(card, player)
                info = "x" if status is PlayerStatus.Owns else "-" if status is PlayerStatus.DoesNotOwn else " "
                player_info += info.center(len(player) + 2) + "|"
            print(f"| {card:<14} | {innocent} |{player_info}")
        print(header)
    
    
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
