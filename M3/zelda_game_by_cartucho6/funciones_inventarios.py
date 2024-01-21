


def calcular_max_hearts_remaining (game):
    max_hearts_remaining=2
    for key, value in game["sanctuaries_opened"].items():
        if value['open'] == 1:
            max_hearts_remaining += 1
    return max_hearts_remaining







#----------------- FUNCIONES PRINTS INVENTARIOS -----------------

# FUNCION PARA GENERAR INVENTARIO MAIN
def generate_inv_main(game,max_hearts_remaining):
    un = game['player']['user_name']
    tbm = game['player']['blood_moon_countdown']
    hea = game['player']["hearts_remaining"]
    tw = ((game["weapons"]["Shield"]["total_weapons"] + game["weapons"]["Wood Shield"]["total_weapons"]
           + game["weapons"]["Sword"]["total_weapons"]) + game["weapons"]["Wood Sword"]["total_weapons"])

    tf = ((game['foods']["Fish"]["quantity_remaining"] + game['foods']["Vegetables"]["quantity_remaining"]
           + game['foods']["Meat"]["quantity_remaining"]) + game['foods']["Salads"]["quantity_remaining"]
          + game['foods']["Pescatarian"]["quantity_remaining"] + game['foods']["Roasted"]["quantity_remaining"])

    weapon_list = []
    for weapon_name, weapon_info in game["weapons"].items():
        equiped_value = weapon_info["equiped"]
        if weapon_info["equiped"] == 1:
            weapon_list.append(weapon_name)

    if len(weapon_list) == 0:
        weapon_list.append(' ')
        weapon_list.append(' ')
    elif len(weapon_list) == 1:
        weapon_list.append(' ')

    menu_inventory =  [" * * * Inventory *",
                      "                 *",
                      f" {str(un).ljust(10)}♥ {str(hea).ljust(1)}/{str(max_hearts_remaining).ljust(1)} *",
                      f" Blood moon in{str(tbm).rjust(2)} *",
                      "                 *",
                      " Equipament      *",
                      f"     {str(weapon_list[0]).rjust(11)} *",
                      f"     {str(weapon_list[1]).rjust(11)} *",
                      "                 *",
                      f" Food        {str(tf).rjust(3)} *",
                      f" Weapons     {str(tw).rjust(3)} *",
                      "                 *"]

    return menu_inventory




# FUNCION PARA GENERAR INVENTARIO FOOD
def generate_inv_food(game):
    vegetables = game['foods']['Vegetables']['quantity_remaining']
    fish = game['foods']['Fish']['quantity_remaining']
    meat = game['foods']['Meat']['quantity_remaining']
    salads = game['foods']['Salads']['quantity_remaining']
    pescatarian = game['foods']['Pescatarian']['quantity_remaining']
    roasted = game['foods']['Roasted']['quantity_remaining']

    menu_food = [" * * * * *  Food *",
                  "                 *",
                  "                 *",
                f" Vegetables   {str(vegetables).rjust(2)} *",
                f" Fish         {str(fish).rjust(2)} *",
                f" Meat         {str(meat).rjust(2)} *",
                 "                 *",
                f" Salads       {str(salads).rjust(2)} *",
                f" Pescatarian  {str(pescatarian).rjust(2)} *",
                f" Roasted      {str(roasted).rjust(2)} *",
                "                 *"]

    return menu_food




# FUNCION PARA GENERAR INVENTARIO WEAPONS
def generate_inv_weapons(game):
    ws = game['weapons']["Wood Sword"]["lives_remaining"]
    ws1 =game['weapons']["Wood Sword"]["total_weapons"]
    if game['weapons']["Wood Sword"]["equiped"] == 1:
        ws2 = "(equiped)"
    else:
        ws2 =""


    sw = game['weapons']["Sword"]["lives_remaining"]
    sw1 =game['weapons']["Sword"]["total_weapons"]
    if game['weapons']["Sword"]["equiped"] == 1:
        sw2 = "(equiped)"
    else:
        sw2 =""


    w = game['weapons']["Wood Shield"]["lives_remaining"]
    w1 =game['weapons']["Wood Shield"]["total_weapons"]
    if game['weapons']["Wood Shield"]["equiped"] == 1:
        w2 = "(equiped)"
    else:
        w2 =""


    sh = game['weapons']["Shield"]["lives_remaining"]
    sh1 =game['weapons']["Shield"]["total_weapons"]
    if game['weapons']["Shield"]["equiped"] == 1:
        sh2 = "(equiped)"
    else:
        sh2 =""

    menu_weapons = [" * * * * Weapons *",
                    "                 *",
                    "                 *",
                    f" Wood Sword {str(ws).rjust(2)}/{str(ws1).rjust(1)} *",
                    f" {str(ws2).ljust(10)}      *",
                    f" Sword      {str(sw).rjust(2)}/{str(sw1).rjust(1)} *",
                    f" {str(sw2).ljust(10)}      *",
                    f" Wood Shield{str(w).rjust(2)}/{str(w1).rjust(1)} *",
                    f" {str(w2).ljust(10)}      *",
                    f" Shield     {str(sh).rjust(2)}/{str(sh1).rjust(1)} *",
                    f" {str(sh2).ljust(10)}      *"]


    return menu_weapons





