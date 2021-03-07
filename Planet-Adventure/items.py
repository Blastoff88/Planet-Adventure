__author__ = 'Zac Keepers and Caleb Durda'


class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Pocket_Knife(Weapon):
    def __init__(self):
        super().__init__(name="Pocket_Knife",
                         description="A pocket-sized knife, suitable for fighting.",
                         value=5,
                         damage=10)


class Blaster(Weapon):
    def __init__(self):
        super().__init__(name="Blaster",
                         description="A small blaster with some rust. Somewhat more dangerous than a Pocket Knife.",
                         value=30,
                         damage=25)

class Laser_Bazooka(Weapon):
    def __init__(self):
        super().__init__(name="Laser Bazooka",
                         description="A freshly made giant bazooka, that has the ultimate power.",
                         value=250,
                         damage=100)

class Celestial_Sword(Weapon):
    def __init__(self):
        super().__init__(name="Celestial Sword",
                         description="The lost sword of the Celestial Knight, that has the power of the cosmos!",
                         value=1000,
                         damage=500)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin made out of gold".format(str(self.amt)),
                         value=self.amt)
