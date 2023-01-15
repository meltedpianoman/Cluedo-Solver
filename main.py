import inquirer
from cluedo.cluedo import *


def print_notebook(game):
    notebook = game.get_notebook()
    print("----------------------")
    for character in notebook.get_characters():
        tick = "x" if character['innocent'] else " "
        print(f"| {character['name']:<14} | {tick} |")
    print("----------------------")
    for weapon in notebook.get_weapons():
        tick = "x" if weapon['innocent'] else " "
        print(f"| {weapon['name']:<14} | {tick} |")
    print("----------------------")
    for room in notebook.get_rooms():
        tick = "x" if room['innocent'] else " "
        print(f"| {room['name']:<14} | {tick} |")
    print("----------------------")

def get_initial_cards(game):
    choices = game.ALL_CARDS
    choices.append("Done")
    while True:
        choice = inquirer.list_input("initial cards", choices=choices)
        if choice == "Done":
            break
        game.make_note(choice, True)
        choices.remove(choice)
 

def main():
    game = Cluedo()
    print_notebook(game)
    get_initial_cards(game)
    print_notebook(game)


if __name__ == "__main__":
    main()
