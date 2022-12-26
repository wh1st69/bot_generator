import telebot
from string import ascii_letters
from random import randint

token = ''.join(map(lambda x: chr(int(x, 16)), open('token', 'r').readlines()))
bot = telebot.TeleBot(token)

s = ''.join([ascii_letters[randint(0, len(ascii_letters)-1)] for _ in range(randint(10, 30))])
print(f'secrete code: {s}')


@bot.message_handler(content_types=["text"])
def any_msg(message):
    if message.text == s:
        bot.send_message(message.chat.id, 'Аккаунт админа подтвержден')
        print(f'admin id: {message.chat.id}')
        bot.stop_polling()


bot.stop_polling()
bot.polling()
