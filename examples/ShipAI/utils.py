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
        fire=str(mkRand(10))
        morale=str(mkRand(5))
        component=config.module_list[mkRand(9)-1]
        result= component +' is holed, '+fire+' ppl burned, '+morale+' morale is lost'
        return result
    if res==2:
        component=config.module_list[mkRand(9)-1]
        result=component+ ' is damaged '
        return result
    if res==3:
        return "sensors are destroyed, we are blind now"
    if res==4:
        tmpVal=mkRand(10)
        if tmpVal>7:
            return "Thrusters completely ruined"
        else :
            return "Thrusters are damaged by enemy fire"
    if res==5:
        fire=str(mkRand(5))
        morale=str(mkRand(10))
        component=config.module_list[mkRand(9)-1]
        result= component +' burning now '+fire+' ppl burned alive, '+morale+' morale is lost'
        return result
def fire_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    dakka_type=['Lance','Macro 1','Macro 2']
    for el in dakka_type:
        markup.add(el)
    return markup

def gen_dmg():
    return None

def LanceCalc(intValue):
    tmp_val=mkRand(100)
    #strOutValue=''
    if tmp_val >intValue:
        strOutValue= "toHit roll failed, {0} rolled and BS just {1}".format(tmp_val,intValue)
    else:
        succ_res=((intValue -tmp_val)/10) -1
        if (succ_res -config.LanceCrRate)>=0:
            crDmg=mkRand(10)
            if crDmg>1:
                Hull=str(crDmg-1)
                new_output1=Hull+" hullpoints crashed, "
                txt1=crResult()
                new_output1+= txt1
                strOutValue=new_output1
            else:
                Hull="1"
                new_output2=Hull+" hullpoints crashed, "
                txt2=str(crResult())
                new_output2+= txt2
                strOutValue=new_output2
        else:
            K= mkRand(10)-1
            k="Hull gets "+str(K)+" points of damage"
            strOutValue=k



    return strOutValue

def MacroCalc(intBSValue,intCannonNum=0):
    tmp_val=mkRand(100)
    CannonNumber=config.CannonPower*intCannonNum
    #strOutValue=''
    if tmp_val >intBSValue:
        strOutValue= "Only MinMatars use to shoot with projectile, are you? toHit roll failed, {0} rolled and BS just {1}".format(tmp_val,intBSValue)
        return strOutValue
    else:
        if CannonNumber>=config.CannonCrRate:
            succ_res=((intBSValue -tmp_val)/10) -1
            if (succ_res -config.CannonCrRate )>=0:
                crDmg=mkRand(10)
                damage=0
                for elem in range(succ_res):
                    damage+=mkRand(10)
                if damage>(config.dict_ship['armour']+1):
                    Hull=str(damage-1-config.dict_ship['armour'])
                    new_output1=Hull+" hullpoints crashed, "
                    txt1=crResult()
                    new_output1+= txt1
                    return new_output1
                else:
                    Hull="1"
                    new_output2=Hull+" hullpoints crashed, "
                    txt2=str(crResult())
                    new_output2+= txt2
                    return new_output2
        else:
            K= mkRand(10)-1
            k="Hull gets "+str(K)+" points of damage"
            strOutValue=k
            return strOutValue
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

def dakka_result(chat_id,msg,bsVal):
    #this one returns string format
    try:
        #list_item=['Lance','Macro 1','Macro 2']
        bs_val=int(bsVal)
        arg=str(msg)
        if arg =='Lance':
            output_text= LanceCalc(bs_val) # text
            return output_text
        elif arg=='Macro 1':
            output_text= MacroCalc(bs_val,1) # text
            return output_text
        elif arg=='Macro 2':
            output_text= MacroCalc(bs_val,2) # text
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