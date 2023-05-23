from Character import Character


# Crée la classe Guerrier ainsi qu'une classe Mage, qui étend la classe Personnage

class Warrior(Character):
    RpgClass = "Warrior"

    def __init__(self, name, life, agility, strength, wit):
        super().__init__(name, life, agility, strength, wit)  # appelle le constructeur de la classe mère
        self.life = 100
        self.agility = 8
        self.strength = 10
        self.wit = 3

    # appelle la méthode attack de la classe mère et le guerrier peut attaquer avec un "marteau" ou une "épée"
    def attack(self, string):
        if string == "hammer" or string == "sword":
            print(self.name + ": My name will go down in history!")
            print(self.name + ": Rrrrrrrrr....")
            print(self.name + ": I'll crush you with my " + string + "!")
        else:
            print("You can't attack with this")


warrior = Warrior("Kevyn", 50, 2, 2, 2)
print(warrior.get_wit())

warrior.attack("hammer")
