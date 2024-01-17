import mysql.connector
import datetime

game = { #JUGADOR
    "game_id": 6,
    "player": {
        "user_name": "Link",
        "health": 2,
        "bm_countdown": 25,
        "total_blood_moon": 0,
        "region": "hyrule",
        "created_at": datetime.datetime.now(),
        "modified_at": datetime.datetime.now(),

    },
    "foods": { #COMIDA
        "Fish": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Vegetables": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Meat": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Salads": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Pescatarian": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Roasted": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        }
    },
    "weapons": { #ARMAS
        "Shield": {
            "equipped": 0,
            "lives_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "total_weapons": 0
        },
        "Sword": {
            "equipped": 0,
            "lives_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "total_weapons": 0
        },
        "Wood Sword": {
            "equipped": 0,
            "lives_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "total_weapons": 0
        },
        "Wood Shield": {
            "equipped": 0,
            "lives_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "total_weapons": 0
        }
    },
    "enemies": { #ENEMIGOS
            0: {
            "region": "hyrule",
            "xpos": 36,
            "ypos": 5,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at":datetime.datetime.now()
        },
            1: {
            "region": "hyrule",
            "xpos": 21,
            "ypos": 9,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            2: {
            "region": "death_mountain",
            "xpos": 51,
            "ypos": 3,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            3: {
            "region": "death_mountain",
            "xpos": 13,
            "ypos": 4,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            4: {
            "region": "gerudo",
            "xpos": 3,
            "ypos": 4,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            5: {
            "region": "gerudo",
            "xpos": 38,
            "ypos": 6,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            6: {
            "region": "necluda",
            "xpos": 10,
            "ypos": 2,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            7: {
            "region": "necluda",
            "xpos": 38,
            "ypos": 6,
            "lifes_remaining": 2,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },

    },
    "chests_opened": {
        0: {
            "region": "hyrule",
            "xpos": 48,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        1: {
            "region": "death_mountain",
            "xpos": 36,
            "ypos": 8,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        2: {
            "region": "gerudo",
            "xpos": 52,
            "ypos": 1,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        3: {
            "region": "gerudo",
            "xpos": 8,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        4: {
            "region": "necluda",
            "xpos": 22,
            "ypos": 1,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        5: {
            "region": "necluda",
            "xpos": 51,
            "ypos": 2,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        6: {
            "region": "necluda",
            "xpos": 23,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        }
    },
    "sanctuaries_opened": {
        0: {
            "region": "hyrule",
            "xpos": 44,
            "ypos": 6,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        1: {
            "region": "hyrule",
            "xpos": 31,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
         2: {
            "region": "death_mountain",
            "xpos": 6,
            "ypos": 3,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
             "open":0
        },
         3: {
            "region": "death_mountain",
            "xpos": 49,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
             "open":0
        },
         4: {
            "region": "gerudo",
            "xpos": 46,
            "ypos": 3,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
             "open":0
        },
        5: {
            "region": "necluda",
            "xpos": 51,
            "ypos": 6,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        6: {
            "region": "necluda",
            "xpos": 33,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        }

    }
}

def Get_Game(game_id):
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }
    conexion = mysql.connector.connect(**config)

    try:
        cursor = conexion.cursor(dictionary=True)

        # player
        query = f"SELECT * FROM game WHERE game_id = {game_id}"
        cursor.execute(query)
        player_data = cursor.fetchone()

        # food
        query = f"SELECT * FROM game_food WHERE game_id = {game_id}"
        cursor.execute(query)
        foods_data = cursor.fetchall()

        # weapons
        query = f"SELECT * FROM game_weapons WHERE game_id = {game_id}"
        cursor.execute(query)
        weapons_data = cursor.fetchall()

        # enemies
        query = f"SELECT * FROM game_enemies WHERE game_id = {game_id}"
        cursor.execute(query)
        enemies_data = cursor.fetchall()

        # chests
        query = f"SELECT * FROM game_chests_opened WHERE game_id = {game_id}"
        cursor.execute(query)
        chests_data = cursor.fetchall()

        # sanctuaries
        query = f"SELECT * FROM game_sanctuaries_opened WHERE game_id = {game_id}"
        cursor.execute(query)
        sanctuaries_data = cursor.fetchall()

        # DICCIONARIO RECUPÈRADO
        game = {
            "game_id": game_id,
            "player": player_data,
            "foods": {food["food_name"]: food for food in foods_data},
            "weapons": {weapon["weapon_name"]: weapon for weapon in weapons_data},
            "enemies": {enemy["num"]: enemy for enemy in enemies_data},
            "chests_opened": {chest["num"]: chest for chest in chests_data},
            "sanctuaries_opened": {sanctuary["num"]: sanctuary for sanctuary in sanctuaries_data}
        }

        return game

    finally:
        cursor.close()
        conexion.close()




#PASARLE LA ID DE LA PARTIDA SELECCIONADA EN EL MENU SAVED GAMES
game_id = 9
#game_recuperado = Get_Game(game_id)
#print(game_recuperado)
Get_Game(game_id)

# game_id = 3  # id a recuperar
# GetGame(game_id)
