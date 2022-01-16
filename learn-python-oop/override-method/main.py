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
    super().__init__(name, 100)

  # method-overriding / menimpa method di super class (method dengan nama yang sama yang ada di super class nya)
  @property
  def showInfo():
    pass
  @showInfo.getter
  def showInfo(self):
    return "{} (tipe dps) dengan attack {}".format(self.name, self.attack)

class Character_shield(Character):
  def __init__(self, name):
    super().__init__(name, 50)

hutao = Character_dps('hutao')
noelle = Character_shield('noelle')
print(hutao.name," attack : ", hutao.attack)
print(noelle.name," attack : ", noelle.attack)
print(hutao.showInfo)  # menggunakan method yang ada di class Character_dps
print(noelle.showInfo)  # menggunakan method yang ada di class Character