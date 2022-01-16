class Character:
  def __init__(self, name, hp, attack, defense, vision):
    self.name = name
    self.hp = hp
    self.attack = attack
    self.defense = defense
    self.vision = vision
  
  def attacking(self, opponet):
    print(self.name + " attacks " + opponet.name)
    opponet.attacked(self, self.attack)

  def attacked(self, opponent, oppentsAttack):
    print(self.name + " is attacked by " + opponent.name)
    attackRecieved = oppentsAttack - (self.defense / 2)
    print(self.name + " received " + str(attackRecieved) + " DMG")
    self.hp -= attackRecieved


ayaka = Character("ayaka", 15000, 2300, 600, "cryo")
pyroSlime = Character("pyro slime", 10000, 600, 1500, "pyro")

print("before attack :")
print(ayaka.__dict__)
print(pyroSlime.__dict__, "\n")

print("in attacking :")
ayaka.attacking(pyroSlime)
print('')
pyroSlime.attacking(ayaka)

print("\nafter attack :")
print(ayaka.__dict__)
print(pyroSlime.__dict__)