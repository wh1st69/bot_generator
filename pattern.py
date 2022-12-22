import telebot
from telebot import types
from json import load, dumps
from TelegramBotData import *

bot = telebot.TeleBot(config.BotKey)

inventory.Inventory.node = config.node
inventory.Inventory.size = config.inventory_size
inventory.Inventory.visit_req = [[] for _ in range(inventory.Inventory.node)]
inventory.Inventory.inventory_req = [[] for _ in range(inventory.Inventory.node)]

reverse_button = {}

with open('TelegramBotData/text.json') as fp:
    text = load(fp)
with open('TelegramBotData/adjacency_list.json') as fp:
    inventory.adjacency_list = load(fp)
with open('TelegramBotData/button.json') as fp:
    button = load(fp)
with open('TelegramBotData/save.json') as fp:
    save = load(fp)

for i in button:
    for v, k in enumerate(i):
        reverse_button[k] = v


def save_wrapper(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        open('TelegramBotData/save.json', 'w').write(dumps(save, indent=4, ensure_ascii=False))
    return wrapper


print(f'{text=}')
print(f'{inventory.adjacency_list=}')
print(f'{save=}')
print(f'{button=}')
print(f'{reverse_button=}')
print(f'{config.BotKey=}')
