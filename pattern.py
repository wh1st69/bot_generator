import telebot
from telebot import types
from json import load, dumps
from TelegramBotData import *
from TelegramBotData import config

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


@bot.message_handler(commands=['start'])
@save_wrapper
def any_msg(message):
    client_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    v = 0
    i = inventory.Inventory()
    save[client_id] = [v, i.__dict__]
    bot.send_message(message.chat.id, "Нажми на команду /restart", reply_markup=keyboard)


@bot.message_handler(commands=['restart'])  # Начать заново
@save_wrapper
def any_msg(message):
    client_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keybord_remove = telebot.types.ReplyKeyboardRemove()
    v = 0
    i = inventory.Inventory()
    bot.send_message(message.chat.id, text[0], reply_markup=keybord_remove)
    for j in inventory.adjacency_list[v]:  # Добавление всех кнопок
        if inventory.go(v, j, i):
            keyboard.add(types.KeyboardButton(text=button[v][j]))
    bot.send_message(message.chat.id, 'Что будете делать;)?', reply_markup=keyboard)
    save[client_id] = [v, i.__dict__]


@bot.message_handler(content_types=["text"])
@save_wrapper
def any_msg(message):
    client_id = message.chat.id
    keybord_remove = telebot.types.ReplyKeyboardRemove()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text not in reverse_button.keys():
        bot.send_message(message.chat.id, "Жмякай кнопки падла!", reply_markup=keyboard)
        return
    u = reverse_button[message.text]
    v = save[client_id][0]
    i = inventory.Inventory()
    print(v, u)
    i.__dict__ = save[client_id][1]
    if u not in inventory.adjacency_list[v]:
        bot.send_message(message.chat.id, f"Жмякай кнопки падла!", reply_markup=keyboard)
        return
    if not inventory.go(v, u, i):
        bot.send_message(message.chat.id, "Ты не можешь это сделать!", reply_markup=keyboard)
        return
    bot.send_message(message.chat.id, text[u], reply_markup=keybord_remove)

    for j in inventory.adjacency_list[u]:
        if inventory.go(u, j, i):
            keyboard.add(types.KeyboardButton(text=button[u][j]))

    i.visit_add(u)
    bot.send_message(message.chat.id, 'Что будете делать;)?', reply_markup=keyboard)
    save[client_id] = [u, i.__dict__]



print(f'{text=}')
print(f'{inventory.adjacency_list=}')
print(f'{save=}')
print(f'{button=}')
print(f'{reverse_button=}')
print(f'{config.BotKey=}')
input()
