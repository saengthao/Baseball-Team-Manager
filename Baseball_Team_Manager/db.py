#######################################################################################################
# Import the sqlite3 library into the program.                                                        #
#######################################################################################################
import sqlite3

from contextlib import closing

from objects import Player, Lineup

DB_FILE = "player_db.sqlite"

conn = None

def connect():
    global conn
    if not conn:
#######################################################################################################
# Assign the DB_FILE variable with the name of the .sqlite database.  IE: myDB.sqlite                 #                                                    
#######################################################################################################
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_player(row):
    return Player(row["firstName"], row["lastName"],
                  row["position"], row["atBats"], row["hits"],
                  row["batOrder"], row["playerID"])

#######################################################################################################
# Assign the query variable below for the get_players() method. From the Player table,                #
# select playerID, batOrder,firstName, lastName,position, atBats, hits.  Order the select by batOrder.#
#######################################################################################################
def get_players():    
    query = '''SELECT playerID, batOrder, firstName, lastName, position, atBats, hits FROM Player ORDER BY batOrder'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    players = Lineup()
    for row in results:
        player = make_player(row)
        players.add(player)
    return players

def get_player(id):
    query = '''SELECT playerID, batOrder, firstName, lastName,
                      position, atBats, hits
               FROM Player
               WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (id,))
        row = c.fetchone()
        if row:
            player = make_player(row)
            return player
        else:
            return None

#######################################################################################################
# Assign the sql variable below for the add_players(player) method. Insert firstName, lastName,       #
# position, atBats, hits, batOrder.  Use a ? for each of the values in the values list.               #
#######################################################################################################

def add_player(player):
    sql = '''INSERT INTO Player (firstName, lastName, position, atBats, hits, batOrder) VALUES (?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.firstName, player.lastName, player.position,
                        player.atBats, player.hits, player.batOrder))
        conn.commit()

#######################################################################################################
# Assign the sql variable below for the delete_players(player) method. Ensure you use a WHERE         #
# clause that filters on playerID that is passed into the parameter.                                  #
#######################################################################################################
def delete_player(player):
    sql = '''DELETE FROM Player WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.playerID,))
        conn.commit()

def update_bat_order(lineup):
    for num, player in enumerate(lineup, start=1):
        player.batOrder = num
        sql = '''UPDATE Player
                 SET batOrder = ?
                 WHERE playerID = ?'''
        with closing(conn.cursor()) as c:
            c.execute(sql, (player.batOrder, player.playerID))
    conn.commit()      

#######################################################################################################
# Assign the sql variable below for the update_players(player) method. You will want to set the       #
# position, atBats, and hits fields.  Ensure you use a WHERE clause to filter on the playerID.        #
#######################################################################################################
def update_player(player):
    sql = '''UPDATE Player SET position = ?, atBats = ?, hits = ? WHERE playerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (player.position, player.atBats,
                        player.hits, player.playerID))
        conn.commit()

def main():
    connect()
    players = get_players()
    for player in players:
        print(player.batOrder, player.firstName, player.lastName,
              player.position, player.atBats, player.hits,
              player.battingAvg)


if __name__ == "__main__":
    main()
