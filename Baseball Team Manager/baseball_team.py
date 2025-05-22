import db
from objects import Player
from datetime import datetime

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

def display_separator():
    print("============================================================")

def display_title():
    print("\t\tBaseball Team Manager")

def display_dates():
    print()
    date_format = "%Y-%m-%d"
    now = datetime.now()
    current_date = datetime(now.year, now.month, now.day)
    print(f"CURRENT DATE:    {current_date.strftime(date_format)}")

    while True:
        game_date_str = input("GAME DATE:       ")
        if game_date_str == "":
            print()
            return

        try:
            game_date = datetime.strptime(game_date_str, date_format)
        except ValueError:
            print("Incorrect date format. Please try again.")
            continue

        time_span = game_date - current_date

        if time_span.days > -1:
            print(f"DAYS UNTIL GAME: {time_span.days}")
        print()
        break

def display_menu():
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Show menu")
    print("8 - Exit program\n")

def display_positions():
    print("POSITIONS")
    print(", ".join(POSITIONS))

def get_player_position():
    while True:
        pos = input("Position: ").upper()
        if pos in POSITIONS:
            return pos
        else:
            print("Invalid position. Must be one of the following:")
            display_positions()

def get_at_bats():
    while True:
        try:
            ab = int(input("At bats: "))
            if ab >= 0:
                return ab
            print("Invalid entry. Must be 0 or greater.")
        except ValueError:
            print("Please enter a valid number.")

def get_hits(at_bats):
    while True:
        try:
            hits = int(input("Hits: "))
            if 0 <= hits <= at_bats:
                return hits
            print(f"Invalid entry. Must be from 0 to {at_bats}.")
        except ValueError:
            print("Please enter a valid number.")

def get_lineup_number(players, prompt):
    while True:
        try:
            num = int(input(prompt))
            if 1 <= num <= len(players):
                return num - 1
            print(f"Invalid entry. Must be from 1 to {len(players)}.")
        except ValueError:
            print("Please enter a valid number.")

def add_player(players):
    first = input("First name: ")
    last = input("Last name: ")
    pos = get_player_position()
    ab = get_at_bats()
    h = get_hits(ab)
    new_player = Player(first, last, pos, ab, h)
    players.append(new_player)
    print(f"{new_player.fullName} was added.")

def delete_player(players):
    num = get_lineup_number(players, "Lineup number to delete: ")
    removed = players.pop(num)
    print(f"{removed.fullName} was removed.")

def move_player(players):
    current = get_lineup_number(players, "Current lineup number: ")
    new = get_lineup_number(players, "New lineup number: ")
    player = players.pop(current)
    players.insert(new, player)
    print(f"{player.fullName} was moved.")

def edit_player_position(players):
    num = get_lineup_number(players, "Lineup number: ")
    pos = get_player_position()
    players[num].position = pos
    print(f"{players[num].fullName}'s position updated.")

def edit_player_stats(players):
    num = get_lineup_number(players, "Lineup number: ")
    ab = get_at_bats()
    h = get_hits(ab)
    players[num].atBats = ab
    players[num].hits = h
    print(f"{players[num].fullName}'s stats updated.")

def display_lineup(players):
    print()
    print("\tPlayer\t\tPOS\tAB\tH\tAVG")
    print("------------------------------------------------------------")
    for i, player in enumerate(players, 1):
        avg = player.battingAvg
        print(f"{i}\t{player.fullName}\t{player.position}\t{player.atBats}\t{player.hits}\t{player.battingAvg:.3f}")

def main():
    display_separator()
    display_title()
    display_dates()
    display_menu()
    display_positions()
    display_separator()

    players = db.read_players()

    while True:
        option = input("Menu option: ")

        if option == "1":
            display_lineup(players)
        elif option == "2":
            add_player(players)
        elif option == "3":
            delete_player(players)
        elif option == "4":
            move_player(players)
        elif option == "5":
            edit_player_position(players)
        elif option == "6":
            edit_player_stats(players)
        elif option == "7":
            display_menu()
        elif option == "8":
            db.write_players(players)
            print("Bye!")
            break
        else:
            print("Invalid menu option.")
        print()

main()
