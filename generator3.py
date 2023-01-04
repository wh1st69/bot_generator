import json  # Сохранение списков
import os  # Переход в другую директорию

# Переход в папку бота
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)

# Считывание текстов вершин
text = json.load(open('text.json', 'r'))

# Вывод текстов
print('Сейчас тексты для вершин графа выглядят так:')
for u, t in enumerate(text):
    if t:
        print(f'Текст для вершины {u} (индексация с нуля): \n{t}')

# Обновление текстов вершин
for i in range(int(input('Введите количество вершин в графе, тексты для которых вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = input('Введите текст для этой вершины:\n')
    text[u] = t

# Сохранение текстов
open('text.json', 'w').write(json.dumps(text, indent=4, ensure_ascii=False))
