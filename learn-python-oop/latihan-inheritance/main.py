from Character_dps import Character_dps
from Character_shield import Character_shield

hutao = Character_dps("hu tao")
noelle = Character_shield("noelle")

hutao.show_info()
noelle.show_info()

hutao.gain_exp = 200
noelle.gain_exp = 250

hutao.show_info()
noelle.show_info()