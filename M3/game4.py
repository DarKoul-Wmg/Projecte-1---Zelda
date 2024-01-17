import os
import platform

import base_zelda
import funciones1
from funciones1 import *
from base_zelda import *
import random

#----COPIA DE DICCIONARIOS ORIGINALES PARA PLAYER----
locations=copiar_diccionario_anidado(base_zelda.locations)
data=copiar_diccionario_anidado(base_zelda.data)
#---------------------------------------!
#faltan diccionarios "Weapons", "Food", "Game"
#falta que datos sea modificado con las tablas "Enemies", "Sanctuaries", "Chests"
#---------------------------------------!


#Cosas que debe coger del diccionario de GAME
actual_location='hyrule'
bm_countdown=25
bm_appearances=0
promptlist=["hola"]



#----- PRINTS PARA RESTAURAR LOCATION según data del player -----
#-- Busca donde esta el "!" para posicionar ahi al player
playerY, playerX=funciones1.buscar_exclamacion(locations, actual_location)
#pone al player en la location "!"
locations[actual_location][playerY][playerX]="X"

#FOX rate visible?
promptlist.append(fox_spawn(actual_location, data))




while True:
    if bm_countdown==0:
        promptlist.append("The Blood Moon rises once again. Please be careful, Link.")
        #si el countdown llega a 0, se añade una aparición al contador de appearances
        bm_appearances+=1
        #............restaurar vida de todos los enemigos y poner en original pos
        #se restaura el contador a 25
        bm_countdown == 25

    #---- LISTA INTERACCIONES REINICIO:
    attack=True
    attack_weapon = True #............CAMBIAR SEGUN SI LLEVA ARMA
    attack_entity = False #si hay un enemigo, zorro
    attack_tree = False #si hay un arbol
    cook = False
    fish = False
    open = False


    #---- ACTUALIZACION DE LOCATIONS:
    # pone a los enemigos su vida actual
    funciones1.cambiador_vidas_numero(locations, actual_location, data)
    # quita el "?" de los santuarios ya abiertos
    sanctuaries_opened_location(locations, actual_location, data)
    # cambia los chests abiertos de M a W
    funciones1.cambiador_chests(locations, actual_location, data)
    # pone el fox en el mapa si es visible
    funciones1.cambiador_fox(locations, actual_location, data)
    #pone los respawns de los arboles, los actualiza, y le pone vida a los que han terminado su respawn
    arboles_respawn(locations, actual_location, data)

    #---- DETECCION INTERACCIONES PARA SABER ACCIONES DISPONIBLES PARA EL PLAYER
    if attack_weapon==True and (locations[actual_location][playerY][playerX - 1] in ("E", "F") or
        locations[actual_location][playerY - 1][playerX] in ("E", "F") or
        locations[actual_location][playerY][playerX + 1] in ("E", "F") or
        locations[actual_location][playerY + 1][playerX] in ("E", "F")):
        attack_entity = True

    if (locations[actual_location][playerY][playerX - 1] == "T" or
       locations[actual_location][playerY - 1][playerX] == "T" or
       locations[actual_location][playerY][playerX + 1] == "T" or
       locations[actual_location][playerY + 1][playerX] == "T"):
        attack_tree = True

    if (locations[actual_location][playerY][playerX - 1] == "C" or
        locations[actual_location][playerY - 1][playerX] == "C" or
        locations[actual_location][playerY][playerX + 1] == "C" or
        locations[actual_location][playerY + 1][playerX] == "C"):
        cook = True

    if (locations[actual_location][playerY][playerX - 1] == "~" or
         locations[actual_location][playerY - 1][playerX] == "~" or
         locations[actual_location][playerY][playerX + 1] == "~" or
         locations[actual_location][playerY + 1][playerX] == "~"):
        fish = True

    if (locations[actual_location][playerY][playerX - 1] in ("S", "M") or
         locations[actual_location][playerY - 1][playerX] in ("S", "M") or
         locations[actual_location][playerY][playerX + 1] in ("S", "M") or
         locations[actual_location][playerY + 1][playerX] in ("S", "M")):
        open = True


    # ---- PRINTS MAPA ----
    #con todo lo que se ha cambiado en el mapa en actualizacion de locations, inventario se imprime pantalla
    #Prints mapa (.............falta sumar inventario)
    for y in range(len(locations[actual_location])):
        for x in range(len(locations[actual_location][0])):
            print((locations[actual_location][y][x]), end="")
        print()

    #Print línea de acciones
    print(actions(cook,fish,open))

    prompt(promptlist)




    #----------------------------------------------------
    #------------- INICIO INTERACCION -------------------
    pregunta= input("What to do now?")
    pregunta=pregunta.lower()
    promptlist.append(pregunta)
    # ----------------------------------------------------
    # ----------------------------------------------------

    #---- CAMBIO DE LOCATION ----
    if pregunta[0:5]== 'go to':
        if pregunta.replace('go to ', "")=='hyrule' and actual_location in ('death_mountain', 'castle', 'gerudo'):
            #donde antes estaba la X lo deja en blanco
            locations[actual_location][playerY][playerX] = " "
            #cambia la actual_location
            actual_location='hyrule'
            #en la nueva location se busca el "!" y se pone al player en ese lugar
            playerY, playerX = funciones1.buscar_exclamacion(locations, actual_location)
            locations[actual_location][playerY][playerX]="X"

            promptlist.append("You are now in Hyrule.")
            #se calcula el rate de spawn del fox
            promptlist.append(fox_spawn(actual_location, data))

        elif pregunta.replace('go to ', "")=='death mountain'and actual_location in ('hyrule', 'castle', 'necluda'):
            locations[actual_location][playerY][playerX] = " "
            actual_location='death_mountain'
            playerY, playerX = funciones1.buscar_exclamacion(locations, actual_location)
            locations[actual_location][playerY][playerX]="X"

            promptlist.append("You are now in Death Mountain.")
            promptlist.append(fox_spawn(actual_location, data))

        elif pregunta.replace('go to ', "")=='gerudo'and actual_location in ('hyrule', 'castle', 'necluda'):
            locations[actual_location][playerY][playerX] = " "
            actual_location='gerudo'
            playerY, playerX = funciones1.buscar_exclamacion(locations, actual_location)
            locations[actual_location][playerY][playerX]="X"

            promptlist.append("You are now in Gerudo.")
            promptlist.append(fox_spawn(actual_location, data))

        elif pregunta.replace('go to ', "")=='necluda'and actual_location in ('death_mountain', 'castle', 'gerudo'):
            locations[actual_location][playerY][playerX] = " "
            actual_location='necluda'
            playerY, playerX = funciones1.buscar_exclamacion(locations, actual_location)
            locations[actual_location][playerY][playerX]="X"

            promptlist.append("You are now in Necluda.")
            promptlist.append(fox_spawn(actual_location, data))

        else:
            respuesta="You can't go to " + (pregunta.replace('go to ', "")).title() + " from here."
            promptlist.append(respuesta)

    #----- MOVIMIENTO -----
    elif pregunta[:-2] in ('go right ', 'go left ', 'go up ', 'go down ','go right', 'go left', 'go up', 'go down'):
        cantidad = int(pregunta[-2:])
        #se pone en blanco el sitio donde antes estaba
        locations[actual_location][playerY][playerX] = " "

        #------ DERECHA
        if ("go right") in pregunta:
            for i in range(cantidad):
                playerX+=1
                if locations[actual_location][playerY][playerX]!=" ":
                    playerX-=1
                    break
                else:
                    continue

        #---- IZQUIERDA
        elif ("go left") in pregunta:
            for i in range(cantidad):
                playerX-=1
                if locations[actual_location][playerY][playerX]!=" ":
                    playerX+=1
                    break
                else:
                    continue

        #---- ARRIBA
        elif ("go up") in pregunta:
            for i in range(cantidad):
                playerY-=1
                if locations[actual_location][playerY][playerX]!=" " or playerY==0:
                    playerY+=1
                    break
                else:
                    continue

        #---- ABAJO
        elif ("go down") in pregunta:
            for i in range(cantidad):
                playerY+=1
                if locations[actual_location][playerY][playerX]!=" " or playerY==11:
                    playerY-=1
                    break
                else:
                    continue

        #se pone la X en su nueva coordenada
        locations[actual_location][playerY][playerX] = "X"


    #------------------ ATTACK ------------------:

    #---- ATTACK hierba ----
    elif pregunta=="attack" and attack_weapon==True and attack_entity==False and attack_tree==False:
        #se calcula el drop de la hierba
        promptlist.append(attack_grass())
        #...............falta que se añada 1 meat al inventario

    #---- ATTACK tree a puños
    elif pregunta=="attack" and attack_weapon==False and attack_tree==True:
        #se calcula el drop del arbol
        promptlist.append(attack_tree_weaponless())
        #.............falta que se añade lo que cae al inventario


    #---- ATTACK tree a espada
    elif pregunta=="attack" and attack_weapon==True and attack_tree==True:

        # si tree en DERECHA:
        if locations[actual_location][playerY][playerX + 1]=="T":
            # busca cual es el id del tree a la derecha del player
            for tree_key in data[actual_location]["trees"].keys():
                if data[actual_location]["trees"][tree_key]["ypos"] == playerY and data[actual_location]["trees"][tree_key]["xpos"] == playerX + 1:
                    # quitamos 1 corazon al tree
                    data[actual_location]["trees"][tree_key]["hearts"] -= 1
                    #si dejamos el arbol a 0 de vida, entonces se pone una cuenta atrás de 9 para respawn
                    if data[actual_location]["trees"][tree_key]["hearts"]==0:
                        data[actual_location]["trees"][tree_key]["respawn"]=10
                    promptlist.append(attack_tree_weapon())
                    # ...........falta que se añade lo que cae al inventario
                    #............falta quitar 1 uso a la espada

        # si tree en ARRIBA:
        elif locations[actual_location][playerY - 1][playerX]=="T":
            # busca cual es el id del tree a la derecha del player
            for tree_key in data[actual_location]["trees"].keys():
                if data[actual_location]["trees"][tree_key]["ypos"] == playerY - 1 and data[actual_location]["trees"][tree_key]["xpos"] == playerX:
                    # quitamos 1 corazon al tree
                    data[actual_location]["trees"][tree_key]["hearts"] -= 1
                    #si dejamos el arbol a 0 de vida, entonces se pone una cuenta atrás de 9 para respawn
                    if data[actual_location]["trees"][tree_key]["hearts"]==0:
                        data[actual_location]["trees"][tree_key]["respawn"]=10
                    promptlist.append(attack_tree_weapon())
                    # ...........falta que se añade lo que cae al inventario
                    #............falta quitar 1 uso a la espada

        # si treee en ABAJO:
        elif locations[actual_location][playerY + 1][playerX]=="T":
            # busca cual es el id del tree a la derecha del player
            for tree_key in data[actual_location]["trees"].keys():
                if data[actual_location]["trees"][tree_key]["ypos"] == playerY + 1 and data[actual_location]["trees"][tree_key]["xpos"] == playerX:
                    # quitamos 1 corazon al tree
                    data[actual_location]["trees"][tree_key]["hearts"] -= 1
                    #si dejamos el arbol a 0 de vida, entonces se pone una cuenta atrás de 9 para respawn
                    if data[actual_location]["trees"][tree_key]["hearts"]==0:
                        data[actual_location]["trees"][tree_key]["respawn"]=10
                    promptlist.append(attack_tree_weapon())
                    # ...........falta que se añade lo que cae al inventario
                    #............falta quitar 1 uso a la espada

        # si tree en DERECHA:
        elif locations[actual_location][playerY][playerX - 1] =="T":
            # busca cual es el id del tree a la derecha del player
            for tree_key in data[actual_location]["trees"].keys():
                if data[actual_location]["trees"][tree_key]["ypos"] == playerY and data[actual_location]["trees"][tree_key]["xpos"] == playerX - 1:
                    # quitamos 1 corazon al tree
                    data[actual_location]["trees"][tree_key]["hearts"] -= 1
                    #si dejamos el arbol a 0 de vida, entonces se pone una cuenta atrás de 9 para respawn
                    if data[actual_location]["trees"][tree_key]["hearts"]==0:
                        data[actual_location]["trees"][tree_key]["respawn"]=10
                    promptlist.append(attack_tree_weapon())
                    # ...........falta que se añade lo que cae al inventario
                    #............falta quitar 1 uso a la espada


    #---- ATTACK entidades con espada
    elif pregunta=="attack" and attack_weapon==True and attack_entity == True:
        #si enemy/fox/tree en DERECHA:
        if locations[actual_location][playerY][playerX + 1] in ("E", "F"):
            if locations[actual_location][playerY][playerX + 1]=="E":
                #busca cual es el id del enemigo a la derecha del player
                for enemy_key in data[actual_location]["enemies"].keys():
                    if data[actual_location]["enemies"][enemy_key]["ypos"] == playerY and data[actual_location]["enemies"][enemy_key]["xpos"] == playerX + 1:
                        #quitamos 1 corazon al enemigo
                        data[actual_location]["enemies"][enemy_key]["hearts"] -= 1
                        # ............falta quitar 1 uso a la espada

            elif locations[actual_location][playerY][playerX + 1]=="F":
                #quitamos 1 corazon al fox
                data[actual_location]["fox"]["hearts"]-=1
                promptlist.append("You got meat.")
                #............añadir al inventario 1 meat
                # ............falta quitar 1 uso a la espada

        # si enemy/fox/tree en ARRIBA:
        if locations[actual_location][playerY - 1][playerX] in ("E", "F"):
            if locations[actual_location][playerY - 1][playerX] == "E":
                # busca cual es el id del enemigo a la derecha del player
                for enemy_key in data[actual_location]["enemies"].keys():
                    if data[actual_location]["enemies"][enemy_key]["ypos"] == playerY-1 and data[actual_location]["enemies"][enemy_key]["xpos"] == playerX:
                        # quitamos 1 corazon al enemigo
                        data[actual_location]["enemies"][enemy_key]["hearts"] -= 1
                        # ............falta quitar 1 uso a la espada

            elif locations[actual_location][playerY - 1][playerX] == "F":
                # quitamos 1 corazon al fox
                data[actual_location]["fox"]["hearts"] -= 1
                promptlist.append("You got meat.")
                #......................añadir al inventario 1 meat
                # ............falta quitar 1 uso a la espada

        # si enemy/fox/tree en ABAJO:
        if locations[actual_location][playerY + 1][playerX] in ("E", "F"):
            if locations[actual_location][playerY + 1][playerX] == "E":
                # busca cual es el id del enemigo a la derecha del player
                for enemy_key in data[actual_location]["enemies"].keys():
                    if data[actual_location]["enemies"][enemy_key]["ypos"] == playerY + 1 and data[actual_location]["enemies"][enemy_key]["xpos"] == playerX:
                        # quitamos 1 corazon al enemigo
                        data[actual_location]["enemies"][enemy_key]["hearts"] -= 1
                        # ............falta quitar 1 uso a la espada

            elif locations[actual_location][playerY + 1][playerX] == "F":
                # quitamos 1 corazon al fox
                data[actual_location]["fox"]["hearts"] -= 1
                promptlist.append("You got meat.")
                # ...........añadir al inventario 1 meat
                # ............falta quitar 1 uso a la espada

        # si enemy/fox/tree en DERECHA:
        if locations[actual_location][playerY][playerX - 1] in ("F"):
            # quitamos 1 corazon al fox
            data[actual_location]["fox"]["hearts"] -= 1
            promptlist.append("You got meat.")
            # ...........añadir al inventario 1 meat
            # ............falta quitar 1 uso a la espada


    #---- COOK
    elif pregunta=="cook" and cook==True:
        print("we cookin")
        #...................comandos de cook y sus cambios de food_inventory

    #---- FISH
    elif pregunta=="fish" and fish==True:
        promptlist.append(fishing())
        #................ añadir 1 fish al inventario
        #................. hacer que solo se pueda obtener pez 1 vez

    #---- OPEN
    elif pregunta=="open" and open==True:

        # si sanctuary/chest en DERECHA:
        if locations[actual_location][playerY][playerX + 1] in ("S", "M"):
            if locations[actual_location][playerY][playerX + 1] == "S":
                # busca cual es el id del santuario a la derecha del player
                for sanctuary_key in data[actual_location]["sanctuaries"].keys():
                    if data[actual_location]["sanctuaries"][sanctuary_key]["ypos"] == playerY and data[actual_location]["sanctuaries"][sanctuary_key]["xpos"] == playerX + 1:
                        # cambiamos a abierto el santuario
                        data[actual_location]["sanctuaries"][sanctuary_key]["open"] = True
                        promptlist.append("You opened the sanctuary, your maximum health has increased by 1.")

            elif locations[actual_location][playerY][playerX + 1] == "M":
                # busca cual es el id del chest a la derecha del player
                for chest_key in data[actual_location]["chests"].keys():
                    if data[actual_location]["chests"][chest_key]["ypos"] == playerY and data[actual_location]["chests"][chest_key]["xpos"] == playerX + 1:
                        # cambiamos a abierto el chest
                        data[actual_location]["chests"][chest_key]["open"] = True

        # si sanctuary/chest en ARRIBA:
        if locations[actual_location][playerY-1][playerX] in ("S", "M"):
            if locations[actual_location][playerY-1][playerX] == "S":
                # busca cual es el id del santuario a la derecha del player
                for sanctuary_key in data[actual_location]["sanctuaries"].keys():
                    if data[actual_location]["sanctuaries"][sanctuary_key]["ypos"] == playerY-1 and data[actual_location]["sanctuaries"][sanctuary_key]["xpos"] == playerX:
                        # cambiamos a abierto el santuario
                        data[actual_location]["sanctuaries"][sanctuary_key]["open"] = True
                        promptlist.append("You opened the sanctuary, your maximum health has increased by 1.")

            elif locations[actual_location][playerY-1][playerX] == "M":
                # busca cual es el id del chest a la derecha del player
                for chest_key in data[actual_location]["chests"].keys():
                    if data[actual_location]["chests"][chest_key]["ypos"] == playerY-1 and data[actual_location]["chests"][chest_key]["xpos"] == playerX:
                        # cambiamos a abierto el chest
                        data[actual_location]["chests"][chest_key]["open"] = True

        # si sanctuary/chest en ABAJO:
        if locations[actual_location][playerY+1][playerX] in ("S", "M"):
            if locations[actual_location][playerY+1][playerX] == "S":
                # busca cual es el id del santuario a la derecha del player
                for sanctuary_key in data[actual_location]["sanctuaries"].keys():
                    if data[actual_location]["sanctuaries"][sanctuary_key]["ypos"] == playerY+1 and data[actual_location]["sanctuaries"][sanctuary_key]["xpos"] == playerX:
                        # cambiamos a abierto el santuario
                        data[actual_location]["sanctuaries"][sanctuary_key]["open"] = True
                        promptlist.append("You opened the sanctuary, your maximum health has increased by 1.")

            elif locations[actual_location][playerY+1][playerX] == "M":
                # busca cual es el id del chest a la derecha del player
                for chest_key in data[actual_location]["chests"].keys():
                    if data[actual_location]["chests"][chest_key]["ypos"] == playerY+1 and data[actual_location]["chests"][chest_key]["xpos"] == playerX:
                        # cambiamos a abierto el chest
                        data[actual_location]["chests"][chest_key]["open"] = True

        # si chest en IZQUIERDA:
        if locations[actual_location][playerY][playerX - 1] == "M":
            # busca cual es el id del chest a la derecha del player
            for chest_key in data[actual_location]["chests"].keys():
                if data[actual_location]["chests"][chest_key]["ypos"] == playerY and data[actual_location]["chests"][chest_key]["xpos"] == playerX - 1:
                    # cambiamos a abierto el chest
                    data[actual_location]["chests"][chest_key]["open"] = True


    # ---- NO VALIDA
    else:
        #cualquier otra cosa no recogida anteriormente es inválida
        promptlist.append("Invalid action!")

    #al final del turno, quitamos 1 de la cuenta atrás de blood moons
    bm_countdown -= 1

