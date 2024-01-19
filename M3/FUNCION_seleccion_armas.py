
from armario_FUNCIONES import*

from diccionario_general import*

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

##PARA PROBAR QUE FUNCIONA LA FUNCION LLAMO LA FUNCION INVENTARIO ARMAS
while True:
    pregunta1 = 'Show inventory weapons'

    weapons(pregunta1)
    ##EQUIPAR ARMAS

######ESTA PARTE SERVIRA PARA LLAMAR FUNCION Y CRIBAR COMANDOS
    pregunta_promptlist_weapon = ["equip the sword","equip the wood shield"
        ,"equip the wood sword","equip the shield","unequip the sword"
        ,"unequip the wood shield","unequip the wood sword","unequip the shild"]
    promptlist = []
    pregunta=input()
    promptlist.append(pregunta)
    #prompt(promptlist)
    ##ATENTOS DONDE SE PONE EL PROMPT PARA NO REPETIR MENSAJES
    if pregunta in pregunta_promptlist_weapon:

        cambio_weapon(pregunta,game)
    clear_screen()





