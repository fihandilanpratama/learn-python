class Character:
  def __init__(self, name, attack):
    self.name = name
    self.attack = attack
  @property
  def showInfo():
    pass
  @showInfo.getter
  def showInfo(self):
    return "{} dengan attack {}".format(self.name, self.attack)

class Character_dps(Character):
  def __init__(self, name):
    # Character.__init__(self, name, 100)
    super().__init__(name, 100)

class Character_shield(Character):
  def __init__(self, name):
    # Character.__init__(self, name, 50)
    super().__init__(name, 50)

hutao = Character_dps('hutao')
noelle = Character_shield('noelle')
print(hutao.name," attack : ", hutao.attack)
print(noelle.name," attack : ", noelle.attack)
print(noelle.showInfo)
print(hutao.showInfo)