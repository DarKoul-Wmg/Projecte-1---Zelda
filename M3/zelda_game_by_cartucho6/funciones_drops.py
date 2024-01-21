from funciones_flujo_de_datos import sobrescribir_game_con_data
from funciones_flujo_de_datos import update_all
import random


#---- FUNCIONES DE ACCIONES QUE DROPEAN ----
def attack_grass(data,game): #RATE DE ATACAR A LA HIERBA
    resultado = "You got nothing."
    if random.randrange(10) <= 0:
        resultado = "You got a Lizard!"
        game['foods']['Meat']['quantity_remaining']+=1
        sobrescribir_game_con_data(data, game)
        update_all()
    return resultado

def attack_tree_weapon(data,game): #RATE DE ATACAR UN ÁRBOL CON ESPADA
    resultado = "The tree didn't give you anything."
    rate = random.randrange(10)
    num_apple = [0,1,2,3]
    if rate in num_apple:#40%
        resultado = "You got an apple!"
        game['foods']['Vegetables']['quantity_remaining'] += 1
        sobrescribir_game_con_data(data, game)
        update_all()
    else:
        if rate == 4 or rate == 5:#20%
            resultado =  "You got a Wood Sword!"
            game['weapons']['Wood Sword']['total_weapons'] += 1
            if game['weapons']['Wood Sword']['total_weapons']==1:
                game['weapons']['Wood Sword']['lives_remaining'] =5
            sobrescribir_game_con_data(data, game)
            update_all()
        elif rate == 6 or rate == 7:#20%
            resultado ="You got a Wood Shield!"
            game['weapons']['Wood Shield']['total_weapons'] += 1
            if game['weapons']['Wood Shield']['total_weapons'] == 1:
                game['weapons']['Wood Shield']['lives_remaining'] = 5
            sobrescribir_game_con_data(data, game)
            update_all()
    return resultado

def attack_tree_weaponless(data,game): #RATE DE ATACAR UN ÁRBOL A PUÑOS
    resultado="The tree didn't give you anything."
    rate = random.randrange(10)
    num = [1,2,3,4]
    if rate == 0: #10%
        if random.randrange(10) %2 == 0:
            resultado = "You got a Wood Sword!"
            game['weapons']['Wood Sword']['total_weapons'] += 1
            if game['weapons']['Wood Sword']['total_weapons']==1:
                game['weapons']['Wood Sword']['lives_remaining'] =5
            sobrescribir_game_con_data(data, game)
            update_all()
        else:
            resultado = "You got a Wood Shield!"
            game['weapons']['Wood Shield']['total_weapons'] += 1
            if game['weapons']['Wood Shield']['total_weapons'] == 1:
                game['weapons']['Wood Shield']['lives_remaining'] = 5
            sobrescribir_game_con_data(data, game)
            update_all()
    elif rate in num: #40%
        resultado = "You got an apple!"
        game['foods']['Vegetables']['quantity_remaining'] += 1
        sobrescribir_game_con_data(data, game)
        update_all()
    return resultado

def fishing(data,game): #RATE DE PESCAR
    resultado = "You didn't get a fish."
    rate = random.randrange(10)
    if rate == 0 or rate == 9:
        resultado = "You got a fish!"
        game['foods']['Fish']['quantity_remaining'] += 1
        sobrescribir_game_con_data(data, game)
        update_all()
    return resultado


def drop_cofre(data,game):
    if game['player']['region'] in ['hyrule','gerudo']:
        game['weapons']['Sword']['total_weapons'] += 1
        if game['weapons']['Sword']['total_weapons'] == 1:
            game['weapons']['Sword']['lives_remaining'] = 5
        resultado="You got a Sword!"
        sobrescribir_game_con_data(data, game)
        update_all()
    elif game['player']['region'] in ['death_mountain','necluda']:
        game['weapons']['Shield']['total_weapons'] += 1
        if game['weapons']['Shield']['total_weapons'] == 1:
            game['weapons']['Shield']['lives_remaining'] = 5
        resultado="You got a Shield!"
        sobrescribir_game_con_data(data, game)
        update_all()
    return resultado


