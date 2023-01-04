import json  # Сохранение списков
import os  # Переход в другую директорию


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


# Переход в папку бота
cls = 'cls' if os.name == 'nt' else 'clear'
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)

# Требования по предметам в инвентаре
# Считывание требований
inv_req = json.load(open('inventory_req_list.json', 'r'))

# Вывод требований
print_ireq(inv_req)

for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    t = [int(i) for i in input('Введите индекс вершины и поле инвенторя:\n').split()]
    while t in inv_req:
        inv_req.remove(t)
		
# Вывод требований
print_ireq(inv_req)

# Добавление новых требований
for _ in range(int(input('Введите количество требований по инвентарю, которые вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = int(input('Введите индекс вершины инвентаря (индексация с нуля): '))
    inv_req.append([u, t])

# Сохранение
open('inventory_req_list.json', 'w').write(json.dumps(inv_req, indent=4, ensure_ascii=False))
os.system(cls)


# Требования по посещенным вершинам
# Считывание требований
visit_req = json.load(open('visited_req_list.json', 'r'))

# Вывод требований
print_vreq(visit_req)

for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    t = [int(i) for i in input('Введите индексы двух вершин:\n').split()]
    while t in visit_req:
        visit_req.remove(t)
		
# Вывод требований
print_vreq(visit_req)

# Добавление новых требований
for _ in range(int(input('Введите количество требований по посещённым вершинам, которые вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = int(input('Введите индекс вершины, которую нужно посетить (индексация с нуля): '))
    visit_req.append([u, t])

# Сохранение
open('visited_req_list.json', 'w').write(json.dumps(visit_req, indent=4, ensure_ascii=False))
os.system(cls)


# Обновления полей инвентаря
# Считывание
inv_list = json.load(open('inventory_list.json', 'r'))

# Вывод
print_ilist(inv_list)

for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    v = int(input('Введите индекс вершины для которой производится удаление: '))
    t = int(input('Введите номер поля инвенторя (индексайия с нуля): '))
    while t in inv_list[v]:
        inv_list[v].remove(t)

# Вывод
print_ilist(inv_list)

# Обновление
for _ in range(int(input('Введите количество изменений инвентаря: '))):
    u = int(input('Введите индекс вершины, в которой меняется инвентарь (индексация с нуля): '))
    t = int(input('Введите индекс вершины инвентаря (индексация с нуля): '))
    inv_list[u].append(t)

# Сохранение
open('inventory_list.json', 'w').write(json.dumps(inv_list, indent=4, ensure_ascii=False))
os.system(cls)
