import numpy

class character:
    def __init__(self) -> None:
        self.str = 10
        self.agi = 10
        self.int = 10
        self.hp_base = 100
        self.hp = self.hp_base + (self.str*100)
        self.speed = 10 + (self.agi*5)
        self.dmg = 10 

        self.inventory_slot_remain = 6
        self.inventory_contain = []

    def equip_item(self,item):
        if self.inventory_slot_remain <= 0:
            print("can not equip the item")
        else:
            self.inventory_contain.append(item.name)
            self.inventory_slot_remain -= 1
            self.dmg += item.dmg
            self.str += item.str
            self.agi += item.agi
            self.int += item.int
            self.hp = self.hp_base + (self.str*100)
    
    def __repr__(self):
        rep = "str = " + str(self.str) + \
            "\nagi = " + str(self.agi) + \
            "\nint = " + str(self.int) + \
            "\nhp = " + str(self.hp)   + \
            "\nspeed = " + str(self.speed)  + \
            "\ndmg = " + str(self.dmg)  + \
            "\ninventory_slot_remain = " + str(self.inventory_slot_remain) + \
            "\ninventory_contain = " + str(self.inventory_contain) 
        return rep

class item:
    def __init__(self,name,dmg,str,agi,int) -> None:
        self.name = name
        self.dmg = dmg
        self.str = str
        self.agi = agi
        self.int = int

tom = character()
sword = item("sword",50,10,10,0)