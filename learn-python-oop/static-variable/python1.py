class Character:
  jumlah = 0   # variable static (kepunyaan class)
  def __init__(self, name, hp, attack, defense, vision): # magic keyword / constructor in python
      # instance variable / attribute (kepunyaan objek)
      self.name = name
      self.hp = hp
      self.attack = attack
      self.defense = defense
      self.vision = vision
      Character.jumlah += 1
      print("character", self.name, "dibuat, vision :", self.vision)
      print("jumlah character :", Character.jumlah)

character1 = Character("ayaka", 15000, 2500, 700, "cryo")
character2 = Character("Hu Tao", 17000, 1800, 600, "pyro")
character3 = Character("qiqi", 18000, 1200, 900, "cryo")