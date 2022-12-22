import telebot
from telebot import types
from random import random
from json import load, dumps
from TelegramBotData import inventory as inv
BotKey = '{BotKey}'
bot = telebot.TeleBot(BotKey)

global text
global ways
global button
global reverse_button
global save

text = []
ways = []
button = []
reverse_button = {{}}
save = {{}}

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

@bot.message_handler(commands=['start'])
def any_msg(message):
    client_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    v = 0
    i = inv.Inventory()
    save[client_id] = [v, i.__dict__]
    open("TelegramBotData/save.json", "w").write(dumps(save))
    bot.send_message(message.chat.id, "Нажми на команду /restart", reply_markup=keyboard)


@bot.message_handler(commands=['restart'])  # Начать заново
def any_msg(message):
    client_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keybord_remove = telebot.types.ReplyKeyboardRemove()
    v = 0
    i = inv.Inventory()
    bot.send_message(message.chat.id, text[0], reply_markup=keybord_remove)
    for j in ways[v]:  # Добавление всех кнопок
        if inv.go(v, j, i):
            keyboard.add(types.KeyboardButton(text=button[v][j]))
    # keyboard.add(types.KeyboardButton(text='/restart'))
    bot.send_message(message.chat.id, 'Что будете делать;)?', reply_markup=keyboard)
    save[client_id] = [v, i.__dict__]
    open("TelegramBotData/save.json", "w").write(dumps(save))


@bot.message_handler(content_types=["text"])
def ane_msg(message):
    client_id = message.chat.id
    keybord_remove = telebot.types.ReplyKeyboardRemove()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text not in reverse_button.keys():
        bot.send_message(message.chat.id, "Жмякай кнопки падла!", reply_markup=keyboard)
        return
    u = reverse_button[message.text]
    v = save[client_id][0]
    i = inv.Inventory()
    print(v, u)
    i.__dict__ = save[client_id][1]
    if u not in ways[v]:
        bot.send_message(message.chat.id, f"Жмякай кнопки падла!", reply_markup=keyboard)
        return
    if not inv.go(v, u, i):
        bot.send_message(message.chat.id, "Ты не можешь это сделать!", reply_markup=keyboard)
        return
    bot.send_message(message.chat.id, text[u], reply_markup=keybord_remove)
    if u in [27, 29]:
        bot.send_message(message.chat.id, 'Пошёл нафиг, никакого продолжения', reply_markup=keybord_remove)
        keyboard.add(types.KeyboardButton(text='/restart'))
        bot.send_message(message.chat.id, 'Хочешь начать с начала?', reply_markup=keyboard)
        return

    # if u == 25 or u == 31:  # Пропуск в ад
    #    i.inventory_add(0)
    # if u == 30:  # Получение клинка
    #    i.inventory_add(1)
    # if u == 17:  # Получение молитвы
    #    i.inventory_add(2)
    #
    # if u == 22:  # Чтение молитвы 50%
    #    if random() < 0.5:
    #        keyboard.add(types.KeyboardButton(text=button[22][25]))
    #    else:
    #        keyboard.add(types.KeyboardButton(text=button[22][24]))
    # elif u == 23:  # Чтение молитвы 5%
    #    if random() < 0.95:
    #        keyboard.add(types.KeyboardButton(text=button[23][25]))
    #    else:
    #        keyboard.add(types.KeyboardButton(text=button[23][24]))
    # elif u == 18:  # Проход в комнату с клинком
    #    if random() < 0.1 and not i.inventory_get(1):
    #        keyboard.add(types.KeyboardButton(text=button[18][30]))
    #    else:
    #        keyboard.add(types.KeyboardButton(text=button[18][11]))
    #    for j in ways[u]:
    #        if inv.go(u, j, i) and j != 30 and j != 11:
    #            keyboard.add(types.KeyboardButton(text=button[u][j]))
    #            if (button[u][j] == 'Тебя не должно быть здесь'):
    #                print(f'Error: {u=} {j=}')
    # elif u == 8:  # Проход в комнату с клинком
    #    if random() < 0.1 and not i.inventory_get(1):
    #        keyboard.add(types.KeyboardButton(text=button[8][30]))
    #    else:
    #        keyboard.add(types.KeyboardButton(text=button[8][11]))
    #    for j in ways[u]:
    #        if inv.go(u, j, i) and j != 30 and j != 11:
    #            keyboard.add(types.KeyboardButton(text=button[u][j]))
    #            if (button[u][j] == 'Тебя не должно быть здесь'):
    #                print(f'Error: {u=} {j=}')
    else:
        for j in ways[u]:
            if inv.go(u, j, i):
                # print(t[u][j])
                keyboard.add(types.KeyboardButton(text=button[u][j]))
    i.visit_add(u)
    # keyboard.add(types.KeyboardButton(text='/restart'))
    bot.send_message(message.chat.id, 'Что будете делать;)?', reply_markup=keyboard)
    save[client_id] = [u, i.__dict__]
    open("TelegramBotData/save.json", "w").write(dumps(save))


if __name__ == '__main__':
    bot.infinity_polling()