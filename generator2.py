import json
import os
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)
adj_list = json.load(open('adjacency_list.json', 'r'))
print('Сейчас список смежости бота выглядит так (индексация с нуля):')
for i, l in enumerate(adj_list):
    print(f'Из вершины {i} можно попасть в вершины: ', *l)
for i in range(int(input('Введите количество ребер в графе, которое вы хотите сейчас добавить: '))):
    u, v = list(map(int, input('Введите номера вершин, между которыми есть ребро (из первой во вторую) (индексация '
                               'идет с нуля): \n').split()))
    adj_list[u].append(v)
open('adjacency_list.json', 'w').write(json.dumps(adj_list, indent=4, ensure_ascii=False))
