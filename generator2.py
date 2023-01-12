import json  # Сохранение словарей
import os  # Переход в директорию бота


def print_adj_list(lst):
    """Функция вывода списка смежности"""
    print('Сейчас список смежости бота выглядит так (индексация с нуля):')
    for i, l in enumerate(lst):
        print(f'Из вершины {i} можно попасть в вершины: ', *l)


# Переход в папку бота
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData{sep}static'
os.chdir(s)

# Считывание списка смежности
adj_list = json.load(open('adjacency_list.json', 'r'))

# Вывод списка смежности
print_adj_list(adj_list)

# Удаление ребер
for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    v = int(input('Введите индекс вершины, у которой хотите удалить связь: '))
    u = int(input('Введите индекс вершины, связь с которой хотите удалить: '))
    while u in adj_list[v]:
        adj_list[v].remove(u)

# Вывод списка смежности
print_adj_list(adj_list)

# Добавление новых ребер
for _ in range(int(input('Введите количество ребер в графе, которое вы хотите сейчас добавить: '))):
    u, v = list(map(int, input('Введите номера вершин, между которыми есть ребро (из первой во вторую) (индексация '
                               'идет с нуля): \n').split()))
    adj_list[u].append(v)

# Сохранение изменений
open('adjacency_list.json', 'w').write(json.dumps(adj_list, indent=4, ensure_ascii=False))
