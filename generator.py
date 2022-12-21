import os
import shutil
s = input('Введите адрес папки для бота:\n')
l = ''.join(open('pattern.txt', 'r').readlines())
l = l.format(BotKey=input('Введите ключ бота:\n'))
d = os.getcwd()
os.chdir(s)
if 'TelegramBotData' not in os.listdir(path='.'):
    os.mkdir('TelegramBotData')
open('bot.py', 'w').write(l)
open('TelegramBotData\\__init__.py', 'w').write('import TelegramBotData.inventory')
shutil.copy(d + '\\TelegramBotData\\inventory.py', 'TelegramBotData\\inventory.py')
shutil.copy(d + '\\TelegramBotData\\__init__.py', 'TelegramBotData\\__init__.py')
open('TelegramBotData\\save.json', 'w').write('{}')
open('TelegramBotData\\text.json', 'w').write('[]')
open('TelegramBotData\\ways.json', 'w').write('[]')
open('TelegramBotData\\button.json', 'w').write('[]')