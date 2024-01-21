coordenadas = []
        for y in range(len(locations[actual_location])):
            for x in range(len(locations[actual_location][y])):
                if locations[actual_location][y][x] == "E":
                    pos_x = x
                    pos_y = y

                    coordenadas.append((pos_x, pos_y))
                    print(coordenadas)
                    break
                else:
                    continue

        locations[actual_location][playerY][playerX] = playerX, playerY
        E0 = coordenadas[0]

        hipo_e0 = calcular_hipotenusa(locations[actual_location][playerY][playerX], E0)

        E1 = coordenadas[1]

        hipo_e1 = calcular_hipotenusa(locations[actual_location][playerY][playerX], E1)

        if hipo_e0 < hipo_e1:
            locations[actual_location][playerY][playerX] = ' '
            playerY = coordenadas[0][1]
            playerX = coordenadas[0][0] - 1
            locations[actual_location][playerY][playerX] = 'X'

        else:
            locations[actual_location][playerY][playerX] = ' '
            playerY = coordenadas[1][1]
            playerX = coordenadas[1][0] - 1
            locations[actual_location][playerY][playerX] = 'X'
