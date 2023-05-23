from Character import Character


class Mage(Character):
    RpgClass = "Mage"

    def __int__(self, name, life, agility, strength, wit):
        super().__init__(name, life, agility, strength, wit)  # appelle le constructeur de la classe mère
        self.life = 70
        self.agility = 10
        self.strength = 3
        self.wit = 10

    # appelle la méthode attack de la classe mère et le mage peut attaquer avec une "baguette" ou de la "magie"
    def attack(self, string):
        if string == "wand" or string == "magic":
            print(self.name + ": May the gods be with me.")
            print(self.name + ": Rrrrrrrrr....")
            print(self.name + ": Feel the power of my " + string + "!")
        else:
            print("You can't attack with this")


mage = Mage("VynoDePal", 50, 2, 2, 2)
print(mage.get_agility())

mage.attack("magic")
