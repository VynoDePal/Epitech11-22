from Character import Character


class Warrior_movable(Character):
    def moveRight(self):
        print(self.name + ": moves right like a bad boy.")

    def moveLeft(self):
        print(self.name + ": moves left like a bad boy.")

    def moveBack(self):
        print(self.name + ": moves back like a bad boy.")

    def moveForward(self):
        print(self.name + ": moves forward like a bad boy.")


warrior = Warrior_movable("DePal", 50, 2, 2, 2)
warrior.moveForward()


class Mage_movable(Character):
    def moveRight(self):
        print(self.name + ": moves right furtively.")

    def moveLeft(self):
        print(self.name + ": moves left furtively.")

    def moveBack(self):
        print(self.name + ": moves back furtively.")

    def moveForward(self):
        print(self.name + ": moves forward furtively.")


mage = Mage_movable("VynoDePal", 50, 2, 2, 2)
mage.moveBack()
