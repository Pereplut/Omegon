# -*- coding: utf-8 -*-
import config
import utils
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)

#def listener(messages):
#    for m in messages:
#        if m.content_type == 'text':
#            bot.send_message(m.chat.id, m.text)

@bot.message_handler(commands=['show'])
def show(message):

    try:
        command, arg = message.text.split(" ", 1)
        markup=utils.gen_markup(arg)
        bot.send_message(message.chat.id, 'choose a view', reply_markup=markup)
        return True
    except AttributeError:
        markup=utils.gen_markup(0)
        bot.send_message(message.chat.id, 'choose a view', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    msg="""
    hello,bot isn't finished now
    """
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    try:
            answer,dictOut=utils.get_answer(message.chat.id,message.text)   # this is LIST
            if not answer:
                bot.send_message(message.chat.id, 'Чтобы что-то случилось, нажмите  /show')

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
    except ValueError:
        bot.send_message(message.chat.id, 'ERROR что-то случилось, нажмите')


if __name__ == '__main__':
    bot = telebot.TeleBot(config.token)
    #bot.set_update_listener(listener)
    bot.polling(none_stop=True)