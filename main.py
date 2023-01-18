from cluedo.cluedo import *
import inquirer

class ConsoleGame:
    def print_notebook(self):
        notebook = self.game.get_notebook()
        print("+----------------+---+")
        for character in notebook.get_characters():
            tick = "x" if character['innocent'] else " "
            print(f"| {character['name']:<14} | {tick} |")
        print("+----------------+---+")
        for weapon in notebook.get_weapons():
            tick = "x" if weapon['innocent'] else " "
            print(f"| {weapon['name']:<14} | {tick} |")
        print("+----------------+---+")
        for room in notebook.get_rooms():
            tick = "x" if room['innocent'] else " "
            print(f"| {room['name']:<14} | {tick} |")
        print("+----------------+---+")
    
    
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
