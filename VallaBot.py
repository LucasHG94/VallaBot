# coding=utf-8

import json
import telegram
import logging
import os
from flask import Flask, request
app = Flask(__name__)
TOKEN = '206483377:AAHnQ_ohMuvDhI5mfbDMrHKTnTGIi7YhT6A' # Ponemos nuestro Token generado con el @BotFather
bot=None

@app.route("/mensaje")
def hello():
    print request.data
    telegram.Bot(TOKEN).sendMessage(chat_id=request.data["message"]["chat"]["id"], text="rehola")
    return request.data

def telebot():
    print("voy a crear el bot")
    bot = telegram.Bot(TOKEN)
    bot.setWebhook('https://vallbot.herokuapp.com/mensaje')
    print("bot creado")


if __name__=="__main__":
    print("empiezo")
    telebot()
    app.run(host='0.0.0.0',debug=True,port=int(os.environ.get("PORT",5000)))
