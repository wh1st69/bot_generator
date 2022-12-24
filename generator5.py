import json
import os
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)
button = json.load(open('button.json', 'r'))
print('сейчас кнопки для вершин выглядят вот так:')
for i, l in enumerate(button):
    for j, t in enumerate(l):
        print(f'Переход из вершины {i} в вершину {j} (индексация с нуля) сопровождается текстом:\n{t}')
for i in range(int(input('Введите количество текстов для кнопочек, которое вы хотите добавить: '))):
    u, v = [int(i) for i in input('Введите индексы двух вершин:\n').split()]
    t = input('Введите текст для кнопочки. Важно чтобы у одной вершины не было кнопочек с одинаковым названием\n')
    button[u][v] = t
open('button.json', 'w').write(json.dumps(button, indent=4, ensure_ascii=False))