import json
import os
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)

inv_req = json.load(open('inventory_req_list.json', 'r'))
print('Сейчас требования по инвентарю выглядят так:')
for u, t in inv_req:
    print(f'Что-бы попасть в вершину {u} (индексация с нуля), нужно иметь элемент инвентаря №{t}')
for i in range(int(input('Введите количество требований по инвентарю, которые вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = int(input('Введите индекс вершины инвентаря (индексация с нуля): '))
    inv_req.append([u, t])
open('inventory_req_list.json', 'w').write(json.dumps(inv_req, indent=4, ensure_ascii=False))

visit_req = json.load(open('visited_req_list.json', 'r'))
print('Сейчас требования по посещ.вершинам выглядят так:')
for u, t in visit_req:
    print(f'Что-бы попасть в вершину {u} (индексация с нуля), нужно посетить вершину №{t}')
for i in range(int(input('Введите количество требований по посещённым вершинам, которые вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = int(input('Введите индекс вершины, которую нужно посетить (индексация с нуля): '))
    visit_req.append([u, t])
open('visited_req_list.json', 'w').write(json.dumps(visit_req, indent=4, ensure_ascii=False))

inv_list = json.load(open('inventory_list.json', 'r'))
print('Сейчас в этих токах обновляется инвентарь так:')
for u, t in enumerate(inv_list):
    print(f'В точке {u} (индексация с нуля), изменяются элементы инвентаря ', *t)
for i in range(int(input('Введите количество изменений инвентаря: '))):
    u = int(input('Введите индекс вершины, в которой меняется инвентарь (индексация с нуля): '))
    t = int(input('Введите индекс вершины инвентаря (индексация с нуля): '))
    inv_list[u].append(t)
open('inventory_list.json', 'w').write(json.dumps(inv_list, indent=4, ensure_ascii=False))
