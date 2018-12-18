def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit


from playerClass import Player
from playerClass import Alien
import random

name = input("Type in your player name: ")

player = {'a':Player(name)}
badguy = {'a':Alien("Sectoid"), 'b':Alien("Sectopod"), 'c':Alien("Mechtoid"), 'd':Alien("Thin Man"), 'e':Alien("Chosen"), 'f':Alien("Muton"), 'g':Alien("Chryssalid")}
score = 0

print ()
print ('*' * 30)
print ("You are %s" %name)
print (player['a'])
print ('*' * 30)
print ()

player_character = player['a']

def generateBadGuy():
    encounter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    enemy_character = badguy[encounter]
    print ()
    print ('*' * 30)
    print ("A random", badguy[encounter].name, "appears")
    print (badguy[encounter])
    print ('*' * 30)
    return badguy[encounter]

enemy_character = generateBadGuy()

while player_character.hp >0:
    print
    action = input("Do you attack, defend or heal? atk/def ")
    if action == 'atk':
        print ('*' * 30)
        player_character.atk(enemy_character)
        print (enemy_character)
        if enemy_character.alive:
            enemy_character.atk(player_character)
        print (player_character)
        print ('*' * 30)
    elif action == 'def':
        print ('*' * 30)
        enemy_character.weakened_atk(player_character)
        print (player_character)
        print ('*' * 30)
    elif action == 'heal' and player_character.hp>=1:
        print ('*' * 30)
        player_character.heal()
        enemy_character.atk(player_character)
        print (player_character)
        print ('*' * 30)
    else:
        print ('*' * 30)
        print ("You did nothing!")
        enemy_character.atk(player_character)
        print (player_character)
        print ('*' * 30)
    if not enemy_character.alive and player_character.hp>0:
        score+=1
        badguy = {'a':Alien("Sectoid"), 'b':Alien("Sectopod"), 'c':Alien("Mechtoid"), 'd':Alien("Thin Man"), 'e':Alien("Chosen"), 'f':Alien("Muton"), 'g':Alien("Chryssalid")}
        enemy_character = generateBadGuy()

k= input("Game over. Score: %i kills" %score)
