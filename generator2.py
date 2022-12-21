import json
import os
s = input('Введите адрес папки для бота:\n') + '\\TelegramBotData'
os.chdir(s)
l = []
with open('ways.json', 'r') as fp:
    l = json.load(fp)
print('Сейчас список смежости бота выглядит так (индексация с нуля):')
for i in range(len(l)):
    print(f'Из вершины {i} можно попасть в вершины: ', *l[i])
for i in range(int(input('Введите количество ребер в графе, которое вы хотите сейчас добавить: '))):
    u, v = list(map(int, input('Введите номера вершин, между которыми есть ребро (из первой во вторую) (индексация идет с нуля): \n').split()))
    l[u].append(v)
open('ways.json', 'w').write(json.dumps(l, indent=4))