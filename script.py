import os

from flask import Flask, request
import requests
import telebot

TOKEN = '664435594:AAHUcl61psQuC5LvPqq7L-JZvMCmOX62SGU'
secret = 'hjrt5344rekjhd4o3weks4'
url = 'http://distaboo.pythonanywhere.com/'+secret
bot = telebot.TeleBot(TOKEN, threaded = False)
bot.remove_webhook()
bot.set_webhook(url = url)

app = Flask(__name__)
@app.route('/'+secret, methods = ['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok',200



@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, "Привет")
