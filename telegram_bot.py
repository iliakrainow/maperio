import telebot

bot = telebot.TeleBot('1242649621:AAH0aGPCowr8TVQ2F-zizFJn3JZK0qLkd5Y')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling(none_stop=True, timeout=123)
