import os
import platform
from diccionario_general import*

#funcion validar usuario
def nombre_usuario(nombre):

    nombre_correcto = False
    while not nombre_correcto:
        nombre = input(':')
        print(len(nombre))

        if len(nombre)!= 0 and len(nombre) < 3:
            print(nombre,"is not a valid name")


        elif len(nombre) > 10:
            print(nombre,"is not a valid name")


        elif len(nombre) == 0:##no funciona lo de link
            nombre = 'Link'
            nombre_correcto = True

        else:
            print('Welcome to the game,',nombre)

            nombre_correcto = True
    return nombre

#funcion prompt1

def prompt(list):


    while len(list)>8:
        list=list[1:]
    if len(list)<9:
        for i in range(len(list)):
             print(list[i])



##limpiar pantalla
def clear_screen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

##FUINCION PRINT INVENTARIO FOOD

pregunta = 'Show inventory food'

def inv_food(pregunta):


    menu_foods = ["* * * * *   Food *",
                  "                 *",
                  "                 *",
                f"Vegetables    {str(z).rjust(2)} *",
                f"Fish          {str(v).rjust(2)} *",
                f"Meat          {str(m).rjust(2)} *",
                f"Salads        {str(s).rjust(2)} *",
                f"Pescatarian   {str(p).rjust(2)} *",
                f"Roasted       {str(r).rjust(2)} *",
                "                 *"]

    inv_actual = menu_foods
    for i in range(len(inv_actual)):
        print(inv_actual[i])

#inv_food(pregunta)

##FUNCION PRINT PANTALLA WEAPONS



pregunta = 'Show inventory weapons'

def weapons(pregunta):
    if pregunta == 'Show inventory weapons':

        q = game['weapons']["Wood Sword"]["lives_remaining"]
        q1 =game['weapons']["Wood Sword"]["total_weapons"]

        if game['weapons']["Wood Sword"]["equipped"] == 1:
            q2 = "(equiped)"
        else:
            q2 =""

        s = game['weapons']["Sword"]["lives_remaining"]
        s1 =game['weapons']["Sword"]["total_weapons"]


        if game['weapons']["Sword"]["equipped"] == 1:
            s2 = "(equiped)"
        else:
            s2 =""

        w = game['weapons']["Wood Shield"]["lives_remaining"]
        w1 =game['weapons']["Wood Shield"]["total_weapons"]


        if game['weapons']["Wood Shield"]["equipped"] == 1:
            w2 = "(equiped)"
        else:
            w2 =""

        sh = game['weapons']["Shield"]["lives_remaining"]
        sh1 =game['weapons']["Shield"]["total_weapons"]


        if game['weapons']["Shield"]["equipped"] == 1:
            sh2 = "(equiped)"
        else:
            sh2 =""

        menu_weapons = ["* * * * * Weapons *",
                        "                  *",
                        "                  *",
                        f"Wood Sword   {str(q).rjust(2)}/{str(q1).rjust(1)} *",
                        f" {str(q2).ljust(10)}       *",
                        f"Sword        {str(s).rjust(2)}/{str(s1).rjust(1)} *",
                        f" {str(s2).ljust(10)}       *",
                        "                  *",
                        f"Wood Shield  {str(w).rjust(2)}/{str(w1).rjust(1)} *",
                        f" {str(w2).ljust(10)}       *",
                        f"Shield       {str(sh).rjust(2)}/{str(sh1).rjust(1)} *",
                        f" {str(sh2).ljust(10)}       *"]

        inv_actual = menu_weapons
        for i in range(len(inv_actual)):
            print(inv_actual[i])

        return inv_actual



#weapons(pregunta)




#FUNCION PRINT PANTALLA INVENTARIO
pregunta = 'Show inventory main'

