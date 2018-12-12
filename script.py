import os

from flask import Flask, request
import requests
import telebot

TOKEN = '664435594:AAHUcl61psQuC5LvPqq7L-JZvMCmOX62SGU'
secret = 'hjrt5344rekjhd4o3weks4'
url = 'https://distaboo.pythonanywhere.com/'+secret
bot = telebot.TeleBot(TOKEN, threaded = False)
bot.remove_webhook()
bot.set_webhook(url = url)

TOKEN2 = '405823545:AAHT8vByxjot138gjLW4LYT1qIWvALIxFMM'
secret2 = 'dshfjglrmken45tlkrje45'
url2 = 'https://distaboo.pythonanywhere.com/'+secret2
bot2 = telebot.TeleBot(TOKEN2, threaded = False)
bot2.remove_webhook()
bot2.set_webhook(url = url2)

app = Flask(__name__)
@app.route('/'+secret, methods = ['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok',200

@app.route('/'+secret2, methods = ['POST'])
def webhook2():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot2.process_new_updates([update])
    return 'ok',200



@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hellouu, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, "Приветики")

@bot2.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot2.reply_to(message, "Приветос")
