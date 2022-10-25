import telebot
import password

token1 = password.token
bot = telebot.TeleBot(token1)

@bot.message_handler(content_types=['text'])
def write_message(message):
   if message.text == "1": #число
      bot.send_message(message.from_user.id, "Я не понимаю чисел, введи текст!")
   elif message.text == "hey": #текст на английском
      bot.send_message(message.from_user.id, "Я не понимаю английского языка, пиши по русски")
   elif message.text == "/":#символы
      bot.send_message(message.from_user.id, "Что за каракули? Пиши тест")
   else:
      bot.send_message(message.from_user.id, "Привет, я Валютный бот\nДля начала обмена введите exchange")
@bot.message_handler(commands=['exchange'])
def exchange_message(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   row1 = keyboard.row(telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'))
   row2 = keyboard.row(telebot.types.InlineKeyboardButton('RUR', callback_data='get-RUR'), telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'))
   keyboard.add (row1, row2)
   bot.send_message(message.from_use.id, 'Выберите валюту для обмена', reply_markup=keyboard)
   
bot.polling(none_stop=True, interval=0)