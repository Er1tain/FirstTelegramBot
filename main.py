from telebot import TeleBot, types

botTimeWeb = TeleBot('7202504458:AAFLN8AC95eQNEbpMJBDU9HsWRklQ26NrhE')  #Уникальный токен бота

#Реализуем /start
@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f'Приветствую, друг мой! Начнём работу)'
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
    markup.add(button_yes)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)