def main(pregunta):
    if pregunta == 'Show inventory main':
        weapon_list = []

        for weapon_name, weapon_info in game["weapons"].items():
            equipped_value = weapon_info["equipped"]
            if weapon_info["equipped"] == 1:

                weapon_list.append(weapon_name)

        menu_inventory =  ["* * * * Inventory *",
                      "                  *",
                      f"{str(n).ljust(10)}  ♥ {str(b).ljust(1)}/5 *",
                      "                  *",
                      "Equipament        *",
                      "                  *",
                      f"      {str(weapon_list[0]).rjust(11)} *",
                      f"      {str(weapon_list[1]).rjust(11)} *",
                      "                  *",
                      f"Food          {str(tf).rjust(3)} *",
                      f"Weapons       {str(tw).rjust(3)} *",
                      "                  *"]

        for i in range(len(menu_inventory)):
            print(menu_inventory[i])
            inv_actual = menu_inventory
        return menu_inventory


#main(pregunta)


##menus

menu1 = ("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
        "*                                                                  ##         *\n"
        "*                                                                  ##         *\n"
        "*                                                               ##~~~         *\n"
        "*                                                              ###~~~O        *\n"
        "*  Zelda, Breath of the Wild                                   ###~~~ \       *\n"
        "*                                                                |@@@| \      *\n"
        "*                                                                |   |  \     *\n"
        "*                                                                =   ==       *\n"
        "*                                                            %%%%%%%%%%%%     *\n"
        "*                                                         %%%%%%%%%%%%%%%     *\n"
        "* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *\n"
         )



menu2 = ("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
        "*                                                                  &&         *\n"
        "*                                                                 oo &        *\n"
        "*                                                         $       -- &##      *\n"
        "*                                                         $$     <<OO####     *\n"
        "*  Zelda, Breath of the Wild                               $$  //OOO####      *\n"
        "*                                                           $$// OO#####      *\n"
        "*                                                            **   OOO###      *\n"
        "*                                                             &   @@@@\       *\n"
        "*                                                                 Q  Q        *\n"
        "*                                                                 Q  Q        *\n"
        "* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *\n"
         )


menu3 = ("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
        "*                                                                  &&         *\n"
        "*                                                                 ####        *\n"
        "*                                                                \" || \"       *\n"
        "*                                                             @@@@@@@@@@@@    *\n"
        "*  Zelda, Breath of the Wild                                 @     ||@@@      *\n"
        "*                                                                  |@@@       *\n"
        "*                                                                 @@@         *\n"
        "*                                                               @@@||     @   *\n"
        "*                                                            @@@@@@@@@@@@@    *\n"
        "*                                                                  ||         *\n"
        "* Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * *\n"
         )

menu11 = ("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
        "*                                                                  ##         *\n"
        "*                                                                  ##         *\n"
        "*                                                               ##~~~         *\n"
        "*                                                              ###~~~O        *\n"
        "*  Zelda, Breath of the Wild                                   ###~~~ \       *\n"
        "*                                                                |@@@| \      *\n"
        "*                                                                |   |  \     *\n"
        "*                                                                =   ==       *\n"
        "*                                                            %%%%%%%%%%%%     *\n"
        "*                                                         %%%%%%%%%%%%%%%     *\n"
        "* New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * * * * * *\n"
         )

menu22 = ("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
        "*                                                                  &&         *\n"
        "*                                                                 oo &        *\n"
        "*                                                         $       -- &##      *\n"
        "*                                                         $$     <<OO####     *\n"
        "*  Zelda, Breath of the Wild                               $$  //OOO####      *\n"
        "*                                                           $$// OO#####      *\n"
        "*                                                            **   OOO###      *\n"
        "*                                                             &   @@@@\       *\n"
        "*                                                                 Q  Q        *\n"
        "*                                                                 Q  Q        *\n"
        "* New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * * * * * *\n"
         )

