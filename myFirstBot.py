#!/usr/bin/python -u
import telebot
import time
import urllib
from telebot import types

bot = telebot.TeleBot("180801311:AAHlah5SsktJxmVoMbs4_QueoGpnMwv5F3U")
tiempo = time.strftime("%H horas %M minutos y %S segundos exactamente")

@bot.message_handler(commands=['start'])
def recibe(messages):
    for m in messages:
        if m.content_type == "text":
            if m.text == "hello":
                bot.send_message(m.chat.id, "hola hamijo")
            elif m.text == "id":
                bot.send_message(m.chat.id, "180801311:AAHlah5SsktJxmVoMbs4_QueoGpnMwv5F3U")
                bot.send_message(m.chat.id, "cuidado con mi codigo, por favor...")
            elif m.text == "hora":
                bot.send_message(m.chat.id, "Son las " + tiempo)
            elif m.text == "clases":
                bot.send_message(m.chat.id, "Lunes: DES, TID y CC. Martes: DSS, IC y DSS, Miercoles: CC y PGPI, Jueves: IC y PGPI y Viernes: DES y TID")
                bot.send_message(m.chat.id, "Si quieres mas detalles, dime que dia es hoy")
            elif m.text == "lunes":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:30 y tienes hora y media de teoria de DES y TID, y dos horas de CC")
            elif m.text == "martes":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:00 y tienes hora y media de teoria de DSS, dos horas de practicas de IC y hora y media de practicas de DSS")
            elif m.text == "miercoles":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:30 y tienes dos horas de CC y dos horas de practicas de PGPI")
            elif m.text == "jueves":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:30 y  tienes dos horas de teoria de IC y de PGPI")
            elif m.text == "viernes":
                bot.send_message(m.chat.id, "Hoy empiezas a las 16:00 y  tiene hora y media de practicas de DES y TID")
            elif m.text == "gracias":
                bot.send_message(m.chat.id, "Un placer")
            elif m.text == "ayuda":
                bot.send_message(m.chat.id, "Puedes preguntar por: 'clases' saludar, decir el dia de la semana preguntar la hora 'hora' o mi id 'id'. Escriba siempre en minuscula. Cuando no entiendo algo, lo repito")
            else:
                bot.send_message(m.chat.id,m.text)

bot.set_update_listener(recibe)

bot.polling()
