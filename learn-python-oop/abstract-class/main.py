from abc import ABC, abstractmethod

# abstrac class tidak bisa diinstansiasi
class Character(ABC):
  def __init__(self, name, vision):
    self.name = name
    self.vision = vision
  @abstractmethod
  def showInfo(self):  # interface
    pass  # implementasinya ada di class turunannya

class Character_dps(Character):
  def __init__(self, name, vision):
    super().__init__(name, vision)
  def showInfo(self):  # implementasi method abstract
    print(f'{self.name} (dps) with vision {self.vision}')

class Character_shield(Character):
  def __init__(self, name, vision):
    super().__init__(name, vision)
  def showInfo(self):  # implementasi method abstract
    print(f'{self.name} (shield) with vision {self.vision}')

ayaka = Character_dps('ayaka', 'cryo')
noelle = Character_shield('noelle', 'geo')
ayaka.showInfo()
noelle.showInfo()


