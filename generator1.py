import os
import shutil
import json

sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n')
BotKey = input('Введите ключ бота:\n')
n = int(input('Введите количество вершин в графе: '))
i = int(input('Введите число используемых полей инвенторя: '))
cfg = ''.join(open(f'TelegramBotData{sep}config.py').readlines()).format(node=n, inventory_size=i, BotKey=BotKey)
d = os.getcwd()
os.chdir(s)
if 'TelegramBotData' not in os.listdir(path='.'):
    os.mkdir('TelegramBotData')

shutil.copy(d + f'{sep}TelegramBotData{sep}inventory.py', f'TelegramBotData{sep}inventory.py')
shutil.copy(d + f'{sep}TelegramBotData{sep}__init__.py', f'TelegramBotData{sep}__init__.py')
shutil.copy(d + f'{sep}pattern.py', 'bot.py')

open(f'TelegramBotData{sep}config.py', 'w').write(cfg)
open(f'TelegramBotData{sep}save.json', 'w').write(json.dumps({}, indent=4, ensure_ascii=False))
open(f'TelegramBotData{sep}text.json', 'w').write(json.dumps([''] * n, indent=4, ensure_ascii=False))
open(f'TelegramBotData{sep}adjacency_list.json', 'w').write(
    json.dumps([[] for _ in range(n)], indent=4, ensure_ascii=False))
open(f'TelegramBotData{sep}button.json', 'w').write(
    json.dumps([['' for _ in range(n)] for _ in range(n)], indent=4, ensure_ascii=False))
