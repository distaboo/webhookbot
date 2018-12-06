import os

from flask import Flask, request
import requests
import telebot

TOKEN = '664435594:AAHUcl61psQuC5LvPqq7L-JZvMCmOX62SGU'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, "Привет")



TOKEN2 = '405823545:AAHT8vByxjot138gjLW4LYT1qIWvALIxFMM'
bot2 = telebot.TeleBot(TOKEN2)



@bot2.message_handler(commands=['start'])
def start(message):
    bot2.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot2.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot2.reply_to(message, "Привет")
bot2.polling()
bot.polling()
