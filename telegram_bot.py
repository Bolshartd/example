import telebot

token = '5624394655:AAE1_44oPShmKaGaKw_8uk5nDSpk6aB584U'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def write_message(message):
   bot.send_message(message.from_user.id, "Приветствую, друг!")
bot.polling(none_stop=True, interval=0)