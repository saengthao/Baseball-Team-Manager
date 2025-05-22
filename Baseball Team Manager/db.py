import csv
from objects import Player

def read_players():
    players = []
    try:
        with open("players.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 5:
                    first, last, pos, ab, hits = row
                    players.append(Player(first, last, pos, int(ab), int(hits)))
    except FileNotFoundError:
        print("No players has been created yet. Starting a new list.")
    return players

def write_players(players):
    with open("players.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for p in players:
            writer.writerow([p.firstName, p.lastName, p.position, p.atBats, p.hits])
