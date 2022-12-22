import json
import os
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)
l = []
with open('text.json', 'r') as fp:
    l = json.load(fp)
print('Сейчас тексты для вершин графа выглядят так:')
for u, t in enumerate(l):
    print(f'Текст для вершины {u} (индексация с нуля): ')
    print(t)
for i in range(int(input('Введите количество ребер в графе, которое вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = input('Введите текст для этой вершины:\n')
    l[u] = t
open('text.json', 'w').write(json.dumps(l, indent=4))