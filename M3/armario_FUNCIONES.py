import os
import platform
from diccionario_general import*
import time

promptlist = []
#funcion prompt1

def prompt(promptlist):


    while len(promptlist)>8:
        promptlist=promptlist[1:]
    if len(promptlist)<9:
        for i in range(len(promptlist)):
             print(promptlist[i])



##limpiar pantalla
def clear_screen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')

    else:
        os.system('clear')

#clear_screen()

##FUINCION PRINT INVENTARIO FOOD

#pregunta = 'Show inventory food'

def inv_food(pregunta):
    if 'foods' in game:
        z = game['foods']['Vegetables']['quantity_remaining']
        v = game['foods']['Fish']['quantity_remaining']
        m = game['foods']['Meat']['quantity_remaining']
        s = game['foods']['Salads']['quantity_remaining']
        p = game['foods']['Pescatarian']['quantity_remaining']
        r = game['foods']['Roasted']['quantity_remaining']
        if pregunta == 'Show inventory food':

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



pregunta = ('Show inventory weapons')

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
#pregunta = 'Show inventory main'

def main(pregunta):
    n = game['player']['user_name']
    b = game['player']['total_blood_moon']
    tw = ((game["weapons"]["Shield"]["total_weapons"] + game["weapons"]["Wood Shield"]["total_weapons"]
           + game["weapons"]["Sword"]["total_weapons"]) + game["weapons"]["Wood Sword"]["total_weapons"])

    tf = ((game['foods']["Fish"]["quantity_remaining"] + game['foods']["Vegetables"]["quantity_remaining"]
           + game['foods']["Meat"]["quantity_remaining"]) + game['foods']["Salads"]["quantity_remaining"]
          + game['foods']["Pescatarian"]["quantity_remaining"] + game['foods']["Roasted"]["quantity_remaining"])

    if pregunta == 'Show inventory main':
        weapon_list = []

        for weapon_name, weapon_info in game["weapons"].items():
            equipped_value = weapon_info["equipped"]
            if weapon_info["equipped"] == 1:

                weapon_list.append(weapon_name)

        menu_inventory =  ["* * * * Inventory *",
                      "                  *",
                      f"{str(n).ljust(10)}  ♥ {str(b).ljust(1)}/{str(max_blood_moon).ljust(1)} *",
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


##FUNCION CAMBIO ARMAS
def cambio_weapon(pregunta,game):

    if pregunta.lower() == "equip the sword":
        if game['weapons']["Wood Sword"]["equipped"] == 1:
            game['weapons']["Sword"]["equipped"] = 0
            promptlist.append('You cannot equip two swords')
            prompt(promptlist)
        elif game['weapons']["Sword"]["equipped"] == 1:
            promptlist.append('You already have Sword equipped')
            prompt(promptlist)
        else:
            if game['weapons']["Sword"]["total_weapons"] == 0:
                game['weapons']["Sword"]["equipped"] = 0
                promptlist.append("You don't have Sword")
                prompt(promptlist)
            else:
                game['weapons']["Sword"]["equipped"] = 1
                promptlist.append("Sword equipped")
                prompt(promptlist)
    elif pregunta.lower() == "equip the wood shield":
        if game['weapons']["Shield"]["equipped"] == 1:
            game['weapons']["Wood Shield"]["equipped"] = 0
            promptlist.append("You cannot equip two shields")
            prompt(promptlist)
        elif game['weapons']["Wood Shield"]["equipped"] == 1:
            promptlist.append('You already have Wood Shield equipped')
            prompt(promptlist)
        else:
            if game['weapons']["Wood Shield"]["total_weapons"] == 0:
                game['weapons']["Wood Shield"]["equipped"] = 0
                promptlist.append("You don't have Sword")
                prompt(promptlist)
            else:
                game['weapons']["Wood Shield"]["equipped"] = 1
                promptlist.append("Wood shield equipped")
                prompt(promptlist)
    elif pregunta.lower() == "equip the wood sword":
        if game['weapons']["Sword"]["equipped"] == 1:
            game['weapons']["Wood Sword"]["equipped"] = 0
            promptlist.append('You cannot equip two swords')
            prompt(promptlist)
        elif game['weapons']["Wood Sword"]["equipped"] == 1:
            promptlist.append('You already have Wood Sword equipped')
            prompt(promptlist)
        else:
            if game['weapons']["Wood Sword"]["total_weapons"] == 0:
                game['weapons']["Wood Sword"]["equipped"] = 0
                promptlist.append("You don't have Sword")
                prompt(promptlist)
            else:
                game['weapons']["Wood Sword"]["equipped"] = 1
                promptlist.append("Wood Sword equipped")
                prompt(promptlist)
    elif pregunta.lower() == "equip the shield":
        if game['weapons']["Wood Shield"]["equipped"] == 1:
            game['weapons']["Shield"]["equipped"] = 0
            promptlist.append("You cannot equip two shields")
            prompt(promptlist)
        elif game['weapons']["Shield"]["equipped"] == 1:
            promptlist.append('You already have Shield equipped')
            prompt(promptlist)
        else:
            if game['weapons']["Shield"]["total_weapons"] == 0:
                game['weapons']["Shield"]["equipped"] = 0
                promptlist.append("You don't have Sword")
                prompt(promptlist)
            else:
                game['weapons']["Shield"]["equipped"] = 1
                promptlist.append("Shield equipped")
                prompt(promptlist)
    elif pregunta.lower() == "unequip the sword":
        game['weapons']["Sword"]["equipped"] = 0
        promptlist.append('Sword unequipped')
        prompt(promptlist)
    elif pregunta.lower() == "unequip the wood shield":
        game['weapons']["Wood Shield"]["equipped"] = 0
        promptlist.append('Wood Shield unequipped')
        prompt(promptlist)
    elif pregunta.lower() == "unequip the wood sword":
        game['weapons']["Wood Sword"]["equipped"] = 0
        promptlist.append('Wood Sword unequipped')
        prompt(promptlist)
    elif pregunta.lower() == "unequip the shield":
        game['weapons']["Shield"]["equipped"] = 0
        promptlist.append('Shield unequipped')
        prompt(promptlist)
