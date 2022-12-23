import json
import os
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)
inventory = json.load(open('requests_list.json', 'r'))
print('Сейчас в этих токах обновляется инвентарь так:')
for u, t in enumerate(inventory):
    print(f'В точке {u} (индексация с нуля), изменятся {t} элемент инвентаря: ')
for i in range(int(input('Введите количество изменений инвентаря: '))):
    u = int(input('Введите индекс вершины, в которой меняется инвентарь (индексация с нуля): '))
    t = input('Введите индекс вершины инвентаря (индексация с нуля):\n')
    inventory[u] = t
open('requests_list.json', 'w').write(json.dumps(inventory, indent=4, ensure_ascii=False))