import datetime
game = { #JUGADOR
    "game_id": 0,
    "player": {
        "user_name": "Link",
        "health": 2,
        "bm_countdown": 25,
        "total_blood_moon": 0,
        "region": "hyrule",
        "created_at": datetime.datetime.now(),
        "modified_at": datetime.datetime.now(),

    },
    "foods": { #COMIDA
        "Fish": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Vegetables": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Meat": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Salad": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Pescatarian": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
        "Roasted": {
            "quantity_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        }
    },
    "weapons": { #ARMAS
        "Shield": {
            "equipped": 0,
            "lives_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "total_weapons": 0
        },
        "Sword": {
            "equipped": 0,
            "lives_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "total_weapons": 0
        },
        "Wood Sword": {
            "equipped": 0,
            "lives_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "total_weapons": 0
        },
        "Wood Shield": {
            "equipped": 0,
            "lives_remaining": 0,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "total_weapons": 0
        }
    },
    "enemies": { #ENEMIGOS
            0: {
            "region": "hyrule",
            "xpos": 36,
            "ypos": 5,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at":datetime.datetime.now()
        },
            1: {
            "region": "hyrule",
            "xpos": 21,
            "ypos": 9,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            2: {
            "region": "death_mountain",
            "xpos": 51,
            "ypos": 3,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            3: {
            "region": "death_mountain",
            "xpos": 13,
            "ypos": 4,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            4: {
            "region": "gerudo",
            "xpos": 3,
            "ypos": 4,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            5: {
            "region": "gerudo",
            "xpos": 38,
            "ypos": 6,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            6: {
            "region": "necluda",
            "xpos": 10,
            "ypos": 2,
            "lifes_remaining": 4,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },
            7: {
            "region": "necluda",
            "xpos": 38,
            "ypos": 6,
            "lifes_remaining": 2,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now()
        },

    },
    "chests_opened": {
        0: {
            "region": "hyrule",
            "xpos": 48,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        1: {
            "region": "death_mountain",
            "xpos": 36,
            "ypos": 8,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        2: {
            "region": "gerudo",
            "xpos": 52,
            "ypos": 1,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        3: {
            "region": "gerudo",
            "xpos": 8,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        4: {
            "region": "necluda",
            "xpos": 22,
            "ypos": 1,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        5: {
            "region": "necluda",
            "xpos": 51,
            "ypos": 2,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        6: {
            "region": "necluda",
            "xpos": 23,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        }
    },
    "sanctuaries_opened": {
        0: {
            "region": "hyrule",
            "xpos": 44,
            "ypos": 6,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        1: {
            "region": "hyrule",
            "xpos": 31,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
         2: {
            "region": "death_mountain",
            "xpos": 6,
            "ypos": 3,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
             "open":0
        },
         3: {
            "region": "death_mountain",
            "xpos": 49,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
             "open":0
        },
         4: {
            "region": "gerudo",
            "xpos": 46,
            "ypos": 3,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
             "open":0
        },
        5: {
            "region": "necluda",
            "xpos": 51,
            "ypos": 6,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        },
        6: {
            "region": "necluda",
            "xpos": 33,
            "ypos": 9,
            "created_at": datetime.datetime.now(),
            "modified_at": datetime.datetime.now(),
            "open":0
        }

    }
}
