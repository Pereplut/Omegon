# -*- coding: utf-8 -*-
import config
import random
from telebot import types

def mkRand(digit):
    M=digit+1
    K=random.randrange(1, M, 1)
    return K


def crResult():
    res=mkRand(5)
    if res ==1 :
        fire=mkRand(10)
        morale=mkRand(5)
        component=config.module_list[mkRand(9)-1]+' is holed'
        #result= component +' is holed, '+fire+' ppl burned, '+morale+' morale is lost'
        return fire,morale,component
    if res==2:
        fire=0;morale=0
        component=config.module_list[mkRand(9)-1] + ' is damaged '
        #result=component+ ' is damaged '
        return fire,morale,component
    if res==3:
        fire=0;morale=0
        component="sensors are destroyed, we are blind now"
        return fire,morale,component
    if res==4:
        tmpVal=mkRand(10)
        if tmpVal>7:
            component= "Thrusters are damaged beyond repair"
        else :
            component= "Thrusters are damaged by enemy fire"
        fire=0;morale=0
        return fire,morale,component
    if res==5:
        fire=mkRand(5)
        morale=mkRand(10)
        component=config.module_list[mkRand(9)-1] +' burning now '
        #result= component +' burning now '+fire+' ppl burned alive, '+morale+' morale is lost'
        return fire,morale,component
def fire_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    dakka_type=['Lance','Macro 1','Macro 2']
    for el in dakka_type:
        markup.add(el)
    return markup

def gen_dmg():
    return None
#hp=hull point, cp=crew points, mp= morale points,module -damaged ship module
def gen_answer(hp,cp,mp,module):
    HP,CP,MP,Mod='0','0','0','.'
    if hp:
        HP=str(hp) +' structure points are destroyed, '
    if cp:
        CP= str(220*cp)+ ' ppl are died, '
    if mp:
        MP='morale is reduced='+str(mp)+ ' '
    if module:
        Mod=module
    txtOutput= HP+CP+MP+Mod
    #if
    return txtOutput

def LanceCalc(intValue):
    tmp_val=mkRand(100)
    #strOutValue=''
    if tmp_val >intValue:
        #strOutValue= "toHit roll failed, {0} rolled and BS just {1}".format(tmp_val,intValue)
        HullDmg,MoralDmg,CrewDmg,Module=0,0,0,'.'
        return  HullDmg,MoralDmg,CrewDmg,Module
    else:
        succ_res=((intValue -tmp_val)/10) -1
        if (succ_res -config.LanceCrRate)>=0:
            crDmg=mkRand(10)+4

            HullDmg=crDmg
            #new_output1=HullDmg+" hullpoints crashed, "
            MoralDmg,CrewDmg,Module=crResult()
            MoralDmg+=HullDmg
            CrewDmg+=HullDmg
            #new_output1+= txt1
            #strOutValue=new_output1
            return  HullDmg,MoralDmg,CrewDmg,Module
            """
            else:
                Hull="1"
                new_output2=Hull+" hullpoints crashed, "
                txt2=str(crResult())
                new_output2+= txt2
                strOutValue=new_output2
            """
        else:
            HullDmg= mkRand(10)+4
            MoralDmg=HullDmg
            CrewDmg=HullDmg
            Module='.'
            #k="Hull gets "+str(K)+" points of damage"
            #strOutValue=k
            return  HullDmg,MoralDmg,CrewDmg,Module



    #return  HullDmg,MoralDmg,CrewDmg,Module # hp,cp,mp,module

def MacroCalc(intBSValue,intCannonNum=0):
    tmp_val=mkRand(10)
    CannonNumber=config.CannonPower*intCannonNum
    #strOutValue=''
    if tmp_val >intBSValue:
        hp,cp,mp=0,0,0
        strOutValue= "Only minmatarians use to shoot with projectile, aren't you? toHit roll failed, {0} rolled and BS just {1}".format(tmp_val,intBSValue)
        return hp,cp,mp,strOutValue
    elif (intBSValue -tmp_val) < 20:
        hp,cp,mp=0,0,0
        strOutValue='shields absorbs all damage'
        return hp,cp,mp,strOutValue
    else:
        if CannonNumber>=config.CannonCrRate:
            succ_res=((intBSValue -tmp_val)/10) -1
            if (succ_res -config.CannonCrRate )>=0:
                #crDmg=mkRand(10)
                HullDmg=0
                for elem in range(succ_res-1):
                    HullDmg+=mkRand(10)
                if HullDmg>int(config.dict_ship['Armour']):
                    HullDmg-=int(config.dict_ship['Armour'])
                    #new_output1=HullDmg+" hullpoints crashed, "
                    MoralDmg,CrewDmg,Module=crResult()
                    MoralDmg+=HullDmg
                    CrewDmg+=HullDmg
                    #new_output1+= txt1
                    return  HullDmg,MoralDmg,CrewDmg,Module
                else:
                    HullDmg=1
                    #new_output2=Hull+" hullpoints crashed, "
                    MoralDmg,CrewDmg,Module=crResult()
                    MoralDmg+=HullDmg
                    CrewDmg+=HullDmg
                    #new_output2+= txt2
                    return  HullDmg,MoralDmg,CrewDmg,Module
        else:
            succ_res=((intBSValue -tmp_val)/10) -1
            HullDmg=0
            for elem in range(succ_res-1):
                    HullDmg+=mkRand(10)
            if HullDmg > int(config.dict_ship['Armour']):
                HullDmg-=int(config.dict_ship['Armour'])
                strOutValue='.'
            else:
                HullDmg=0
                strOutValue="toHit roll failed, {0} rolled and BS just {1}".format(tmp_val,intBSValue)
            MoralDmg=HullDmg
            CrewDmg=HullDmg
            return HullDmg,MoralDmg,CrewDmg,strOutValue
        #return strOutValue


def gen_markup(order,arg):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    args=str(arg).capitalize()
    list_items=[]
    #if not message:
    #    list_items=['system A','system B']
    if args =='A':
        list_items=config.list_a
    elif  args =='B':
        list_items=config.list_b
    else: list_items=['system A','system B']
    for el in list_items:
        markup.add(el)
    return markup

def dakka_result(chat_id,msg,bsVal,shipClass):
    #this one returns string format
    try:

        bs_val=int(bsVal)
        arg=str(msg)
        if arg =='Lance':
            Hp,Cp,Mp,Module= LanceCalc(bs_val) # text
            output_text=gen_answer(Hp,Cp,Mp,Module)
            return output_text
        elif arg=='Macro 1':
            Hp,Cp,Mp,Module= MacroCalc(bs_val,1) # text
            output_text=gen_answer(Hp,Cp,Mp,Module)
            return output_text
        elif arg=='Macro 2':
            Hp,Cp,Mp,Module= MacroCalc(bs_val,2) # text
            output_text=gen_answer(Hp,Cp,Mp,Module)
            return output_text
        else:
            r='shit happens'
            return r
    except ValueError:
        return None

def get_answer(chat_id,msg):

    try:
        arg = msg
        list_item=['system A','system B',]
        tttDict={'system A':'system A is very big','system B':'system B has only one planet'}
        arg=str(arg).capitalize()
        if arg in list_item:
          tmp_lst=list_item
          return tmp_lst, tttDict
        elif arg =='A':
          tmp_lst=config.dict_a.keys()
          tttDict=config.dict_a
          return tmp_lst, tttDict
        elif  arg =='B':
          tmp_lst=config.dict_b.keys()
          tttDict=config.dict_b
          return tmp_lst, tttDict

    except ValueError:
            return None