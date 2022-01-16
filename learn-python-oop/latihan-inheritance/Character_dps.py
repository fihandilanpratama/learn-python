from Character import Character

class Character_dps(Character):
  def __init__(self, name):
    super().__init__(name)
    self.hp_pool = [0,50,100,150,200,250]
    self.attack_pool = [0,20,40,60,80,100]
    self.defense_pool = [0, 0.5, 1, 1.5, 2, 2.5]
    self.level_up = 1