import json
import os


def print_texts(texts):
    print('Сейчас тексты для вершин графа выглядят так:')
    for v, txt in enumerate(texts):
        print(f'Текст для вершины {v} (индексация с нуля): \n"{txt}"')


sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)
text = json.load(open('text.json', 'r'))
print_texts(text)
for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    u = int(input('Введите индекс вершины, текст которой хотите удалить: '))
    text[u] = ''
print_texts(text)
for _ in range(int(input('Введите количество вершин в графе, тексты для которых вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = input('Введите текст для этой вершины:\n')
    text[u] = t
open('text.json', 'w').write(json.dumps(text, indent=4, ensure_ascii=False))
