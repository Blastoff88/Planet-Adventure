__author__ = 'Zac Keepers and Caleb Durda'

import items, enemies, actions, world


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, the_player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.SaveAndExit())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return ("""
        You find yourself on a planet with a thick cloud of fog!
        You can make out four paths.
        Which way should you go.
        """)

    def modify_player(self, the_player):
        pass


class EmptyPath(MapTile):
    def intro_text(self):
        return ("""
        Another featureless part of the planet. You must venture onwards.
        """)

    def modify_player(self, the_player):
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)


class FindBlasterRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Blaster())

    def intro_text(self):
        return ("""
        You notice something shiny in the corner of a cliff.
        It's a blaster! You pick it up.
        """)

class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Celestial_Sword())

    def intro_text(self):
        return ("""
        You see a bright light coming from a rock,
        It's the Celestial Sword, that has the power of the cosmos!
        """)

class FindBazookaRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Laser_Bazooka())

    def intro_text(self):
        return ("""
        You notice something shiny and giant laying next to a rock.
        It's a Laser Bazooka! You pick it up.
        """)


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return ("""
        Someone dropped 5 gold pieces. You pick them up.
        """)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            return("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class MartianRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Martian())

    def intro_text(self):
        if self.enemy.is_alive():
            return ("""
            A martian jumps down from a rock in front of you!
            """)
        else:
            return ("""
            The body of a dead martian lays on the ground.
            """)


class DragonRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Dragon())

    def intro_text(self):
        if self.enemy.is_alive():
            return ("""
            A dragon is blocking your path!
            """)
        else:
            return ("""
            A dead dragon reminds you of your triumph.
            """)

class KnightRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Celestial_Knight())

    def intro_text(self):
        if self.enemy.is_alive():
            return ("""
            The Celestial Knight is blocking your path!
            """)
        else:
            return ("""
            The dead Knight reminds you of your success!
            """)

class HippieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Evil_Psycho_Hippie())

    def intro_text(self):
        if self.enemy.is_alive():
            return ("""
            The King of the planet, the Evil Psycho Hippie, is blocking your path!
            """)
        else:
            return ("""
            A dead King reminds you of your victory!
            """)


class SnakePitRoom(MapTile):
    def intro_text(self):
        return ("""
        You have fallen into a pit of deadly snakes!

        You have died!
        """)

    def modify_player(self, player):
        player.hp = 0


class PortalRoom(MapTile):
    def intro_text(self):
        return ("""
        You see a bright light in the distance...
        ... it grows as you get closer! It's a portal to Earth!!!


        Victory is yours!
        """)

    def modify_player(self, player):
        player.victory = True
