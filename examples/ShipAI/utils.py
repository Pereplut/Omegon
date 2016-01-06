# -*- coding: utf-8 -*-
import config
from telebot import types


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

def get_answer(chat_id,msg):

    try:
        command, arg = msg.split(" ", 1)
        list_item=['system A','system B']
        tttDict={'system A':'system A is very big','system B':'system B has only one planet'}
        if arg in list_item:
          tmp_lst=list_item
          return tmp_lst, tttDict
        elif arg =='A' or 'a':
          tmp_lst=config.dict_a.keys()
          tttDict=config.dict_a
          return tmp_lst, tttDict
        elif  arg =='B' or 'b':
          tmp_lst=config.dict_b.keys()
          tttDict=config.dict_b
          return tmp_lst, tttDict

    except ValueError:
            return None