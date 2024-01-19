import datetime

game = { #JUGADOR
    "game_id": 3,
    "player": {
        "user_name": "Link",
        "health": 3,
        "bm_countdown": 25,
        "total_blood_moon": 2,
        "region": "hyrule",
        "created_at": "2024-01-11 17:47:28",
        "modified_at": "2024-01-11 17:47:28",

    },
    "foods": { #COMIDA
        "Fish": {
            "quantity_remaining": 5,
            "created_at": "2024-01-11 17:47:28",
            "modified_at": "2024-01-11 17:47:28"
        },
        "Vegetables": {
            "quantity_remaining": 1,
            "created_at": "2024-01-11 17:47:28",
            "modified_at": "2024-01-11 17:47:28"
        },
        "Meat": {
            "quantity_remaining": 3,
            "created_at": "2024-01-11 17:47:28",
            "modified_at": "2024-01-11 17:47:28"
        },
        "Salads": {
            "quantity_remaining": 5,
            "created_at": "2024-01-11 17:47:28",
            "modified_at": "2024-01-11 17:47:28"
        },
        "Pescatarian": {
            "quantity_remaining": 0,
            "created_at": "2024-01-11 17:47:28",
            "modified_at": "2024-01-11 17:47:28"
        },
        "Roasted": {
            "quantity_remaining": 0,
            "created_at": "2024-01-11 17:47:28",
            "modified_at": "2024-01-11 17:47:28"
        }
    },
    "weapons": { #ARMAS
        "Shield": {
            "equipped": 0,
            "lives_remaining": 4,
            "created_at": "2024-01-12 21:47:06",
            "modified_at": "2024-01-12 21:47:06",
            "total_weapons": 0
        },
        "Sword": {
            "equipped": 0,
            "lives_remaining": 2,
            "created_at": "2024-01-11 17:47:50",
            "modified_at": "2024-01-12 20:59:05",
            "total_weapons": 3
        },
        "Wood Sword": {
            "equipped": 1,
            "lives_remaining": 3,
            "created_at": "2024-01-11 17:47:50",
            "modified_at": "2024-01-11 17:47:50",
            "total_weapons": 3
        },
        "Wood Shield": {
            "equipped": 1,
            "lives_remaining": 2,
            "created_at": "2024-01-11 17:47:50",
            "modified_at": "2024-01-11 17:47:50",
            "total_weapons": 2
        }
    },
    "enemies": { #ENEMIGOS
            0: {
            "region": "hyrule",
            "xpos": 4,
            "ypos": 5,
            "lifes_remaining": 2,
            "created_at": "2024-01-11 17:48:06",
            "modified_at": "2024-01-11 17:48:06"
        },
            1: {
            "region": "hyrule",
            "xpos": 20,
            "ypos": 10,
            "lifes_remaining": 3,
            "created_at": "2024-01-11 17:48:06",
            "modified_at": "2024-01-11 17:48:06"
        },
            2: {
            "region": "death_mountain",
            "xpos": 16,
            "ypos": 9,
            "lifes_remaining": 2,
            "created_at": "2024-01-11 17:48:06",
            "modified_at": "2024-01-11 17:48:06"
        },
            3: {
            "region": "death_mountain",
            "xpos": 29,
            "ypos": 5,
            "lifes_remaining": 3,
            "created_at": "2024-01-11 17:48:06",
            "modified_at": "2024-01-11 17:48:06"
        },
            4: {
            "region": "gerudo",
            "xpos": 31,
            "ypos": 8,
            "lifes_remaining": 2,
            "created_at": "2024-01-11 17:48:06",
            "modified_at": "2024-01-11 17:48:06"
        },
            5: {
            "region": "gerudo",
            "xpos": 25,
            "ypos": 11,
            "lifes_remaining": 3,
            "created_at": "2024-01-11 17:48:06",
            "modified_at": "2024-01-11 17:48:06"
        },
            6: {
            "region": "necluda",
            "xpos": 24,
            "ypos": 33,
            "lifes_remaining": 2,
            "created_at": "2024-01-11 17:48:06",
            "modified_at": "2024-01-11 17:48:06"
        },
            7: {
            "region": "necluda",
            "xpos": 12,
            "ypos": 15,
            "lifes_remaining": 2,
            "created_at": "2024-01-11 17:48:06",
            "modified_at": "2024-01-11 17:48:06"
        },

    },
    "chests_opened": {
        0: {
            "region": "hyrule",
            "xpos": 48,
            "ypos": 9,
            "created_at": "2024-01-11 17:48:37",
            "modified_at": "2024-01-11 17:48:37",
            "open":0
        },
        1: {
            "region": "death_mountain",
            "xpos": 36,
            "ypos": 8,
            "created_at": "2024-01-11 17:48:37",
            "modified_at": "2024-01-11 17:48:37",
            "open":0
        }
    },
    "sanctuaries_opened": {
        "sanctuary0": {
            "region": "hyrule",
            "xpos": 44,
            "ypos": 6,
            "created_at": "2024-01-11 17:48:27",
            "modified_at": "2024-01-11 17:48:27",
            "open":0
        },
        "sanctuary1": {
            "region": "hyrule",
            "xpos": 31,
            "ypos": 9,
            "created_at": "2024-01-11 17:48:27",
            "modified_at": "2024-01-11 17:48:27",
            "open":0
        },
         "sanctuary2": {
            "region": "death_mountain",
            "xpos": 6,
            "ypos": 3,
            "created_at": "2024-01-11 17:48:27",
            "modified_at": "2024-01-11 17:48:27",
             "open":1
        },
         "sanctuary3": {
            "region": "death_mountain",
            "xpos": 49,
            "ypos": 9,
            "created_at": "2024-01-11 17:48:27",
            "modified_at": "2024-01-11 17:48:27",
             "open":0
        },
         "sanctuary4": {
            "region": "gerudo",
            "xpos": 46,
            "ypos": 3,
            "created_at": "2024-01-11 17:48:27",
            "modified_at": "2024-01-11 17:48:27",
             "open":0
        },
        "sanctuary5": {
            "region": "necluda",
            "xpos": 51,
            "ypos": 6,
            "created_at": "2024-01-11 17:48:27",
            "modified_at": "2024-01-11 17:48:27",
            "open":0
        },
        "sanctuary6": {
            "region": "necluda",
            "xpos": 33,
            "ypos": 9,
            "created_at": "2024-01-11 17:48:27",
            "modified_at": "2024-01-11 17:48:27",
            "open":0
        }

    }
}
max_blood_moon= 2
for key,value in game["sanctuaries_opened"].items():
    if value['open']== 1:
        max_blood_moon += 1
#print(max_blood_moon)


###VARIABLES APUNTADORES PRINT INVENTARIOS

##PRINT PANTALLA FOOD
vegetables = game['foods']['Vegetables']['quantity_remaining']
fish = game['foods']['Fish']['quantity_remaining']
meat = game['foods']['Meat']['quantity_remaining']
salads = game['foods']['Salads']['quantity_remaining']
pescatarian = game['foods']['Pescatarian']['quantity_remaining']
roasted = game['foods']['Roasted']['quantity_remaining']

##PRINT PANTALLA WEAPONS

un= game['player']['total_blood_moon']

tw= ((game["weapons"]["Shield"]["total_weapons"]+game["weapons"]["Wood Shield"]["total_weapons"]
     +game["weapons"]["Sword"]["total_weapons"])+game["weapons"]["Wood Sword"]["total_weapons"])



tf=((game['foods']["Fish"]["quantity_remaining"]+game['foods']["Vegetables"]["quantity_remaining"]
     +game['foods']["Meat"]["quantity_remaining"])+game['foods']["Salads"]["quantity_remaining"]
    +game['foods']["Pescatarian"]["quantity_remaining"]+game['foods']["Roasted"]["quantity_remaining"])


