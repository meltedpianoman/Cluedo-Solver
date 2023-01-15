from cluedo.cluedo import *


def print_notebook(notebook):
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


def main():
    game = Cluedo()
    notes = game.get_notebook()
    print_notebook(notes)


if __name__ == "__main__":
    main()
