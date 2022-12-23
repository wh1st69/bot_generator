import json
import os
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)
inventory = json.load(open('visited_list.json', 'r'))
print('Сейчас требования по посещ.вершинам выглядят так:')
for u, t in enumerate(inventory):
    print(f'Что-бы попасть в вершину {u} (индексация с нуля), нужно посетить {t} вершину: ')
for i in range(int(input('Введите количество требований по посещённым вершинам, которые вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = input('Введите индекс вершины, которую нужно посетить (индексация с нуля):\n')
    inventory[u] = t
open('visited_list.json', 'w').write(json.dumps(inventory, indent=4, ensure_ascii=False))