from Character import Character

class Character_shield(Character):
  def __init__(self, name):
    super().__init__(name)
    self.hp_pool = [0,200,300,400,500,600]
    self.attack_pool = [0,20,40,60,80,100]
    self.defense_pool = [0, 2, 4, 6, 8, 10]
    self.level_up = 1