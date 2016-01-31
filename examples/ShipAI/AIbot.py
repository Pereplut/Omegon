# -*- coding: utf-8 -*-
import config
import BotToken
import utils
import telebot
from telebot import types
bot = telebot.TeleBot(BotToken.token)

#def listener(messages):
#    for m in messages:
#        if m.content_type == 'text':
#            bot.send_message(m.chat.id, m.text)
#dakka_BS_value=0
shipStats= config.shipFireDrake('testship')


@bot.message_handler(commands=['show'])
def show(message):

    try:
        command, arg = message.text.split(" ", 1)
        markup=utils.gen_markup(command,arg)
        bot.send_message(message.chat.id, 'choose a view', reply_markup=markup)


        return True
    except ValueError:
        markup=utils.gen_markup(0)
        bot.send_message(message.chat.id, 'choose a view', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    msg="""
    hello,bot isn't finished now
    """
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['fire'])
def fire(message):

    try:

        command, BS = message.text.split(" ", 1)
        global dakka_BS_value
        dakka_BS_value=BS
        markup=utils.fire_markup()
        bot.send_message(message.chat.id,'choose a weapon',  reply_markup=markup)

        return True
    except ValueError:
        bot.send_message(message.chat.id, 'specify BS with bonuses')



@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    try:
            answer=utils.dakka_result(message.chat.id,message.text,dakka_BS_value,shipStats)   # this is LIST
            if not answer:
                bot.send_message(message.chat.id, 'Чтобы что-то случилось, нажмите  /fire')
            else :
                keyboard_hider = types.ReplyKeyboardHide()
                bot.send_message(message.chat.id, answer, reply_markup=keyboard_hider)
    except TypeError:
        bot.send_message(message.chat.id, 'ERROR что-то случилось')


"""
            else:
                keyboard_hider = types.ReplyKeyboardHide()
                if message.text in answer:
                 print (message.text)
                 print(dictOut)
                 m=str(message.text)
                 rrr=dictOut[m]
                 bot.send_message(message.chat.id, rrr, reply_markup=keyboard_hider)
                else:
                 bot.send_message(message.chat.id, 'неверный ввод', reply_markup=keyboard_hider)
    except TypeError:
        bot.send_message(message.chat.id, 'ERROR что-то случилось, нажмите')
"""

if __name__ == '__main__':
    #dakka_dice_value=0
    #dakka_bs_value=0
    #bot = telebot.TeleBot(BotToken.token)
    #bot.set_update_listener(listener)
    bot.polling(none_stop=True)