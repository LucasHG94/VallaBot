 # coding=utf-8

import json
import telegram
import logging
from telegram.error import NetworkError, Unauthorized
from time import sleep


TOKEN = '206483377:AAHnQ_ohMuvDhI5mfbDMrHKTnTGIi7YhT6A' # Ponemos nuestro Token generado con el @BotFather

#bot.setWebhook('https://api.tekegram.org/bot/'+TOKEN+'/')

def main():
    bot = telegram.Bot(TOKEN) # mi id de usuario: 23709664
    updates = bot.getUpdates()
    text = [u.message.text for u in updates]
    chatId = [u.message.chat.id for i in updates]


    try:
        update_id = len(bot.getUpdates())-1
    except IndexError:
        update_id = None

    lastId = chatId[update_id]
    lastUp = text[update_id]

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        last = 0
        if lastUp == '/t' and last!=len(bot.getUpdates())-1:
            tiempo(bot, lastId)
            last = len(bot.getUpdates())-1

        updates = bot.getUpdates()
        text = [u.message.text for u in updates]
        chatId = [u.message.chat.id for i in updates]
        update_id = len(bot.getUpdates())-1
        lastId = chatId[update_id]
        lastUp = text[update_id]


def tiempo(bot, id):
    bot.sendMessage(chat_id=id, text='El tiempo de hoy: ')

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hola pucelano')

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')

if __name__ == '__main__':
    main()
