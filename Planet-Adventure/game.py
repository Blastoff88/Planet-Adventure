__author__ = 'Zac Keepers and Caleb Durda'
import world
from player import Player
from pathlib import Path
import pickle
import sys
import time
import random


def play(saved_world=None, saved_player=None):
    if saved_world and saved_player:
      start = input('Would you like to start or go to the market. (Type m = market or s = start)\n')
      if start == 's':
        typing ('Starting game...\n\n\n\n')
        time.sleep(3)
        world._world = saved_world
        player = saved_player
      elif start == 'm':
        typing(' market ')
        
    else:
      start = input('Would you like to start or go to the market. (Type m = market or s = start)\n')
      if start == 's':
        typing ('Starting game...\n\n\n\n')
        time.sleep(3)
        world._world = saved_world
        player = saved_player
      elif start == 'm':
        typing(' market ')
        
        world.load_tiles()
        player = Player()
    game_loop(player)

def game_loop(player):
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            ("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break

def check_for_save():
    if Path("saved_player.p").is_file() and Path("saved_world.p").is_file():
        saved_world = pickle.load(open("saved_world.p", "rb"))
        saved_player = pickle.load(open("saved_player.p", "rb"))
        save_exists = True
    else:
        save_exists = False

    if save_exists:
        valid_input = False
        while not valid_input:
            load = input("Saved game found! Do you want to load the game? Y/N ")
            if load in ['Y','y']:
                play(saved_world, saved_player)
                valid_input = True
            elif load in ['N','n']:
                play()
                valid_input = True
            else:
                print("Invalid choice.")
    else:
        play()

typingspeed = 100

def typing(text):
	for letter in text:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(random.random()*6/typingspeed)

typing('Welecome to Planet Adventure!!!\n\n')
check_for_save()



