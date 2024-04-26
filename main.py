import telebot
import json

from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

users = {}
with open('documents.json') as f:
    json_string = f.read()
documents = json.loads(json_string)
with open('texts.json', encoding='utf-8', mode='r') as f:
    json_string = f.read()
texts = json.loads(json_string)


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="🤓 Экспериментальное задание №17")
    button_2 = telebot.types.InlineKeyboardButton(text="📖 Ресурсы для подготовки")
    button_3 = telebot.types.InlineKeyboardButton(text="✍️ О проекте")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(chat_id, texts['start'], reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == '✍️ О проекте')
def about_project(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, texts['about_project'])


@bot.message_handler(func=lambda message: message.text == '🤓 Экспериментальное задание №17')
def experimental_task_17(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="📌 О задании")
    button_2 = telebot.types.InlineKeyboardButton(text="✅ Решения 19 типов задания №17")
    button_3 = telebot.types.InlineKeyboardButton(text="◀️ Вернуться в главное меню")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(chat_id, texts['experimental'], reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "📌 О задании")
def about_task(message):
    bot.send_message(message.chat.id, texts['about'])


@bot.message_handler(func=lambda message: message.text == "✅ Решения 19 типов задания №17")
def choose_set(message):
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="№1. Выталкивающая сила и её свойства",
                                                      callback_data='set_1')
    button_second = telebot.types.InlineKeyboardButton(text="№2. Жесткость пружины и коэффициенты трения",
                                                       callback_data='set_2')
    button_third = telebot.types.InlineKeyboardButton(text="№3. Электричество",
                                                      callback_data='set_3')
    button_fourth = telebot.types.InlineKeyboardButton(text="№4. Геометрическая оптика", callback_data='set_4')
    button_fifth = telebot.types.InlineKeyboardButton(text="№6. Простейшие механизмы: рычаги и блоки",
                                                      callback_data='set_6')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth)
    bot.send_message(chat_id, f'Выберите комплект:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_1')
