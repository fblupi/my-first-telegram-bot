#!/usr/bin/python3 -u
import telebot
import time
import urllib
from telebot import types

bot = telebot.TeleBot("180801311:AAHlah5SsktJxmVoMbs4_QueoGpnMwv5F3U")
tiempo = time.strftime("%H horas %M minutos y %S segundos exactamente")

@bot.message_handler(commands=['start'])
def send_photo(message):
    bot.send_message(message.chat.id, 'Este es su cyberasistente Neoalfred. Puede usar: \n - clases\n - día de la semana\n - hora?\n - id?\n - gatete\n - ayuda\n   Espero ser de su agrado, para servirle. \n NOTA:  escriba SIEMPRE en minúscula. \n Cuando no entiendo algo, lo repito. ')

def recibe(messages):
    for m in messages:
        if m.content_type == "text":
            if m.text == "hello friend":
                bot.send_message(m.chat.id, "hola hamijo")
                bot.send_message(m.chat.id, "\n¿qué quieres?")
            elif m.text == "id":
                bot.send_message(m.chat.id, "180801311:AAHlah5SsktJxmVoMbs4_QueoGpnMwv5F3U")
                bot.send_message(m.chat.id, "cuidado con mi código, por favor...")
            elif m.text == "hora":
                bot.send_message(m.chat.id, "Son las " + tiempo")
            elif m.text == "clases":
                bot.send_message(m.chat.id, "Lunes: DES, TID y CC. Martes: DSS, IC y DSS, Miércoles: CC y PGPI, Jueves: IC y PGPI y Viernes: DES y TID")
                bot.send_message(m.chat.id, "Si quieres más detalles, dime qué día es hoy")
            elif m.text == "lunes":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:30 y tienes hora y media de teoría de DES y TID, y dos horas de CC")
            elif m.text == "martes":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:00 y tienes hora y media de teoría de DSS, dos horas de prácticas de IC y hora y media de prácticas de DSS")
            elif m.text == "miercoles":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:30 y tienes dos horas de CC y dos horas de prácticas de PGPI")
            elif m.text == "jueves":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:30 y  tienes dos horas de teoría de IC y de PGPI")
            elif m.text == "viernes":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:00 y  tiene hora y media de prácticas de DES y TID")
            elif m.text == "gracias":
                bot.send_message(m.chat.id, "Un placer")
            elif m.text == "ayuda":
                bot.send_message(m.chat.id, "Puedes preguntar por: 'clases' saludar, decir el día de la semana preguntar la hora 'hora' o mi id 'id'. Escriba siempre en minúscula. Cuando no entiendo algo, lo repito")
            else:
                bot.send_message(m.chat.id,m.text)

bot.set_update_listener(recibe)

bot.polling()
