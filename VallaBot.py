# coding=utf-8

import json
import telegram
import logging
import os
from flask import Flask
app = Flask(__name__)

@app.route("/mensaje")
def hello():
    print request.data
    return "Hello World!"




def telebot():
    print("voy a crear el bot")
    TOKEN = '206483377:AAHnQ_ohMuvDhI5mfbDMrHKTnTGIi7YhT6A' # Ponemos nuestro Token generado con el @BotFather
    bot = telegram.Bot(TOKEN)
    bot.setWebhook('https://vallbot.herokuapp.com/mensaje')
    print("bot creado")


if __name__=="__main__":
    print("empiezo")
    app.run(debug=True,port=int(os.environ.get("PORT",5000)))
    telebot()