menu33 = ("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
        "*                                                                  &&         *\n"
        "*                                                                 ####        *\n"
        "*                                                                \" || \"       *\n"
        "*                                                             @@@@@@@@@@@@    *\n"
        "*  Zelda, Breath of the Wild                                 @     ||@@@      *\n"
        "*                                                                  |@@@       *\n"
        "*                                                                 @@@         *\n"
        "*                                                               @@@||     @   *\n"
        "*                                                            @@@@@@@@@@@@@    *\n"
        "*                                                                  ||         *\n"
        "* New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * * * * * *\n"
         )





main_menu = ('* Help, main menu * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n'
                      '*                                                                             *\n'
                      '*                                                                             *\n'
                      "*       Type /'continue/' to continue a saved game                            *\n"
                      "*       Type /'new game/' to start a new game                                 *\n"
                      "*       Type /'about/' to see information about the game                      *\n"
                      "*       Type /'exit/' to exit the game                                        *\n"
                      "*                                                                             *\n"
                      "*                                                                             *\n"
                      "*       Type 'back' now to go back to the 'Main menu'                         *\n"
                      "*                                                                             *\n"
                      "* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")


menu_about = ("* About * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
                   "*                                                                             *\n"
                   "*       Game developed by /‘Team 2, The hometown bugs/’ :                     *\n"
                   "*                                                                             *\n"
                   "*                                                                             *\n"
                   "*            William K. Molina                                                *\n"
                   "*            Mar Melich                                                       *\n"
                   "*            Pau Gracia                                                       *\n"
                   "*                                                                             *\n"
                   "*       Type /'back/' now to go back to the /'Main menu/'                     *\n"
                   "*                                                                             *\n"
                   "* Back* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

new_game = ("* New game * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
           "*                                                                            *\n"
           "*                                                                            *\n"
           "*                                                                            *\n"
           "*                                                                            *\n"
           "*       Set your name ?                                                      *\n"
           "*                                                                            *\n"
           "*                                                                            *\n"
           "*                                                                            *\n"
           "*       Type 'back' now to go back to the 'Main menu'                        *\n"
           "*                                                                            *\n"
           "* Back, Help * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

help_new_game = ("* Help, new game * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
                 "*                                                                            *\n"
                 "*                                                                            *\n"
                 "*       When asked, type your name and press enter                           *\n"
                 "*       if 'Link' is fine for you, just press enter                          *\n"
                 "*                                                                            *\n"
                 "*       Name must be between 3 and 10 characters long and only               *\n"
                 "*       letters, numbers and spaces are allowed                              *\n"
                 "*                                                                            *\n"
                 "*       Type 'back' now to go back to 'Set your name'                        *\n"
                 "*                                                                            *\n"
                 "* Back * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

menu_legend = ("* Legend * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
               "*    10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah *\n"
               "*    tribe. The Sheikah were a tribe of warriors who protected the Triforce, *\n"
               "*    a sacred relic that granted wishes.                                     *\n"
               "*                                                                            *\n"
               "*    But one day, Ganondorf, an evil sorcerer, stole the Triforce and began  *\n"
               "*    to rule Hyrule with an iron fist.                                       *\n"
               "*                                                                            *\n"
               "*    The princess, with the help of a heroic young man, managed to defeat    *\n"
               "*    Ganondorf and recover the Triforce.                                     *\n"
               "*                                                                            *\n"
               "* Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")

menu_help_inv = ("* Help, inventory * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"
                 "*       Type 'show inventory main' to show the main inventory                 *\n"
                 "*            (main, weapons, Food)                                            *\n"
                 "*       Type 'eat X' to eat X, where X is a Food item                         *\n"
                 "*       Type 'Cook X' to Cook X, where X is a Food item                       *\n"
                 "*       Type 'equip X' to equip X, where X is a weapon                        *\n"
                 "*       Type 'unequip X' to unequip X, where X is a weapon                    *\n"
                 "*       Type 'back' now to go back to the 'Game'                              *\n"
                 "* Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n"

)

