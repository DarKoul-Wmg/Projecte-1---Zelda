import mysql.connector
import datetime

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

        for i, resultado in enumerate(resultados):
            game_id, user_name, region, hearts_remaining, total_hearts, modified_at = resultado
            print(f"{game_id} - {modified_at} - {user_name}, {region}  {hearts_remaining}/{total_hearts} ")

        return resultados
    finally:
        cursor.close()
        conexion.close()

partidas_guardadas()
