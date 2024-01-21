
import mysql.connector
import datetime

from base_zelda import game as game

#--------- PARA CONTINUE (recuperar una partida)---------
# recupera datos de la partida que le pidas en game_id, y los sobreescribe encima del diccionario game local
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


#--------- PARA NUEVA PARTIDA---------
# crea la tabla game de un nuevo game_id (nueva partida)
#se le pasa el diccionario game para que establezca los valores default en bbdd
def createGame(game): #no necesita game_id porque se pone en autoincrement
    game["player"]["modified_at"] = datetime.datetime.now()
    created_at = game["player"]["created_at"].strftime('%Y-%m-%d %H:%M:%S')
    modified_at = game["player"]["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

    query = "INSERT INTO game"\
        "(user_name, hearts_remaining, blood_moon_countdown, blood_moon_appearances, region, created_at, modified_at,ganon_dead)"\
        "VALUES ('{}', {}, {}, {}, '{}', '{}', '{}',{});".format(
            game["player"]["user_name"], game["player"]["hearts_remaining"],
            game["player"]["blood_moon_countdown"], game["player"]["blood_moon_appearances"],
            game["player"]["region"], created_at, modified_at,game["player"]["ganon_dead"])

    insertar_datos(query)


# inserta la tabla de comidas con las comidas por defecto del jugador creado
def insertFoods(game):
    for food_name, food_data in game["foods"].items():
        food_data["modified_at"] = datetime.datetime.now()
        created_at = food_data["created_at"].strftime('%Y-%m-%d %H:%M:%S')
        modified_at = food_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO game_food"\
                "(game_id, food_name, quantity_remaining, created_at, modified_at)"\
                "VALUES ({}, '{}', {}, '{}', '{}')".format(game["game_id"], food_name,
                                                           food_data["quantity_remaining"],
                                                           created_at, modified_at)
        insertar_datos(query)


# inserta la tabla de arams con las armas por defecto del jugador creado
def insertWeapons(game):
    for weapon_name, weapon_data in game["weapons"].items():
        weapon_data["modified_at"] = datetime.datetime.now()
        created_at = weapon_data["created_at"].strftime('%Y-%m-%d %H:%M:%S')
        modified_at = weapon_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO game_weapons"\
                "(game_id, weapon_name, equiped, lives_remaining, created_at, modified_at, total_weapons)"\
                "VALUES ({}, '{}', {}, {}, '{}', '{}', {})".format(game["game_id"], weapon_name,
                                                                  weapon_data["equiped"],
                                                                  weapon_data["lives_remaining"],
                                                                  created_at, modified_at,
                                                                  weapon_data["total_weapons"])
        insertar_datos(query)


# inserta la tabla de enemigos con los enemigos por defecto del jugador creado (posicion y vida)
def insertEnemies(game):
    for enemy_id, enemy_data in game["enemies"].items():
        enemy_data["modified_at"] = datetime.datetime.now()
        created_at = enemy_data["created_at"].strftime('%Y-%m-%d %H:%M:%S')
        modified_at = enemy_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO game_enemies"\
                "(game_id, region, num, xpos, ypos, lifes_remaining, created_at, modified_at)"\
                "VALUES ({}, '{}', {}, {}, {}, {}, '{}', '{}')".format(game["game_id"],enemy_data["region"],
                                                                      enemy_id,
                                                                      enemy_data["xpos"],
                                                                      enemy_data["ypos"],
                                                                      enemy_data["lifes_remaining"],
                                                                      created_at, modified_at)
        insertar_datos(query)


# inserta la tabla de cofres con los cofres cerrados por defecto del jugador creado
def insertChestsOpened(game):
    for chest_id, chest_data in game["chests_opened"].items():
        chest_data["modified_at"] = datetime.datetime.now()
        created_at = chest_data["created_at"].strftime('%Y-%m-%d %H:%M:%S')
        modified_at = chest_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO game_chests_opened"\
                "(game_id, region, num, xpos, ypos, created_at, modified_at, open)"\
                "VALUES ({}, '{}', {}, {}, {}, '{}', '{}', {})".format(game["game_id"],
                                                                   chest_data["region"],
                                                                   chest_id,
                                                                   chest_data["xpos"],
                                                                   chest_data["ypos"],
                                                                   created_at, modified_at,
                                                                   chest_data["open"])
        insertar_datos(query)


