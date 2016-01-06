# -*- coding: utf-8 -*-
import config
from telebot import types


def gen_markup(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    #if not message:
    #    list_items=['system A','system B']
    if message =='A' or 'a':
        list_items=config.dict_a
    elif  message =='B' or 'b':
        list_items=config.dict_b
    else: list_items=['system A','system B']
    for el in list_items:
        markup.add(el)
    return markup

def get_answer(chat_id,msg):

    try:
        command, arg = msg.split(" ", 1)
        list_items=['system A','system B']
        tttDict={'system A':'system A is very big','system B':'system B has only one planet'}
        if arg in list_items:
          tmp_lst=list_items
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