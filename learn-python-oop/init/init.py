class Character:
  def __init__(self, name, hp, attack, defense, vision): # magic keyword / constructor in python
      self.name = name
      self.hp = hp
      self.attack = attack
      self.defense = defense
      self.vision = vision

character1 = Character("ayaka", 15000, 2500, 700, "cryo")
print(character1.name)
print(character1.__dict__)

character2 = Character("Hu Tao", 17000, 1800, 600, "pyro")
print(character2.__dict__)