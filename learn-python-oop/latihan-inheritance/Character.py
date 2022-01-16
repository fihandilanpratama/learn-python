class Character:

  def __init__(self, name):
    self.__hp_pool = [0,100,200,300,400,500]
    self.__attack_pool = [0,10,20,30,40,50]
    self.__defense_pool = [0,1,2,3,4,5]
    self.__name = name
    self.__exp = 0
    self.__level = 0
    

  def show_info(self):
    print("""{} : 
        Level = {}
        Hp = {}
        Attack = {}
        Defense = {}
    """.format(self.__name, 
              self.__level, 
              self.__hp, 
              self.__attack, 
              self.__defense
            )
    )

  @property
  def hp_pool(self):
    pass

  @property
  def attack_pool(self):
    pass

  @property
  def defense_pool(self):
    pass

  @property
  def level_up(self):
    pass

  @property
  def gain_exp(self):
    pass

  @hp_pool.setter
  def hp_pool(self, inputan):
    self.__hp_pool = inputan

  @attack_pool.setter
  def attack_pool(self, inputan):
    self.__attack_pool = inputan

  @defense_pool.setter
  def defense_pool(self, inputan):
    self.__defense_pool = inputan


  @gain_exp.setter
  def gain_exp(self, inputan):
    self.__exp += inputan
    if self.__exp >= 100:
      self.level_up = self.__exp//100
      self.__exp %= 100
  
  @level_up.setter
  def level_up(self, inputan):
    self.__level += inputan
    self.__hp = self.__hp_pool[self.__level]
    self.__attack = self.__attack_pool[self.__level]
    self.__defense = self.__defense_pool[self.__level]
   