import os
import shutil
import json
import telebot
from string import ascii_letters
from random import randint

sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n')
BotKey = input('Введите ключ бота:\n')
n = int(input('Введите количество вершин в графе: '))
i = int(input('Введите число используемых полей инвенторя: '))

token = ''.join(map(lambda x: chr(int(x, 16)), open('TelegramBotGeneratorData/token', 'r').readlines()))
bot = telebot.TeleBot(token)

code = ''.join([ascii_letters[randint(0, len(ascii_letters)-1)] for _ in range(randint(10, 30))])
print('Сейчас программа зафиксирует ваш TelegramID для корректной работы админки')
print(f'Секретный код: {code}')
print('Его нужно отправить боту @verification_4_bot_generator_bot')
AdminID = -1


@bot.message_handler(content_types=["text"])
def any_msg(message):
    if message.text == code:
        bot.send_message(message.chat.id, 'Аккаунт админа подтвержден')
        global AdminID
        AdminID = message.chat.id
        print('Аккаунт админа зафиксирован')
        print('Ожидайте создания всех необходимых файлов')
        bot.stop_polling()


bot.stop_polling()
bot.polling()
cfg = ''.join(open(f'TelegramBotGeneratorData{sep}config.py').readlines()).format(
    node=n, inventory_size=i, BotKey=BotKey, AdminId=AdminID)
d = os.getcwd()
os.chdir(s)
if 'TelegramBotData' not in os.listdir(path='.'):
    os.mkdir('TelegramBotData')

shutil.copy(d + f'{sep}TelegramBotGeneratorData{sep}inventory.py', f'TelegramBotData{sep}inventory.py')
shutil.copy(d + f'{sep}TelegramBotGeneratorData{sep}__init__.py', f'TelegramBotData{sep}__init__.py')
shutil.copy(d + f'{sep}TelegramBotGeneratorData{sep}pattern.py', 'bot.py')

open(f'TelegramBotData{sep}config.py', 'w').write(cfg)
open(f'TelegramBotData{sep}save.json', 'w').write(json.dumps({}, indent=4, ensure_ascii=False))
open(f'TelegramBotData{sep}text.json', 'w').write(json.dumps([''] * n, indent=4, ensure_ascii=False))
open(f'TelegramBotData{sep}adjacency_list.json', 'w').write(
    json.dumps([[] for _ in range(n)], indent=4, ensure_ascii=False))
open(f'TelegramBotData{sep}button.json', 'w').write(
    json.dumps([['' for _ in range(n)] for _ in range(n)], indent=4, ensure_ascii=False))


open(f'TelegramBotData{sep}inventory_req_list.json', 'w').write(
    json.dumps([], indent=4, ensure_ascii=False))
open(f'TelegramBotData{sep}visited_req_list.json', 'w').write(
    json.dumps([], indent=4, ensure_ascii=False))
open(f'TelegramBotData{sep}inventory_list.json', 'w').write(
    json.dumps([[] for _ in range(n)], indent=4, ensure_ascii=False))
