import mysql.connector
import datetime
from armario_FUNCIONES import *
from armario_PRINTS import *
from diccionario_general import*

help_save_game = ("* Help, saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
                  "*                                                                             *\n"
                  "*                                                                             *\n"
                  "*       Type 'play X' to continue playing the game 'X'                        *\n"
                  "*       Type 'erase X' to erase the game 'X'                                  *\n"
                  "*       Type 'back' now to go back to the main menu                           *\n"
                  "*                                                                             *\n"
                  "*                                                                             *\n"
                  "*                                                                             *\n"
                  "*       Type 'back' now to go back to 'Saved games'                           *\n"
                  "*                                                                             *\n"
                  "* Back * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")





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
        print("* Saved games  * * ** * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
              "*                                                                             *")

        for i, resultado in enumerate(resultados):
            game_id, user_name, region, hearts_remaining, total_hearts, modified_at = resultado
            print(f"*  {str(game_id).ljust(2)}: {modified_at} - {str(user_name+', '+region).ljust(23)}                     ♥{str(hearts_remaining).rjust(1)}/{str(total_hearts).rjust(1)} *")
        print(    f"*                                                                             *")
        print ("* Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * *" )

        return resultados
    finally:
        cursor.close()
        conexion.close()




flg_help_save_game = False
flg_save_game = True
while flg_save_game:
    clear_screen()
    partidas_guardadas()
    prompt(promptlist)
    opc = input()

    promptlist.append(opc)

    if not opc.replace(" ", "").isalnum():
        # print('Invalid action')

        promptlist.append('Invalid action')
    elif opc.lower() == 'help':

        clear_screen()
        flg_save_game = False
        flg_help_save_game = True
    elif opc[:6].lower() == 'erase ':
        ##borrar
        promptlist.append(opc)
        id_str = opc[6:]
        if not id_str.isdigit():
            promptlist.append('Invalid action')
        else:
            id = int(id_str)
            game_id_value = game["game_id"]
            if id != game_id_value:
                promptlist.append('Invalid action')
                print('BORRAR LA PARTIDA')
            else:
                print('BORRAR LA PARTIDA')
    elif opc[:6].lower() == 'play ':
        ##cargar partida
        promptlist.append(opc)
        id_str = opc[5:]
        if not id_str.isdigit():
            promptlist.append('Invalid action0')
        else:
            id = int(id_str)
            game_id_value = game["game_id"]
            if id != game_id_value:
                promptlist.append('Invalid action2')

            else:
                print('CARGAR PARTIDA')
                ################################################################
                ##FLG PARA JUEGO


    #else:
        #promptlist.append('Invalid action')
    ##help save game
    while flg_help_save_game:
        print(help_save_game)
        prompt(promptlist)

        pregunta = input()  # en blanco pendiente
        promptlist.append(pregunta)

        if not pregunta.replace(" ", "").isalpha():
            # print('Invalid action')
            promptlist.append('Invalid action')
        elif pregunta.lower() == 'back':
            clear_screen()
            flg_help_save_game = False
            flg_save_game = True
        else:
            promptlist.append('Invalid action')






