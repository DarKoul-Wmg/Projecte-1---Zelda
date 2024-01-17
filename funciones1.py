import random
import os
import platform

#---- FUNCIONES DICCIONARIOS COPIA ----
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


#---- FUNCIONES PARA MODIFICAR LOCATIONS ----
def buscar_exclamacion(locations,actual_location):
    global playerY, playerX
    #busca por toda la matriz de locations en qué lugar está la "!" para copiar esa coordenada para el diccionario del jugador
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
    #por cada enemigo en enemigos de la location actual
    for enemy_key in data[actual_location]["enemies"].keys():
        #si los corazones son mayores que 0, en locations, a su derecha poner la cantidad de corazones
        if data[actual_location]["enemies"][enemy_key]['hearts']>0:
            locations[actual_location][data[actual_location]["enemies"][enemy_key]['ypos']][data[actual_location]["enemies"][enemy_key]['xpos']+1]=str(data[actual_location]["enemies"][enemy_key]['hearts'])
        #si los corazones son 0, en la location, printear un espacio en blanco donde antes iba "E", printear espacio en blanco donde antes iba su vida
        elif data[actual_location]["enemies"][enemy_key]['hearts']==0:
            locations[actual_location][data[actual_location]["enemies"][enemy_key]['ypos']][data[actual_location]["enemies"][enemy_key]['xpos']] = " "
            locations[actual_location][data[actual_location]["enemies"][enemy_key]['ypos']][data[actual_location]["enemies"][enemy_key]['xpos'] + 1] = " "


def cambiador_chests(locations,actual_location, data):
    #por cada chest en chests de la location actual
    for chest_key in data[actual_location]["chests"].keys():
        #si está cerrado se pone M en su coordenada en locations
        if data[actual_location]["chests"][chest_key]['open']==False:
            locations[actual_location][data[actual_location]["chests"][chest_key]['ypos']][data[actual_location]["chests"][chest_key]['xpos']]="M"
        #si està abierto se pone W en su coordenada en locations
        elif data[actual_location]["chests"][chest_key]['open'] == True:
            locations[actual_location][data[actual_location]["chests"][chest_key]['ypos']][
                data[actual_location]["chests"][chest_key]['xpos']] = "W"

def cambiador_fox(locations,actual_location, data):
    #si la vida del fox es 1, se pone F en su coordenada en locations
    if data[actual_location]["fox"]['hearts']==1:
            locations[actual_location][data[actual_location]["fox"]['ypos']][data[actual_location]["fox"]['xpos']]="F"
    #si la vida del fox es 0, se pone espacio en blanco en su coordenada en locations
    elif data[actual_location]["fox"]['hearts']==0:
            locations[actual_location][data[actual_location]["fox"]['ypos']][data[actual_location]["fox"]['xpos']]=" "

def sanctuaries_opened_location(locations, actual_location, data):
    #por cada santuario en santuarios de location actual
    for sanct_key in data[actual_location]["sanctuaries"].keys():
        #si santuario está abierto, en su location poner a dos más a su derecha un espacio en blanco para quitar "?"
        if data[actual_location]["sanctuaries"][sanct_key]['open']==True:
            locations[actual_location][data[actual_location]["sanctuaries"][sanct_key]['ypos']][data[actual_location]["sanctuaries"][sanct_key]['xpos']+2]=" "
        #si santuario está cerrado, en su location poner dos más a su derecha un "?"
        elif data[actual_location]["sanctuaries"][sanct_key]['open'] == False:
            locations[actual_location][data[actual_location]["sanctuaries"][sanct_key]['ypos']][data[actual_location]["sanctuaries"][sanct_key]['xpos']+2] = "?"



def arboles_respawn(locations, actual_location, data):
    # por cada tree en trees de location actual
    for tree_key in data[actual_location]["trees"].keys():
        # si tree no tiene vida
        if data[actual_location]["trees"][tree_key]['hearts'] == 0:
            #si le queda más de 1 para hacer respawn
            if data[actual_location]['trees'][tree_key]['respawn']>1:
                #se le resta 1 al respawn
                data[actual_location]['trees'][tree_key]['respawn']-=1
                #se pone en la location, el numero que le queda de respawn en su lugar
                locations[actual_location][data[actual_location]["trees"][tree_key]['ypos']][data[actual_location]["trees"][tree_key]['xpos']] = f"{data[actual_location]['trees'][tree_key]['respawn']}"

            #si le queda 1 para hacer respawn
            elif data[actual_location]['trees'][tree_key]['respawn']==1:
                 #se pone respawn a 0
                 data[actual_location]['trees'][tree_key]['respawn']=0
                 #se pone vida a 4
                 data[actual_location]['trees'][tree_key]['hearts']=4
                 #vuelve a poner una "T" en su sitio
                 locations[actual_location][data[actual_location]["trees"][tree_key]['ypos']][data[actual_location]["trees"][tree_key]['xpos']] = "T"




#---- FUNCIONES DE ACCIONES ----
def attack_grass(): #RATE DE ATACAR A LA HIERBA
    resultado = "You got nothing."
    if random.randrange(10) <= 0:
        resultado = "You got a Lizard!"
    return resultado

def attack_tree_weapon(): #RATE DE ATACAR UN ÁRBOL CON ESPADA
    print("CON ESPADA")
    resultado = "The tree didn't give you anything."
    rate = random.randrange(10)
    num_apple = [0,1,2,3]
    if rate in num_apple:#40%
        resultado = "You got an apple!"
    else:
        if rate == 4 or rate == 5:#20%
            resultado =  "You got a Wood sword!"
        elif rate == 6 or rate == 7:#20%
            resultado ="You got a Wood shield!"
    return resultado

def attack_tree_weaponless(): #RATE DE ATACAR UN ÁRBOL A PUÑOS
    print("SIN ESPADA")
    resultado="The tree didn't give you anything."
    rate = random.randrange(10)
    num = [1,2,3,4]
    if rate == 0: #10%
        if random.randrange(10) %2 == 0:
            resultado = "You got a Wood sword!"
        else:
            resultado = "You got a Wood shield!"
    elif rate in num: #40%
        resultado = "You got an apple!"
    return resultado

def fishing(): #RATE DE PESCAR
    resultado = "You didn't get a fish."
    rate = random.randrange(10)
    if rate == 0 or rate == 9:
        resultado = "You got a fish!"
    return resultado





#---- OTRAS FUNCIONES ----
def fox_spawn(actual_location, data): #RATE DE SPAWNEO DEL ZORRO
    resultado = "You don't see a Fox."
    spawn = random.randrange(10)
    if spawn %2 == 0:
        resultado = "You see a Fox."
        data[actual_location]["fox"]['hearts'] = 1
    else:
        data[actual_location]["fox"]['hearts']=0
    return resultado

def actions(cook,fish,open): #MONTA LA LÍNEA DE ACCIONES
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
