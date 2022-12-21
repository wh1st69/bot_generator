import telebot
from telebot import types
from json import load
from TelegramBotData import *
bot = telebot.TeleBot(config.BotKey)

inventory.Inventory._node = config.node
inventory.Inventory._size = config.inventory_size
inventory.Inventory._visit_req = [[] for _ in range(inventory.Inventory._node)]
inventory.Inventory._inventory_req = [[] for _ in range(inventory.Inventory._node)]

global text
global ways
global button
global reverse_button
global save

text = []
ways = []
button = []
reverse_button = {}
save = {}

with open('TelegramBotData/text.json') as fp:
    text = load(fp)
with open('TelegramBotData/ways.json') as fp:
    ways = load(fp)
with open('TelegramBotData/button.json') as fp:
    button = load(fp)
with open('TelegramBotData/save.json') as fp:
    save = load(fp)

for i in button:
    for v, k in enumerate(i):
        reverse_button[k] = v 
        
print(f'{text=}')
print(f'{ways=}')
print(f'{save=}')
print(f'{button=}')
print(f'{reverse_button=}')
print(f'{config.BotKey=}')