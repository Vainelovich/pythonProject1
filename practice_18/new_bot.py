import telebot

bot = telebot.TeleBot("5201475702:AAHgAQ4n-alsKOcjkYNm7TTZK_0tyODz_vM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, f"Welcome, {message.chat.username}. How r u?")

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD, Anuta!!!')

bot.polling(none_stop=True)