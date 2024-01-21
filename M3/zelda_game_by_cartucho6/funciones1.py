import random
import os
import platform


#---- FUNCIONES DICCIONARIOS COPIA ----
def copiar_diccionario_anidado(diccionario):
    nuevo_diccionario = {}
    for clave, valor in diccionario.items():
        if isinstance(valor, dict):
            # Si el valor es un diccionario, realizar una copia profunda manual
            nuevo_diccionario[clave] = copiar_diccionario_anidado(valor)
        elif isinstance(valor, list):
            # Si el valor es una lista, realizar una copia profunda manual
            nuevo_diccionario[clave] = [item[:] if isinstance(item, list) else item for item in valor]
        else:
            # Si el valor no es un diccionario ni una lista, simplemente copiar
            nuevo_diccionario[clave] = valor

    return nuevo_diccionario



#---- FUNCIONES PARA MODIFICAR LOCATIONS ----
def buscar_exclamacion(locations,game):
    global playerY, playerX
    #busca por toda la matriz de locations en qué lugar está la "!" para copiar esa coordenada para el diccionario del jugador
    for y in range(len(locations[game['player']['region']])):
        for x in range(len(locations[game['player']['region']][y])):
            if locations[game['player']['region']][y][x] == "!":
                playerY = y
                playerX = x
                break
            else:
                continue
    return playerY, playerX

def cambiador_enemigos(locations, game, data):
    #por cada enemigo en enemigos de la location actual
    for enemy_key in data[game['player']['region']]['enemies'].keys():
        #si los corazones son mayores que 0, en locations, a su derecha poner la cantidad de corazones
        if data[game['player']['region']]['enemies'][enemy_key]['hearts']>0:
            locations[game['player']['region']][data[game['player']['region']]['enemies'][enemy_key]['ypos']][data[game['player']['region']]['enemies'][enemy_key]['xpos']] ="E"
            locations[game['player']['region']][data[game['player']['region']]['enemies'][enemy_key]['ypos']][data[game['player']['region']]['enemies'][enemy_key]['xpos']+1]=str(data[game['player']['region']]['enemies'][enemy_key]['hearts'])
        #si los corazones son 0, en la location, printear un espacio en blanco donde antes iba "E", printear espacio en blanco donde antes iba su vida
        elif data[game['player']['region']]['enemies'][enemy_key]['hearts']==0:
            locations[game['player']['region']][data[game['player']['region']]['enemies'][enemy_key]['ypos']][data[game['player']['region']]['enemies'][enemy_key]['xpos']] = " "
            locations[game['player']['region']][data[game['player']['region']]['enemies'][enemy_key]['ypos']][data[game['player']['region']]['enemies'][enemy_key]['xpos'] + 1] = " "


def cambiador_chests(locations,game, data):
    #por cada chest en chests de la location actual
    for chest_key in data[game['player']['region']]["chests"].keys():
        #si está cerrado se pone M en su coordenada en locations
        if data[game['player']['region']]["chests"][chest_key]['open']==False:
            locations[game['player']['region']][data[game['player']['region']]["chests"][chest_key]['ypos']][data[game['player']['region']]["chests"][chest_key]['xpos']]="M"
        #si està abierto se pone W en su coordenada en locations
        elif data[game['player']['region']]["chests"][chest_key]['open'] == True:
            locations[game['player']['region']][data[game['player']['region']]["chests"][chest_key]['ypos']][
                data[game['player']['region']]["chests"][chest_key]['xpos']] = "W"

def cambiador_fox(locations,game, data):
    #si la vida del fox es 1, se pone F en su coordenada en locations
    if data[game['player']['region']]["fox"]['hearts']==1:
            locations[game['player']['region']][data[game['player']['region']]["fox"]['ypos']][data[game['player']['region']]["fox"]['xpos']]="F"
    #si la vida del fox es 0, se pone espacio en blanco en su coordenada en locations
    elif data[game['player']['region']]["fox"]['hearts']==0:
            locations[game['player']['region']][data[game['player']['region']]["fox"]['ypos']][data[game['player']['region']]["fox"]['xpos']]=" "

def sanctuaries_opened_location(locations, game, data):
    #por cada santuario en santuarios de location actual
    for sanct_key in data[game['player']['region']]["sanctuaries"].keys():
        #si santuario está abierto, en su location poner a dos más a su derecha un espacio en blanco para quitar "?"
        if data[game['player']['region']]["sanctuaries"][sanct_key]['open']==True:
            locations[game['player']['region']][data[game['player']['region']]["sanctuaries"][sanct_key]['ypos']][data[game['player']['region']]["sanctuaries"][sanct_key]['xpos']+2]=" "
        #si santuario está cerrado, en su location poner dos más a su derecha un "?"
        elif data[game['player']['region']]["sanctuaries"][sanct_key]['open'] == False:
            locations[game['player']['region']][data[game['player']['region']]["sanctuaries"][sanct_key]['ypos']][data[game['player']['region']]["sanctuaries"][sanct_key]['xpos']+2] = "?"



