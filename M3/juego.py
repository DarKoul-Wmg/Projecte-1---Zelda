import random

from armario_PRINTS import*
from armario_FUNCIONES import*




nombre = ''
promptlist = []
new_prompt = ""


salir = False

flg_01 = False
flg_00 = True
flg_03 = False
flg_02 = False
flg_04 = False
flg_05 = False
flg_06 = False

listamenu = [menu1,menu2,menu3]
listamenu2 = [menu11,menu22,menu33]

cabecera = random.randrange(len(listamenu))
cabecera2 = random.randrange(len(listamenu2))



menu00 = ('continue','new game','help','about','exit')

game = {}



while salir != True:
    if 'game_id'in game:

        while flg_00:
            clear_screen()

            print(listamenu[cabecera])
            prompt(promptlist)
            opc = input()

            list.append(opc)

            if not opc.replace(" ", "").isalpha() :
                #print('Invalid action')

                promptlist.append('Invalid action')

            elif opc.lower() == 'exit':

                clear_screen()
                flg_00 = False
                salir = True

            elif opc.lower() == 'help':

                clear_screen()
                flg_00 = False
                flg_01 = True

            elif opc.lower() == 'about':

                clear_screen()
                flg_00 = False
                flg_02 = True
            elif opc.lower() == ('new game'):

                clear_screen()
                flg_00 = False
                flg_03 = True
            else:
                # print('Invalid action')
                promptlist.append('Invalid action')
                    #version sin partida guardada
    elif not 'game_id'in game:

        while flg_00:


            print(listamenu2[cabecera2])
            prompt(promptlist)
            opc = input()

            promptlist.append(opc)

            if not opc.replace(" ", "").isalpha():
                # print('Invalid action')

                promptlist.append('Invalid action')

            elif opc.lower() == 'exit':

                clear_screen()
                flg_00 = False
                salir = True

            elif opc.lower() == 'help':

                clear_screen()
                flg_00 = False
                flg_01 = True

            elif opc.lower() == 'about':

                clear_screen()
                flg_00 = False
                flg_02 = True
            elif opc.lower() == ('new game'):

                clear_screen()
                flg_00 = False
                flg_03 = True
            else:
                # print('Invalid action')
                promptlist.append('Invalid action')

    ##menu help
    while flg_01:

        print(main_menu)
        prompt(promptlist)

        opcion1 = input()  # en blanco pendiente
        list.append(opcion1)
        if not opcion1.replace(" ", "").isalpha():
            #print('Invalid action')
            promptlist.append('Invalid action')

        elif opcion1.lower() == 'back':
            clear_screen()
            flg_01 = False
            flg_00 = True

        else:
            #print('Invalid action')
            promptlist.append('Invalid action')
    ##menu about
    while flg_02:
        ################probar sin flags

        print(menu_about)
        prompt(list)
        opcion2 = input()  # en blanco pendiente
        list.append(opcion2)
        if not opcion2.replace(" ", "").isalpha():
            #print('Invalid action')
            promptlist.append('Invalid action')

        elif opcion2.lower() == 'back':
            clear_screen()
            flg_02 = False
            flg_00 = True
        else:

            promptlist.append('Invalid action')

    ##menu new game
    while flg_03:
        ###############
        print(new_game)
        prompt(promptlist)

        nombre = input("What\'s your name (Link)?\n")  ######ESTO QUEDA TOPE FEO#####################
        list.append(nombre)
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
            flg_03 = False
            flg_05 = True


        elif nombre.lower() == 'back':
            clear_screen()
            flg_03 = False
            flg_00 = True
        elif nombre.lower() == 'help':
            clear_screen()
            flg_03 = False
            flg_04 = True

        else:

            #print('Welcome to the game,', nombre)
            frase4 = 'Welcome to the game,'+nombre
            promptlist.append(frase4)
            game['game_id'] = 0
            game['user_name'] = nombre
            print(game)##PRUEBA
            clear_screen()
            flg_03 = False
            flg_05 = True


    ##help_new_game
    while flg_04:
            print(help_new_game)
            prompt(promptlist)
            opcion4 = input()  # en blanco pendiente
            promptlist.append(opcion4)
            if not opcion4.replace(" ", "").isalpha():
                #print('Invalid action')
                promptlist.append('Invalid action')
            elif opcion4.lower() == 'back':
                clear_screen()
                flg_04 = False
                flg_03 = True
            else:
                list.append('Invalid action')

    ##legend
    while flg_05:
        print(menu_legend)
        prompt(promptlist)
        opcion5 = input()  # en blanco pendiente
        promptlist.append(opcion5)
        if not opcion5.replace(" ", "").isalpha():
            #print('Invalid action')
            promptlist.append('Invalid action')
        elif opcion5.lower() == 'continue':
            clear_screen()
            flg_05 = False
            flg_06 = True
        else:
            promptlist.append('Invalid action')


    ##plot

    while flg_06:
        t = len(nombre)
        w = 28
        x = w - t
        print("* Plot * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
              "*                                                                            *\n"
              "*                                                                            *\n"
              "*  Now history is repeating itself, and Princess Zelda has been captured by  *\n"
              "*  Ganon. He has taken over the Guardians and filled Hyrule with monsters.   *\n"
              "*                                                                            *\n"
              "*                                                                            *\n"
              f"*  But a young man named '{nombre}' has just awakened and".rjust(78),
              '*'.rjust(x))  ######se espacia la *
        print("*  must reclaim the Guardians to defeat Ganon and save Hyrule.               *\n"
              "*                                                                            *\n"
              "*                                                                            *\n"
              "* Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

        prompt(list)
        opcion5 = input()  # en blanco pendiente
        if not opcion5.replace(" ", "").isalpha():
            #print('Invalid action')
            promptlist.append('Invalid action')

        elif opcion5.lower() == 'continue':
            #print('The adventure begins')
            promptlist.append('The adventure begins')
            clear_screen()
            flg_06 = False
            flg_07 = True
        else:
            promptlist.append('Invalid action')

    while flg_06:
        print('juego')
        ##AQUI DEBERIA IR EL JUEGO