# inserta la tabla de santuarios con los santuarios cerrados por defecto del jugador creado
def insertSanctuariesOpened(game):
    for sanctuary_id, sanctuary_data in game["sanctuaries_opened"].items():
        sanctuary_data["modified_at"] = datetime.datetime.now()
        created_at = sanctuary_data["created_at"].strftime('%Y-%m-%d %H:%M:%S')
        modified_at = sanctuary_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "INSERT INTO game_sanctuaries_opened"\
                "(game_id, region, num, xpos, ypos, created_at, modified_at, open)"\
                "VALUES ({}, '{}', {}, {}, {}, '{}', '{}', {})".format(game["game_id"],
                                                                  sanctuary_data["region"],
                                                                  sanctuary_id,
                                                                  sanctuary_data["xpos"],
                                                                  sanctuary_data["ypos"],
                                                                  created_at, modified_at,
                                                                  sanctuary_data["open"])
        insertar_datos(query)


# conecta python con la base de datos (contiene los parametros de configuracion para establecer la conexion con mysql)
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
    finally:
        cursor.close()
        conexion.close()


#CALCULADOR DEL GAME_ID CREADO (nueva partida)
def get_game_id():
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }

    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()

        cursor.execute("SELECT MAX(game_id) FROM game")
        t_players = cursor.fetchone()[0]

        new_game_id = t_players
        return new_game_id
    finally:

        cursor.close()
        conexion.close()


# ejectuta las funciones de cracion de todas las tablas, una vez obtenido el game_id
def insert_all():

    print("Loading...")
    insertFoods(game)
    #print("food insertado")
    insertWeapons(game)
    #print("weapons insertado")
    insertEnemies(game)
    #print("enemies insertado")
    insertChestsOpened(game)
    #print("chests insertado")
    insertSanctuariesOpened(game)
    #print("sanct insertado")

#-----ORDEN DE EJECUCION-----!!!!!!!!!!!!
# createGame(game)
# print("Game insertado")
# game_id = get_game_id()#recuperar id
# game['game_id']=game_id
# print(game_id)
#
# insert_all()





