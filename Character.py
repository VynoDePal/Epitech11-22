# Crée une classe de personnages abstraite composée des attributs protégés suivants : "name", "life", "agility", "strength", "wit" et un attribut de chaîne constant "RpgClass", avec les getters correspondants

class Character:
    RpgClass = "Character"
    def __init__(self, name, life, agility, strength, wit):
        self.name = name
        self.life = 50
        self.agility = 2
        self.strength = 2
        self.wit = 2

    def moveRight(self):
        print(self.name + ": moves right")

    def moveLeft(self):
        print(self.name + ": moves left")

    def moveBack(self):
        print(self.name + ": moves back")

    def moveForward(self):
        print(self.name + ": moves forward")

    def get_name(self):
        return self.name

    def get_life(self):
        return self.life

    def get_agility(self):
        return self.agility

    def get_strength(self):
        return self.strength

    def get_wit(self):
        return self.wit

    def get_RpgClass(self):
        return self.RpgClass

# Ajoute une méthode d'attaque qui prend une chaîne comme argument et affiche ce qui suit (quel que soit l'argument) :

    def attack(self, string):
        print("Le personnage " + self.name + " attaque avec un/une " + string + ", fait partie de la classe " + self.RpgClass + " et a " + str(self.life) + " points de vie")


character = Character("Jean-luc", 50, 2, 2, 2)
print(character.get_name())
print(character.get_life())
print(character.get_agility())
print(character.get_strength())
print(character.get_wit())

character.attack("epee")