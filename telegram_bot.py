import telebot
import password

token1 = password.token
bot = telebot.TeleBot(token1)

@bot.message_handler(commands=['start'])
def exchange_message(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(telebot.types.InlineKeyboardButton(text = 'USD', callback_data='get-USD'))
   keyboard.add(telebot.types.InlineKeyboardButton(text = 'RUR', callback_data='get-RUR'), telebot.types.InlineKeyboardButton(text = 'EUR', callback_data='get-EUR'))
   bot.send_message(message.chat.id, 'Выберите валюту для обмена', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def write_message(message):
   if message.text == "1": #число
      bot.send_message(message.chat.id, "Я не понимаю чисел, введи текст!")
   elif message.text == "hey": #текст на английском
      bot.send_message(message.chat.id, "Я не понимаю английского языка, пиши по русски")
   elif message.text == "/":#символы
      bot.send_message(message.chat.id, "Что за каракули? Пиши тест")
   elif message.text == "ее":#текст на руссом
      bot.send_message(message.chat.id, "Обычно все люди начинают беседу с привета...")
   else:
      bot.send_message(message.chat.id, "Привет, я Валютный бот\nДля начала обмена нажмите: /start")
     
bot.polling(none_stop=True, interval=0)