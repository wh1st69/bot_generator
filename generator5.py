import json  # Сохранение списков
import os  # Переход в другую директорию


def print_buttons(buttons):
    """Функция вывода текстов для кнопок"""
    print('Сейчас кнопки для вершин выглядят вот так:')
    for i, l in enumerate(buttons):
        for j, txt in enumerate(l):
            if txt:
                print(f'Переход из вершины {i} в вершину {j} (индексация с нуля) сопровождается текстом:\n"{txt}"')


# Переход в папку бота
sep = '\\' if os.name == 'nt' else '/'
s = input('Введите адрес папки для бота:\n') + f'{sep}TelegramBotData{sep}static'
os.chdir(s)

# Считывание текстов кнопок
button = json.load(open('button.json', 'r'))

# Вывод текстов
print_buttons(button)

# Удаление текста кнопки
for _ in range(int(input('Введите количество удалений, которое хотите сделать: '))):
    u, v = [int(i) for i in input('Введите индексы вершин, кнопку между которыми вы хотите удалить: ').split()]
    button[u][v] = ''

# Вывод текстов
print_buttons(button)

# Обновление текстов кнопок
for _ in range(int(input('Введите количество текстов для кнопок, которое вы хотите добавить: '))):
    u, v = [int(i) for i in input('Введите индексы двух вершин:\n').split()]
    t = input('Введите текст для кнопочки. Важно чтобы у одной вершины не было кнопочек с одинаковым названием\n')
    button[u][v] = t

# Сохранение текстов
open('button.json', 'w').write(json.dumps(button, indent=4, ensure_ascii=False))
