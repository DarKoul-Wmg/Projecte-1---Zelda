import datetime
import mysql.connector
game = { #JUGADOR
    "game_id": 9,
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
def updateGame(game):
    game["player"]["modified_at"] = datetime.datetime.now()
    modified_at = game["player"]["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

    query = "UPDATE game SET"\
        " user_name = '{}',"\
        " hearts_remaining = {},"\
        " blood_moon_countdown = {},"\
        " blood_moon_appearances = {},"\
        " region = '{}',"\
        " modified_at = '{}' WHERE game_id = {};".format(
            game["player"]["user_name"], game["player"]["health"],
            game["player"]["bm_countdown"], game["player"]["total_blood_moon"],
            game["player"]["region"], modified_at, game["game_id"]
        )

    insertar_datos(query)

def updateFoods(game):
    for food_name, food_data in game["foods"].items():
        food_data["modified_at"] = datetime.datetime.now()
        modified_at = food_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "UPDATE game_food SET"\
                " quantity_remaining = {},"\
                " modified_at = '{}' WHERE game_id = {} AND food_name = '{}';".format(
                    food_data["quantity_remaining"], modified_at, game["game_id"], food_name
                )
        insertar_datos(query)

def updateWeapons(game):
    for weapon_name, weapon_data in game["weapons"].items():
        weapon_data["modified_at"] = datetime.datetime.now()
        modified_at = weapon_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "UPDATE game_weapons SET"\
                " equiped = {},"\
                " lives_remaining = {},"\
                " modified_at = '{}',"\
                " total_weapons = {} WHERE game_id = {} AND weapon_name = '{}';".format(
                    weapon_data["equipped"], weapon_data["lives_remaining"],
                    modified_at, weapon_data["total_weapons"],
                    game["game_id"], weapon_name
                )
        insertar_datos(query)

def updateEnemies(game):
    for enemy_id, enemy_data in game["enemies"].items():
        enemy_data["modified_at"] = datetime.datetime.now()
        modified_at = enemy_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "UPDATE game_enemies SET"\
                " region = '{}',"\
                " xpos = {},"\
                " ypos = {},"\
                " lifes_remaining = {},"\
                " modified_at = '{}' WHERE game_id = {} AND num = {};".format(
                    enemy_data["region"], enemy_data["xpos"],
                    enemy_data["ypos"], enemy_data["lifes_remaining"],
                    modified_at, game["game_id"], enemy_id
                )
        insertar_datos(query)

def updateChestsOpened(game):
    for chest_id, chest_data in game["chests_opened"].items():
        chest_data["modified_at"] = datetime.datetime.now()
        modified_at = chest_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "UPDATE game_chests_opened SET"\
                " region = '{}',"\
                " xpos = {},"\
                " ypos = {},"\
                " modified_at = '{}',"\
                " open = {} WHERE game_id = {} AND num = {};".format(
                    chest_data["region"], chest_data["xpos"],
                    chest_data["ypos"], modified_at,
                    chest_data["open"], game["game_id"], chest_id
                )
        insertar_datos(query)

def updateSanctuariesOpened(game):
    for sanctuary_id, sanctuary_data in game["sanctuaries_opened"].items():
        sanctuary_data["modified_at"] = datetime.datetime.now()
        modified_at = sanctuary_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "UPDATE game_sanctuaries_opened SET"\
                " region = '{}',"\
                " xpos = {},"\
                " ypos = {},"\
                " modified_at = '{}',"\
                " open = {} WHERE game_id = {} AND num = {};".format(
                    sanctuary_data["region"], sanctuary_data["xpos"],
                    sanctuary_data["ypos"],modified_at,
                    sanctuary_data["open"], game["game_id"], sanctuary_id
                )
        insertar_datos(query)

def insertar_datos(insertar):
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }
    conexion = mysql.connector.connect(**config)
    try:
        cursor = conexion.cursor()
        cursor.execute(insertar)
        conexion.commit()
        return True
    finally:
        cursor.close()
        conexion.close()
        
#GUARDADO TOTAL
def update_all():
    updateGame(game)
    #print("Game actualizado")
    updateFoods(game)
    #print("Foods actualizado")
    updateWeapons(game)
    #print("Weapons actualizado")
    updateEnemies(game)
    #print("Enemies actualizado")
    updateChestsOpened(game)
    #print("Chests actualizado")
    updateSanctuariesOpened(game)
    #print("Sanctuaries actualizado")

update_all()

