 # coding=utf-8

import telebot

TOKEN = '206483377:AAHnQ_ohMuvDhI5mfbDMrHKTnTGIi7YhT6A' #Ponemos nuestro TOKEN generado con el @BotFather
mi_bot = telebot.TeleBot(TOKEN)                         #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN

def listener(*mensajes):  ##Cuando llega un mensaje se ejecuta esta función
    for n in mensajes:
        for m in n:
            print m.chat.id
            chat_id = m.chat.id
            if m.text == '/t':
                mi_bot.send_message(chat_id, 'aún no se qué tal hace hoy')

mi_bot.set_update_listener(listener) #registrar la funcion listener
mi_bot.polling()

while True: #No terminamos nuestro programa
    pass
