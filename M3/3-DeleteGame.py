import mysql.connector

def DeleteGame(game_id):
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }
    conexion = mysql.connector.connect(**config)
    try:
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM game_food WHERE game_id = {}".format(game_id))

        # Delete weapons
        cursor.execute("DELETE FROM game_weapons WHERE game_id = {}".format(game_id))

        # Delete enemies
        cursor.execute("DELETE FROM game_enemies WHERE game_id = {}".format(game_id))

        # Delete chests_opened
        cursor.execute("DELETE FROM game_chests_opened WHERE game_id = {}".format(game_id))

        # Delete sanctuaries_opened
        cursor.execute("DELETE FROM game_sanctuaries_opened WHERE game_id = {}".format(game_id))
        # Delete player 
        cursor.execute("DELETE FROM game WHERE game_id = {}".format(game_id))

        # Delete foods 


        conexion.commit()

    finally:
        cursor.close()
        conexion.close()

#PASARLE LA ID DE LA PARTIDA A BORRAR EN EL MENU SAVED GAMES
game_id = 9
DeleteGame(game_id)
