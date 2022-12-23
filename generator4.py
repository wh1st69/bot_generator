import json
import os
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)
inventory = json.load(open('inventory_list.json', 'r'))
print('Сейчас требования по инвентарю выглядят так:')
for u, t in enumerate(inventory):
    print(f'Что-бы попасть в вершину {u} (индексация с нуля), нужно иметь {t} элемент инвентаря: ')
for i in range(int(input('Введите количество требований по инвентарю, которые вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = input('Введите индекс вершины инвентаря (индексация с нуля):\n')
    inventory[u] = t
open('inventory_list.json', 'w').write(json.dumps(inventory, indent=4, ensure_ascii=False))