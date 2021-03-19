import random
import items, world
import pickle
import os
import sys
import time

__author__ = 'Zac Keepers and Caleb Durda'

class Give_Item():
    def __init__(self, item):
      self.item = item

    def add_loot(self, the_player):
      the_player.inventory.append(self.item)

    def modify_player(self, the_player):
      self.add_loot(the_player)

class Katana(Give_Item):
    def __init__(self):
      super().__init__(items.Martian_Katana())

class Player():
    def __init__(self):
        self.inventory = [items.Pocket_Knife()]
        self.hp = 180
        self.location_x, self.location_y = world.starting_position
        self.victory = False


    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        for item in self.inventory:
            print('\n')
            print(item, '\n')
        print("You have " + str(items.data.coins) + " coins.\n\n")

    def go_to_space_station(self):
      print("Beaming you up to the Space Station\n\n\n")
      while True:
        os.system('clear')
        print("Welcome to THE SPACE STATION!!!")
        print("1) Blacksmith")	    
        print("2) Exit")
        store_options = ""
        while store_options not in ["1", "2"]:
          store_options = input("> ")
        if store_options == "1":
          os.system('clear')
          print("Welcome to the BLACKSMITH!!!")
          print("You have " + str(items.data.coins) + " coins.")
          print("1) Martian Katana - 60 coins")
          print("2) Acid Grenade - 100 coins")
          print("3) Air Pollution - 150 coins")
          print("4) Exit Shop")
          weapon = ""
          while weapon not in ["1", "2", "3", "4"]:
            weapon = input("> ")
          if weapon == "1":
            martian_katana_price = 60
            if items.data.coins < martian_katana_price:
              os.system('clear')
              print("You do not have enough coins to buy this.\n")
              short = str(martian_katana_price - items.data.coins)
              print("You are " + short + " coins short.")
              time.sleep(2)
            else:
              os.system('clear')
              items.data.coins = items.data.coins - martian_katana_price
              print("You now have " + str(items.data.coins) + " coins.\n")
              print("You now wield the Martian Katana.\n")
              Katana()
          elif weapon == '2':
            print('A')
          elif weapon == '3':
            print('P')
          elif weapon == '4':
            os.system('clear')
            break
        elif store_options == '2':
          os.system('clear')
          break

  
            

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def flee(self, tile):
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def save_and_exit(self):
        pickle.dump(self, open( "saved_player.p", "wb" ))
        pickle.dump(world._world, open( "saved_world.p", "wb" ))
        print("Game saved!")
        exit()
      
      

