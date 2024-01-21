import base_zelda
import funciones1
from funciones1 import *
from funciones_flujo_de_datos import *
from funciones_inventarios import *
from funciones_drops import *
from funciones_eat_cook import *
from armario_PRINTS import *
from armario_FUNCIONES import *
from funciones_views import *

nombre = ''
promptlist = []

salir = False

flg_help = False
flg_inicio = True
flg_n_game = False
flg_about = False
flg_h_n_game = False
flg_legend = False
flg_plot = False
flg_juego = False
flg_queries =False
flg_save_game = False
flg_help_save_game = False
menu_help_inventory = False

listamenu = [menu1, menu2, menu3]
listamenu2 = [menu11, menu22, menu33]
cabecera = random.randrange(len(listamenu))
cabecera2 = random.randrange(len(listamenu2))
lista_usuarios = lista_usuarios()
menu_queries = ("===================Consulta"
                "s BD===================\n1)Usuarios que han jugado\n2)Cantidad de partidas jugadas por usuario"
                "\n3)Armas usadas por usuario y datos por partida\n4)Comida consumida por usuario y datos por partida\n5)Estadistica de 'blood Moon'\n6)Back"
                "\n==================================================")


while salir != True:
    # si hay partidas, continue visible
    if lista_usuarios>0:
        # ----FLG INICIO
        while flg_inicio:
            clear_screen()

            print(listamenu[cabecera])
            prompt(promptlist)
            opc = input("What to do now? ")
            promptlist.append(opc)

            if not opc.replace(" ", "").isalpha():
                promptlist.append('Invalid action')

            # ---CONTINUE
            elif opc.lower() == "continue":
                clear_screen()
                flg_inicio = False
                flg_save_game = True

            # ---SALIR
            elif opc.lower() == 'exit':
                clear_screen()
                flg_inicio = False
                salir = True

            # ---HELP
            elif opc.lower() == 'help':
                clear_screen()
                flg_inicio = False
                flg_help = True

            # ---ABOUT
            elif opc.lower() == 'about':
                clear_screen()
                flg_inicio = False
                flg_about = True

            # ---NEW GAME
            elif opc.lower() == ('new game'):
                clear_screen()
                flg_inicio = False
                flg_n_game = True

            # ---QUERIES:
            elif opc.lower() == ('queries'):
                clear_screen()
                flg_inicio = False
                flg_queries = True

            # ---INVALID ACTION
            else:
                promptlist.append('Invalid action')

    # si no hay partidas
    elif lista_usuarios<1:

        # ----FLG INICIO
        while flg_inicio:
            print(listamenu2[cabecera2])
            prompt(promptlist)
            opc = input("What to do now? ")
            promptlist.append(opc)

            if not opc.replace(" ", "").isalpha():
                promptlist.append('Invalid action')

            # ---EXIT
            elif opc.lower() == 'exit':
                clear_screen()
                flg_inicio = False
                salir = True

            # ---HELP
            elif opc.lower() == 'help':
                clear_screen()
                flg_inicio = False
                flg_help = True

            # ---ABOUT
            elif opc.lower() == 'about':
                clear_screen()
                flg_inicio = False
                flg_about = True

            # ---NEW GAME
            elif opc.lower() == ('new game'):
                clear_screen()
                flg_inicio = False
                flg_n_game = True

            # ---INVALID ACTION
            else:
                promptlist.append('Invalid action')

    # ---- FLG HELP ----
    while flg_help:
        print(main_menu)
        prompt(promptlist)

        opcion1 = input("What to do now? ")
        promptlist.append(opcion1)
        if not opcion1.replace(" ", "").isalpha():
            promptlist.append('Invalid action')

        elif opcion1.lower() == 'back':
            clear_screen()
            flg_help = False
            flg_inicio = True

        else:
            promptlist.append('Invalid action')

    # ---- FLG QUERIES ----
    while flg_queries:
        print(menu_queries)
        opc = input("Opc: ")
        print()
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 7):
            print("wrong option")
        elif int(opc) == 1:
            print("Usuario".ljust(12), "Ultima partida".rjust(18))
            print(31 * '-')
            users_last_played()
            print()
            input("Enter to continue")
            print()
        elif int(opc) == 2:
            print("Usuario".ljust(12), "Partidas jugadas".rjust(18))
            print(31 * '-')
            played_by_user()
            print()
            input("Enter to continue")
            print()
        elif int(opc) == 3:
            print("Usuario".ljust(12), "Arma".ljust(15), "Veces obtenida".ljust(14), "Última Fecha de Uso".rjust(22))
            print(64 * '-')
            weapons_used()
            print()
            input("Enter to continue")
            print()
        elif int(opc) == 4:
            print("Usuario".ljust(12), "Comida".ljust(14), "Veces obtenida".ljust(3),
                  "Última Fecha de consumo".rjust(26))
            print(69 * '-')
            print()
            food_consumed()
            print()
            input("Enter to continue")
            print()
        elif int(opc) == 5:
            print("Blood Moons".center(50))
            print(50 * '-')

            blood_moon_stats()
            print()
            input("Enter to continue")
            print()

        elif int(opc) == 6:
            flg_queries=False
            flg_inicio=True

    # ---- FLG ABOUT ----
    while flg_about:
        print(menu_about)
        prompt(promptlist)

        opcion2 = input("What to do now? ")
        promptlist.append(opcion2)
        if not opcion2.replace(" ", "").isalpha():
            promptlist.append('Invalid action')

        elif opcion2.lower() == 'back':
            clear_screen()
            flg_about = False
            flg_inicio = True

        else:
            promptlist.append('Invalid action')

    # ---- FLG NEW GAME ----
    while flg_n_game:
        print(new_game)
        prompt(promptlist)

        nombre = input("What\'s your name (Link)? ")
        promptlist.append(nombre)
        if not nombre.isalnum() and nombre.replace(" ", ""):
            frase = nombre + " is not a valid name1"
            promptlist.append(frase)

        elif len(nombre) == 1 and len(nombre) < 3:
            # print(nombre, "is not a valid name")
            frase0 = nombre + " is not a valid name"
            promptlist.append(frase0)
        elif len(nombre) > 10:
            # print(nombre, "is not a valid name")
            frase2 = nombre + " is not a valid name"
            promptlist.append(frase2)
        elif len(nombre) == 0:  ##no funciona lo de link
            nombre = 'Link'
            frase3 = 'Welcome to the game, ' + nombre
            promptlist.append(frase3)
            # game['game_id'] = 0
            # game['player']['user_name'] = nombre
            # print(game)  ##PRUEBA
            clear_screen()
            # NEW GAME:
            createGame(game)  # crea el juego
            print("Game insertado")
            game_id = get_game_id()  # recuperar id
            game['game_id'] = game_id
            game['player']["user_name"] = nombre
            updateGame(game)

            print(game_id)
            insert_all()  # inserta los default de todas las tablas

            flg_n_game = False
            flg_legend = True

        elif nombre.lower() == 'back':
            clear_screen()
            flg_n_game = False
            flg_inicio = True
        elif nombre.lower() == 'help':
            clear_screen()
            flg_n_game = False
            flg_h_n_game = True

        else:
            frase4 = 'Welcome to the game, ' + nombre
            promptlist.append(frase4)
            # game['game_id'] = 0
            # game['player']['user_name'] = nombre
            # print(game)  ##PRUEBA
            clear_screen()

            # ----------NEW GAME:
            game['player']["user_name"] = nombre
            createGame(game)  # crea el juego
            print("Game insertado")
            game_id = get_game_id()  # recuperar id
            game['game_id'] = game_id

            print(game_id)
            insert_all()  # inserta los default de todas las tablas
            updateGame(game)

            flg_n_game = False
            flg_legend = True

    # ---- HELP NEW GAME ----
    while flg_h_n_game:
        print(help_new_game)
        prompt(promptlist)
        opcion4 = input("What to do now? ")
        promptlist.append(opcion4)
        if not opcion4.replace(" ", "").isalpha():
            promptlist.append('Invalid action')
        elif opcion4.lower() == 'back':
            clear_screen()
            flg_h_n_game = False
            flg_n_game = True
        else:
            promptlist.append('Invalid action')

    # ---- LEGEND ----
    while flg_legend:
        print(menu_legend)
        prompt(promptlist)
        opcion5 = input("What to do now? ")
        promptlist.append(opcion5)
        if not opcion5.replace(" ", "").isalpha():
            promptlist.append('Invalid action')
        elif opcion5.lower() == 'continue':
            clear_screen()
            flg_legend = False
            flg_plot = True
        else:
            promptlist.append('Invalid action')

    # ---- PLOT ----
    while flg_plot:
        longi_nombre = len(nombre)
        total_esp = 28
        e = total_esp - longi_nombre
        print("* Plot * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
              "*                                                                            *\n"
              "*                                                                            *\n"
              "*  Now history is repeating itself, and Princess Zelda has been captured by  *\n"
              "*  Ganon. He has taken over the Guardians and filled Hyrule with monsters.   *\n"
              "*                                                                            *\n"
              "*                                                                            *\n"
              f"*  But a young man named '{nombre}' has just awakened and".rjust(78),
              '*'.rjust(e))  ######se espacia la *
        print("*  must reclaim the Guardians to defeat Ganon and save Hyrule.               *\n"
              "*                                                                            *\n"
              "*                                                                            *\n"
              "* Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

        prompt(promptlist)
        opcion5 = input("What to do now? ")
        if not opcion5.replace(" ", "").isalpha():
            promptlist.append('Invalid action')

        elif opcion5.lower() == 'continue':
            promptlist.append('The adventure begins')
            clear_screen()
            flg_plot = False
            flg_juego = True
        else:
            promptlist.append('Invalid action')

    # ---- FLG CONTINUE ----
    while flg_save_game:
        clear_screen()
        lista_partidas = partidas_guardadas()
        lista_ids = []
        for partida in lista_partidas:
            lista_ids.append(partida[0])
        prompt(promptlist)
        opc = input("What to do now? ")
        promptlist.append(opc)

        if not opc.replace(" ", "").isalnum():
            promptlist.append('Invalid action')
        # ---BACK
        elif opc.lower() == 'back':
            flg_save_game = False
            flg_inicio = True

        # ---HELP
        elif opc.lower() == 'help':
            clear_screen()
            flg_save_game = False
            flg_help_save_game = True

        # ---ERASE
        elif opc[:6].lower() == 'erase ':
            promptlist.append(opc)
            id = opc[6:]
            if not id.isdigit():
                promptlist.append('Invalid action')
            else:
                game_id = int(id)
                if not game_id in lista_ids:
                    promptlist.append('Invalid action')
                else:
                    # borrar partida
                    DeleteGame(game_id)

        # --- PLAY CONTINUE
        elif opc[:5].lower() == 'play ':
            promptlist.append(opc)
            id = opc[5:]
            promptlist.append(id)
            if not id.isdigit():
                promptlist.append('Invalid action')
            else:
                game_id = int(id)
                if not game_id in lista_ids:
                    promptlist.append('Invalid action')
                else:
                    # cargar partida
                    game = Get_Game(game_id)
                    flg_juego = True
                    flg_save_game = False
                    break

    # ---- FLG HELP CONTINUE ----
    while flg_help_save_game:
        print(help_save_game)
        prompt(promptlist)
        opcion4 = input("What to do now? ")
        promptlist.append(opcion4)
        if not opcion4.replace(" ", "").isalpha():
            promptlist.append('Invalid action')
        elif opcion4.lower() == 'back':
            clear_screen()
            flg_help_save_game = False
            flg_save_game = True
        else:
            promptlist.append('Invalid action')



    # --------------------------------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------------------------------

    # ---- PARTIDA ----
    while flg_juego:

        flg_map = False
        flg_link_death = False
        flg_zelda_saved = False

        # ----COPIA DE DICCIONARIOS ORIGINALES PARA PLAYER----
        locations = copiar_diccionario_anidado(base_zelda.locations_og)
        data = copiar_diccionario_anidado(base_zelda.data_og)
        # ---------------------------------------!
        sobrescribir_data_con_game(data, game)

        # Variables propias de la partida (el resto vienen importadas de game)
        max_hearts_remaining = calcular_max_hearts_remaining(game)
        promptlist = []
        ganon_hearts = 0
        inv_actual = "main"
        inv_print = generate_inv_main(game, max_hearts_remaining)

        # ----- PRINTS PARA RESTAURAR LOCATION según data del player -----
        # -- Busca donde esta el "!" para posicionar ahi al player
        playerY, playerX = funciones1.buscar_exclamacion(locations, game)
        # pone al player en la location "!"
        locations[game['player']['region']][playerY][playerX] = "X"

        # FOX rate visible?
        promptlist.append(fox_spawn(game, data))
        flg_game = True

        while flg_game == True:
            clear_screen()
            max_hearts_remaining = calcular_max_hearts_remaining(game)
            if game['player']['hearts_remaining'] == 0:
                flg_link_death = True
            if game['player']['blood_moon_countdown'] == 0:
                revivir_enemigos(game, data)
                promptlist.append(f"The Blood Moon rises once again. Please be careful, {game['player']['user_name']}.")
                # si el countdown llega a 0, se añade una aparición al contador de appearances
                game['player']['blood_moon_appearances'] += 1
                # ............restaurar vida de todos los enemigos y poner en original pos
                # se restaura el contador a 25
                game['player']['blood_moon_countdown'] = 25

            # ---- LISTA INTERACCIONES REINICIO:
            attack_weapon = False  # ............CAMBIAR SEGUN SI LLEVA ARMA
            attack_entity = False  # si hay un enemigo, zorro
            attack_tree = False  # si hay un arbol
            cook = False
            fish = False
            open = False

            # ---- ACTUALIZACION INVENTARIO:
            if inv_actual == "main":
                inv_print = generate_inv_main(game, max_hearts_remaining)
            if inv_actual == "food":
                inv_print = generate_inv_food(game)
            if inv_actual == "weapons":
                inv_print = generate_inv_weapons(game)

            # ---- ACTUALIZACION DE LOCATIONS:
            # pone a los enemigos su vida actual
            funciones1.cambiador_enemigos(locations, game, data)
            # quita el "?" de los santuarios ya abiertos
            sanctuaries_opened_location(locations, game, data)
            # cambia los chests abiertos de M a W
            funciones1.cambiador_chests(locations, game, data)
            # pone el fox en el mapa si es visible
            funciones1.cambiador_fox(locations, game, data)
            # pone los respawns de los arboles, los actualiza, y le pone vida a los que han terminado su respawn
            arboles_respawn(locations, game, data)

            # ---- DETECCION INTERACCIONES PARA SABER ACCIONES DISPONIBLES PARA EL PLAYER
            if game['weapons']['Sword']['equiped']==True or game['weapons']['Wood Sword']['equiped'] == True:
                attack_weapon=True
            if attack_weapon == True and (locations[game['player']['region']][playerY][playerX - 1] in ("E", "F") or
                                          locations[game['player']['region']][playerY - 1][playerX] in ("E", "F") or
                                          locations[game['player']['region']][playerY][playerX + 1] in ("E", "F") or
                                          locations[game['player']['region']][playerY + 1][playerX] in ("E", "F")):
                attack_entity = True

            if (locations[game['player']['region']][playerY][playerX - 1] == "T" or
                    locations[game['player']['region']][playerY - 1][playerX] == "T" or
                    locations[game['player']['region']][playerY][playerX + 1] == "T" or
                    locations[game['player']['region']][playerY + 1][playerX] == "T"):
                attack_tree = True

            if (locations[game['player']['region']][playerY][playerX - 1] == "C" or
                    locations[game['player']['region']][playerY - 1][playerX] == "C" or
                    locations[game['player']['region']][playerY][playerX + 1] == "C" or
                    locations[game['player']['region']][playerY + 1][playerX] == "C"):
                cook = True

            if (locations[game['player']['region']][playerY][playerX - 1] == "~" or
                    locations[game['player']['region']][playerY - 1][playerX] == "~" or
                    locations[game['player']['region']][playerY][playerX + 1] == "~" or
                    locations[game['player']['region']][playerY + 1][playerX] == "~"):
                fish = True

            if (locations[game['player']['region']][playerY][playerX - 1] in ("S", "M") or
                    locations[game['player']['region']][playerY - 1][playerX] in ("S", "M") or
                    locations[game['player']['region']][playerY][playerX + 1] in ("S", "M") or
                    locations[game['player']['region']][playerY + 1][playerX] in ("S", "M")):
                open = True


            # ---- PRINTS MAPA ----
            # con todo lo que se ha cambiado en el mapa en actualizacion de locations, inventario se imprime pantalla
            # Prints mapa (.............falta sumar inventario)
            for y in range(len(locations[game['player']['region']]) - 1):
                for x in range(len(locations[game['player']['region']][0])):
                    print((locations[game['player']['region']][y][x]), end="")
                print(inv_print[y], end="")
                print()

            # Print línea de acciones
            print(actions(cook, fish, open,attack_weapon,attack_tree,attack_entity))

            prompt(promptlist)

            # ----------------------------------------------------
            # ------------- INICIO INTERACCION -------------------
            pregunta = input("What to do now?")
            pregunta = pregunta.lower()
            promptlist.append(pregunta)
            # ----------------------------------------------------
            # ----------------------------------------------------

            # ---- SHOW MAP ----
            if pregunta == "show map":
                flg_map = True

                while flg_map == True:
                    clear_screen()
                    sanctuaries_opened_map(locations, data)
                    for y in range(len(locations["map"]) - 1):
                        for x in range(len(locations["map"][0])):
                            print((locations["map"][y][x]), end="")
                        print(inv_print[y], end="")
                        print()
                    print("* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
                    prompt(promptlist)
                    pregunta = input("What to do now?")
                    promptlist.append(pregunta)
                    if pregunta.lower() == "back":
                        flg_map = False

                    else:
                        promptlist.append("Invalid action!")


            # ---- INVENTORY HELP
            if pregunta == "show inventory help":
                menu_help_inventory=True
                while menu_help_inventory:
                    clear_screen()
                    print(menu_help_inv)
                    pregunta = input("What to do now?")
                    promptlist.append(pregunta)
                    if pregunta.lower() == "back":
                        menu_help_inventory = False

                    else:
                        promptlist.append("Invalid action!")


            # ---- CAMBIO DE LOCATION ----
            elif pregunta[0:5] == 'go to':
                # --- Go to HYRULE
                if pregunta.replace('go to ', "") == 'hyrule' and game['player']['region'] in (
                'death_mountain', 'castle', 'gerudo'):
                    # donde antes estaba la X lo deja en blanco
                    locations[game['player']['region']][playerY][playerX] = " "
                    # cambia la game['player']['region']
                    game['player']['region'] = 'hyrule'
                    sobrescribir_game_con_data(data, game)
                    update_all()

                    # en la nueva location se busca el "!" y se pone al player en ese lugar
                    locations = copiar_diccionario_anidado(base_zelda.locations_og)
                    print(locations)
                    playerY, playerX = funciones1.buscar_exclamacion(locations, game)
                    locations[game['player']['region']][playerY][playerX] = "X"

                    promptlist.append("You are now in Hyrule.")
                    # se calcula el rate de spawn del fox
                    promptlist.append(fox_spawn(game, data))

                # --- Go to DEATH MOUNTAIN
                elif pregunta.replace('go to ', "") == 'death mountain' and game['player']['region'] in (
                'hyrule', 'castle', 'necluda'):
                    locations[game['player']['region']][playerY][playerX] = " "
                    game['player']['region'] = 'death_mountain'
                    sobrescribir_game_con_data(data, game)
                    update_all()
                    locations = copiar_diccionario_anidado(base_zelda.locations_og)
                    playerY, playerX = funciones1.buscar_exclamacion(locations, game)
                    locations[game['player']['region']][playerY][playerX] = "X"

                    promptlist.append("You are now in Death Mountain.")
                    promptlist.append(fox_spawn(game, data))

                # --- Go to GERUDO
                elif pregunta.replace('go to ', "") == 'gerudo' and game['player']['region'] in (
                'hyrule', 'castle', 'necluda'):
                    locations[game['player']['region']][playerY][playerX] = " "
                    game['player']['region'] = 'gerudo'
                    sobrescribir_game_con_data(data, game)
                    update_all()
                    locations = copiar_diccionario_anidado(base_zelda.locations_og)
                    playerY, playerX = funciones1.buscar_exclamacion(locations, game)
                    locations[game['player']['region']][playerY][playerX] = "X"

                    promptlist.append("You are now in Gerudo.")
                    promptlist.append(fox_spawn(game, data))

                # --- Go to NECLUDA
                elif pregunta.replace('go to ', "") == 'necluda' and game['player']['region'] in (
                'death_mountain', 'castle', 'gerudo'):
                    locations[game['player']['region']][playerY][playerX] = " "
                    game['player']['region'] = 'necluda'
                    sobrescribir_game_con_data(data, game)
                    update_all()
                    locations = copiar_diccionario_anidado(base_zelda.locations_og)
                    playerY, playerX = funciones1.buscar_exclamacion(locations, game)
                    locations[game['player']['region']][playerY][playerX] = "X"

                    promptlist.append("You are now in Necluda.")
                    promptlist.append(fox_spawn(game, data))

                # --- Go to CASTLE
                elif pregunta.replace('go to ', "") == 'castle':
                    locations[game['player']['region']][playerY][playerX] = " "
                    game['player']['region'] = 'castle'
                    locations = copiar_diccionario_anidado(base_zelda.locations_og)
                    playerY, playerX = funciones1.buscar_exclamacion(locations, game)
                    locations[game['player']['region']][playerY][playerX] = "X"
                    flg_castle = True
                    if game['player']['ganon_dead'] == False:
                        ganon_hearts = 8
                        ganon_hearts_start(ganon_hearts, locations, game)

                    # ----------------------------------
                    # ---------- BUCLE CASTLE ----------
                    # ----------------------------------
                    while flg_castle:
                        clear_screen()
                        max_hearts_remaining = calcular_max_hearts_remaining(game)
                        if game['player']['hearts_remaining'] == 0:
                            flg_link_death = True
                            break

                        # actualizar corazones
                        ganon_hearts_change(ganon_hearts, locations, game)

                        # ----REINICIA ACTIONS
                        attack_ganon = False
                        attack_weapon = False  # ............CAMBIAR SEGUN SI LLEVA ARMA
                        attack_tree = False

                        # ---- ACTIONS:
                        if game['weapons']['Sword']['equiped'] == True or game['weapons']['Wood Sword'][
                            'equiped'] == True:
                            attack_weapon = True
                        if locations[game['player']['region']][playerY][playerX - 1] == "T":
                            attack_tree = True
                        if locations[game['player']['region']][playerY][playerX + 1] == "\\" and attack_weapon == True:
                            attack_ganon = True

                        # ---- ACTUALIZACION INVENTARIO:
                        if inv_actual == "main":
                            inv_print = generate_inv_main(game, max_hearts_remaining)
                        if inv_actual == "food":
                            inv_print = generate_inv_food(game)
                        if inv_actual == "weapons":
                            inv_print = generate_inv_weapons(game)

                        # ----PRINTEO----
                        for y in range(len(locations[game['player']['region']]) - 1):
                            for x in range(len(locations[game['player']['region']][0])):
                                print((locations[game['player']['region']][y][x]), end="")
                            print(inv_print[y], end="")
                            print()
                        print(actions_castle(attack_ganon, attack_tree))
                        prompt(promptlist)

                        # ------------- INICIO INTERACCION -------------------
                        pregunta = input("What to do now?")
                        pregunta = pregunta.lower()
                        promptlist.append(pregunta)
                        # ----------------------------------------------------
                        if pregunta.lower() == "back":
                            game['player']['region'] = 'hyrule'
                            locations = copiar_diccionario_anidado(base_zelda.locations_og)
                            playerY, playerX = funciones1.buscar_exclamacion(locations, game)
                            locations[game['player']['region']][playerY][playerX] = "X"
                            flg_castle = False

                        # ---- SHOW INVENTORY
                        elif pregunta[:14] == "show inventory":
                            if pregunta[15:] == "main":
                                inv_actual = "main"
                            elif pregunta[15:] == "food":
                                inv_actual = "food"
                            elif pregunta[15:] == "weapons":
                                inv_actual = "weapons"

                        # ---- EQUIP AND UNEQUIP
                        elif pregunta[:10] == "equip the " or pregunta[:12] == "unequip the ":
                            cambio_weapon(pregunta, game, promptlist)


                        # --- EAT
                        elif pregunta[:3] == "eat":
                            comer(pregunta, game, promptlist, max_hearts_remaining)

                        # ---- ATTACK tree a puños
                        elif pregunta == "attack" and attack_weapon == False and attack_tree == True:
                            # se calcula el drop del arbol
                            promptlist.append(attack_tree_weaponless(data, game))

                        # ---- ATTACK tree a espada
                        elif pregunta == "attack" and attack_weapon == True and attack_tree == True:
                            data[game['player']['region']]["trees"]['tree1']["hearts"] -= 1
                            # si dejamos el arbol a 0 de vida, entonces se pone una cuenta atrás de 9 para respawn
                            if data[game['player']['region']]["trees"]['tree1']["hearts"] == 0:
                                data[game['player']['region']]["trees"]['tree1']["respawn"] = 10
                            promptlist.append(attack_tree_weapon(data, game))
                            if game['weapons']['Sword']['equiped'] == True:
                                game['weapons']['Sword']['lives_remaining'] -= 1
                            elif game['weapons']['Wood Sword']['equiped'] == True:
                                game['weapons']['Wood Sword']['lives_remaining'] -= 1

                        # ---- ATTACK a Ganon
                        elif pregunta == "attack" and attack_ganon == True:
                            ganon_hearts -= 1
                            if game['weapons']['Sword']['equiped'] == True:
                                game['weapons']['Sword']['lives_remaining'] -= 1
                            elif game['weapons']['Wood Sword']['equiped'] == True:
                                game['weapons']['Wood Sword']['lives_remaining'] -= 1
                            promptlist.append(ganon_frases_random())
                            if ganon_hearts > 0:
                                game['player']['hearts_remaining'] -= 1
                                if game['weapons']['Shield']['equiped'] == True:
                                    game['weapons']['Shield']['lives_remaining'] -= 1
                                elif game['weapons']['Wood Shield']['equiped'] == True:
                                    game['weapons']['Wood Shield']['lives_remaining'] -= 1
                            if ganon_hearts == 0:
                                ganon_hearts_change(ganon_hearts, locations, game)
                                for y in range(len(locations[game['player']['region']])):
                                    for x in range(len(locations[game['player']['region']][0])):
                                        print((locations[game['player']['region']][y][x]), end="")
                                    print()
                                promptlist.append(
                                    "It has been an exhausting fight, but with persistence, you have achieved it.")
                                promptlist.append("You saved Zelda, you won the game.")
                                # poner corazones de link al maximo
                                ganon_dead = True
                                flg_zelda_saved = True



                        # --- CHEATING:
                        # game over:
                        elif pregunta == "cheating: cheat game over":
                            game['player']['hearts_remaining'] = 0
                            flg_link_death = True

                        # win game:
                        elif pregunta == "cheating: cheat win game":
                            ganon_hearts=0
                            game['player']['ganon_dead'] = True
                            flg_zelda_saved = True


                        elif pregunta[:9] == "cheating:":
                            cheating(pregunta, game, promptlist, data, max_hearts_remaining)



                        # ---- MOVIMIENTO
                        elif pregunta[:-2] in ('go right ', 'go left ', 'go right', 'go left'):
                            cantidad = int(pregunta[-2:])
                            locations[game['player']['region']][playerY][playerX] = " "

                            # ---- DERECHA
                            if ("go right") in pregunta:
                                for i in range(cantidad):
                                    playerX += 1
                                    if locations[game['player']['region']][playerY][playerX] != " ":
                                        playerX -= 1
                                        break
                                    else:
                                        continue

                                # si te mueves al lado de ganon recibes 1 damage
                                if locations['castle'][playerY][playerX + 1] == "\\":
                                    game['player']['hearts_remaining'] -= 1

                                    if game['weapons']['Shield']['equiped'] == True:
                                        game['weapons']['Shield']['lives_remaining'] -= 1
                                    elif game['weapons']['Wood Shield']['equiped'] == True:
                                        game['weapons']['Wood Shield']['lives_remaining'] -= 1

                            # ---- IZQUIERDA
                            elif ("go left") in pregunta:
                                for i in range(cantidad):
                                    playerX -= 1
                                    if locations[game['player']['region']][playerY][playerX] != " ":
                                        playerX += 1
                                        break
                                    else:
                                        continue

                        locations[game['player']['region']][playerY][playerX] = "X"

                        # ---- FLAG ZELDA SAVED
                        while flg_zelda_saved:
                            clear_screen()
                            print(zelda_seved)
                            prompt(promptlist)
                            pregunta = input("What to do now?")
                            pregunta = pregunta.lower()
                            promptlist.append(pregunta)

                            if pregunta == "continue":
                                game['player']['region'] = 'hyrule'
                                game['player']['ganon_dead'] = 1
                                game['player']['hearts_remaining'] = calcular_max_hearts_remaining(game)
                                sobrescribir_game_con_data(data, game)
                                update_all()
                                flg_game = False
                                flg_juego = False
                                flg_castle = False
                                flg_zelda_saved = False
                                flg_inicio=True
                            else:
                                promptlist.append("Invalid action!")


                        # ---- LINK DEATH
                        while flg_link_death:
                            clear_screen()
                            promptlist.append("Nice try, you died, game is over.")
                            print(link_death)
                            prompt(promptlist)
                            pregunta = input("What to do now?")
                            pregunta = pregunta.lower()
                            promptlist.append(pregunta)

                            if pregunta == "continue":
                                game['player']['region'] = 'hyrule'
                                flg_game = False
                                flg_juego=False
                                flg_castle = False
                                flg_link_death = False
                                flg_inicio=True
                            else:
                                promptlist.append("Invalid action!")


                        # ---- DESGASTE DE WEAPONS
                        for weapon in game['weapons']:
                            if game['weapons'][weapon]['total_weapons'] > 1 and game['weapons'][weapon]['lives_remaining'] == 0:
                                game['weapons'][weapon]['total_weapons'] -= 1
                                game['weapons'][weapon]['lives_remaining'] = 5
                            if game['weapons'][weapon]['total_weapons'] == 1 and game['weapons'][weapon]['lives_remaining'] == 0:
                                game['weapons'][weapon]['total_weapons'] = 0
                                game['weapons'][weapon]['equiped'] = False

                # --- Go to INVALID ACTIONS
                else:
                    respuesta = "You can't go to " + (pregunta.replace('go to ', "")).title() + " from here."
                    promptlist.append(respuesta)

            # ----- MOVIMIENTO -----
            elif pregunta[:-2] in (
            'go right ', 'go left ', 'go up ', 'go down ', 'go right', 'go left', 'go up', 'go down'):
                cantidad = int(pregunta[-2:])
                # se pone en blanco el sitio donde antes estaba
                locations[game['player']['region']][playerY][playerX] = " "

                # ------ DERECHA
                if ("go right") in pregunta:
                    for i in range(cantidad):
                        playerX += 1
                        if locations[game['player']['region']][playerY][playerX] != " ":
                            playerX -= 1
                            break
                        else:
                            continue

                # ---- IZQUIERDA
                elif ("go left") in pregunta:
                    for i in range(cantidad):
                        playerX -= 1
                        if locations[game['player']['region']][playerY][playerX] != " ":
                            playerX += 1
                            break
                        else:
                            continue

                # ---- ARRIBA
                elif ("go up") in pregunta:
                    for i in range(cantidad):
                        playerY -= 1
                        if locations[game['player']['region']][playerY][playerX] != " " or playerY == 0:
                            playerY += 1
                            break
                        else:
                            continue

                # ---- ABAJO
                elif ("go down") in pregunta:
                    for i in range(cantidad):
                        playerY += 1
                        if locations[game['player']['region']][playerY][playerX] != " " or playerY == 11:
                            playerY -= 1
                            break
                        else:
                            continue

                # se pone la X en su nueva coordenada
                locations[game['player']['region']][playerY][playerX] = "X"


            # ------------------ ATTACK ------------------:

            # ---- ATTACK hierba ----
            elif pregunta == "attack" and attack_weapon == True and attack_entity == False and attack_tree == False:
                # se calcula el drop de la hierba
                promptlist.append(attack_grass(data, game))

            # ---- ATTACK tree a puños
            elif pregunta == "attack" and attack_weapon == False and attack_tree == True:
                # se calcula el drop del arbol
                promptlist.append(attack_tree_weaponless(data, game))


            # ---- ATTACK tree a espada
            elif pregunta == "attack" and attack_weapon == True and attack_tree == True:

                # si tree en DERECHA:
                if locations[game['player']['region']][playerY][playerX + 1] == "T":
                    # busca cual es el id del tree a la derecha del player
                    for tree_key in data[game['player']['region']]["trees"].keys():
                        if data[game['player']['region']]["trees"][tree_key]["ypos"] == playerY and \
                                data[game['player']['region']]["trees"][tree_key]["xpos"] == playerX + 1:
                            # quitamos 1 corazon al tree
                            data[game['player']['region']]["trees"][tree_key]["hearts"] -= 1
                            # si dejamos el arbol a 0 de vida, entonces se pone una cuenta atrás de 9 para respawn
                            if data[game['player']['region']]["trees"][tree_key]["hearts"] == 0:
                                data[game['player']['region']]["trees"][tree_key]["respawn"] = 10
                            promptlist.append(attack_tree_weapon(data, game))

                            if game['weapons']['Sword']['equiped'] == True:
                                game['weapons']['Sword']['lives_remaining'] -= 1
                            elif game['weapons']['Wood Sword']['equiped'] == True:
                                game['weapons']['Wood Sword']['lives_remaining'] -= 1

                # si tree en ARRIBA:
                elif locations[game['player']['region']][playerY - 1][playerX] == "T":
                    # busca cual es el id del tree a la derecha del player
                    for tree_key in data[game['player']['region']]["trees"].keys():
                        if data[game['player']['region']]["trees"][tree_key]["ypos"] == playerY - 1 and \
                                data[game['player']['region']]["trees"][tree_key]["xpos"] == playerX:
                            # quitamos 1 corazon al tree
                            data[game['player']['region']]["trees"][tree_key]["hearts"] -= 1
                            # si dejamos el arbol a 0 de vida, entonces se pone una cuenta atrás de 9 para respawn
                            if data[game['player']['region']]["trees"][tree_key]["hearts"] == 0:
                                data[game['player']['region']]["trees"][tree_key]["respawn"] = 10
                            promptlist.append(attack_tree_weapon(data, game))

                            if game['weapons']['Sword']['equiped'] == True:
                                game['weapons']['Sword']['lives_remaining'] -= 1
                            elif game['weapons']['Wood Sword']['equiped'] == True:
                                game['weapons']['Wood Sword']['lives_remaining'] -= 1

                # si treee en ABAJO:
                elif locations[game['player']['region']][playerY + 1][playerX] == "T":
                    # busca cual es el id del tree a la derecha del player
                    for tree_key in data[game['player']['region']]["trees"].keys():
                        if data[game['player']['region']]["trees"][tree_key]["ypos"] == playerY + 1 and \
                                data[game['player']['region']]["trees"][tree_key]["xpos"] == playerX:
                            # quitamos 1 corazon al tree
                            data[game['player']['region']]["trees"][tree_key]["hearts"] -= 1
                            # si dejamos el arbol a 0 de vida, entonces se pone una cuenta atrás de 9 para respawn
                            if data[game['player']['region']]["trees"][tree_key]["hearts"] == 0:
                                data[game['player']['region']]["trees"][tree_key]["respawn"] = 10
                            promptlist.append(attack_tree_weapon(data, game))

                            if game['weapons']['Sword']['equiped'] == True:
                                game['weapons']['Sword']['lives_remaining'] -= 1
                            elif game['weapons']['Wood Sword']['equiped'] == True:
                                game['weapons']['Wood Sword']['lives_remaining'] -= 1

                # si tree en IZQUIERDA:
                elif locations[game['player']['region']][playerY][playerX - 1] == "T":
                    # busca cual es el id del tree a la derecha del player
                    for tree_key in data[game['player']['region']]["trees"].keys():
                        if data[game['player']['region']]["trees"][tree_key]["ypos"] == playerY and \
                                data[game['player']['region']]["trees"][tree_key]["xpos"] == playerX - 1:
                            # quitamos 1 corazon al tree
                            data[game['player']['region']]["trees"][tree_key]["hearts"] -= 1
                            # si dejamos el arbol a 0 de vida, entonces se pone una cuenta atrás de 9 para respawn
                            if data[game['player']['region']]["trees"][tree_key]["hearts"] == 0:
                                data[game['player']['region']]["trees"][tree_key]["respawn"] = 10
                            promptlist.append(attack_tree_weapon(data, game))

                            if game['weapons']['Sword']['equiped'] == True:
                                game['weapons']['Sword']['lives_remaining'] -= 1
                            elif game['weapons']['Wood Sword']['equiped'] == True:
                                game['weapons']['Wood Sword']['lives_remaining'] -= 1


            # ---- ATTACK entidades con espada
            elif pregunta == "attack" and attack_weapon == True and attack_entity == True:
                # si enemy/fox/tree en DERECHA:
                if locations[game['player']['region']][playerY][playerX + 1] in ("E", "F"):
                    if locations[game['player']['region']][playerY][playerX + 1] == "E":
                        # busca cual es el id del enemigo a la derecha del player
                        for enemy_key in data[game['player']['region']]["enemies"].keys():
                            if data[game['player']['region']]["enemies"][enemy_key]["ypos"] == playerY and \
                                    data[game['player']['region']]["enemies"][enemy_key]["xpos"] == playerX + 1:
                                # quitamos 1 corazon al enemigo
                                data[game['player']['region']]["enemies"][enemy_key]["hearts"] -= 1
                                enemyY = data[game['player']['region']]["enemies"][enemy_key]["ypos"]
                                enemyX = data[game['player']['region']]["enemies"][enemy_key]["xpos"]
                                movimiento_enemy(data, locations, enemy_key, enemyY, enemyX, game)
                                promptlist.append(f"Brave, keep fighting {game['player']['user_name']}!")
                                game['player']['hearts_remaining'] -= 1
                                promptlist.append(
                                    f"Be careful, you only have {game['player']['hearts_remaining']} hearts.")

                                if game['weapons']['Sword']['equiped'] == True:
                                    game['weapons']['Sword']['lives_remaining'] -= 1
                                elif game['weapons']['Wood Sword']['equiped'] == True:
                                    game['weapons']['Wood Sword']['lives_remaining'] -= 1
                                if game['weapons']['Shield']['equiped'] == True:
                                    game['weapons']['Shield']['lives_remaining'] -= 1
                                elif game['weapons']['Wood Shield']['equiped'] == True:
                                    game['weapons']['Wood Shield']['lives_remaining'] -= 1

                    elif locations[game['player']['region']][playerY][playerX + 1] == "F":
                        # quitamos 1 corazon al fox
                        data[game['player']['region']]["fox"]["hearts"] -= 1
                        promptlist.append("You got meat.")
                        game['foods']['Meat']['quantity_remaining'] += 1
                        sobrescribir_game_con_data(data, game)
                        update_all()

                        if game['weapons']['Sword']['equiped'] == True:
                            game['weapons']['Sword']['lives_remaining'] -= 1
                        elif game['weapons']['Wood Sword']['equiped'] == True:
                            game['weapons']['Wood Sword']['lives_remaining'] -= 1

                # si enemy/fox/tree en ARRIBA:
                if locations[game['player']['region']][playerY - 1][playerX] in ("E", "F"):
                    if locations[game['player']['region']][playerY - 1][playerX] == "E":
                        # busca cual es el id del enemigo a la derecha del player
                        for enemy_key in data[game['player']['region']]["enemies"].keys():
                            if data[game['player']['region']]["enemies"][enemy_key]["ypos"] == playerY - 1 and \
                                    data[game['player']['region']]["enemies"][enemy_key]["xpos"] == playerX:
                                # quitamos 1 corazon al enemigo
                                data[game['player']['region']]["enemies"][enemy_key]["hearts"] -= 1
                                enemyY = data[game['player']['region']]["enemies"][enemy_key]["ypos"]
                                enemyX = data[game['player']['region']]["enemies"][enemy_key]["xpos"]
                                movimiento_enemy(data, locations, enemy_key, enemyY, enemyX, game)
                                promptlist.append(f"Brave, keep fighting {game['player']['user_name']}!")
                                game['player']['hearts_remaining'] -= 1
                                promptlist.append(
                                    f"Be careful, you only have {game['player']['hearts_remaining']} hearts.")

                                if game['weapons']['Sword']['equiped'] == True:
                                    game['weapons']['Sword']['lives_remaining'] -= 1
                                elif game['weapons']['Wood Sword']['equiped'] == True:
                                    game['weapons']['Wood Sword']['lives_remaining'] -= 1
                                if game['weapons']['Shield']['equiped'] == True:
                                    game['weapons']['Shield']['lives_remaining'] -= 1
                                elif game['weapons']['Wood Shield']['equiped'] == True:
                                    game['weapons']['Wood Shield']['lives_remaining'] -= 1

                    elif locations[game['player']['region']][playerY - 1][playerX] == "F":
                        # quitamos 1 corazon al fox
                        data[game['player']['region']]["fox"]["hearts"] -= 1
                        promptlist.append("You got meat.")
                        game['foods']['Meat']['quantity_remaining'] += 1
                        sobrescribir_game_con_data(data, game)
                        update_all()

                        if game['weapons']['Sword']['equiped'] == True:
                            game['weapons']['Sword']['lives_remaining'] -= 1
                        elif game['weapons']['Wood Sword']['equiped'] == True:
                            game['weapons']['Wood Sword']['lives_remaining'] -= 1

                # si enemy/fox/tree en ABAJO:
                if locations[game['player']['region']][playerY + 1][playerX] in ("E", "F"):
                    if locations[game['player']['region']][playerY + 1][playerX] == "E":
                        # busca cual es el id del enemigo a la derecha del player
                        for enemy_key in data[game['player']['region']]["enemies"].keys():
                            if data[game['player']['region']]["enemies"][enemy_key]["ypos"] == playerY + 1 and \
                                    data[game['player']['region']]["enemies"][enemy_key]["xpos"] == playerX:
                                # quitamos 1 corazon al enemigo
                                data[game['player']['region']]["enemies"][enemy_key]["hearts"] -= 1
                                enemyY = data[game['player']['region']]["enemies"][enemy_key]["ypos"]
                                enemyX = data[game['player']['region']]["enemies"][enemy_key]["xpos"]
                                movimiento_enemy(data, locations, enemy_key, enemyY, enemyX, game)
                                promptlist.append(f"Brave, keep fighting {game['player']['user_name']}!")
                                game['player']['hearts_remaining'] -= 1
                                promptlist.append(
                                    f"Be careful, you only have {game['player']['hearts_remaining']} hearts.")

                                if game['weapons']['Sword']['equiped'] == True:
                                    game['weapons']['Sword']['lives_remaining'] -= 1
                                elif game['weapons']['Wood Sword']['equiped'] == True:
                                    game['weapons']['Wood Sword']['lives_remaining'] -= 1
                                if game['weapons']['Shield']['equiped'] == True:
                                    game['weapons']['Shield']['lives_remaining'] -= 1
                                elif game['weapons']['Wood Shield']['equiped'] == True:
                                    game['weapons']['Wood Shield']['lives_remaining'] -= 1

                    elif locations[game['player']['region']][playerY + 1][playerX] == "F":
                        # quitamos 1 corazon al fox
                        data[game['player']['region']]["fox"]["hearts"] -= 1
                        promptlist.append("You got meat.")
                        game['foods']['Meat']['quantity_remaining'] += 1
                        sobrescribir_game_con_data(data, game)
                        update_all()

                        if game['weapons']['Sword']['equiped'] == True:
                            game['weapons']['Sword']['lives_remaining'] -= 1
                        elif game['weapons']['Wood Sword']['equiped'] == True:
                            game['weapons']['Wood Sword']['lives_remaining'] -= 1

                # si enemy/fox/tree en DERECHA:
                if locations[game['player']['region']][playerY][playerX - 1] in ("F"):
                    # quitamos 1 corazon al fox
                    data[game['player']['region']]["fox"]["hearts"] -= 1
                    promptlist.append("You got meat.")
                    game['foods']['Meat']['quantity_remaining'] += 1
                    sobrescribir_game_con_data(data, game)
                    update_all()

                    if game['weapons']['Sword']['equiped'] == True:
                        game['weapons']['Sword']['lives_remaining'] -= 1
                    elif game['weapons']['Wood Sword']['equiped'] == True:
                        game['weapons']['Wood Sword']['lives_remaining'] -= 1


            # ---- COOK
            elif pregunta[:4] == "cook" and cook == True:
                cocinar(pregunta, game, promptlist)

            # ---- FISH
            elif pregunta == "fish" and fish == True:
                promptlist.append(fishing(data, game))
                # ................. hacer que solo se pueda obtener pez 1 vez

            # ---- OPEN
            elif pregunta == "open" and open == True:

                # si sanctuary/chest en DERECHA:
                if locations[game['player']['region']][playerY][playerX + 1] in ("S", "M"):
                    if locations[game['player']['region']][playerY][playerX + 1] == "S":
                        # busca cual es el id del santuario a la derecha del player
                        for sanctuary_key in data[game['player']['region']]["sanctuaries"].keys():
                            if data[game['player']['region']]["sanctuaries"][sanctuary_key]["ypos"] == playerY and \
                                    data[game['player']['region']]["sanctuaries"][sanctuary_key]["xpos"] == playerX + 1:
                                # si ya está abierto
                                if data[game['player']['region']]["sanctuaries"][sanctuary_key]["open"] == True:
                                    promptlist.append("You already opened this sanctuary!")
                                # si está cerrado, abrimos
                                elif data[game['player']['region']]["sanctuaries"][sanctuary_key]["open"] == False:
                                    # cambiamos a abierto el santuario
                                    data[game['player']['region']]["sanctuaries"][sanctuary_key]["open"] = True
                                    promptlist.append(f"Sanctuary {sanctuary_key} done.")
                                    max_hearts_remaining = calcular_max_hearts_remaining(game)
                                    game['player']['hearts_remaining'] = max_hearts_remaining + 1
                                    promptlist.append(
                                        "You opened the sanctuary, your maximum hearts_remaining has increased by 1.")
                                    sobrescribir_game_con_data(data, game)
                                    update_all()




                    elif locations[game['player']['region']][playerY][playerX + 1] == "M":
                        # busca cual es el id del chest a la derecha del player
                        for chest_key in data[game['player']['region']]["chests"].keys():
                            if data[game['player']['region']]["chests"][chest_key]["ypos"] == playerY and \
                                    data[game['player']['region']]["chests"][chest_key]["xpos"] == playerX + 1:
                                # cambiamos a abierto el chest
                                data[game['player']['region']]["chests"][chest_key]["open"] = True
                                promptlist.append(drop_cofre(data, game))

                # si sanctuary/chest en ARRIBA:
                if locations[game['player']['region']][playerY - 1][playerX] in ("S", "M"):
                    if locations[game['player']['region']][playerY - 1][playerX] == "S":
                        # busca cual es el id del santuario a la derecha del player
                        for sanctuary_key in data[game['player']['region']]["sanctuaries"].keys():
                            if data[game['player']['region']]["sanctuaries"][sanctuary_key]["ypos"] == playerY - 1 and \
                                    data[game['player']['region']]["sanctuaries"][sanctuary_key]["xpos"] == playerX:
                                # si ya está abierto
                                if data[game['player']['region']]["sanctuaries"][sanctuary_key]["open"] == True:
                                    promptlist.append("You already opened this sanctuary!")
                                # si está cerrado, abrimos
                                elif data[game['player']['region']]["sanctuaries"][sanctuary_key]["open"] == False:
                                    # cambiamos a abierto el santuario
                                    data[game['player']['region']]["sanctuaries"][sanctuary_key]["open"] = True
                                    promptlist.append(f"Sanctuary {sanctuary_key} done.")
                                    max_hearts_remaining = calcular_max_hearts_remaining(game)
                                    game['player']['hearts_remaining'] = max_hearts_remaining + 1
                                    promptlist.append(
                                        "You opened the sanctuary, your maximum hearts_remaining has increased by 1.")
                                    sobrescribir_game_con_data(data, game)
                                    update_all()

                    elif locations[game['player']['region']][playerY - 1][playerX] == "M":
                        # busca cual es el id del chest a la derecha del player
                        for chest_key in data[game['player']['region']]["chests"].keys():
                            if data[game['player']['region']]["chests"][chest_key]["ypos"] == playerY - 1 and \
                                    data[game['player']['region']]["chests"][chest_key]["xpos"] == playerX:
                                # cambiamos a abierto el chest
                                data[game['player']['region']]["chests"][chest_key]["open"] = True
                                promptlist.append(drop_cofre(data, game))

                # si sanctuary/chest en ABAJO:
                if locations[game['player']['region']][playerY + 1][playerX] in ("S", "M"):
                    if locations[game['player']['region']][playerY + 1][playerX] == "S":
                        # busca cual es el id del santuario a la derecha del player
                        for sanctuary_key in data[game['player']['region']]["sanctuaries"].keys():
                            if data[game['player']['region']]["sanctuaries"][sanctuary_key]["ypos"] == playerY + 1 and \
                                    data[game['player']['region']]["sanctuaries"][sanctuary_key]["xpos"] == playerX:
                                # si ya está abierto
                                if data[game['player']['region']]["sanctuaries"][sanctuary_key]["open"] == True:
                                    promptlist.append("You already opened this sanctuary!")
                                # si está cerrado, abrimos
                                elif data[game['player']['region']]["sanctuaries"][sanctuary_key]["open"] == False:
                                    # cambiamos a abierto el santuario
                                    data[game['player']['region']]["sanctuaries"][sanctuary_key]["open"] = True
                                    promptlist.append(f"Sanctuary {sanctuary_key} done.")
                                    max_hearts_remaining = calcular_max_hearts_remaining(game)
                                    game['player']['hearts_remaining'] = max_hearts_remaining + 1
                                    promptlist.append(
                                        "You opened the sanctuary, your maximum hearts_remaining has increased by 1.")
                                    sobrescribir_game_con_data(data, game)
                                    update_all()

                    elif locations[game['player']['region']][playerY + 1][playerX] == "M":
                        # busca cual es el id del chest a la derecha del player
                        for chest_key in data[game['player']['region']]["chests"].keys():
                            if data[game['player']['region']]["chests"][chest_key]["ypos"] == playerY + 1 and \
                                    data[game['player']['region']]["chests"][chest_key]["xpos"] == playerX:
                                # cambiamos a abierto el chest
                                data[game['player']['region']]["chests"][chest_key]["open"] = True
                                promptlist.append(drop_cofre(data, game))

                # si chest en IZQUIERDA:
                if locations[game['player']['region']][playerY][playerX - 1] == "M":
                    # busca cual es el id del chest a la derecha del player
                    for chest_key in data[game['player']['region']]["chests"].keys():
                        if data[game['player']['region']]["chests"][chest_key]["ypos"] == playerY and \
                                data[game['player']['region']]["chests"][chest_key]["xpos"] == playerX - 1:
                            # cambiamos a abierto el chest
                            data[game['player']['region']]["chests"][chest_key]["open"] = True
                            promptlist.append(drop_cofre(data, game))

            # ---- SHOW INVENTORY
            elif pregunta[:14] == "show inventory":
                if pregunta[15:] == "main":
                    inv_actual = "main"
                elif pregunta[15:] == "food":
                    inv_actual = "food"
                elif pregunta[15:] == "weapons":
                    inv_actual = "weapons"

            # ---- EQUIP AND UNEQUIP
            elif pregunta[:10] == "equip the " or pregunta[:12] == "unequip the ":
                cambio_weapon(pregunta, game, promptlist)

            # --- EAT
            elif pregunta[:3] == "eat":
                comer(pregunta, game, promptlist, max_hearts_remaining)

            # ---- GO BY
            elif pregunta[:10] == "go by the ":

                # go by en Hyrule
                if game['player']['region']=='hyrule':
                    locations[game['player']['region']][playerY][playerX] = " "
                    playerY, playerX = go_by_hyrule(pregunta, playerX, playerY,locations,game)

                #go by en Death Mountain
                elif game['player']['region']=='death_mountain':
                    locations[game['player']['region']][playerY][playerX] = " "
                    playerY, playerX = go_by_death_mountain(pregunta, playerX, playerY,locations,game)

                #go by en Gerudo
                elif game['player']['region'] == 'gerudo':
                    locations[game['player']['region']][playerY][playerX] = " "
                    playerY, playerX = go_by_gerudo(pregunta, playerX, playerY,locations,game)

                # go by en Necluda
                elif game['player']['region'] == 'necluda':
                    locations[game['player']['region']][playerY][playerX] = " "
                    playerY, playerX = go_by_necluda(pregunta, playerX, playerY,locations,game)


                locations[game['player']['region']][playerY][playerX] = "X"


            # --- CHEATING:
                # game over:
            elif pregunta == "cheating: cheat game over":
                game['player']['hearts_remaining'] = 0
                flg_link_death=True

                # win game:
            elif pregunta == "cheating: cheat win game":
                game['player']['ganon_dead'] = True
                flg_zelda_saved = True
                while flg_zelda_saved:
                    clear_screen()
                    print(zelda_seved)
                    prompt(promptlist)
                    pregunta = input("What to do now?")
                    pregunta = pregunta.lower()
                    promptlist.append(pregunta)

                    if pregunta == "continue":
                        game['player']['region'] = 'hyrule'
                        game['player']['ganon_dead'] = 1
                        game['player']['hearts_remaining'] = calcular_max_hearts_remaining(game)
                        sobrescribir_game_con_data(data, game)
                        update_all()
                        flg_game = False
                        flg_juego = False
                        flg_zelda_saved = False
                        flg_inicio= True
                    else:
                        promptlist.append("Invalid action!")

            elif pregunta[:9] == "cheating:":
                cheating(pregunta, game, promptlist,data,max_hearts_remaining)

            # ---- EXIT
            elif pregunta == "exit":
                flg_game = False
                flg_juego = False
                flg_inicio = True


            # ---- NO VALIDA
            else:
                # cualquier otra cosa no recogida anteriormente es inválida
                promptlist.append("Invalid action!")

            # ---- DESGASTE DE WEAPONS
            for weapon in game['weapons']:
                if game['weapons'][weapon]['total_weapons']>1 and game['weapons'][weapon]['lives_remaining']==0:
                    game['weapons'][weapon]['total_weapons']-=1
                    game['weapons'][weapon]['lives_remaining'] = 5
                if game['weapons'][weapon]['total_weapons']==1 and game['weapons'][weapon]['lives_remaining']==0:
                    game['weapons'][weapon]['total_weapons']=0
                    game['weapons'][weapon]['equiped']=False


            # ---- BLOOD MOONS COUNTDOWN
            # al final del turno, quitamos 1 de la cuenta atrás de blood moons
            game['player']['blood_moon_countdown'] -= 1

            # ---- LINK DEATH ----
            while flg_link_death:
                clear_screen()
                promptlist.append("Nice try, you died, game is over.")
                print(link_death)
                prompt(promptlist)
                pregunta = input("What to do now?")
                pregunta = pregunta.lower()
                promptlist.append(pregunta)

                if pregunta == "continue":
                    game['player']['region'] = 'hyrule'
                    flg_game = False
                    flg_juego=False
                    flg_castle = False
                    flg_link_death = False
                    flg_inicio=True
                    break
                else:
                    promptlist.append("Invalid action!")

