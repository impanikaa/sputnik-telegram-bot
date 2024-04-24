import telebot
import json
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

users = {}
with open('documents.json') as f:
    json_string = f.read()
tasks = json.loads(json_string)


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="🤓 Экспериментальное задание №17")
    button_2 = telebot.types.InlineKeyboardButton(text="📖 Ресурсы для подготовки")
    button_3 = telebot.types.InlineKeyboardButton(text="✍️ О проекте")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(chat_id, 'Добро пожаловать в бот Спутник', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == '🤓 Экспериментальное задание №17')
def experimental_task_17(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="О задании")
    button_2 = telebot.types.InlineKeyboardButton(text="Решения 19 типов этого задания")
    button_3 = telebot.types.InlineKeyboardButton(text="Вернуться в главное меню")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(chat_id, 'Что Вас интересует?', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "О задании")
def about_task(message):
    bot.send_message(message.chat.id, "Описание задания")


@bot.message_handler(func=lambda message: message.text == "Решения 19 типов этого задания")
def choose_set(message):
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="1", callback_data='set_1')
    button_second = telebot.types.InlineKeyboardButton(text="2", callback_data='set_2')
    button_third = telebot.types.InlineKeyboardButton(text="3", callback_data='set_3')
    button_fourth = telebot.types.InlineKeyboardButton(text="4", callback_data='set_4')
    button_fifth = telebot.types.InlineKeyboardButton(text="6", callback_data='set_5')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth)
    bot.send_message(chat_id, f'Выберите комплект', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_1')
def first_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="1", callback_data='1_task_1')
    button_second = telebot.types.InlineKeyboardButton(text="2", callback_data='1_task_2')
    button_third = telebot.types.InlineKeyboardButton(text="3", callback_data='1_task_3')
    button_fourth = telebot.types.InlineKeyboardButton(text="4", callback_data='1_task_4')
    button_fifth = telebot.types.InlineKeyboardButton(text="5", callback_data='1_task_5')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Первый комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_2')
def second_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="6", callback_data='2_task_6')
    button_second = telebot.types.InlineKeyboardButton(text="7", callback_data='2_task_7')
    button_third = telebot.types.InlineKeyboardButton(text="8", callback_data='2_task_8')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Второй комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_3')
def third_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="9", callback_data='3_task_9')
    button_second = telebot.types.InlineKeyboardButton(text="10", callback_data='3_task_10')
    button_third = telebot.types.InlineKeyboardButton(text="11", callback_data='3_task_11')
    button_fourth = telebot.types.InlineKeyboardButton(text="12", callback_data='3_task_12')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Третий комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_4')
def fourth_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="13", callback_data='4_task_13')
    button_second = telebot.types.InlineKeyboardButton(text="14", callback_data='4_task_14')
    button_third = telebot.types.InlineKeyboardButton(text="15", callback_data='4_task_15')
    button_fourth = telebot.types.InlineKeyboardButton(text="16", callback_data='4_task_16')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Четвёртый комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_6')
def sixth_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="17", callback_data='6_task_17')
    button_second = telebot.types.InlineKeyboardButton(text="18", callback_data='6_task_18')
    button_third = telebot.types.InlineKeyboardButton(text="19", callback_data='6_task_19')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Шестой комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data[2:7] == 'task_')
def task_information(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="Таблица",
                                                      callback_data=call.data[:2]+'link_table'+call.data[6:])
    button_second = telebot.types.InlineKeyboardButton(text="Инстурцкция",
                                                       callback_data=call.data[:2]+'link_instruction'+call.data[6:])
    button_third = telebot.types.InlineKeyboardButton(text="Бланк",
                                                      callback_data=call.data[:2]+'link_blank'+call.data[6:])
    button_fourth = telebot.types.InlineKeyboardButton(text="Схема",
                                                       callback_data=call.data[:2]+'link_scheme'+call.data[6:])
    button_fifth = telebot.types.InlineKeyboardButton(text="Видео",
                                                      callback_data=call.data[:2]+'video_id'+call.data[6:])
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='set_'+call.data[0])
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Задача ' + call.data[7:],
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: (call.data[1:7] == '_link_' or call.data[1:7] == '_video'))
def links(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    s = call.data[2:-1]
    if s[-1] != '_':
        s = s[:-2]
    else:
        s = s[:-1]
    p = call.data.split('_')[-1]
    print(tasks[p][s])
    if call.data[1:7] == '_video':
        t = 'https://www.youtube.com/watch?v=' + tasks[p][s]
    else:
        t = tasks[p][s]
    print(t)
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data=call.data[:2]+'task_'+p)
    keyboard.add(button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=t,
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'back')
def choose_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="1", callback_data='set_1')
    button_second = telebot.types.InlineKeyboardButton(text="2", callback_data='set_2')
    button_third = telebot.types.InlineKeyboardButton(text="3", callback_data='set_3')
    button_fourth = telebot.types.InlineKeyboardButton(text="4", callback_data='set_4')
    button_fifth = telebot.types.InlineKeyboardButton(text="6", callback_data='set_6')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Выберите комплект", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == '📖 Ресурсы для подготовки')
def resources(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="Для ОГЭ")
    button_2 = telebot.types.InlineKeyboardButton(text="Источники для изучения физики")
    button_3 = telebot.types.InlineKeyboardButton(text="Полезные приложения и сайты для учебы")
    button_4 = telebot.types.InlineKeyboardButton(text="Учебники по физике (углубленные)")
    button_5 = telebot.types.InlineKeyboardButton(text="Вернуться в главное меню")
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    bot.send_message(chat_id, 'Выберите интересующий ресурс', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Для ОГЭ')
def for_oge(message):
    bot.send_message(message.chat.id, "Что-то для ОГЭ")


@bot.message_handler(func=lambda message: message.text == 'Источники для изучения физики')
def sources_for_physics(message):
    bot.send_message(message.chat.id, "Какие-то источники для изучения физики")


@bot.message_handler(func=lambda message: message.text == 'Полезные приложения и сайты для учебы')
def useful_applications(message):
    bot.send_message(message.chat.id, "Какие-то полезные приложения и сайты для учебы")


@bot.message_handler(func=lambda message: message.text == 'Учебники по физике (углубленные)')
def advanced_physics(message):
    bot.send_message(message.chat.id, "Какие-то учебники по физике (углубленные)")


@bot.message_handler(func=lambda message: message.text == '✍️ О проекте')
def about(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="Вернуться в главное меню")
    keyboard.add(button_1)
    bot.send_message(chat_id, 'Описание проекта', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Вернуться в главное меню")
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="🤓 Экспериментальное задание №17")
    button_2 = telebot.types.InlineKeyboardButton(text="📖 Ресурсы для подготовки")
    button_3 = telebot.types.InlineKeyboardButton(text="✍️ О проекте")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(chat_id, 'Добро пожаловать в бот Спутник', reply_markup=keyboard)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
