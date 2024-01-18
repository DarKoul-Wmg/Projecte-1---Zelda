

from armario_FUNCIONES import prompt, main

from diccionario_general import*
promptlist = []

def cocinar(pregunta,game):
    #salad
    if pregunta.lower() == 'cook salad':
        if not game["foods"]["Vegetables"]["quantity_remaining"]> 2:
            promptlist.append("Not enough Vegetables")
            prompt(promptlist)
        else:
            game["foods"]["Vegetables"]["quantity_remaining"] -= 2
            game["foods"]["Salads"]["quantity_remaining"] += 1
    #pescatarian
    if pregunta.lower() == 'cook salad':
        if not game["foods"]["Vegetables"]["quantity_remaining"] > 0:
            promptlist.append("Not enough Vegetables")
            prompt(promptlist)
        elif not game["foods"]["Fish"]["quantity_remaining"] > 0:
            promptlist.append("Not enough Fish")
            prompt(promptlist)
        else:
            game["foods"]["Vegetables"]["quantity_remaining"] -= 1
            game["foods"]["Fish"]["quantity_remaining"] -= 1
            game["foods"]["Pescatarian"]["quantity_remaining"] += 1
    # roasted
    if pregunta.lower() == 'cook roasted':
        if not game["foods"]["Vegetables"]["quantity_remaining"] > 0:
            promptlist.append("Not enough Vegetables")
            prompt(promptlist)
        elif not game["foods"]["Meat"]["quantity_remaining"] > 0:
            promptlist.append("Not enough Meat")
            prompt(promptlist)
        else:
            game["foods"]["Vegetables"]["quantity_remaining"] -= 1
            game["foods"]["Meat"]["quantity_remaining"] -= 1
            game["foods"]["Roasted"]["quantity_remaining"] += 1

cocinar(pregunta,game)