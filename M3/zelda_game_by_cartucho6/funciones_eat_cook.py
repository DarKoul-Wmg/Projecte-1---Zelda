

#----- FUNCION DE COMER
def comer(pregunta,game,promptlist,max_hearts_remaining):
    #Vegetable
    if pregunta.lower() == 'eat vegetable':
        if game["foods"]["Vegetables"]["quantity_remaining"]== 0:
            promptlist.append("Not enough Vegetables!")
        elif game['player']['hearts_remaining']== max_hearts_remaining:
            promptlist.append("Limit hearts_remaining acquired!")
        else:
            game["foods"]["Vegetables"]["quantity_remaining"] -= 1
            game['player']['hearts_remaining'] += 1
            promptlist.append("You have eaten a Vegetable, you have gained a heart.")

    #Salad
    elif pregunta.lower() == 'eat salad':
        if game["foods"]["Salads"]["quantity_remaining"] == 0:
            promptlist.append("Not enough Salads!")
        elif game['player']['hearts_remaining'] == max_hearts_remaining:
            promptlist.append("Limit hearts_remaining acquired!")
        else:
            game["foods"]["Salads"]["quantity_remaining"] -= 1
            game['player']['hearts_remaining'] += 2
            promptlist.append("You have eaten a Salad, you have gained 2 hearts.")
            if game['player']['hearts_remaining'] > max_hearts_remaining:
                game['player']['hearts_remaining'] = max_hearts_remaining

    #Pescatarian
    elif pregunta.lower() == 'eat pescatarian':
        if game["foods"]["Pescatarian"]["quantity_remaining"]== 0:
            promptlist.append("Not enough Pescatarian!")
        elif game['player']['hearts_remaining']== max_hearts_remaining:
            promptlist.append("Limit hearts_remaining acquired!")
        else:
            game["foods"]["Pescatarian"]["quantity_remaining"] -=1
            game['player']['hearts_remaining'] += 3
            promptlist.append("You have eaten a Pescatarian, you have gained 3 hearts.")
            if game['player']['hearts_remaining'] > max_hearts_remaining:
                game['player']['hearts_remaining']=max_hearts_remaining

     #Roasted
    elif pregunta.lower() == 'eat roasted':
        if game["foods"]["Roasted"]["quantity_remaining"] == 0:
            promptlist.append("Not enough Roasted!")
        elif game['player']['hearts_remaining'] == max_hearts_remaining:
            promptlist.append("Limit hearts_remaining acquired!")
        else:
            game["foods"]["Roasted"]["quantity_remaining"] -= 1
            game['player']['hearts_remaining'] += 3
            promptlist.append("You have eaten a Roasted, you have gained 3 hearts.")
            if game['player']['hearts_remaining'] > max_hearts_remaining:
                game['player']['hearts_remaining'] = max_hearts_remaining

    else:
        promptlist.append("Invalid action!")





# FUNCION DE COCINAR
def cocinar(pregunta,game,promptlist):
    #salad
    if pregunta.lower() == 'cook salad':
        if not game["foods"]["Vegetables"]["quantity_remaining"]> 2:
            promptlist.append("Not enough Vegetables!")
        else:
            game["foods"]["Vegetables"]["quantity_remaining"] -= 2
            game["foods"]["Salads"]["quantity_remaining"] += 1
            promptlist.append("You have cooked a salad.")

    #pescatarian
    elif pregunta.lower() == 'cook pescatarian':
        if not game["foods"]["Vegetables"]["quantity_remaining"] > 0:
            promptlist.append("Not enough Vegetables!")
        elif not game["foods"]["Fish"]["quantity_remaining"] > 0:
            promptlist.append("Not enough Fish!")
        else:
            game["foods"]["Vegetables"]["quantity_remaining"] -= 1
            game["foods"]["Fish"]["quantity_remaining"] -= 1
            game["foods"]["Pescatarian"]["quantity_remaining"] += 1
            promptlist.append("You have cooked pescatarian.")

    # roasted
    elif pregunta.lower() == 'cook roasted':
        if not game["foods"]["Vegetables"]["quantity_remaining"] > 0:
            promptlist.append("Not enough Vegetables!")
        elif not game["foods"]["Meat"]["quantity_remaining"] > 0:
            promptlist.append("Not enough Meat!")
        else:
            game["foods"]["Vegetables"]["quantity_remaining"] -= 1
            game["foods"]["Meat"]["quantity_remaining"] -= 1
            game["foods"]["Roasted"]["quantity_remaining"] += 1
            promptlist.append("You have cooked a roasted.")

    else:
        promptlist.append("Invalid action!")


