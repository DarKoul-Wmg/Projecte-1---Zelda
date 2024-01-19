import math


def calcular_hipotenusa(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    hipotenusa = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return hipotenusa

locations={ "hyrule":[["*"," ","H","y","r","u","l","e"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","O","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","O","O","~","O","O","O","O","~","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","C"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~"," "," "," ","~","~","~","~","~","~","*"],
                ["*"," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","E","9"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","0"," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," ","!"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","O","O"," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," ","E","1"," "," "," "," "," "," "," "," ","S","1","?"," "," "," "," "," "," "," "," "," "," "," "," ","T"," ","M"," "," "," ","F"," "," "," "," "," ","*"],
                ["*","O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"]],

            "death_mountain":[["*"," ","D","e","a","t","h"," ","m","o","u","n","t","a","i","n"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
                ["*"," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," ","F"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","~","~"," "," ","S","2","?"," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","E","2"," "," "," "," "," ","*"],
                ["*"," ","~","~","~"," "," "," "," "," "," "," "," ","E","2"," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","O","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," ","O","O"," "," "," "," ","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","~","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," ","~","~","~"," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," ","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," ","M"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","!"," "," "," ","C"," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," ","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","3","?"," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"]],

            "gerudo": [["*"," ","G","e","r","u","d","o"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
                ["*","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","M"," "," "," "," "," ","*"],
                ["*"," "," ","O","O","O","O","O"," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T","T","T"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T","T"," "," "," "," "," "," "," "," "," "," "," "," "," ","S","4"," "," "," "," "," "," "," "," "," ","O","*"],
                ["*"," "," ","E","1"," "," "," "," "," "," "," "," "," "," ","C"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," ","A","A","A","A","A","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","E","2"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," ","A","A","A","A","A","A","A","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," ","T"," "," "," "," "," "," "," ","A","A","A","A","A","A","A"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," ","F"," "," "," "," "," "," "," ","~","~","*"],
                ["*"," ","!"," "," "," "," "," ","M"," "," "," "," "," "," ","A","A","A"," "," "," "," "," "," "," "," ","O","O","O","O","O"," "," "," "," ","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","*"],
                ["*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"]],

            "necluda":[["*"," ","N","e","c","l","u","d","a"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","M"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","!"," "," "," "," "," "," "," ","E","1"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T","T"," "," "," "," "," "," "," "," "," "," "," "," ","M"," "," "," "," "," "," ","*"],
                ["*","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","C"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T","T"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","*"],
                ["*","O","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","*"],
                ["*","O","O","O","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","T"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","E","2"," "," "," "," "," "," "," "," "," "," "," ","S","5","~","~","~","~","~","*"],
                ["*"," "," "," "," "," ","F"," "," "," "," "," "," "," ","T","9"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","*"],
                ["*","~","~"," "," "," "," "," "," "," "," "," "," "," "," ","T","6"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","*"],
                ["*","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","M"," "," "," "," "," "," "," "," "," ","S","6"," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","*"],
                ["*","~","~","~","~","~","~","~","~","~","~","~","~"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","~","*"],
                ["*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"]],

            "map":[["*"," ","M","a","p"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," ","H","y","r","u","l","e"," "," "," "," "," "," "," ","S","0"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","D","e","a","t","h"," ","m","o","u","n","t","a","i","n"," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","2","?"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," ","S","1","?"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","3","?"," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","C","a","s","t","l","e"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","4"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","5"," "," ","*"],
                ["*"," "," ","G","e","r","u","d","o"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","S","6","?"," "," "," "," "," "," ","N","e","c","l","u","d","a"," "," ","*"],
                ["*"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","*"],
                ["*"," ","B","a","c","k"," "," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"," ","*"]]
}



data={"hyrule":{'trees': {'tree1': {'ypos': 4, 'xpos': 6, 'respawn': 0, 'hearts': 4},
                       'tree2': {'ypos': 8, 'xpos': 48, 'respawn': 0, 'hearts': 4},
                       'tree3': {'ypos': 9, 'xpos': 46, 'respawn': 0, 'hearts': 4}},
             'fox': {'ypos': 9, 'xpos': 52, 'hearts': 1},
             'sanctuaries': {0: {'ypos': 6, 'xpos': 44, 'open': False},
                             1: {'ypos': 9, 'xpos': 31, 'open': False}},
             'chests': {0: {'ypos': 9, 'xpos': 48, 'open': False}},
             'enemies': {0: {'ypos': 5, 'xpos': 36, 'hearts': 5},
                         1: {'ypos': 9, 'xpos': 21, 'hearts': 5}}},

    "death_mountain":{'trees': {'tree1': {'ypos': 7, 'xpos': 19, 'respawn': 0, 'hearts': 4},
                                'tree2': {'ypos': 8, 'xpos': 18, 'respawn': 0, 'hearts': 4},
                                'tree3': {'ypos': 9, 'xpos': 18, 'respawn': 0, 'hearts': 4}},
                      'fox': {'ypos': 2, 'xpos': 30, 'hearts': 1},
                      'sanctuaries': {2: {'ypos': 3, 'xpos': 6, 'open': False},
                                      3: {'ypos': 9, 'xpos': 49, 'open': False}},
                      'chests': {1: {'ypos': 8, 'xpos': 36, 'open': False}},
                      'enemies': {2: {'ypos': 3, 'xpos': 51, 'hearts': 5},
                                  3: {'ypos': 4, 'xpos': 13, 'hearts': 5}}},

    "gerudo":{'trees': {'tree1': {'ypos': 2, 'xpos': 29, 'respawn': 0, 'hearts': 4},
                        'tree2': {'ypos': 2, 'xpos': 30, 'respawn': 0, 'hearts': 4},
                        'tree3': {'ypos': 2, 'xpos': 31, 'respawn': 0, 'hearts': 4},
                        'tree4': {'ypos': 3, 'xpos': 31, 'respawn': 0, 'hearts': 4},
                        'tree5': {'ypos': 3, 'xpos': 32, 'respawn': 0, 'hearts': 4},
                        'tree6': {'ypos': 8, 'xpos': 5, 'respawn': 0, 'hearts': 4}},
              'fox': {'ypos': 8, 'xpos': 48, 'hearts': 1},
              'sanctuaries': {4: {'ypos': 3, 'xpos': 46, 'open': False}},
              'chests': {2: {'ypos': 1, 'xpos': 52, 'open': False},
                         3: {'ypos': 9, 'xpos': 8, 'open': False}},
              'enemies': {4: {'ypos': 4, 'xpos': 3, 'hearts': 5},
                          5: {'ypos': 6, 'xpos': 38, 'hearts': 5}}},

    "necluda":{'trees': {'tree1': {'ypos': 2, 'xpos': 37, 'respawn': 0, 'hearts': 4},
                         'tree2': {'ypos': 2, 'xpos': 38, 'respawn': 0, 'hearts': 4},
                         'tree3': {'ypos': 3, 'xpos': 35, 'respawn': 0, 'hearts': 4},
                         'tree4': {'ypos': 3, 'xpos': 36, 'respawn': 0, 'hearts': 4},
                         'tree5': {'ypos': 6, 'xpos': 15, 'respawn': 0, 'hearts': 4},
                         'tree6': {'ypos': 7, 'xpos': 14, 'respawn': 0, 'hearts': 4},
                         'tree7': {'ypos': 8, 'xpos': 15, 'respawn': 0, 'hearts': 4}},
               'fox': {'ypos': 7, 'xpos': 6, 'hearts': 1},
               'sanctuaries': {5: {'ypos': 6, 'xpos': 51, 'open': False},
                               6: {'ypos': 9, 'xpos': 33, 'open': False}},
               'chests': {4: {'ypos': 1, 'xpos': 22, 'open': False},
                          5: {'ypos': 2, 'xpos': 51, 'open': False},
                          6: {'ypos': 9, 'xpos': 23, 'open': False}},
               'enemies': {6: {'ypos': 2, 'xpos': 10, 'hearts': 5},
                           7: {'ypos': 6, 'xpos': 38, 'hearts': 5}}}

    }



actual_location=('death_mountain')

#-- Busca donde esta el "!" para posicionar ahi al player
for y in range(len(locations[actual_location])):
   for x in range(len(locations[actual_location][y])):
       if locations[actual_location][y][x]=="!":
           playerX = x
           playerY = y
           break
       else:
           continue




locations[actual_location][playerY][playerX]="X"

#PRINT INICIAL
for y in range(len(locations[actual_location])):
    for x in range(len(locations[actual_location][0])):
        print((locations[actual_location][y][x]), end="")
    print()


while True:
    # LISTA INTERACCIONES:
    attack=True
    attack_weapon = True #CAMBIAR SEGUN SI LLEVA ARMA
    attack_entity = False
    cook = False
    fish = False
    open = False

    #DETECCION INTERACCIONES PARA SABER ACCIONES DISPONIBLES PARA EL INPUT
    if (locations[actual_location][playerY][playerX - 1] in ("E", "F", "T") or
       locations[actual_location][playerY - 1][playerX] in ("E", "F", "T") or
       locations[actual_location][playerY][playerX + 1] in ("E", "F", "T") or
       locations[actual_location][playerY + 1][playerX] in ("E", "F", "T")):
        attack_entity = True

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

    #------------- INICIO INTERACCION -------------------
    pregunta= input("What to do now?")

    #----- MOVIMIENTO -----
    if pregunta[:-2] in ('go right ', 'go left ', 'go up ', 'go down ','go right', 'go left', 'go up', 'go down'):
        cantidad = int(pregunta[-2:])
        print(cantidad)
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

        print(playerY)
        print(playerX)
        locations[actual_location][playerY][playerX] = "X"


    #---- ATTACK
    elif pregunta=="attack" and attack==True and attack_entity == True:
        print("SE PEGA")
        #si enemy/fox/tree en DERECHA:
        if locations[actual_location][playerY][playerX + 1] in ("E", "F", "T"):
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

            elif locations[actual_location][playerY][playerX + 1]=="T":
                # busca cual es el id del tree a la derecha del player
                for tree_key in data[actual_location]["trees"].keys():
                    if data[actual_location]["trees"][tree_key]["ypos"] == playerY and data[actual_location]["trees"][tree_key]["xpos"] == playerX + 1:
                        print(f"Hearts iniciales del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                        # quitamos 1 corazon al tree
                        data[actual_location]["trees"][tree_key]["hearts"] -= 1
                        print(f"Hearts restantes del tree: {data[actual_location]['trees'][tree_key]['hearts']}")

        # si enemy/fox/tree en ARRIBA:
        if locations[actual_location][playerY - 1][playerX] in ("E", "F", "T"):
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

            elif locations[actual_location][playerY - 1][playerX] == "T":
                # busca cual es el id del tree a la derecha del player
                for tree_key in data[actual_location]["trees"].keys():
                    if data[actual_location]["trees"][tree_key]["ypos"] == playerY - 1 and data[actual_location]["trees"][tree_key]["xpos"] == playerX:
                        print(f"Hearts iniciales del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                        # quitamos 1 corazon al tree
                        data[actual_location]["trees"][tree_key]["hearts"] -= 1
                        print(f"Hearts restantes del tree: {data[actual_location]['trees'][tree_key]['hearts']}")

        # si enemy/fox/tree en ABAJO:
        if locations[actual_location][playerY + 1][playerX] in ("E", "F", "T"):
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

            elif locations[actual_location][playerY + 1][playerX] == "T":
                # busca cual es el id del tree a la derecha del player
                for tree_key in data[actual_location]["trees"].keys():
                    if data[actual_location]["trees"][tree_key]["ypos"] == playerY + 1 and data[actual_location]["trees"][tree_key]["xpos"] == playerX:
                        print(f"Hearts iniciales del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                        # quitamos 1 corazon al tree
                        data[actual_location]["trees"][tree_key]["hearts"] -= 1
                        print(f"Hearts restantes del tree: {data[actual_location]['trees'][tree_key]['hearts']}")

        # si enemy/fox/tree en DERECHA:
        if locations[actual_location][playerY][playerX - 1] in ("F", "T"):
            if locations[actual_location][playerY][playerX - 1] == "F":
                # solo hay 1 fox en el mapa
                print(f"Hearts iniciales del fox: {data[actual_location]['fox']['hearts']}")
                data[actual_location]["fox"]["hearts"] -= 1
                print(f"Hearts restantes del fox: {data[actual_location]['fox']['hearts']}")
                # te dropea 1 meat

            elif locations[actual_location][playerY][playerX - 1] == "T":
                # busca cual es el id del tree a la derecha del player
                for tree_key in data[actual_location]["trees"].keys():
                    if data[actual_location]["trees"][tree_key]["ypos"] == playerY and data[actual_location]["trees"][tree_key]["xpos"] == playerX - 1:
                        print(f"Hearts iniciales del tree: {data[actual_location]['trees'][tree_key]['hearts']}")
                        # quitamos 1 corazon al tree
                        data[actual_location]["trees"][tree_key]["hearts"] -= 1
                        print(f"Hearts restantes del tree: {data[actual_location]['trees'][tree_key]['hearts']}")


    #---- COOK
    elif pregunta=="cook" and cook==True:
        print("we cookin")

    #---- FISH
    elif pregunta=="fish" and fish==True:
        print("se pesca")

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


                #################################################################################################################################
    ##death_mon

    #enemigos
    if pregunta.lower() == 'go by the e':

        locations[actual_location][playerY][playerX] = playerX, playerY
        E2 = 51, 3

        hipo_e2 = calcular_hipotenusa(locations[actual_location][playerY][playerX], E2)

        E3 = 13, 4

        hipo_e3 = calcular_hipotenusa(locations[actual_location][playerY][playerX], E3)


        if hipo_e2 < hipo_e3:
            locations[actual_location][playerY][playerX] = ' '
            playerY = 3
            playerX = 50
            locations[actual_location][playerY][playerX] ='X'

        else:
            locations[actual_location][playerY][playerX] = ' '
            playerY = 4
            playerX = 12
            locations[actual_location][playerY][playerX] = 'X'

    #fox
    if pregunta.lower() == 'go by the f':
        locations[actual_location][playerY][playerX] = ' '
        playerY = 2
        playerX = 29
        locations[actual_location][playerY][playerX] = 'X'

    #TTT
    if pregunta.lower() == 'go by the t':

        #11,9
        #[playerY][playerX]

        locations[actual_location][playerY][playerX] = playerX , playerY
        tree1 = 19,7

        hipo_tree1=calcular_hipotenusa(locations[actual_location][playerY][playerX], tree1)

        tree2 = 18,8

        hipo_tree2 = calcular_hipotenusa(locations[actual_location][playerY][playerX], tree2)

        tree3 = 18, 9

        hipo_tree3 = calcular_hipotenusa(locations[actual_location][playerY][playerX], tree3)

        if hipo_tree1 < hipo_tree2 and hipo_tree1 < hipo_tree3:
            locations[actual_location][playerY][playerX] = ' '
            playerY = 7
            playerX = 18
            locations[actual_location][playerY][playerX] = 'X'
        elif hipo_tree2 < hipo_tree1 and hipo_tree2 < hipo_tree3:
            locations[actual_location][playerY][playerX] = ' '
            playerY = 8
            playerX = 17
            locations[actual_location][playerY][playerX] = 'X'
        elif hipo_tree3 < hipo_tree1 and hipo_tree3 < hipo_tree2:
            locations[actual_location][playerY][playerX] = ' '
            playerY = 9
            playerX = 17
            locations[actual_location][playerY][playerX] = 'X'



    #s
    if pregunta.lower() == 'go by the s':

        locations[actual_location][playerY][playerX] = playerX, playerY
        S2 = 6, 3

        hipo_s2 = calcular_hipotenusa(locations[actual_location][playerY][playerX], S2)

        S3 = 49, 9

        hipo_s3 = calcular_hipotenusa(locations[actual_location][playerY][playerX], S3)


        if hipo_s2 < hipo_s3:
            locations[actual_location][playerY][playerX] = ' '
            playerY = 3
            playerX = 5
            locations[actual_location][playerY][playerX] = 'X'

        else:
            locations[actual_location][playerY][playerX] = ' '
            playerY = 9
            playerX = 48
            locations[actual_location][playerY][playerX] = 'X'

    #water
    if pregunta.lower() == 'go by the water':
        locations[actual_location][playerY][playerX] = ' '
        playerY = 6
        playerX = 11
        locations[actual_location][playerY][playerX] = 'X'











            #locations[actual_location][playerY][playerX]








    # ---- NO VALIDA
    else:
        print("Invalid action!")

    for y in range(len(locations[actual_location])):
        for x in range(len(locations[actual_location][0])):
            print((locations[actual_location][y][x]), end="")
        print()