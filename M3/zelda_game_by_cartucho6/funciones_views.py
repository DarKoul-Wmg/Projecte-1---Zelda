import mysql.connector

########################### 1 USUARIOS  ####################
def users_last_played():
    config = {
    'user': 'Cartucho6r',
    'password': 'Cartucho61234',
    'host': '20.199.46.206',
    'database': 'zelda',
    }
    connection = mysql.connector.connect(**config)

    try:
        cursor = connection.cursor()
        query = """
            SELECT user_name, modified_at as last_played
            FROM game;
        """

        cursor.execute(query)
        resultado = cursor.fetchall()
        for user, last_played in resultado:
            print(f"{str(user).ljust(12)}{str(last_played).ljust(20)}")

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

########################### 2 PARTIDAS  ####################
def played_by_user():
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }

    # Conectarse a la base de datos
    connection = mysql.connector.connect(**config)

    try:
        cursor = connection.cursor()

        # Consulta SQL para obtener la cantidad de partidas jugadas por usuario
        query = """
            SELECT user_name, COUNT(user_name) as games_played
            FROM game
            GROUP BY user_name;
        """

        cursor.execute(query)

        # Obtener los resultados de la consulta
        results = cursor.fetchall()

        for user, games_played in results:
            print(f"{str(user).ljust(12)}                {str(games_played).rjust(3)}")

    finally:
        cursor.close()
        connection.close()



########################### ARMAS USADAS ####################
def weapons_used():
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }

    connection = mysql.connector.connect(**config)

    try:
        cursor = connection.cursor()

        query = """
                SELECT
                g.user_name,
                w.weapon_name,
                SUM(1 + IFNULL(total_weapons, 0)) as usos,
                MAX(g.modified_at) as ultima_partida
                FROM game g
                JOIN game_weapons w ON g.game_id = w.game_id
                WHERE total_weapons > 0 or lives_remaining > 0
                GROUP BY g.user_name, w.weapon_name;
        """

        cursor.execute(query)

        results = cursor.fetchall()


        for user, arma, usos, ultima_partida in results:
            print(f"{str(user).ljust(12)}{str(arma).ljust(15)}{str(usos).rjust(14)}{str(ultima_partida).rjust(22)}")

    finally:

        cursor.close()
        connection.close()



########################### COMIDA USADA ####################
def food_consumed():
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }

    connection = mysql.connector.connect(**config)

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                g.user_name,
                f.food_name,
                MAX(f.quantity_remaining) as total_consumido,
                MAX(g.modified_at) as ultima_partida
            FROM game g
            JOIN game_food f ON g.game_id = f.game_id
            WHERE f.quantity_remaining > 0
            GROUP BY g.user_name, f.food_name;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        for user, food, veces_obtenido, ultima_partida in results:
            print(f"{str(user).ljust(12)} {str(food).ljust(14)}            {str(veces_obtenido).rjust(3)} {str(ultima_partida).rjust(26)}")

    finally:
        cursor.close()
        connection.close()


########################### BLOOD MOONS ####################
def blood_moon_stats():
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }
    connection = mysql.connector.connect(**config)

    try:
        cursor = connection.cursor()
        # media de blood moons
        avg_query = "SELECT ROUND(AVG(blood_moon_appearances), 2) FROM game;"
        cursor.execute(avg_query)
        avg_result = cursor.fetchone()[0] #ASEGURAMOS QUE SALGA UN VALOR
        print(f"Media de Blood Moons de las partidas jugadas: {avg_result}")

        # partida con mas blood moons (LIMIT 1 para evitar que 2 partidas tengan la misma cantidad)
        max_query = """
            SELECT g.user_name, g.blood_moon_appearances, g.modified_at
            FROM game g
            WHERE g.blood_moon_appearances = (
                SELECT MAX(blood_moon_appearances) FROM game)
            ORDER BY g.modified_at
            LIMIT 1;
        """
        cursor.execute(max_query)
        max_result = cursor.fetchone()
        if max_result:
            date, player, blood_moons = max_result
            print(f"Partida con más Blood Moons:\nFecha: {blood_moons} \nJugador: {date}\nCantidad de Blood Moons: {player}")
        else:
            print("No hay datos de Blood Moons.")

    finally:
        cursor.close()
        connection.close()



# ----- SABER SI HAY USERS -----
def lista_usuarios():
    config = {
        'user': 'Cartucho6r',
        'password': 'Cartucho61234',
        'host': '20.199.46.206',
        'database': 'zelda',
    }

    connection = mysql.connector.connect(**config)

    try:
        cursor = connection.cursor()

        query = """
            SELECT COUNT(game_id) as users
            FROM game;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        return len(result)

    finally:
        cursor.close()
        connection.close()