# FUNCION CAMBIO ARMAS
def cambio_weapon(pregunta,game,promptlist):

    if pregunta.lower() == "equip the sword":
        if game['weapons']["Wood Sword"]["equiped"] == 1:
            game['weapons']["Sword"]["equiped"] = 0
            promptlist.append('You cannot equip two swords')
        elif game['weapons']["Sword"]["equiped"] == 1:
            promptlist.append('You already have Sword equiped')
        else:
            if game['weapons']["Sword"]["total_weapons"] == 0:
                game['weapons']["Sword"]["equiped"] = 0
                promptlist.append("You don't have Sword")
            else:
                game['weapons']["Sword"]["equiped"] = 1
                promptlist.append("Sword equiped")
    elif pregunta.lower() == "equip the wood shield":
        if game['weapons']["Shield"]["equiped"] == 1:
            game['weapons']["Wood Shield"]["equiped"] = 0
            promptlist.append("You cannot equip two shields")
        elif game['weapons']["Wood Shield"]["equiped"] == 1:
            promptlist.append('You already have Wood Shield equiped')
        else:
            if game['weapons']["Wood Shield"]["total_weapons"] == 0:
                game['weapons']["Wood Shield"]["equiped"] = 0
                promptlist.append("You don't have Sword")
            else:
                game['weapons']["Wood Shield"]["equiped"] = 1
                promptlist.append("Wood shield equiped")
    elif pregunta.lower() == "equip the wood sword":
        if game['weapons']["Sword"]["equiped"] == 1:
            game['weapons']["Wood Sword"]["equiped"] = 0
            promptlist.append('You cannot equip two swords')
        elif game['weapons']["Wood Sword"]["equiped"] == 1:
            promptlist.append('You already have Wood Sword equiped')
        else:
            if game['weapons']["Wood Sword"]["total_weapons"] == 0:
                game['weapons']["Wood Sword"]["equiped"] = 0
                promptlist.append("You don't have Sword")
            else:
                game['weapons']["Wood Sword"]["equiped"] = 1
                promptlist.append("Wood Sword equiped")
    elif pregunta.lower() == "equip the shield":
        if game['weapons']["Wood Shield"]["equiped"] == 1:
            game['weapons']["Shield"]["equiped"] = 0
            promptlist.append("You cannot equip two shields")
        elif game['weapons']["Shield"]["equiped"] == 1:
            promptlist.append('You already have Shield equiped')
        else:
            if game['weapons']["Shield"]["total_weapons"] == 0:
                game['weapons']["Shield"]["equiped"] = 0
                promptlist.append("You don't have Sword")
            else:
                game['weapons']["Shield"]["equiped"] = 1
                promptlist.append("Shield equiped")
    elif pregunta.lower() == "unequip the sword":
        game['weapons']["Sword"]["equiped"] = 0
        promptlist.append('Sword unequiped')
    elif pregunta.lower() == "unequip the wood shield":
        game['weapons']["Wood Shield"]["equiped"] = 0
        promptlist.append('Wood Shield unequiped')
    elif pregunta.lower() == "unequip the wood sword":
        game['weapons']["Wood Sword"]["equiped"] = 0
        promptlist.append('Wood Sword unequiped')
    elif pregunta.lower() == "unequip the shield":
        game['weapons']["Shield"]["equiped"] = 0
        promptlist.append('Shield unequiped')
    else:
        promptlist.append('Invalid action!')
