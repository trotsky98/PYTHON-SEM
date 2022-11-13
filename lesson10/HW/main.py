import telebot
from tok import token
from board import calculater
from log import *


bot = telebot.TeleBot(token)
value = ''          # текущее значение калькулятора
start_value = ''


@bot.message_handler(commands=["start", "calculater"])              # функция отправки сообщения
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)
    logger.debug('"start" - the program works perfectly!')
    

@bot.callback_query_handler(func=lambda call: True)             # обработчик событий 
def callback_func(query):
    global value,start_value
    data =  query.data               # data - это то,чему равен аргумент нажатой кнопки

    if data == "C":
        value = ""
        logger.debug("Сброс значения пользователем")

    elif data == "<=":
        if value != '':
            value = value[:len(value)-1]
    elif data == "=":
        try:             # обработчик исключений
            value = str(eval(value))        # выводим результат при помощи метода eval, конвертируя в строку
        except:
            value = "Ошибка!"
            logger.debug('Не верный ввод пользователем')

    else:
        value += data

    if (value != start_value and value != '') or ('0' != start_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text = "0", reply_markup=keyboard)
            start_value = "0"
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text = value, reply_markup=keyboard)
            start_value = value

    if value == "Ошибка!": 
        value = ''

    logger.debug(f'Пользователь ввел {value}')

@bot.message_handler(content_types=["text"]) # обрабатывает сообщения от пользователя
def mess(message):
    mess = f'{message.from_user.first_name}, пожалуйста, кликай кнопки калькулятора!'
    bot.send_message(message.chat.id,mess)
    logger.debug('Не верный ввод пользователем')

keyboard = calculater()

bot.polling(none_stop=False, interval=0) 