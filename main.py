from cluedo.cluedo import *
import inquirer

def print_notebook(game):
    notebook = game.get_notebook()
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


def get_player_names():
    players = []
    name = inquirer.text("What is your name?")
    players.append(name)
    while True:
        name = inquirer.text("Next player name?")
        if not name:
            break
        players.append(name)
        
    return players

def get_initial_cards(game):
    choices = ["Done"] + game.ALL_CARDS
    while True:
        choice = inquirer.list_input("Give your initial cards", choices=choices)
        if choice == "Done":
            break
        game.make_note(choice, True)
        choices.remove(choice)
 

def main():
    players = get_player_names()
    game = Cluedo(players)
    get_initial_cards(game)
    print_notebook(game)


if __name__ == "__main__":
    main()
