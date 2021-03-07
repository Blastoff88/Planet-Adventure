__author__ = 'Zac Keepers and Caleb Durda'


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Martian(Enemy):
    def __init__(self):
        super().__init__(name="Martian", hp=16, damage=5)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=50, damage=15)

class Evil_Psycho_Hippie(Enemy):
    def __init__(self):
        super().__init__(name="Evil Psycho Hippie", hp=1000, damage=50)

class Celestial_Knight(Enemy):
    def __init__(self):
        super().__init__(name="Celestial Knight", hp=200, damage=25)
