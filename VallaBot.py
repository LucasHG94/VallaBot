# coding=utf-8

import json
import telegram
import logging
import os
from flask import Flask, request
app = Flask(__name__)

bot=None

@app.route("/mensaje")
def hello():
    print request.data
    return 'hola'

def telebot():
    print("voy a crear el bot")
    TOKEN = '206483377:AAHnQ_ohMuvDhI5mfbDMrHKTnTGIi7YhT6A' # Ponemos nuestro Token generado con el @BotFather
    bot = telegram.Bot(TOKEN)
    bot.setWebhook('https://vallbot.herokuapp.com/mensaje')
    print("bot creado")


if __name__=="__main__":
    print("empiezo")
    app.run(host='0.0.0.0',debug=True,port=int(os.environ.get("PORT",5000)))
    telebot()