#--------- PARA GUARDAR PARTIDA (en la bbdd)---------
# actualiza los valores de la tabla game de la bbdd en funcion del diccionario de la partida en local (game)
def updateGame(game):
    game["player"]["modified_at"] = datetime.datetime.now()
    modified_at = game["player"]["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

    query = "UPDATE game SET"\
        " user_name = '{}',"\
        " hearts_remaining = {},"\
        " blood_moon_countdown = {},"\
        " blood_moon_appearances = {},"\
        " region = '{}',"\
        " modified_at = '{}'," \
        "ganon_dead = {} WHERE game_id = {};".format(
            game["player"]["user_name"], game["player"]["hearts_remaining"],
            game["player"]["blood_moon_countdown"], game["player"]["blood_moon_appearances"],
            game["player"]["region"], modified_at, game["player"]["ganon_dead"],game["game_id"]
        )

    insertar_datos(query)

# actualiza los valores de la tabla food de la bbdd en funcion del diccionario de la partida en local (game)
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

# actualiza los valores de la tabla weapons de la bbdd en funcion del diccionario de la partida en local (game)
def updateWeapons(game):
    for weapon_name, weapon_data in game["weapons"].items():
        weapon_data["modified_at"] = datetime.datetime.now()
        modified_at = weapon_data["modified_at"].strftime('%Y-%m-%d %H:%M:%S')

        query = "UPDATE game_weapons SET"\
                " equiped = {},"\
                " lives_remaining = {},"\
                " modified_at = '{}',"\
                " total_weapons = {} WHERE game_id = {} AND weapon_name = '{}';".format(
                    weapon_data["equiped"], weapon_data["lives_remaining"],
                    modified_at, weapon_data["total_weapons"],
                    game["game_id"], weapon_name
                )
        insertar_datos(query)

# actualiza los valores de la tabla enemies de la bbdd en funcion del diccionario de la partida en local (game)
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

# actualiza los valores de la tabla chests de la bbdd en funcion del diccionario de la partida en local (game)
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

# actualiza los valores de la tabla sanctuaries de la bbdd en funcion del diccionario de la partida en local (game)
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


# ejectuta las funciones de update de todas las tablas del jugador en la bbdd
def update_all():
    print("\nSaving game, please wait ...")
    updateGame(game)
    updateFoods(game)
    updateWeapons(game)
    updateEnemies(game)
    updateChestsOpened(game)
    updateSanctuariesOpened(game)





#--------- PARA DELETE (borrar partida de la bbdd)---------
# borra las tablas del juego del que pases la game_id
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


#--------- PARA PASAR A DATA LOS VALUES DE GAME ---------
def sobrescribir_data_con_game(data, game):
    ############## ENEMIES ###################
    for enemy_id, enemy_data in game['enemies'].items():#extraer valores a pasar
        region = enemy_data['region']
        xpos = enemy_data['xpos']
        ypos = enemy_data['ypos']
        hearts = enemy_data['lifes_remaining']

        try:
            data[region]['enemies'][enemy_id]['xpos'] = xpos # sobreescribe X
            data[region]['enemies'][enemy_id]['ypos'] = ypos # sobreescribe Y
            data[region]['enemies'][enemy_id]['hearts'] = hearts # sobreescribe hearts

        except KeyError: #ENEMIGO QUE DA ERROR
            print(f"Error: No se pudo encontrar el índice {enemy_id} en la región {region}.")

    ############## CHESTS ###################
    for chest_id, chest_data in game['chests_opened'].items():#extraer valores a pasar
        region = chest_data['region']
        open = chest_data['open']
        if open == 1:
            open = True
        else:
            open = False
        try:
            data[region]['chests'][chest_id]['open'] = open # OPEN

        except KeyError: #CHESTS QUE DA ERROR
            print(f"Error: No se pudo encontrar el índice {chest_id} en la región {region}.")

    ############## SANCTUARY ###################
    for sanctuary_id, sanctuaries_data in game['sanctuaries_opened'].items():#extraer valores a pasar
        region = sanctuaries_data['region']
        open = sanctuaries_data['open']
        if open == 1:
            open = True
        else:
            open = False
        try:
            data[region]['sanctuaries'][sanctuary_id]['open'] = open # OPEN

        except KeyError: #CHESTS QUE DA ERROR
            print(f"Error: No se pudo encontrar el índice {sanctuary_id} en la región {region}.")


#--------- PARA PASAR A GAME LOS VALUES DE DATA ---------
def sobrescribir_game_con_data(data,game):
    ############## ENEMIES ###################
    for region, region_data in data.items():
        if 'enemies' in region_data:
            for enemy_id, enemy_data in region_data['enemies'].items():
                try:
                    game['enemies'][enemy_id]['xpos'] = enemy_data['xpos']
                    game['enemies'][enemy_id]['ypos'] = enemy_data['ypos']
                    game['enemies'][enemy_id]['lifes_remaining'] = enemy_data['hearts']

                except KeyError: #ENEMIGO QUE DA ERROR
                    print(f"Error: No se pudo encontrar el índice {enemy_id} en la región {region}.")

    ############## CHESTS ###################
    for region, region_data in data.items():
        if 'chests' in region_data:
            for chest_id, chest_data in region_data['chests'].items():
                try:

                    if chest_data['open'] == False:
                        game['chests_opened'][chest_id]['open'] = 0
                    else:
                        game['chests_opened'][chest_id]['open'] = 1


                except KeyError: #CHEST QUE DA ERROR
                    print(f"Error: No se pudo encontrar el índice {chest_id} en la región {region}.")

    ############## SANCTUARY ###################
    for region, region_data in data.items():
        if 'sanctuaries' in region_data:
            for sanctuary_id, sanctuary_data in region_data['sanctuaries'].items():
                 try:

                    if sanctuary_data['open'] == False:
                        game['sanctuaries_opened'][sanctuary_id]['open'] = 0
                    else:
                        game['sanctuaries_opened'][sanctuary_id]['open'] = 1

                 except KeyError: #SANCTUARY QUE DA ERROR
                    print(f"Error: No se pudo encontrar el índice {sanctuary_id} en la región {region}.")





#----- RECUPERAR PARTIDAS: CONTINUE----

def partidas_guardadas():
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }

    query = """
    SELECT
        g.game_id,
        user_name,
        region,
        hearts_remaining,
        COALESCE(2 + s.total_sanctuaries, 2) AS total_hearts,
        modified_at
    FROM
        game g
    LEFT JOIN (
        SELECT
            game_id,
            COUNT(*) AS total_sanctuaries
        FROM
            game_sanctuaries_opened
        WHERE
            open = 1
        GROUP BY
            game_id
    ) s ON g.game_id = s.game_id
    ORDER BY
        g.modified_at DESC
    LIMIT 8;
    """

    conexion = mysql.connector.connect(**config)

    try:
        cursor = conexion.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        print("* Saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
              "*                                                                             *")

        for i, resultado in enumerate(resultados):
            game_id, user_name, region, hearts_remaining, total_hearts, modified_at = resultado
            print(
                f"*  {str(game_id).ljust(2)}: {modified_at} - {str(user_name + ', ' + region).ljust(23)}                     ♥{str(hearts_remaining).rjust(1)}/{str(total_hearts).rjust(1)} *")
        print(f"*                                                                             *")
        print("* Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * *")

        return resultados
    finally:
        cursor.close()
        conexion.close()



