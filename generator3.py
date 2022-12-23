import json
import os
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)
text = json.load(open('text.json', 'r'))
print('Сейчас тексты для вершин графа выглядят так:')
for u, t in enumerate(text):
    print(f'Текст для вершины {u} (индексация с нуля): ')
    print(t)
for i in range(int(input('Введите количество вершин в графе, тексты для которых вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = input('Введите текст для этой вершины:\n')
    text[u] = t
open('text.json', 'w').write(json.dumps(text, indent=4, ensure_ascii=False))