def first_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text=texts["task_1"], callback_data='1_task_1')
    button_second = telebot.types.InlineKeyboardButton(text=texts["task_2"], callback_data='1_task_2')
    button_third = telebot.types.InlineKeyboardButton(
        text=texts["task_3"], callback_data='1_task_3')
    button_fourth = telebot.types.InlineKeyboardButton(
        text=texts["task_4"], callback_data='1_task_4')
    button_fifth = telebot.types.InlineKeyboardButton(text=texts["task_5"],
                                                      callback_data='1_task_5')
    button_back = telebot.types.InlineKeyboardButton(text="◀️ Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="✅ Комплект №1. Выберите задание (1-5)",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_2')
def second_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text=texts["task_6"], callback_data='2_task_6')
    button_second = telebot.types.InlineKeyboardButton(text=texts["task_7"],
                                                       callback_data='2_task_7')
    button_third = telebot.types.InlineKeyboardButton(text=texts["task_8"], callback_data='2_task_8')
    button_back = telebot.types.InlineKeyboardButton(text="◀️ Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="✅ Комплект №2. Выберите задание (6-8)",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_3')
def third_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text=texts["task_9"], callback_data='3_task_9')
    button_second = telebot.types.InlineKeyboardButton(text=texts["task_10"],
                                                       callback_data='3_task_10')
    button_third = telebot.types.InlineKeyboardButton(text=texts["task_11"], callback_data='3_task_11')
    button_fourth = telebot.types.InlineKeyboardButton(text=texts["task_12"], callback_data='3_task_12')
    button_back = telebot.types.InlineKeyboardButton(text="◀️ Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="✅ Комплект №3. Выберите задание (9-12)",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_4')
def fourth_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text=texts["task_13"], callback_data='4_task_13')
    button_second = telebot.types.InlineKeyboardButton(text=texts["task_14"], callback_data='4_task_14')
    button_third = telebot.types.InlineKeyboardButton(text=texts["task_15"], callback_data='4_task_15')
    button_fourth = telebot.types.InlineKeyboardButton(text=texts["task_16"], callback_data='4_task_16')
    button_back = telebot.types.InlineKeyboardButton(text="◀️ Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="✅ Комплект №4. Выберите задание (13-16)",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'set_6')
def sixth_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text=texts["task_17"], callback_data='6_task_17')
    button_second = telebot.types.InlineKeyboardButton(text=texts["task_18"], callback_data='6_task_18')
    button_third = telebot.types.InlineKeyboardButton(text=texts["task_19"], callback_data='6_task_19')
    button_back = telebot.types.InlineKeyboardButton(text="◀️ Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="✅ Комплект №6. Выберите задание (17-19)",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data[2:7] == 'task_')
def task_information(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="🔍 Таблица анализа условия",
                                                      callback_data=call.data[:2] + 'link_table' + call.data[6:])
    button_second = telebot.types.InlineKeyboardButton(text="📋 Текстовая инструкция",
                                                       callback_data=call.data[:2] + 'link_instruction' + call.data[6:])
    button_third = telebot.types.InlineKeyboardButton(text="📝 Образец бланка",
                                                      callback_data=call.data[:2] + 'link_blank' + call.data[6:])
    button_fourth = telebot.types.InlineKeyboardButton(text="📊 Рисунок или схема",
                                                       callback_data=call.data[:2] + 'link_scheme' + call.data[6:])
    button_fifth = telebot.types.InlineKeyboardButton(text="📽 Видеоинструкция",
                                                      callback_data=call.data[:2] + 'video_id' + call.data[6:])
    button_back = telebot.types.InlineKeyboardButton(text="◀️ Назад", callback_data='set_' + call.data[0])
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth, button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text='Задача ' + texts[call.data[2:]],
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
    if 'video' in call.data[1:7]:
        t = texts[call.data.split('_')[1]] + 'https://www.youtube.com/watch?v=' + documents[p][s]
    else:
        t = texts[call.data.split('_')[2]] + 'https://disk.yandex.ru/d/' + documents[p][s]
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_back = telebot.types.InlineKeyboardButton(text="◀️ Назад", callback_data=call.data[:2] + 'task_' + p)
    keyboard.add(button_back)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=t,
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'back')
def choose_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="№1. Выталкивающая сила и её свойства",
                                                      callback_data='set_1')
    button_second = telebot.types.InlineKeyboardButton(text="№2. Жесткость пружины и коэффициенты трения",
                                                       callback_data='set_2')
    button_third = telebot.types.InlineKeyboardButton(text="№3. Электричество",
                                                      callback_data='set_3')
    button_fourth = telebot.types.InlineKeyboardButton(text="№4. Геометрическая оптика", callback_data='set_4')
    button_fifth = telebot.types.InlineKeyboardButton(text="№6. Простейшие механизмы: рычаги и блоки",
                                                      callback_data='set_6')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth)
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Выберите комплект:", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == '📖 Ресурсы для подготовки')
def resources(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="Для ОГЭ")
    button_2 = telebot.types.InlineKeyboardButton(text="Физика")
    button_3 = telebot.types.InlineKeyboardButton(text="Сайты и приложения для учебы")
    button_4 = telebot.types.InlineKeyboardButton(text="Учебники для любознательных")
    button_5 = telebot.types.InlineKeyboardButton(text="◀️ Вернуться в главное меню")
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    bot.send_message(chat_id, 'Выберите интересующий ресурс:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Для ОГЭ')
def for_oge(message):
    bot.send_message(message.chat.id, texts['oge-resources'])


@bot.message_handler(func=lambda message: message.text == 'Физика')
def sources_for_physics(message):
    bot.send_message(message.chat.id, texts['physics-resources'])


@bot.message_handler(func=lambda message: message.text == 'Сайты и приложения для учебы')
def useful_applications(message):
    bot.send_message(message.chat.id, texts['apps-resources'])


@bot.message_handler(func=lambda message: message.text == 'Учебники для любознательных')
def advanced_physics(message):
    bot.send_message(message.chat.id, texts['books-resources'])


@bot.message_handler(func=lambda message: message.text == '✍️ О проекте')
def about(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="◀️ Вернуться в главное меню")
    keyboard.add(button_1)
    bot.send_message(chat_id, 'Описание проекта', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "◀️ Вернуться в главное меню")
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="🤓 Экспериментальное задание №17")
    button_2 = telebot.types.InlineKeyboardButton(text="📖 Ресурсы для подготовки")
    button_3 = telebot.types.InlineKeyboardButton(text="✍️ О проекте")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(chat_id, texts['start'], reply_markup=keyboard)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
