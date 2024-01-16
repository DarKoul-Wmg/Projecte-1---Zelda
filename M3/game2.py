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


actual_location='hyrule'
bm_countdown=25


#----- PRINTS PARA RESTAURAR LOCATION según data del player -----
#-- Busca donde esta el "!" para posicionar ahi al player
playerY, playerX=funciones1.buscar_exclamacion(locations, actual_location)
#pone al player en la location "!"
locations[actual_location][playerY][playerX]="X"
#pone a los enemigos su vida actual
funciones1.cambiador_vidas_numero(locations, actual_location, data)
#santuarios abiertos
sanctuaries_opened_location(locations, actual_location, data)
#chests abiertos
funciones1.cambiador_chests(locations,actual_location, data)
#FOX visible?
prompt = fox_spawn(actual_location, data)
print(prompt)
funciones1.cambiador_fox(locations,actual_location, data)




while True:
    # LISTA INTERACCIONES:
    attack=True
    attack_weapon = True #CAMBIAR SEGUN SI LLEVA ARMA
    attack_entity = False #si hay un enemigo, zorro
    attack_tree = False #si hay un arbol
    cook = False
    fish = False
    open = False

    #DETECCION INTERACCIONES PARA SABER ACCIONES DISPONIBLES PARA EL INPUT
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
    funciones1.cambiador_vidas_numero(locations, actual_location, data)
    funciones1.cambiador_chests(locations, actual_location, data)
    funciones1.cambiador_fox(locations, actual_location, data)
    sanctuaries_opened_location(locations, actual_location, data)

    for y in range(len(locations[actual_location])):
        for x in range(len(locations[actual_location][0])):
            print((locations[actual_location][y][x]), end="")
        print()



    print(actions(cook,fish,open))
    #----------------------------------------------------
    #------------- INICIO INTERACCION -------------------
    pregunta= input("What to do now?")
    pregunta=pregunta.lower()
    # ----------------------------------------------------
    # ----------------------------------------------------

    #---- CAMBIO DE LOCATION ----
    if pregunta[0:5]== 'go to':
        if pregunta.replace('go to ', "")=='hyrule' and actual_location in ('death_mountain', 'castle', 'gerudo'):
            locations[actual_location][playerY][playerX] = " "
            actual_location='hyrule'
            playerY, playerX = funciones1.buscar_exclamacion(locations, actual_location)
            locations[actual_location][playerY][playerX]="X"

            prompt = fox_spawn(actual_location, data)
            print(prompt)
            funciones1.cambiador_fox(locations, actual_location, data)

        elif pregunta.replace('go to ', "")=='death mountain'and actual_location in ('hyrule', 'castle', 'necluda'):
            locations[actual_location][playerY][playerX] = " "
            actual_location='death_mountain'
            playerY, playerX = funciones1.buscar_exclamacion(locations, actual_location)
            locations[actual_location][playerY][playerX]="X"

            prompt = fox_spawn(actual_location, data)
            print(prompt)
            funciones1.cambiador_fox(locations, actual_location, data)

        elif pregunta.replace('go to ', "")=='gerudo'and actual_location in ('hyrule', 'castle', 'necluda'):
            locations[actual_location][playerY][playerX] = " "
            actual_location='gerudo'
            playerY, playerX = funciones1.buscar_exclamacion(locations, actual_location)
            locations[actual_location][playerY][playerX]="X"

            prompt = fox_spawn(actual_location, data)
            print(prompt)
            funciones1.cambiador_fox(locations, actual_location, data)

        elif pregunta.replace('go to ', "")=='necluda'and actual_location in ('death_mountain', 'castle', 'gerudo'):
            locations[actual_location][playerY][playerX] = " "
            actual_location='necluda'
            playerY, playerX = funciones1.buscar_exclamacion(locations, actual_location)
            locations[actual_location][playerY][playerX]="X"

            prompt = fox_spawn(actual_location, data)
            print(prompt)
            funciones1.cambiador_fox(locations, actual_location, data)

        else:
            print("You can't go to",(pregunta.replace('go to ', "")).title())


    #----- MOVIMIENTO -----
    elif pregunta[:-2] in ('go right ', 'go left ', 'go up ', 'go down ','go right', 'go left', 'go up', 'go down'):
        cantidad = int(pregunta[-2:])
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

        locations[actual_location][playerY][playerX] = "X"


    #------------------ ATTACK ------------------:

    #---- ATTACK hierba ----
    elif pregunta=="attack" and attack_weapon==True and attack_entity==False and attack_tree==False:
        prompt = attack_grass()
        #falta que se añada 1 meat al inventario
        print(prompt)

    #---- ATTACK tree a puños
    elif pregunta=="attack" and attack_weapon==False and attack_tree==True:
        prompt = attack_tree_weaponless()
        #falta que se añade lo que cae al inventario
        print(prompt)


    #---- ATTACK tree a espada
    elif pregunta=="attack" and attack_weapon==True and attack_tree==True:
        # si tree en DERECHA:
        if locations[actual_location][playerY][playerX + 1]=="T":
            # busca cual es el id del tree a la derecha del player
            for tree_key in data[actual_location]["trees"].keys():
                if data[actual_location]["trees"][tree_key]["ypos"] == playerY and \
                        data[actual_location]["trees"][tree_key]["xpos"] == playerX + 1:
                    print(f"Hearts iniciales del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                    # quitamos 1 corazon al tree
                    data[actual_location]["trees"][tree_key]["hearts"] -= 1
                    print(f"Hearts restantes del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                    prompt = attack_tree_weapon()
                    # falta que se añade lo que cae al inventario
                    print(prompt)

        # si tree en ARRIBA:
        elif locations[actual_location][playerY - 1][playerX]=="T":
            # busca cual es el id del tree a la derecha del player
            for tree_key in data[actual_location]["trees"].keys():
                if data[actual_location]["trees"][tree_key]["ypos"] == playerY - 1 and data[actual_location]["trees"][tree_key]["xpos"] == playerX:
                    print(f"Hearts iniciales del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                    # quitamos 1 corazon al tree
                    data[actual_location]["trees"][tree_key]["hearts"] -= 1
                    print(f"Hearts restantes del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                    prompt = attack_tree_weapon()
                    # falta que se añade lo que cae al inventario
                    print(prompt)

        # si treee en ABAJO:
        elif locations[actual_location][playerY + 1][playerX]=="T":
            # busca cual es el id del tree a la derecha del player
            for tree_key in data[actual_location]["trees"].keys():
                if data[actual_location]["trees"][tree_key]["ypos"] == playerY + 1 and \
                        data[actual_location]["trees"][tree_key]["xpos"] == playerX:
                    print(f"Hearts iniciales del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                    # quitamos 1 corazon al tree
                    data[actual_location]["trees"][tree_key]["hearts"] -= 1
                    print(f"Hearts restantes del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                    prompt = attack_tree_weapon()
                    # falta que se añade lo que cae al inventario
                    print(prompt)

        # si tree en DERECHA:
        elif locations[actual_location][playerY][playerX - 1] =="T":
            # busca cual es el id del tree a la derecha del player
            for tree_key in data[actual_location]["trees"].keys():
                if data[actual_location]["trees"][tree_key]["ypos"] == playerY and \
                        data[actual_location]["trees"][tree_key]["xpos"] == playerX - 1:
                    print(f"Hearts iniciales del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                    # quitamos 1 corazon al tree
                    data[actual_location]["trees"][tree_key]["hearts"] -= 1
                    print(f"Hearts restantes del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                    prompt = attack_tree_weapon()
                    # falta que se añade lo que cae al inventario
                    print(prompt)


    #---- ATTACK entidades con espada
    elif pregunta=="attack" and attack_weapon==True and attack_entity == True:
        print("SE PEGA")
        #si enemy/fox/tree en DERECHA:
        if locations[actual_location][playerY][playerX + 1] in ("E", "F"):
            if locations[actual_location][playerY][playerX + 1]=="E":
                #busca cual es el id del enemigo a la derecha del player
                for enemy_key in data[actual_location]["enemies"].keys():
                    if data[actual_location]["enemies"][enemy_key]["ypos"] == playerY and data[actual_location]["enemies"][enemy_key]["xpos"] == playerX + 1:
                        print(f"Hearts iniciales del enemigo: {data[actual_location]['enemies'][enemy_key]['hearts']}")
                        #quitamos 1 corazon al enemigo
                        data[actual_location]["enemies"][enemy_key]["hearts"] -= 1
                        print(f"Hearts restantes del enemigo: {data[actual_location]['enemies'][enemy_key]['hearts']}")
                        print("Brave, keep fighting Link")

            elif locations[actual_location][playerY][playerX + 1]=="F":
                #solo hay 1 fox en el mapa
                print(f"Hearts iniciales del fox: {data[actual_location]['fox']['hearts']}")
                data[actual_location]["fox"]["hearts"]-=1
                print(f"Hearts restantes del fox: {data[actual_location]['fox']['hearts']}")
                #te dropea 1 meat

        # si enemy/fox/tree en ARRIBA:
        if locations[actual_location][playerY - 1][playerX] in ("E", "F"):
            if locations[actual_location][playerY - 1][playerX] == "E":
                # busca cual es el id del enemigo a la derecha del player
                for enemy_key in data[actual_location]["enemies"].keys():
                    if data[actual_location]["enemies"][enemy_key]["ypos"] == playerY-1 and data[actual_location]["enemies"][enemy_key]["xpos"] == playerX:
                        print(f"Hearts iniciales del enemigo: {data[actual_location]['enemies'][enemy_key]['hearts']}")
                        # quitamos 1 corazon al enemigo
                        data[actual_location]["enemies"][enemy_key]["hearts"] -= 1
                        print(f"Hearts restantes del enemigo: {data[actual_location]['enemies'][enemy_key]['hearts']}")
                        print("Brave, keep fighting Link")

            elif locations[actual_location][playerY - 1][playerX] == "F":
                # solo hay 1 fox en el mapa
                print(f"Hearts iniciales del fox: {data[actual_location]['fox']['hearts']}")
                data[actual_location]["fox"]["hearts"] -= 1
                print(f"Hearts restantes del fox: {data[actual_location]['fox']['hearts']}")
                # te dropea 1 meat

        # si enemy/fox/tree en ABAJO:
        if locations[actual_location][playerY + 1][playerX] in ("E", "F"):
            if locations[actual_location][playerY + 1][playerX] == "E":
                # busca cual es el id del enemigo a la derecha del player
                for enemy_key in data[actual_location]["enemies"].keys():
                    if data[actual_location]["enemies"][enemy_key]["ypos"] == playerY + 1 and data[actual_location]["enemies"][enemy_key]["xpos"] == playerX:
                        print(f"Hearts iniciales del enemigo: {data[actual_location]['enemies'][enemy_key]['hearts']}")
                        # quitamos 1 corazon al enemigo
                        data[actual_location]["enemies"][enemy_key]["hearts"] -= 1
                        print(f"Hearts restantes del enemigo: {data[actual_location]['enemies'][enemy_key]['hearts']}")
                        print("Brave, keep fighting Link")

            elif locations[actual_location][playerY + 1][playerX] == "F":
                # solo hay 1 fox en el mapa
                print(f"Hearts iniciales del fox: {data[actual_location]['fox']['hearts']}")
                data[actual_location]["fox"]["hearts"] -= 1
                print(f"Hearts restantes del fox: {data[actual_location]['fox']['hearts']}")
                # te dropea 1 meat

        # si enemy/fox/tree en DERECHA:
        if locations[actual_location][playerY][playerX - 1] in ("F"):
            # solo hay 1 fox en el mapa
            print(f"Hearts iniciales del fox: {data[actual_location]['fox']['hearts']}")
            data[actual_location]["fox"]["hearts"] -= 1
            print(f"Hearts restantes del fox: {data[actual_location]['fox']['hearts']}")
            # te dropea 1 meat



    #---- COOK
    elif pregunta=="cook" and cook==True:
        print("we cookin")

    #---- FISH
    elif pregunta=="fish" and fish==True:
        print("se pesca")
        prompt = fishing()
        print(prompt)

    #---- OPEN
    elif pregunta=="open" and open==True:
        print("abrir")
        # si sanctuary/chest en DERECHA:
        if locations[actual_location][playerY][playerX + 1] in ("S", "M"):
            if locations[actual_location][playerY][playerX + 1] == "S":
                # busca cual es el id del santuario a la derecha del player
                for sanctuary_key in data[actual_location]["sanctuaries"].keys():
                    if data[actual_location]["sanctuaries"][sanctuary_key]["ypos"] == playerY and data[actual_location]["sanctuaries"][sanctuary_key]["xpos"] == playerX + 1:
                        print(f"Santuario esta: {data[actual_location]['sanctuaries'][sanctuary_key]['open']}")
                        # cambiamos a abierto el santuario
                        data[actual_location]["sanctuaries"][sanctuary_key]["open"] = True
                        print(f"Santuario esta: {data[actual_location]['sanctuaries'][sanctuary_key]['open']}")

            elif locations[actual_location][playerY][playerX + 1] == "M":
                # busca cual es el id del chest a la derecha del player
                for chest_key in data[actual_location]["chests"].keys():
                    if data[actual_location]["chests"][chest_key]["ypos"] == playerY and data[actual_location]["chests"][chest_key]["xpos"] == playerX + 1:
                        print(f"Chest esta: {data[actual_location]['chests'][chest_key]['open']}")
                        # cambiamos a abierto el chest
                        data[actual_location]["chests"][chest_key]["open"] = True
                        print(f"Chest esta: {data[actual_location]['chests'][chest_key]['open']}")

        # si sanctuary/chest en ARRIBA:
        if locations[actual_location][playerY-1][playerX] in ("S", "M"):
            if locations[actual_location][playerY-1][playerX] == "S":
                # busca cual es el id del santuario a la derecha del player
                for sanctuary_key in data[actual_location]["sanctuaries"].keys():
                    if data[actual_location]["sanctuaries"][sanctuary_key]["ypos"] == playerY-1 and data[actual_location]["sanctuaries"][sanctuary_key]["xpos"] == playerX:
                        print(f"Santuario esta: {data[actual_location]['sanctuaries'][sanctuary_key]['open']}")
                        # cambiamos a abierto el santuario
                        data[actual_location]["sanctuaries"][sanctuary_key]["open"] = True
                        print(f"Santuario esta: {data[actual_location]['sanctuaries'][sanctuary_key]['open']}")

            elif locations[actual_location][playerY-1][playerX] == "M":
                # busca cual es el id del chest a la derecha del player
                for chest_key in data[actual_location]["chests"].keys():
                    if data[actual_location]["chests"][chest_key]["ypos"] == playerY-1 and data[actual_location]["chests"][chest_key]["xpos"] == playerX:
                        print(f"Chest esta: {data[actual_location]['chests'][chest_key]['open']}")
                        # cambiamos a abierto el chest
                        data[actual_location]["chests"][chest_key]["open"] = True
                        print(f"Chest esta: {data[actual_location]['chests'][chest_key]['open']}")

        # si sanctuary/chest en ABAJO:
        if locations[actual_location][playerY+1][playerX] in ("S", "M"):
            if locations[actual_location][playerY+1][playerX] == "S":
                # busca cual es el id del santuario a la derecha del player
                for sanctuary_key in data[actual_location]["sanctuaries"].keys():
                    if data[actual_location]["sanctuaries"][sanctuary_key]["ypos"] == playerY+1 and data[actual_location]["sanctuaries"][sanctuary_key]["xpos"] == playerX:
                        print(f"Santuario esta: {data[actual_location]['sanctuaries'][sanctuary_key]['open']}")
                        # cambiamos a abierto el santuario
                        data[actual_location]["sanctuaries"][sanctuary_key]["open"] = True
                        print(f"Santuario esta: {data[actual_location]['sanctuaries'][sanctuary_key]['open']}")

            elif locations[actual_location][playerY+1][playerX] == "M":
                # busca cual es el id del chest a la derecha del player
                for chest_key in data[actual_location]["chests"].keys():
                    if data[actual_location]["chests"][chest_key]["ypos"] == playerY+1 and data[actual_location]["chests"][chest_key]["xpos"] == playerX:
                        print(f"Chest esta: {data[actual_location]['chests'][chest_key]['open']}")
                        # cambiamos a abierto el chest
                        data[actual_location]["chests"][chest_key]["open"] = True
                        print(f"Chest esta: {data[actual_location]['chests'][chest_key]['open']}")

        # si chest en IZQUIERDA:
        if locations[actual_location][playerY][playerX - 1] == "M":
            # busca cual es el id del chest a la derecha del player
            for chest_key in data[actual_location]["chests"].keys():
                if data[actual_location]["chests"][chest_key]["ypos"] == playerY and data[actual_location]["chests"][chest_key]["xpos"] == playerX - 1:
                    print(f"Chest esta: {data[actual_location]['chests'][chest_key]['open']}")
                    # cambiamos a abierto el chest
                    data[actual_location]["chests"][chest_key]["open"] = True
                    print(f"Chest esta: {data[actual_location]['chests'][chest_key]['open']}")


    # ---- NO VALIDA
    else:
        print("Invalid action!")

    bm_countdown -= 1

