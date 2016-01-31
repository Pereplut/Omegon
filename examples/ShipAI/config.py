#!/usr/bin/env python
# -*- coding: utf-8 -*-

#token='162596669:AAFNdt_HmUMk-mK-fD1wU4qm2RUWQgQo0zI'
LanceCrRate=3
CannonCrRate=5
CannonPower=3

dict_a={'system A':'system A descr','val1':'value one','val2':'value data'}
list_a=['system A','val1','val2']
dict_b={'system b':'system b descr','1st planet':'water everywere','2nd planet':'value data','3rd planet':'planet s data'}
list_b=['system b','1st planet','2nd planet','3rd planet']

dict_ship={
'Speed': '7',
'Manoeuvrability': '+20',
'Detection': '15',
'Hull': '38',
'Armour': '18',
'Turret Rating': '1',
'Space': '40',
'SP': '41',
'Weapon Capacity': 'Dorsal 1, Prow 1'}

crit_result=[
            'Holed',
            'Internal Damage',
            'Sensors Damaged',
            'Thrusters damaged',
            'Fire']

class shipFireDrake :
    def __init__(self, name):
        self.name = name

    dict_ship={
        'Speed': '7',
        'Manoeuvrability': '+20',
        'Detection': '15',
        'Hull': '38',
        'Armour': '18',
        'Turret Rating': '1',
        'Space': '40',
        'SP': '41',
        'Weapon Capacity': 'Dorsal 1, Prow 1'}
    def getVal (self,valname):
        return self.dict_ship[valname]




module_list=[
    'Geller Field',
    'M–1.r LifeSustainer',
    'Voidsmen Quarters',
    'R–50 Multi-band Auspex',
    'Dorsal Sunsear Laser Battery',
    'Prow Titanforge LanceWeapon',
    'Compartmentalised Cargo Hold',
    'Reinforced Interior Bulkheads',
    'Luxury Passenger Quarters']