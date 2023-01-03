import json
import os


def print_ireq(ireq):
    print('Сейчас требования по инвентарю выглядят так:')
    for u, t in ireq:
        print(f'Что-бы попасть в вершину {u} (индексация с нуля), нужно иметь элемент инвентаря №{t}')


def print_vreq(vreq):
    print('Сейчас требования по посещённым вершинам выглядят так:')
    for u, t in vreq:
        print(f'Что-бы попасть в вершину {u} (индексация с нуля), нужно посетить вершину №{t}')


def print_ilist(ilst):
    print('Сейчас в этих токах обновляется инвентарь так:')
    for u, t in enumerate(ilst):
        print(f'В точке {u} (индексация с нуля), изменяются элементы инвентаря ', *t)


cls = 'cls' if os.name == 'nt' else 'clear'
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)

inv_req = json.load(open('inventory_req_list.json', 'r'))
print_ireq(inv_req)
for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    t = [int(i) for i in input('Введите индекс вершины и поле инвенторя:\n').split()]
    while t in inv_req:
        inv_req.remove(t)
print_ireq(inv_req)
for _ in range(int(input('Введите количество требований по инвентарю, которые вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = int(input('Введите индекс вершины инвентаря (индексация с нуля): '))
    inv_req.append([u, t])
open('inventory_req_list.json', 'w').write(json.dumps(inv_req, indent=4, ensure_ascii=False))
os.system(cls)

visit_req = json.load(open('visited_req_list.json', 'r'))
print_vreq(visit_req)
for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    t = [int(i) for i in input('Введите индексы двух вершин:\n').split()]
    while t in visit_req:
        visit_req.remove(t)
print_vreq(visit_req)
for _ in range(int(input('Введите количество требований по посещённым вершинам, которые вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = int(input('Введите индекс вершины, которую нужно посетить (индексация с нуля): '))
    visit_req.append([u, t])
open('visited_req_list.json', 'w').write(json.dumps(visit_req, indent=4, ensure_ascii=False))
os.system(cls)

inv_list = json.load(open('inventory_list.json', 'r'))
print_ilist(inv_list)
for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    v = int(input('Введите индекс вершины для которой производится удаление: '))
    t = int(input('Введите номер поля инвенторя (индексайия с нуля): '))
    while t in inv_list[v]:
        inv_list[v].remove(t)
print_ilist(inv_list)
for _ in range(int(input('Введите количество изменений инвентаря: '))):
    u = int(input('Введите индекс вершины, в которой меняется инвентарь (индексация с нуля): '))
    t = int(input('Введите индекс вершины инвентаря (индексация с нуля): '))
    inv_list[u].append(t)
open('inventory_list.json', 'w').write(json.dumps(inv_list, indent=4, ensure_ascii=False))
os.system(cls)
