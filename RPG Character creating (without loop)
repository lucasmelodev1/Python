#class defining area
class Character:
    def __init__(self,name,age,skin,c_class,specie,premium=False,test_class=False,pvp=False):
        self.name = name
        self.age = age
        self.skin = skin
        self.c_class = c_class
        self.specie = specie
        self.premium = premium
        self.test_class = test_class
        self.pvp = pvp
    #Is this a premium character?
    def premium_character(self):
        if self.test_class:
            print("You can't create a premium test class!")
            return
        self.premium = True
    #Is this a test class character?
    def test_class_character(self):
        if self.pvp and self.test_class:
            print("You can't create a pvp test class!")
            return
        self.test_class = True
    #Is this a pvp character?
    def pvp_character(self):
        self.pvp = True
    #Class/specie verification
    def character_class(self):
        if self.c_class == 'Mage' and self.specie == 'Orc':
            print("Orcs can't be mages!")
            return
        if self.c_class == 'Archer' and self.specie != 'Elf':
            print("Archers can be nothing but elfs!")
            return
        if self.c_class == 'Warrior' and self.specie == 'Elf':
            print("Elfs can't be wariors!")
            return
            
#---------------------------------------------------------------------------            
#main app
def createCharacter():
    name = input('How is called your character?\n->')
    age = int(input('Type the age:\n->'))
    skin = input('Type your skin tone:\n->')
    c_class = input('->Warrior\t->Mage\n->Archer\t->Summoner\nSelect a class:\n->').title()
    specie = input('->Orc\t->Elf\n->Human\t->Undead\nSelect a specie:\n->').title()
    premium = input('Is that a premium character?\n1: Yes\t2:No\n->')
    test_character = input('Is that a test character?\n1:Yes\t2:No\n->')
    pvp = input('Is that a pvp character?\n1:Yes\t2:No\n->')
    if premium == '1':
        premium = True
    elif premium == '2':
        premium = False
    else:
        premium = False
    if test_character == '1':
        test_character = True
    elif test_character == '2':
        test_character = False
    else:
        test_character = False
    if pvp == '1':
        pvp = True
    elif pvp == '2':
        pvp = False
    else:
        test_character = False
    return [name,age,skin,c_class,specie,premium,test_character,pvp]
inputs = [i for i in createCharacter()]
c1 = Character(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], inputs[7])
c1.premium_character()
c1.test_class_character()
c1.pvp_character()
c1.character_class()
