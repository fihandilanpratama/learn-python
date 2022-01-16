class Character:
  # privat class variable
  __jumlah = 0
  def __init__(self, name):
    self.name = name
    Character.__jumlah += 1

  # method ini hanya berlaku untuk objek
  def getJumlah(self):
    return Character.__jumlah

  # method ini belaku untuk class
  def getJumlah2():
    return Character.__jumlah

  # static method (decorator), nempel ke objek dan class
  @staticmethod
  def getJumlah3():
    return Character.__jumlah

  # class method (bisa untuk class & object)
  @classmethod
  def getJumlah4(cls):
    return cls.__jumlah

ayaka = Character('ayaka')
print(ayaka.getJumlah3())
hutao = Character('hutao')
print(Character.getJumlah3())
print(hutao.getJumlah4())
