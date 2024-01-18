from armario_FUNCIONES import*

from diccionario_general import*
promptlist = []

def comer(pregunta,game):
    #vegetables
    if pregunta.lower() == 'eat vegetable':
        if game["foods"]["Vegetables"]["quantity_remaining"]== 0:
            promptlist.append("Not enough Vegetables")
            prompt(promptlist)
        elif game['player']['total_blood_moon']>= max_blood_moon:
            promptlist.append("limit blood moon acquired")
            prompt(promptlist)
        else:
            game["foods"]["Vegetables"]["quantity_remaining"] -= 1
            game['player']['total_blood_moon'] += 1
            promptlist.append("You have eaten a Vegetable, you have gained a heart")
            prompt(promptlist)
    #pescatarian
    if pregunta.lower() == 'eat pescatarian':
        if game["foods"]["Pescatarian"]["quantity_remaining"]== 0:
            promptlist.append("Not enough Vegetables")
            prompt(promptlist)
        elif game['player']['total_blood_moon']>= max_blood_moon:
            promptlist.append("limit blood moon acquired")
            prompt(promptlist)
        else:
            game["foods"]["Pescatarian"]["quantity_remaining"] -=1
            game['player']['total_blood_moon'] += 3
            promptlist.append("You have eaten a Pescatarian, you have gained 3 hearts")
            prompt(promptlist)
            if game['player']['total_blood_moon'] > max_blood_moon:
                game['player']['total_blood_moon']=max_blood_moon

     #"Roasted"
    if pregunta.lower() == 'eat roasted':
        if game["foods"]["Roasted"]["quantity_remaining"] == 0:
            promptlist.append("Not enough Vegetables")
            prompt(promptlist)
        elif game['player']['total_blood_moon'] >= max_blood_moon:
            promptlist.append("limit blood moon acquired")
            prompt(promptlist)
        else:
            game["foods"]["Roasted"]["quantity_remaining"] -= 1
            game['player']['total_blood_moon'] += 3
            promptlist.append("You have eaten a Roasted, you have gained 3 hearts")
            prompt(promptlist)
            if game['player']['total_blood_moon'] > max_blood_moon:
                game['player']['total_blood_moon'] = max_blood_moon

     #"Salads"
    if pregunta.lower() == 'eat salads':
        if game["foods"]["Salads"]["quantity_remaining"] == 0:
            promptlist.append("Not enough Vegetables")
            prompt(promptlist)
        elif game['player']['total_blood_moon'] >= max_blood_moon:
            promptlist.append("limit blood moon acquired")
            prompt(promptlist)
        else:
            game["foods"]["Salads"]["quantity_remaining"] -= 1
            game['player']['total_blood_moon'] += 2
            promptlist.append("You have eaten a Salads, you have gained 2 hearts")
            prompt(promptlist)
            if game['player']['total_blood_moon'] > max_blood_moon:
                game['player']['total_blood_moon'] = max_blood_moon




##CODIGO PRUEBA

while True:
    ##printsss
    pregunta1 = 'Show inventory food'

    inv_food(pregunta1)

    pregunta = 'Show inventory main'

    main(pregunta)

######ESTA PARTE SERVIRA PARA LLAMAR FUNCION Y CRIBAR COMANDOS
    pregunta_promptlist_eat = ["eat vegetable","eat salad","eat pescatarian","eat roasted"]
    promptlist = []
    pregunta=input()
    promptlist.append(pregunta)
    #prompt(promptlist)
    ##ATENTOS DONDE SE PONE EL PROMPT PARA NO REPETIR MENSAJES
    if pregunta in pregunta_promptlist_eat:

        comer(pregunta,game)
        #clear_screen()







