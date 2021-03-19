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

class Martian_Katana(Weapon):
    def __init__(self):
        super().__init__(name="Martian Katana",
                         description="A sharp curved blade once wielded by martians.",
                         value=45,
                         damage=450)

class Acid_Grenade(Weapon):
    def __init__(self):
        super().__init__(name="Acid Grenade",
                         description="A grenade that shoots out deadly acid instead of small metal pieces.",
                         value=85,
                         damage=750)

class Air_Pollution(Weapon):
    def __init__(self):
        super().__init__(name="Air Pollution",
                         description="The best weapon in the game!!!",
                         value=135,
                         damage=1000)

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


class Data():
	def __init__(self):
		self.coins = 0

data = Data()