def arboles_respawn(locations, game, data):
    # por cada tree en trees de location actual
    for tree_key in data[game['player']['region']]["trees"].keys():
        # si tree no tiene vida
        if data[game['player']['region']]["trees"][tree_key]['hearts'] == 0:
            #si le queda más de 1 para hacer respawn
            if data[game['player']['region']]['trees'][tree_key]['respawn']>1:
                #se le resta 1 al respawn
                data[game['player']['region']]['trees'][tree_key]['respawn']-=1
                #se pone en la location, el numero que le queda de respawn en su lugar
                locations[game['player']['region']][data[game['player']['region']]["trees"][tree_key]['ypos']][data[game['player']['region']]["trees"][tree_key]['xpos']] = f"{data[game['player']['region']]['trees'][tree_key]['respawn']}"

            #si le queda 1 para hacer respawn
            elif data[game['player']['region']]['trees'][tree_key]['respawn']==1:
                 #se pone respawn a 0
                 data[game['player']['region']]['trees'][tree_key]['respawn']=0
                 #se pone vida a 4
                 data[game['player']['region']]['trees'][tree_key]['hearts']=4
                 #vuelve a poner una "T" en su sitio
                 locations[game['player']['region']][data[game['player']['region']]["trees"][tree_key]['ypos']][data[game['player']['region']]["trees"][tree_key]['xpos']] = "T"

def sanctuaries_opened_map(locations, data,):
    lista_locations=[]
    for location in data.keys():
        lista_locations.append(location)
    lista_locations=lista_locations[:4]

    for location in lista_locations:
        for sanct_key in data[location]['sanctuaries'].keys():
            if data[location]['sanctuaries'][sanct_key]['open']==True:
                for y in range(len(locations['map'])):
                    for x in range(len(locations['map'][y])):
                        if locations['map'][y][x] == f"{sanct_key}":
                            locations['map'][y][x + 1] = " "






#---- OTRAS FUNCIONES ----
def fox_spawn(game, data): #RATE DE SPAWNEO DEL ZORRO
    resultado = "You don't see a Fox."
    spawn = random.randrange(10)
    if spawn %2 == 0:
        resultado = "You see a Fox."
        data[game['player']['region']]["fox"]['hearts'] = 1
    else:
        data[game['player']['region']]["fox"]['hearts']=0
    return resultado

def actions(cook, fish, open,attack_weapon,attack_tree,attack_entity): #MONTA LA LÍNEA DE ACCIONES
    action_menu= "* Exit, Go, Equip, Unequip, Eat"
    if attack_entity==True or attack_tree==True or attack_weapon==True:
        action_menu+=", Attack"
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

def revivir_enemigos(game, data):
    for enemy_key in data[game['player']['region']]['enemies'].keys():
        #si los corazones son mayores que 0, en locations, a su derecha poner la cantidad de corazones
        data[game['player']['region']]['enemies'][enemy_key]['hearts']=4



#------------------------------ FUNCIONES ALGORITMO ------------------------------

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






#------------------------------ FUNCIONES CASTLE ------------------------------
def ganon_hearts_start(ganon_hearts, locations, game):
    for i in range(ganon_hearts):
        locations[game['player']['region']][2][56 - i] = "♥"

def ganon_hearts_change(ganon_hearts, locations, game):
    for i in range(9-ganon_hearts):
        locations[game['player']['region']][2][56-i]=" "

def actions_castle(attack_ganon,attack_tree):
    action_menu= "* Back, Go"
    if attack_ganon == True or attack_tree==True:
        action_menu+=", Attack"
    action_menu+=" "
    falta=78-len(action_menu)
    falta=int(falta/2)
    action_menu+=" *"*falta
    return action_menu

def ganon_frases_random():
    lista_ganon = ["Ganon is powerful, are you sure you can defeat him?",
                   "Ganon's strength is supernatural, Zelda fought with bravery.",
                   "To Ganon you are like a fly, find a weak spot and attack.",
                   "Ganon will not easily surrender.",
                   "Link, transform your fears into strengths.",
                   "Keep it up, Link, Ganon can't hold out much longer.",
                   "Link, history repeats itself, Ganon can be defeated.",
                   "Think of all the warriors who have tried before.",
                   "You fight for the weaker ones, Link, persevere."]
    numero= random.randint(0,8)
    return lista_ganon[numero]





#------------------------------ FUNCIONES MOVIMIENTO ENEMIGOS ------------------------------
def movimiento_enemy(data,locations,enemy_key,enemyY,enemyX,game):
    locations[game['player']['region']][enemyY][enemyX]=" "
    locations[game['player']['region']][enemyY][enemyX+1]= " "

    #arriba
    if locations[game['player']['region']][enemyY-1][enemyX]==" ":
        data[game['player']['region']]["enemies"][enemy_key]["ypos"]-=1
    #abajo
    elif locations[game['player']['region']][enemyY+1][enemyX]==" ":
        data[game['player']['region']]["enemies"][enemy_key]["ypos"] += 1



