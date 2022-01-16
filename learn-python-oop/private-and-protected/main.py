class Character:
  # private variable
  __privat = "private"
  def __init__(self, name, hp):
    # public variable
    self.name = name
    self.hp = hp

    # instance private variable
    self.__height = 160

    # instance protected variable
    self._race = "asian"


ayaka = Character('ayaka', 1500)

print(ayaka.__dict__)
ayaka.__height = 150   # membuat attribute baru
print(ayaka.__height)  # -> 150
print(ayaka._race)
print(ayaka.__dict__)
