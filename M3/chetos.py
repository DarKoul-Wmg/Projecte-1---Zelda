from armario_FUNCIONES import*
from diccionario_general import*



pregunta = "cheating: cheat add vegetable"

promptlist = []
#if pregunta[:8].lower() == 'cheating:':

def cheating(pregunta):
    #cambio nombre
    if pregunta[:33].lower() == "cheating: cheat rename player to ":
            new_name = pregunta[33:]
            prompt(promptlist)
            if len(new_name.replace(" ", "")) > 10 or len(new_name.replace(" ", "")) < 3:
                promptlist.append('Invalid action')
                prompt(promptlist)
            elif not new_name.isalnum():
                promptlist.append('Invalid action')
                prompt(promptlist)
            else:
                game['player']['user_name'] = new_name
                promptlist.append('Hello, '+new_name)
                prompt(promptlist)

    #+1vegetal
    elif pregunta.lower() == "cheating: cheat add vegetable":
        game["foods"]["Vegetables"]["quantity_remaining"] += 1
        promptlist.append('you have one more vegetable')
        prompt(promptlist)
        # +1fish
    elif pregunta.lower() == "cheating: cheat add fish":
        game["foods"]["Fish"]["quantity_remaining"] += 1
        promptlist.append('you have one more fish')
        prompt(promptlist)
        # +1meat
    elif pregunta.lower() == "cheating: cheat add meat":
        game["foods"]["Meat"]["quantity_remaining"] += 1
        promptlist.append('you have one more meat')
        prompt(promptlist)
        # +1salad
    elif pregunta.lower() == "cheating: cheat add salad":
        game["foods"]["Salad"]["quantity_remaining"] += 1
        promptlist.append('you have one more salad')
        prompt(promptlist)
        # +1pescatarian
    elif pregunta.lower() == "cheating: cheat add vegetable":
        game["foods"]["Pescatarian"]["quantity_remaining"] += 1
        promptlist.append('you have one more pescatarian')
        prompt(promptlist)
        # +1vegetal
    elif pregunta.lower() == "cheating: cheat add roasted":
        game["foods"]["Roasted"]["quantity_remaining"] += 1
        promptlist.append('you have one more roasted')
        prompt(promptlist)
    # +1wood sword
    elif pregunta.lower() == "cheating: cheat add wood sword":
        game["weapons"]["Wood Sword"]["total_weapons"] += 1
        promptlist.append('you have one more wood sword')
        prompt(promptlist)
    # +1 sword
    elif pregunta.lower() == "cheating: cheat add sword":
        game["weapons"]["Sword"]["total_weapons"] += 1
        promptlist.append('you have one more sword')
        prompt(promptlist)
    # +1 wood shield:
    elif pregunta.lower() == "cheating: cheat add wood shield:":
        game["weapons"]["Wood Shield:"]["total_weapons"] += 1
        promptlist.append('you have one more wood shield:')
        prompt(promptlist)
    # +1 wood shield:
    elif pregunta.lower() == "cheating: cheat add shield:":
        game["weapons"]["Shield:"]["total_weapons"] += 1
        promptlist.append('you have one more shield:')
        prompt(promptlist)

######faltan los tres ultimos

cheating(pregunta)

