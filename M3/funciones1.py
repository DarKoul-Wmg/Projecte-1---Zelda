import random


def copiar_diccionario_anidado(diccionario):
    nuevo_diccionario = {}
    for clave, valor in diccionario.items():
        if isinstance(valor, dict):
            # Si el valor es un diccionario, realizar una copia recursiva
            nuevo_diccionario[clave] = copiar_diccionario_anidado(valor)
        else:
            # Si el valor no es un diccionario, simplemente copiar
            nuevo_diccionario[clave] = valor
    return nuevo_diccionario



def buscar_exclamacion(locations,actual_location):
    global playerY, playerX
    for y in range(len(locations[actual_location])):
        for x in range(len(locations[actual_location][y])):
            if locations[actual_location][y][x] == "!":
                playerY = y
                playerX = x
                break
            else:
                continue
    return playerY, playerX

def cambiador_vidas_numero(locations, actual_location, data):
    for enemy_key in data[actual_location]["enemies"].keys():
        if data[actual_location]["enemies"][enemy_key]['hearts']>0:
            locations[actual_location][data[actual_location]["enemies"][enemy_key]['ypos']][data[actual_location]["enemies"][enemy_key]['xpos']+1]=str(data[actual_location]["enemies"][enemy_key]['hearts'])
        elif data[actual_location]["enemies"][enemy_key]['hearts']==0:
            locations[actual_location][data[actual_location]["enemies"][enemy_key]['ypos']][data[actual_location]["enemies"][enemy_key]['xpos']] = " "
            locations[actual_location][data[actual_location]["enemies"][enemy_key]['ypos']][data[actual_location]["enemies"][enemy_key]['xpos'] + 1] = " "


def cambiador_chests(locations,actual_location, data):
    for chest_key in data[actual_location]["chests"].keys():
        if data[actual_location]["chests"][chest_key]['open']==False:
            locations[actual_location][data[actual_location]["chests"][chest_key]['ypos']][data[actual_location]["chests"][chest_key]['xpos']]="M"
        elif data[actual_location]["chests"][chest_key]['open'] == True:
            locations[actual_location][data[actual_location]["chests"][chest_key]['ypos']][
                data[actual_location]["chests"][chest_key]['xpos']] = "W"

def cambiador_fox(locations,actual_location, data):
    if data[actual_location]["fox"]['hearts']==1:
            locations[actual_location][data[actual_location]["fox"]['ypos']][data[actual_location]["fox"]['xpos']]="F"
    elif data[actual_location]["fox"]['hearts']==0:
            locations[actual_location][data[actual_location]["fox"]['ypos']][data[actual_location]["fox"]['xpos']]=" "



def attack_grass(): #RATE DE ATACAR A LA HIERBA
    resultado = "You got nothing"
    if random.randrange(10) <= 0:
        resultado = "You got a Lizard!"
    return resultado


def attack_tree_weapon():
    print("CON ESPADA")
    resultado = "The tree didn't give you anything"
    rate = random.randrange(10)
    num_apple = [0,1,2,3]
    if rate in num_apple:#40%
        resultado = "You got an apple"
    else:
        if rate == 4 or rate == 5:#20%
            resultado =  "You got a Wood sword"
        elif rate == 6 or rate == 7:#20%
            resultado ="You got a Wood shield"
    return resultado

def attack_tree_weaponless():
    print("SIN ESPADA")
    resultado="The tree didn't give you anything"
    rate = random.randrange(10)
    num = [1,2,3,4]
    if rate == 0: #10%
        if random.randrange(10) %2 == 0:
            resultado = "You got a Wood sword"
        else:
            resultado = "You got a Wood shield"
    elif rate in num: #40%
        resultado = "You got an apple"
    return resultado


def fishing():
    resultado = "You didn't get a fish"
    rate = random.randrange(10)
    if rate == 0 or rate == 9:
        resultado = "You got a fish"
    return resultado

def fox_spawn(actual_location, data):
    resultado = "You don't see a Fox"
    spawn = random.randrange(10)
    if spawn %2 == 0:
        resultado = "You see a Fox"
        data[actual_location]["fox"]['hearts'] = 1
    else:
        data[actual_location]["fox"]['hearts']=0
    return resultado


def sanctuaries_opened_location(locations, actual_location, data):
    for sanct_key in data[actual_location]["sanctuaries"].keys():
        if data[actual_location]["sanctuaries"][sanct_key]['open']==True:
            locations[actual_location][data[actual_location]["sanctuaries"][sanct_key]['ypos']][data[actual_location]["sanctuaries"][sanct_key]['xpos']+2]=" "
        elif data[actual_location]["sanctuaries"][sanct_key]['open'] == False:
            locations[actual_location][data[actual_location]["sanctuaries"][sanct_key]['ypos']][data[actual_location]["sanctuaries"][sanct_key]['xpos']+2] = "?"



def actions(cook,fish,open):
    action_menu= "* Exit, Attack, Go, Equip, Unequip, Eat"
    if cook == True:
        action_menu+=", Cook"
    if fish == True:
        action_menu+=", Fish"
    if open==True:
        action_menu+=", Open"
    falta=78-len(action_menu)
    falta=int(falta/2)
    action_menu+=" *"*falta
    return action_menu
