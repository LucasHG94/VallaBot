# coding=utf-8

import json
import telegram
import logging
from flask import Flask
app = Flask(__name__)

@app.route("/mensaje")
def hello():
    print request.data
    return "Hello World!"


def telebot():
    TOKEN = '206483377:AAHnQ_ohMuvDhI5mfbDMrHKTnTGIi7YhT6A' # Ponemos nuestro Token generado con el @BotFather
    bot = telegram.Bot(TOKEN)
    bot.setWebhook('https://vallbot.herokuapp.com/mensaje')


if __name__=="__main__":
    app.run(port=33507)
    telebot()
