import os

from flask import Flask, request
import requests
from bot import bot

TOKEN = '664435594:AAHUcl61psQuC5LvPqq7L-JZvMCmOX62SGU'
TOKEN2 = '405823545:AAHT8vByxjot138gjLW4LYT1qIWvALIxFMM'
url = 'https://distaboo.pythonanywhere.com/'

app = Flask(__name__)

bot1 = bot(TOKEN,406407068,app,url)
bot2 = bot(TOKEN2,406407068,app,url)
