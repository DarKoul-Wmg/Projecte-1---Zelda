import random
from armario_PRINTS import*
from armario_FUNCIONES import*
from consultasBD import*



nombre = ''
promptlist = []

new_prompt = ""


salir = False
exit = False
flg_principal = True
flg_queries =False
flg_help = False
flg_inicio = False
flg_n_game = False
flg_about = False
flg_h_n_game = False
flg_legend = False
flg_plot = False
flg_juego = False

listamenu = [menu1,menu2,menu3]
listamenu2 = [menu11,menu22,menu33]

cabecera = random.randrange(len(listamenu))
cabecera2 = random.randrange(len(listamenu2))


menu_principal ="1)Game 2)Queries BD 3)Exit"
menu_queries = ("===================Consulta"
                "s BD===================\n1)Usuarios que han jugado\n2)Cantidad de partidas jugadas por usuario"
                "\n3)Armas usadas por usuario y datos por partida\n4)Comida consumida por usuario y datos por partida\n5)Estadistica de 'blood Moon'"
                "\n==================================================")
#menu00 = ('continue','new game','help','about','exit')

game = {}

while exit != True:
    while flg_principal:

        print(menu_principal0)
        print(menu_principal)

        opc = input("Opc: ")

        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 4):
            print("wrong option")
        elif int(opc) == 1:
            flg_inicio = True
            flg_principal = False
        elif int(opc) == 2:
            flg_principal = False
            flg_queries = True
        else:
            exit = True
            flg_principal = False
    #queries
    while flg_queries:
        print(menu_queries)
        opc = input("Opc: ")
        print()
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 6):
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
            print("Usuario".ljust(12), "Arma".ljust(13), "Veces obtenida".rjust(3), "Última Fecha de Uso".rjust(22))
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


###############################################################################################################################################3
####parte vieja
    while flg_inicio:
        if 'game_id'in game:


            clear_screen()

            print(listamenu[cabecera])
            prompt(promptlist)
            opc = input()

            promptlist.append(opc)

            if not opc.replace(" ", "").isalpha() :
                #print('Invalid action')

                promptlist.append('Invalid action')

            elif opc.lower() == 'exit':

                clear_screen()
                flg_inicio = False
                flg_principal = True

            elif opc.lower() == 'help':

                clear_screen()
                flg_inicio = False
                flg_help = True

            elif opc.lower() == 'about':

                clear_screen()
                flg_inicio = False
                flg_about = True
            elif opc.lower() == ('new game'):

                clear_screen()
                flg_inicio = False
                flg_n_game = True
            else:
                # print('Invalid action')
                promptlist.append('Invalid action')
                    #version sin partida guardada
        elif not 'game_id'in game:

            while flg_inicio:


                print(listamenu2[cabecera2])
                prompt(promptlist)
                opc = input()

                promptlist.append(opc)

                if not opc.replace(" ", "").isalpha():
                    # print('Invalid action')

                    promptlist.append('Invalid action')

                elif opc.lower() == 'exit':

                    clear_screen()
                    flg_inicio = False
                    flg_principal = True

                elif opc.lower() == 'help':

                    clear_screen()
                    flg_inicio = False
                    flg_help = True

                elif opc.lower() == 'about':

                    clear_screen()
                    flg_inicio = False
                    flg_about = True
                elif opc.lower() == ('new game'):

                    clear_screen()
                    flg_inicio = False
                    flg_n_game = True
                else:
                    # print('Invalid action')
                    promptlist.append('Invalid action')

    ##menu help
    while flg_help:

        print(main_menu)
        prompt(promptlist)

        opcion1 = input()  # en blanco pendiente
        promptlist.append(opcion1)
        if not opcion1.replace(" ", "").isalpha():
            #print('Invalid action')
            promptlist.append('Invalid action')

        elif opcion1.lower() == 'back':
            clear_screen()
            flg_help = False
            flg_inicio = True

        else:
            #print('Invalid action')
            promptlist.append('Invalid action')
    ##menu about
    while flg_about:
        ################probar sin flags

        print(menu_about)
        prompt(promptlist)
        opcion2 = input()  # en blanco pendiente
        promptlist.append(opcion2)
        if not opcion2.replace(" ", "").isalpha():
            #print('Invalid action')
            promptlist.append('Invalid action')

        elif opcion2.lower() == 'back':
            clear_screen()
            flg_about = False
            flg_inicio = True
        else:

            promptlist.append('Invalid action')

    ##menu new game
    while flg_n_game:
        ###############
        print(new_game)
        prompt(promptlist)

        nombre = input("What\'s your name (Link)?\n")  ######ESTO QUEDA TOPE FEO#####################
        promptlist.append(nombre)
        if not nombre.isalnum() and nombre.replace(" ", ""):
            frase = nombre + " is not a valid name1"
            promptlist.append(frase)

        elif len(nombre)== 1 and len(nombre) < 3:
            #print(nombre, "is not a valid name")
            frase0 = nombre+ " is not a valid name"
            promptlist.append(frase0)
        elif len(nombre) > 10:
            #print(nombre, "is not a valid name")
            frase2 = nombre + " is not a valid name"
            promptlist.append(frase2)
        elif len(nombre) == 0:  ##no funciona lo de link
            nombre = 'Link'
            frase3 = 'Welcome to the game,' + nombre
            promptlist.append(frase3)
            game['game_id'] = 0
            game['user_name'] = nombre
            print(game)  ##PRUEBA
            clear_screen()
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

            #print('Welcome to the game,', nombre)
            frase4 = 'Welcome to the game,'+nombre
            promptlist.append(frase4)
            game['game_id'] = 0
            game['user_name'] = nombre
            print(game)##PRUEBA
            clear_screen()
            flg_n_game = False
            flg_legend = True


    ##help_new_game
    while flg_h_n_game:
            print(help_new_game)
            prompt(promptlist)
            opcion4 = input()  # en blanco pendiente
            promptlist.append(opcion4)
            if not opcion4.replace(" ", "").isalpha():
                #print('Invalid action')
                promptlist.append('Invalid action')
            elif opcion4.lower() == 'back':
                clear_screen()
                flg_h_n_game = False
                flg_n_game = True
            else:
                promptlist.append('Invalid action')

    ##legend
    while flg_legend:
        print(menu_legend)
        prompt(promptlist)
        opcion5 = input()  # en blanco pendiente
        promptlist.append(opcion5)
        if not opcion5.replace(" ", "").isalpha():
            #print('Invalid action')
            promptlist.append('Invalid action')
        elif opcion5.lower() == 'continue':
            clear_screen()
            flg_legend = False
            flg_plot = True
        else:
            promptlist.append('Invalid action')


    ##plot

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
        opcion5 = input()  # en blanco pendiente
        if not opcion5.replace(" ", "").isalpha():
            #print('Invalid action')
            promptlist.append('Invalid action')

        elif opcion5.lower() == 'continue':
            #print('The adventure begins')
            promptlist.append('The adventure begins')
            clear_screen()
            flg_plot = False
            flg_juego = True
        else:
            promptlist.append('Invalid action')


    while flg_juego:
        print('juego')
        break
        ##AQUI DEBERIA IR EL JUEGO











