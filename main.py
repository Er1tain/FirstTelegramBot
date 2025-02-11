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

@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Мы облачная платформа для разработчиков и бизнеса. Более детально можешь ознакомиться с нами на нашем сайте!"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://timeweb.cloud/"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)

botTimeWeb.infinity_polling()