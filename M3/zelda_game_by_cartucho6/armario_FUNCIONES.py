
import math
from funciones_flujo_de_datos import sobrescribir_game_con_data
from funciones_inventarios import calcular_max_hearts_remaining

# ---- CALCULOS HIPOTENUSA ----
def calcular_hipotenusa(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    hipotenusa = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return hipotenusa



# ---- CHEATING ----
def cheating(pregunta,game,promptlist,data,max_hearts_remaining):
    #cambio nombre
    if pregunta[:33].lower() == "cheating: cheat rename player to ":
            new_name = pregunta[33:]
            if len(new_name.replace(" ", "")) > 10 or len(new_name.replace(" ", "")) < 3:
                promptlist.append('Invalid action')
                
            elif not new_name.isalnum():
                promptlist.append('Invalid action')
                
            else:
                game['player']['user_name'] = new_name
                promptlist.append('Hello, '+new_name)
                

    #+1vegetal
    elif pregunta.lower() == "cheating: cheat add vegetable":
        game["foods"]["Vegetables"]["quantity_remaining"] += 1
        promptlist.append('You have one more vegetable')
        
        # +1fish
    elif pregunta.lower() == "cheating: cheat add fish":
        game["foods"]["Fish"]["quantity_remaining"] += 1
        promptlist.append('You have one more fish')
        
        # +1meat
    elif pregunta.lower() == "cheating: cheat add meat":
        game["foods"]["Meat"]["quantity_remaining"] += 1
        promptlist.append('You have one more meat')
        
        # +1salad
    elif pregunta.lower() == "cheating: cheat cook salad":
        game["foods"]["Salads"]["quantity_remaining"] += 1
        promptlist.append('You have one more salad')
        
        # +1pescatarian
    elif pregunta.lower() == "cheating: cheat cook pescatarian":
        game["foods"]["Pescatarian"]["quantity_remaining"] += 1
        promptlist.append('You have one more pescatarian')
        
        # +1vegetal
    elif pregunta.lower() == "cheating: cheat cook roasted":
        game["foods"]["Roasted"]["quantity_remaining"] += 1
        promptlist.append('You have one more roasted')
        
    # +1wood sword
    elif pregunta.lower() == "cheating: cheat add wood sword":
        game["weapons"]["Wood Sword"]["total_weapons"] += 1
        game["weapons"]["Wood Sword"]["lives_remaining"]=5
        promptlist.append('You have one more wood sword')
        
    # +1 sword
    elif pregunta.lower() == "cheating: cheat add sword":
        game["weapons"]["Sword"]["total_weapons"] += 1
        game["weapons"]["Sword"]["lives_remaining"] = 5
        promptlist.append('You have one more sword')
        
    # +1 wood shield:
    elif pregunta.lower() == "cheating: cheat add wood shield":
        game["weapons"]["Wood Shield"]["total_weapons"] += 1
        game["weapons"]["Wood Shield"]["lives_remaining"] = 5
        promptlist.append('You have one more wood shield')
        
    # +1 wood shield:
    elif pregunta.lower() == "cheating: cheat add shield":
        game["weapons"]["Shield"]["total_weapons"] += 1
        game["weapons"]["Shield"]["lives_remaining"] = 5
        promptlist.append('You have one more shield')

    # open sanctuaries:
    elif pregunta.lower() == "cheating: cheat open sanctuaries":
        lista_locations = []
        for location in data.keys():
            lista_locations.append(location)
        lista_locations = lista_locations[:4]

        for location in lista_locations:
            for sanct_key in data[location]['sanctuaries'].keys():
                data[location]["sanctuaries"][sanct_key]["open"] = True
        promptlist.append('All sanctuaries have been opened')
        sobrescribir_game_con_data(data, game)
        max_hearts_remaining = calcular_max_hearts_remaining(game)
        game['player']['hearts_remaining'] = max_hearts_remaining
        sobrescribir_game_con_data(data, game)





# ---- GO BY: Hyrule ----
def go_by_hyrule(pregunta, playerX, playerY,locations,game):
    # enemigos
    if pregunta.lower() == 'go by the e':
        coordenadas = []
        for y in range(len(locations[game['player']['region']])):
            for x in range(len(locations[game['player']['region']][y])):
                if locations[game['player']['region']][y][x] == "E":
                    pos_x = x
                    pos_y = y

                    coordenadas.append((pos_x, pos_y))
                    print(coordenadas)
                    break
                else:
                    continue

        player_coordenada = playerX, playerY
        E0 = coordenadas[0]
        hipo_e0 = calcular_hipotenusa(player_coordenada, E0)

        E1 = coordenadas[1]
        hipo_e1 = calcular_hipotenusa(player_coordenada, E1)

        if hipo_e0 < hipo_e1:
            playerY = coordenadas[0][1]
            playerX = coordenadas[0][0] - 1

        else:
            playerY = coordenadas[1][1]
            playerX = coordenadas[1][0] - 1

    # fox
    elif pregunta.lower() == 'go by the f':
        playerY = 9
        playerX = 51
        player_coordenada = 'X'

    # TTT
    elif pregunta.lower() == 'go by the t':
        player_coordenada = playerX, playerY
        tree1 = 6, 4
        hipo_tree1 = calcular_hipotenusa(player_coordenada, tree1)

        tree2 = 48, 8
        hipo_tree2 = calcular_hipotenusa(player_coordenada, tree2)

        tree3 = 46, 9
        hipo_tree3 = calcular_hipotenusa(player_coordenada, tree3)

        if hipo_tree1 < hipo_tree2 and hipo_tree1 < hipo_tree3:
            playerY = 4
            playerX = 5

        elif hipo_tree2 < hipo_tree1 and hipo_tree2 < hipo_tree3:
            playerY = 8
            playerX = 47

        elif hipo_tree3 < hipo_tree1 and hipo_tree3 < hipo_tree2:
            playerY = 9
            playerX = 45

    # s
    elif pregunta.lower() == 'go by the s0':
        playerY = 6
        playerX = 43

    elif pregunta.lower() == 'go by the s1':
        playerY = 9
        playerX = 30

    # water
    elif pregunta.lower() == 'go by the water':
        playerY = 3
        playerX = 42

    return playerY, playerX





# ---- GO BY: Death Mountain ----
def go_by_death_mountain(pregunta, playerX, playerY,locations,game):
    # enemigos
    if pregunta.lower() == 'go by the e':
        coordenadas = []
        for y in range(len(locations[game['player']['region']])):
            for x in range(len(locations[game['player']['region']][y])):
                if locations[game['player']['region']][y][x] == "E":
                    pos_x = x
                    pos_y = y

                    coordenadas.append((pos_x, pos_y))
                    print(coordenadas)
                    break
                else:
                    continue

        player_coordenada = playerX, playerY
        E0 = coordenadas[0]
        hipo_e0 = calcular_hipotenusa(player_coordenada, E0)

        E1 = coordenadas[1]
        hipo_e1 = calcular_hipotenusa(player_coordenada, E1)

        if hipo_e0 < hipo_e1:
            playerY = coordenadas[0][1]
            playerX = coordenadas[0][0] - 1

        else:
            playerY = coordenadas[1][1]
            playerX = coordenadas[1][0] - 1
            

    # fox
    elif pregunta.lower() == 'go by the f':
        playerY = 2
        playerX = 29
        

    # TTT
    elif pregunta.lower() == 'go by the t':
        player_coordenada = playerX, playerY
        tree1 = 19, 7
        hipo_tree1 = calcular_hipotenusa(player_coordenada, tree1)

        tree2 = 18, 8
        hipo_tree2 = calcular_hipotenusa(player_coordenada, tree2)

        tree3 = 18, 9
        hipo_tree3 = calcular_hipotenusa(player_coordenada, tree3)

        if hipo_tree1 < hipo_tree2 and hipo_tree1 < hipo_tree3:
            playerY = 7
            playerX = 18
            
        elif hipo_tree2 < hipo_tree1 and hipo_tree2 < hipo_tree3:
            playerY = 8
            playerX = 17
            
        elif hipo_tree3 < hipo_tree1 and hipo_tree3 < hipo_tree2:
            playerY = 9
            playerX = 17
            

    # s
    elif pregunta.lower() == 'go by the s2':
        playerY = 3
        playerX = 5

    elif pregunta.lower() == 'go by the s3':
        playerY = 9
        playerX = 48

    # water
    elif pregunta.lower() == 'go by the water':
        playerY = 6
        playerX = 11
        

    return playerY, playerX





# ---- GO BY: Gerudo ----
def go_by_gerudo(pregunta, playerX, playerY,locations,game):
    # enemigos
    if pregunta.lower() == 'go by the e':
        coordenadas = []
        for y in range(len(locations[game['player']['region']])):
            for x in range(len(locations[game['player']['region']][y])):
                if locations[game['player']['region']][y][x] == "E":
                    pos_x = x
                    pos_y = y

                    coordenadas.append((pos_x, pos_y))
                    print(coordenadas)
                    break
                else:
                    continue

        player_coordenada = playerX, playerY
        E0 = coordenadas[0]
        hipo_e0 = calcular_hipotenusa(player_coordenada, E0)

        E1 = coordenadas[1]
        hipo_e1 = calcular_hipotenusa(player_coordenada, E1)

        if hipo_e0 < hipo_e1:
            playerY = coordenadas[0][1]
            playerX = coordenadas[0][0] - 1

        else:
            playerY = coordenadas[1][1]
            playerX = coordenadas[1][0] - 1

        # fox
    elif pregunta.lower() == 'go by the f':
        playerY = 8
        playerX = 47
        

        # TTT
    elif pregunta.lower() == 'go by the t':
        player_coordenada = playerX, playerY
        tree1 = 29, 2
        hipo_tree1 = calcular_hipotenusa(player_coordenada, tree1)

        tree2 = 30, 2
        hipo_tree2 = calcular_hipotenusa(player_coordenada, tree2)

        tree3 = 31, 2
        hipo_tree3 = calcular_hipotenusa(player_coordenada, tree3)

        tree4 = 31, 3
        hipo_tree4 = calcular_hipotenusa(player_coordenada, tree4)

        tree5 = 33, 3
        hipo_tree5 = calcular_hipotenusa(player_coordenada, tree5)

        tree6 = 5, 8
        hipo_tree6 = calcular_hipotenusa(player_coordenada, tree6)

        if (hipo_tree1 < hipo_tree2 and hipo_tree1 < hipo_tree3 and hipo_tree1 < hipo_tree4 and
                hipo_tree1 < hipo_tree5 and hipo_tree1 < hipo_tree6):
            playerY = 2
            playerX = 28
            
        elif (hipo_tree2 < hipo_tree1 and hipo_tree2 < hipo_tree3 and hipo_tree2 < hipo_tree4 and
              hipo_tree2 < hipo_tree5 and hipo_tree2 < hipo_tree6):
            playerY = 1
            playerX = 30
            
        elif (hipo_tree3 < hipo_tree1 and hipo_tree3 < hipo_tree2 and hipo_tree3 < hipo_tree4 and
              hipo_tree3 < hipo_tree5 and hipo_tree3 < hipo_tree6):
            playerY = 1
            playerX = 31
            
        elif (hipo_tree4 < hipo_tree1 and hipo_tree4 < hipo_tree2 and hipo_tree4 < hipo_tree3 and
              hipo_tree4 < hipo_tree5 and hipo_tree4 < hipo_tree6):
            playerY = 3
            playerX = 30
            
        elif (hipo_tree5 < hipo_tree1 and hipo_tree5 < hipo_tree2 and hipo_tree5 < hipo_tree3 and
              hipo_tree5 < hipo_tree4 and hipo_tree5 < hipo_tree6):
            playerY = 4
            playerX = 32
            
        elif (hipo_tree6 < hipo_tree1 and hipo_tree6 < hipo_tree2 and hipo_tree6 < hipo_tree3 and
              hipo_tree6 < hipo_tree4 and hipo_tree6 < hipo_tree5):
            playerY = 9
            playerX = 5


        # s
    elif pregunta.lower() == 'go by the s4':
        playerY = 3
        playerX = 45

        # water
    elif pregunta.lower() == 'go by the water':
        playerY = 9
        playerX = 53

    return playerY, playerX





# ---- GO BY: Necluda ----
def go_by_necluda(pregunta, playerX, playerY,locations,game):
    # enemigos
    if pregunta.lower() == 'go by the e':
        coordenadas = []
        for y in range(len(locations[game['player']['region']])):
            for x in range(len(locations[game['player']['region']][y])):
                if locations[game['player']['region']][y][x] == "E":
                    pos_x = x
                    pos_y = y

                    coordenadas.append((pos_x, pos_y))
                    print(coordenadas)
                    break
                else:
                    continue

        player_coordenada = playerX, playerY
        E0 = coordenadas[0]
        hipo_e0 = calcular_hipotenusa(player_coordenada, E0)

        E1 = coordenadas[1]
        hipo_e1 = calcular_hipotenusa(player_coordenada, E1)

        if hipo_e0 < hipo_e1:
            playerY = coordenadas[0][1]
            playerX = coordenadas[0][0] - 1

        else:
            playerY = coordenadas[1][1]
            playerX = coordenadas[1][0] - 1

        # fox
    elif pregunta.lower() == 'go by the f':
        playerY = 6
        playerX = 6

        # TTT
    elif pregunta.lower() == 'go by the t':
        player_coordenada = playerX, playerY
        tree1 = 37, 2
        hipo_tree1 = calcular_hipotenusa(player_coordenada, tree1)

        tree2 = 38, 2
        hipo_tree2 = calcular_hipotenusa(player_coordenada, tree2)

        tree3 = 35, 3
        hipo_tree3 = calcular_hipotenusa(player_coordenada, tree3)

        tree4 = 36, 3
        hipo_tree4 = calcular_hipotenusa(player_coordenada, tree4)

        tree5 = 15, 6
        hipo_tree5 = calcular_hipotenusa(player_coordenada, tree5)

        tree6 = 14, 7
        hipo_tree6 = calcular_hipotenusa(player_coordenada, tree6)

        tree7 = 15, 8
        hipo_tree7 = calcular_hipotenusa(player_coordenada, tree7)

        if (hipo_tree1 < hipo_tree2 and hipo_tree1 < hipo_tree3 and hipo_tree1 < hipo_tree4 and
                hipo_tree1 < hipo_tree5 and hipo_tree1 < hipo_tree6 and hipo_tree1 < hipo_tree7):
            playerY = 2
            playerX = 36
            
        elif (hipo_tree2 < hipo_tree1 and hipo_tree2 < hipo_tree3 and hipo_tree2 < hipo_tree4 and
              hipo_tree2 < hipo_tree5 and hipo_tree2 < hipo_tree6 and hipo_tree2 < hipo_tree7):
            playerY = 1
            playerX = 38
            
        elif (hipo_tree3 < hipo_tree1 and hipo_tree3 < hipo_tree2 and hipo_tree3 < hipo_tree4 and
              hipo_tree3 < hipo_tree5 and hipo_tree3 < hipo_tree6 and hipo_tree3 < hipo_tree7):
            playerY = 3
            playerX = 34
            
        elif (hipo_tree4 < hipo_tree1 and hipo_tree4 < hipo_tree2 and hipo_tree4 < hipo_tree3 and
              hipo_tree4 < hipo_tree5 and hipo_tree4 < hipo_tree6 and hipo_tree4 < hipo_tree7):
            playerY = 4
            playerX = 36
            
        elif (hipo_tree5 < hipo_tree1 and hipo_tree5 < hipo_tree2 and hipo_tree5 < hipo_tree3 and
              hipo_tree5 < hipo_tree4 and hipo_tree5 < hipo_tree6 and hipo_tree5 < hipo_tree7):
            playerY = 6
            playerX = 14
            
        elif (hipo_tree6 < hipo_tree1 and hipo_tree6 < hipo_tree2 and hipo_tree6 < hipo_tree3 and
              hipo_tree6 < hipo_tree4 and hipo_tree6 < hipo_tree5 and hipo_tree6 < hipo_tree7):
            playerY = 7
            playerX = 13
            
        elif (hipo_tree7 < hipo_tree1 and hipo_tree7 < hipo_tree2 and hipo_tree7 < hipo_tree3 and
              hipo_tree7 < hipo_tree4 and hipo_tree7 < hipo_tree5 and hipo_tree7 < hipo_tree6):
            playerY = 8
            playerX = 14


        # s
    elif pregunta.lower() == 'go by the s5':
        playerY = 6
        playerX = 50

    elif pregunta.lower() == 'go by the s6':
        playerY = 9
        playerX = 32

    # water
    elif pregunta.lower() == 'go by the water':
        player_coordenada = playerX, playerY
        W1 = 3, 8
        hipo_w1 = calcular_hipotenusa(player_coordenada, W1)

        W2 = 50, 5
        hipo_w2 = calcular_hipotenusa(player_coordenada, W2)

        if hipo_w1 < hipo_w2:
            playerY = 8
            playerX = 3

        else:
            playerY = 5
            playerX = 50
            
    return playerY, playerX



