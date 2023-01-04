import json  # Сохранение списков
import os  # Переход в другую директорию


def print_texts(texts):
    print('Сейчас тексты для вершин графа выглядят так:')
    for v, txt in enumerate(texts):
		if txt:
        	print(f'Текст для вершины {v} (индексация с нуля): \n"{txt}"')


# Переход в папку бота
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData'
os.chdir(s)

# Считывание текстов вершин
text = json.load(open('text.json', 'r'))

# Вывод текстов
print_texts(text)

for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    u = int(input('Введите индекс вершины, текст которой хотите удалить: '))
	text[u] = ''
	
# Вывод текстов
print_texts(text)

# Обновление текстов вершин
for _ in range(int(input('Введите количество вершин в графе, тексты для которых вы хотите сейчас добавить: '))):
    u = int(input('Введите индекс вершины (индексация с нуля): '))
    t = input('Введите текст для этой вершины:\n')
    text[u] = t

# Сохранение текстов
open('text.json', 'w').write(json.dumps(text, indent=4, ensure_ascii=False))
