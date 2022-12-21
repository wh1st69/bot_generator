import os
import shutil
import json
s = input('Введите адрес папки для бота:\n')
BotKey = input('Введите ключ бота:\n')
n = int(input('Введите количество вершин в графе: '))
i = int(input('Введите число используемых полей инвенторя: '))
l = ''.join(open('TelegramBotData\\config.py').readlines()).format(node=n, inventory_size=i, BotKey=BotKey)
d = os.getcwd()
os.chdir(s)
if 'TelegramBotData' not in os.listdir(path='.'):
    os.mkdir('TelegramBotData')

shutil.copy(d + '\\TelegramBotData\\inventory.py', 'TelegramBotData\\inventory.py')
shutil.copy(d + '\\TelegramBotData\\__init__.py', 'TelegramBotData\\__init__.py')
shutil.copy(d + '\\pattern.py', 'bot.py')

open('TelegramBotData\\config.py', 'w').write(l)
open('TelegramBotData\\save.json', 'w').write('{}')
open('TelegramBotData\\text.json', 'w').write(json.dumps([''] * n, indent=4))
open('TelegramBotData\\ways.json', 'w').write(json.dumps([[] for _ in range(n)], indent=4))
open('TelegramBotData\\button.json', 'w').write(json.dumps([['' for _ in range(n)] for _ in range(n)], indent=4))
