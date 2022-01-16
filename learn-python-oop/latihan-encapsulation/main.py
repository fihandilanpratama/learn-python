class Character:
  # private class variable
  __jumlah = 0
  def __init__(self, name, hp, attack, defense):
    self.__name = name
    self.__hpBase = hp
    self.__attackBase = attack
    self.__defenseBase = defense
    self.__level = 1
    self.__exp = 0
    self.__hpMax = self.__hpBase * self.__level
    self.__attack = self.__attackBase * self.__level
    self.__defense = self.__defenseBase * self.__level
    self.__hp = self.__hpMax
    Character.__jumlah += 1
  
  @property
  def info(self):
    return """{} : 
        Level = {}
        Hp = {}/{}
        Attack = {}
        Defense = {}
    """.format(self.__name, self.__level, self.__hp, self.__hpMax, self.__attack, self.__defense)

  @property
  def gainExp(self):
    pass
  
  @gainExp.setter
  def gainExp(self, addExp):
    self.__exp += addExp
    if self.__exp >= 100:
      print(self.__name, 'level up!')
      self.__level += 1
      self.__exp -= 100

      self.__hpMax = self.__hpBase * self.__level
      self.__attack = self.__attackBase * self.__level
      self.__defense = self.__defenseBase * self.__level
  
  def attack(self, opponent):
    self.gainExp = 50


hutao = Character('Hu Tao', 1500, 190, 70)
kairagi = Character('Kairagi', 4000, 300, 100)
print(hutao.info)
# hutao.attack(kairagi)
hutao.attack(kairagi)
print(hutao.info)