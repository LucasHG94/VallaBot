# coding=utf-8

import json
import telegram
import logging
import os
import urllib2
import json
from flask import Flask, request
app = Flask(__name__)
TOKEN = '206483377:AAHnQ_ohMuvDhI5mfbDMrHKTnTGIi7YhT6A' # Ponemos nuestro Token generado con el @BotFather
bot=None

@app.route("/mensaje",methods=['POST'])
def hello():
    if request.method == "POST":
        # print request.data #int(request.data["message"]["chat"]["id"]) 23709664
        #telegram.Bot(TOKEN).sendMessage(chat_id=23709664, text=request.data)

        update = telegram.Update.de_json(request.get_json(force=True))
        chat_id = update.message.chat.id
        telegram.Bot(TOKEN).sendMessage(chat_id=chat_id, text=tiempo())
        #telegram.Bot(TOKEN).sendMessage(chat_id=chat_id, text="La temperatura es: "+str(tiempo()))
    return "Hola"

def telebot():
    print("voy a crear el bot")
    bot = telegram.Bot(TOKEN)
    bot.setWebhook('https://vallbot.herokuapp.com/mensaje')
    print("bot creado")

def tiempo():
    req = urllib2.Request("https://api.forecast.io/forecast/bc81c2ffb5df746f4ad745932d67c536/41.651981,%20-4.728561?units=si")
    opener = urllib2.build_opener()
    f = opener.open(req)
    j = json.loads(f.read())
    return "Actual: "+ str(j["currently"]["temperature"])+"ºC, "\
        +str(j["currently"]["summary"])+" \nMáxima: "\
        +str(j["daily"]["data"][0]["temperatureMax"])+"ºC\nMínima: "\
        +str(j["daily"]["data"][0]["temperatureMin"])+"ºC"
if __name__=="__main__":
    print("empiezo")
    telebot()
    app.run(host='0.0.0.0',debug=True,port=int(os.environ.get("PORT",5000)))
