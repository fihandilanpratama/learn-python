class Character:
  def __init__(self, name, health, defend):
    self.__name = name
    self.__health = health
    self.__defend = defend
    self.__info = "name : {} \n\thealth : {}".format(self.__name, self.__health)
  
  @property   # membuat sebuah method seperti property
  def info(self):
    return self.__info
  
  @property
  def defend(self):
    pass

  @defend.getter
  def defend(self):
    return self.__defend

  @defend.setter
  def defend(self, inpt):
    self.__defend = inpt

  @defend.deleter
  def defend(self):
    self.__defend = None

ayaka = Character('ayaka', 15000, 800)
print(ayaka.info)

print('setter and getter untuk __defend :')
print(ayaka.defend)
ayaka.defend = 500
print(ayaka.__dict__)

print('deleter :')
del ayaka.defend
print(ayaka.__dict__)
# print(ayaka.defend)
