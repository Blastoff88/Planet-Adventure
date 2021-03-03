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
        super().__init__(name="Martian", hp=10, damage=2)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=30, damage=15)
